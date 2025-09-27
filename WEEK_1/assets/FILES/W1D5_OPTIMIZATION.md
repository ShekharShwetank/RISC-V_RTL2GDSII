# OPTIMIZATION:

## IF_ELSE & CASE:
Note:	
	variables used in if-else/case should be reg
	if-else/case used inside always block

# if_else: 
>insert basic if else syntax and construct of the if else
>danger/caution with if: inferred latches -> bad coding style -> incomplete if/else if statements
>sometimes intended latch: example for a counter design

# case
>insert vasic case statement syntax and construct
>caveats with case:
	1. incomplete case:
	leads to inferred latches -> solution: always code case with a default
	2. partial assignments in case:
	<define it here>

# Priority:
>comapare if-else and case:
>if-else: only one portion can excute.
>case: should not have over-lapping case statements

# Commands:
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

# Looping Constructs:

1. for loop -> used inside always block -> used for evaluating expressions, and not for instantiating hardware.
2. generate for loop -> used outside always, and can't be used inside always -> used to instantiate Hardware, multiple times, example: instantiate an 'and' gate 100 times

# Commands:
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



