# Day 5 - Optimization:

## IF_ELSE & CASE:
**Note:** `if-else` and `case` statements are procedural constructs used inside `always` blocks. The variables assigned within these blocks must be of type `reg`.

### `if-else` Statements
The `if-else` construct creates a priority-encoded logic structure. Conditions are evaluated sequentially.

**Syntax:**
```verilog
if (condition1) begin
    // Statements for condition1
end 
else if (condition2) begin
    // Statements for condition2
end 
else begin
    // Default statements
end
```

**Caveat: Inferred Latches**
A common pitfall in combinational logic (`always @(*)`) is inferring a latch. This happens if an output is not assigned a value in every possible branch of the `if-else` structure. The synthesis tool must then "latch" (hold) the previous value, which is usually unintended and can cause timing issues.

*   **Bad Practice (Infers a latch for `y`):**
    ```verilog
    always @(*) begin
        if (enable)
            y = data_in;
        // No 'else' part! 'y' holds its value if 'enable' is false.
    end
    ```
*   **Good Practice (Combinational):**
    To avoid latches, ensure a value is assigned in all conditions or set a default value at the start of the block.
    ```verilog
    always @(*) begin
        y = default_value; // Assign a default
        if (enable)
            y = data_in;
    end
    ```

!Inferred Latch

### `case` Statements
The `case` statement compares an expression to a list of cases and executes the corresponding statements. It is ideal for implementing multiplexers as it implies parallel logic (no priority).

**Syntax:**
```verilog
case (control_signal)
    case_value1: begin
        // Statements for case_value1
    end
    case_value2: begin
        // Statements for case_value2
    end
    default: begin
        // Default statements (crucial!)
    end
endcase
```

**Caveats with `case`:**
1.  **Incomplete `case`**: If not all possible values of `control_signal` are covered and no `default` case is provided, a latch will be inferred. **Solution: Always include a `default` case.**
2.  **Partial Assignment**: If a variable is not assigned a value in every single `case` branch (including `default`), a latch will be inferred for that variable. **Solution: Assign a default value to all outputs before the `case` statement.**

!Incomplete Case Latch

### Priority: `if-else` vs. `case`
*   **`if-else`**: Synthesizes to **priority logic**. The first `if` condition has the highest priority. This can create a longer critical path if the chain is long.
*   **`case`**: Synthesizes to a balanced multiplexer structure (parallel logic). It's generally faster and preferred for selecting between multiple data sources based on a single control signal. Avoid overlapping case items, as this is not synthesizable in standard Verilog.


#### Commands for `if-else` and `case` Labs
files: all incomp_*.v files & corresonding tb_incomp_*.v *_case.v & tb_*_case.v

```
ls *incomp* or ls *case*
iverilog <incomp_*.v> <tb_incomp_*.v>
./a.out
gtkwave <tb_incomp_*.vcd>
yosys
read_liberty -lib <lib_path>
read_verilog <incomp_*.v>
synth -top <top_module_name>
abc -liberty <lib_path>
write_verilog -noattr <incomp_*_noattr_generated_netlist.v>
show
```

### Looping Constructs:

1. for loop -> used inside always block -> used for evaluating expressions, and not for instantiating hardware.
2. generate for loop -> used outside always, and can't be used inside always -> used to instantiate Hardware, multiple times, example: instantiate an 'and' gate 100 times

#### Commands:
files: mux_generate, demux_case, demux_generate, fa, rca

```
iverilog <*.v> <tb_*.v>
./a.out
gtkwave <tb_*.vcd>
yosys
read_liberty -lib <lib_path>
read_verilog <*.v>
synth -top <top_module_name>
abc -liberty <lib_path>
write_verilog -noattr <*_noattr_generated_netlist.v>
show
# GLS:
iverilog /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/primitives.v /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v <*.v> <tb_*.v>
./a.out
gtkwave <tb_*.vcd>
```
