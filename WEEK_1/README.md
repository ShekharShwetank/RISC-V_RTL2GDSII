# Week 1: RTL Design and Synthesis
# Check ![WEEK_1/assets](../WEEK_1/assets) for proof of work

This week focuses on the fundamentals of RTL design using Verilog, simulation, and logic synthesis.

## Design and Synthesis Flow

![Design Flow](assets/flow.png)

---

## Day 1: Introduction to Verilog RTL Design and Synthesis

### # 1. The Building Blocks of Verilog

Before we build a circuit, let's understand the language. Verilog allows us to describe hardware at different levels of abstraction.

#### Module Structure and Hierarchy

A **module** is the basic building block in Verilog, like a function in software or a schematic block in a circuit diagram. We practice **hierarchical design** by instantiating (creating a copy of) one module inside another, which allows us to build complex systems from simpler, reusable parts.

#### Key Data Types

In synthesizable Verilog, two primary data types are used to connect these modules:

  * **`wire`**: Represents a physical wire. It's a connection point that cannot store a value on its own. It must be continuously driven by something, like the output of a gate. It's used for combinational logic with the `assign` keyword.
  * **`reg`**: Represents a storage element, like a flip-flop or a latch. Despite its name, it doesn't always mean a hardware register. It's used inside procedural blocks (like `always`) and holds its value until the next assignment.
  * **`parameter`**: A constant value defined within a module, making the design configurable and reusable (e.g., setting the width of a bus with `parameter WIDTH = 8`).

#### Verilog Constructs

We describe logic using two main types of blocks:

  * **Combinational Logic (`assign`)**: These describe circuits whose outputs depend only on the current inputs (e.g., logic gates). They are defined with continuous assignments.
    ```verilog
    assign y = a & b; // y is the AND of a and b
    ```
  * **Sequential Logic (`always`)**: These describe circuits with memory elements that depend on a clock signal. The `always @(posedge clk)` block is the standard way to create flip-flops and registers.
    ```verilog
    always @(posedge clk) begin
      if (reset)
        q <= 1'b0;
      else
        q <= d; // q gets the value of d on the rising clock edge
    end
    ```
  * **Control Statements**: Inside `always` blocks, we can use familiar statements like `if-else` and `case` to describe complex logic.

---

### # 2. Simulation: Does My Design Work?

Writing code is one thing; proving it's correct is another. We use a **testbench** to verify our design's functionality before moving on.

A testbench is a **non-synthesizable** Verilog module that wraps around our design (often called the DUT - Design Under Test). It has two jobs:

1.  **Stimulus Generation**: It creates and applies inputs to the DUT, such as clock signals, reset signals, and data. This is done inside `initial` and `always` blocks.
2.  **Response Observation**: It watches the outputs of the DUT to see if they are correct. This is often done by writing the signal values to a file (`$dumpfile`, `$dumpvars`) for viewing in a waveform analyzer.

#### Simulation Workflow with iverilog & GTKWave

This is a two-step process to compile and run the simulation. Let's use a concrete example of a 2-to-1 multiplexer.

**Example Design: `good_mux.v`**
```verilog
module good_mux (input i0 , input i1 , input sel , output reg y);
always @ (*)
begin
	if(sel)
		y <= i1;
	else 
		y <= i0;
end
endmodule
```

**Example Testbench: `tb_good_mux.v`**
```verilog
`timescale 1ns / 1ps
module tb_good_mux;
	// Inputs
	reg i0,i1,sel;
	// Outputs
	wire y;

        // Instantiate the Unit Under Test (UUT)
	good_mux uut (
		.sel(sel),
		.i0(i0),
		.i1(i1),
		.y(y)
	);

	initial begin
	$dumpfile("tb_good_mux.vcd");
	$dumpvars(0,tb_good_mux);
	// Initialize Inputs
	sel = 0;
	i0 = 0;
	i1 = 0;
	#300 $finish;
	end

always #75 sel = ~sel;
always #10 i0 = ~i0;
always #55 i1 = ~i1;
endmodule
```

1.  **Compile and Run**: Use `iverilog` to compile your design and its testbench. The output of the iverilog is a `.vcd` file and `a.out` file is created. By executing `a.out` iverilog dump the vcd file.
    ```bash
    iverilog good_mux.v tb_good_mux.v
    ```
2.  **View**: Use `gtkwave` to open the Value Change Dump (`.vcd`) file and visually inspect the waveforms to verify the circuit's behavior.
    ```bash
    gtkwave tb_good_mux.vcd
    ```

---

### # 3. Logic Synthesis: Turning Code into Gates

**Logic synthesis** is the process of automatically converting abstract RTL code into a **gate-level netlist**. This netlist is a detailed blueprint of the circuit, describing which specific logic gates (AND, OR, Flip-Flops) to use and how to connect them with wires. Yosys is the synthesizer used to convert RTL to netlist. Netlist should be the same as the Design but represented in the form of standard cells. The same testbench can be used to verify RTL and Synthesized Netlist.

![Synthesis Illustration](assets/synthesis_illustration.png)

  * **Inputs**:
    1.  **RTL Design (`.v`)**: Your synthesizable Verilog code.
    2.  **Standard Cell Library (`.lib`)**: A technology-specific library defining the available logic gates and their characteristics (timing, power, area).
  * **Tool**: We use **Yosys**, a powerful open-source synthesis tool.
  * **Output**:
    1.  **Gate-Level Netlist (`.v`)**: A structural Verilog file describing the synthesized circuit.

A lab on logic synthesis will be done using Yosys and SKY130 PDKs.

### # 4. The Standard Cell Library (`.lib`)

The `.lib` file is the "parts catalog" for the synthesis tool. It contains different "flavors" (e.g., slow, typical, fast) of each logic gate.

#### Why Different Flavors?

Digital circuit speed is determined by timing constraints. The two most important are:

1.  **Setup Time**: Data must arrive at a flip-flop *before* the clock edge. The total delay of the data path must be less than the clock period.
      * $T\_{clk} \> T\_{CQ} + T\_{combi} + T\_{setup}$
      * To meet this, we sometimes need **fast cells** to reduce the combinational delay ($T\_{combi}$).
2.  **Hold Time**: Data must remain stable at a flip-flop for a short time *after* the clock edge. The data path must be slow enough to not change too quickly.
      * $T\_{hold} \< T\_{CQ} + T\_{combi}$
      * To meet this, we sometimes need **slow cells** to increase the combinational delay.

#### The Performance vs. Area/Power Trade-off

  * **Fast Cells**: Use wider transistors that can source more current, charging/discharging capacitance faster. This leads to **low delay** but comes at the cost of **more area and power**.
  * **Slow Cells**: Use narrower transistors, resulting in **higher delay** but **less area and power**.

The synthesizer's job is to intelligently pick a combination of these cells to meet performance goals while minimizing area and power.

---

### # 5. Practical Synthesis Workflow with Yosys

Here's how to synthesize your design and, crucially, verify that the resulting netlist is functionally identical to your original RTL.

#### Step 1: Synthesize with Yosys

You can run Yosys interactively or with a script. Here are the essential commands:

```tcl
# Start the yosys tool
yosys

# Read the standard cell library. This tells yosys what gates are available.
# The path will depend on where your PDK is installed.
read_liberty -lib /path/to/your/sky130_fd_sc_hd__tt_025C_1v80.lib

# Read your synthesizable Verilog design file
read_verilog my_design.v

# The main synthesis command. It performs high-level optimizations.
# -top specifies the top-level module to be synthesized.
synth -top my_design

# Map the design to the specific gates in your library.
# This is a crucial technology mapping step.
abc -liberty /path/to/your/sky130_fd_sc_hd__tt_025C_1v80.lib

# Clean up the design for a simpler netlist
clean

# Write the final gate-level netlist.
# The -noattr flag removes extra attributes to make it cleaner for simulation.
write_verilog -noattr my_design_netlist.v

# (Optional) Display a graphical view of the synthesized circuit
show
```

#### Step 2: Verify the Netlist

How do you know the synthesis was correct? **You simulate the netlist with the same testbench\!**

1.  **Simulate the RTL** (as done in section 2) and generate `rtl_waves.vcd`.
2.  **Simulate the Netlist**: Compile the *netlist*, the *standard cell library's Verilog model*, and the *original testbench* together.
    ```bash
    # Note: We now include the netlist and the PDK's primitive cell models.
    iverilog -o netlist_sim.vvp tb_my_design.v my_design_netlist.v /path/to/sky130_fd_sc_hd.v
    vvp netlist_sim.vvp
    ```
    This generates `netlist_waves.vcd`.
3.  **Compare**: Open both `rtl_waves.vcd` and `netlist_waves.vcd` in GTKWave. **The waveforms for all inputs and outputs must be identical.** If they are, then the synthesis was functionally correct.

---

## Day 2: Timing Libraries, Synthesis Strategies, and Flop Coding

### Understanding Timing Libraries (.lib)

Timing libraries, with the `.lib` extension, are crucial for synthesis. They characterize the behavior of standard cells for different operating conditions.

#### PVT Corners

The behavior of silicon chips is heavily influenced by **PVT (Process, Voltage, Temperature)** conditions. Libraries are provided for different corners to ensure the design works reliably across all of them.

*   **Process**: Variations in the manufacturing process.
*   **Voltage**: Variations in the supply voltage.
*   **Temperature**: Variations in the operating temperature.

A typical library name like `sky130_fd_sc_hd__tt_025C_1v80.lib` can be decoded as:

*   `tt`: **T**ypical-**T**ypical process corner.
*   `025C`: **25 degrees Celsius** temperature.
*   `1v80`: **1.80V** supply voltage.

#### Library Content

A `.lib` file contains detailed information for each standard cell, including:

*   **Timing**: Delay models (often using look-up tables).
*   **Power**: Leakage and dynamic power consumption.
*   **Area**: The physical area of the cell.
*   **Pin Information**: Capacitance, direction, and function of each pin.

#### Cell Variations

Libraries provide different versions of the same logic gate (e.g., `and2_0`, `and2_2`). As the number increases:

*   **Area increases**: Larger cells use wider transistors.
*   **Delay decreases**: Wider transistors lead to faster switching times.
*   **Power increases**: Larger transistors consume more power.

### Synthesis Strategies: Hierarchical vs. Flat

#### Hierarchical Synthesis

In hierarchical synthesis, the module hierarchy of the design is preserved in the synthesized netlist. This is the default behavior.

**Steps:**
```tcl
yosys
read_liberty -lib <path_to_lib>
read_verilog multiple_modules.v
synth -top multiple_modules
abc -liberty <path_to_lib>
show
write_verilog -noattr hierarchical_netlist.v
```

#### Flat Synthesis

In flat synthesis, the entire design hierarchy is flattened into a single module containing only standard cells.

**Steps:**
```tcl
# ... (read library and verilog) ...
synth -top multiple_modules
flatten
abc -liberty <path_to_lib>
show
write_verilog -noattr flat_netlist.v
```

#### Sub-module Level Synthesis

This approach involves synthesizing each sub-module independently. This is useful for:

*   **Reusability**: Synthesize a module once and use it multiple times.
*   **Divide and Conquer**: Break down a large design into smaller, manageable parts.

**Steps:**
```tcl
yosys
read_liberty -lib <path_to_lib>
read_verilog multiple_modules.v
synth -top <sub_module_name>
abc -liberty <path_to_lib>
show
```

### Flip-Flop Coding Styles and Synthesis

#### Why Use Flip-Flops?

Flip-flops are essential for sequential logic and play a crucial role in preventing glitches. Combinational logic can produce transient incorrect outputs (glitches) as signals propagate through different paths with different delays. Flip-flops sample their inputs only on a clock edge, ensuring that the output is stable and glitch-free.

#### Simulating and Synthesizing Flip-Flops

Different types of flip-flops (with synchronous/asynchronous set/reset) can be designed and verified.

**Simulation:**
```bash
iverilog <filename.v> <tb_filename.v>
./a.out
gtkwave <tb_filename.vcd>
```

**Synthesis:**
```tcl
yosys
read_liberty -lib <path_to_lib>
read_verilog <filename.v>
synth -top <module_name>
dfflibmap -liberty <path_to_lib>
abc -liberty <path_to_lib>
show
write_verilog -noattr netlist.v
```

### Synthesis Optimizations

Synthesis tools perform various optimizations, including:

*   **Logic Implementation**: The tool might choose an implementation that is more efficient in CMOS technology. For example, an `OR` gate might be implemented as an inverted-input `NAND` gate to avoid stacked PMOS transistors, which have poor mobility.
*   **Set/Reset Logic**: If the RTL code uses an active-high reset but the library only contains active-low reset flip-flops, the tool will automatically insert an inverter.
*   **Arithmetic Optimizations**:
    *   **Multiplication by 2^n**: This is implemented as a simple left shift, which corresponds to wiring (appending `n` zeros) and requires no logic gates.
    *   **Multiplication by a constant**: For example, `y = a * 9` can be implemented as `y = a * 8 + a`, which translates to a left shift and an addition.
