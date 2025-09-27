# Day 3 - Logic Optimization
	1. Combinational Logic Optimization
	2. Sequential Logic Optimization

### Combinational Logic Optimization:
It means squeezing the logic to get the most optimized design in terms of area and power. the most commonly used techniques are:
1. Constant Propagation
	>Direct Optimization
2. Boolean Logic Optimization
	>K-Map
	>Quine McKluskey

### Sequential Logic Optimizations:
> Basic:
	1. Sequential Contant Propagation
> Advanced:
	1. State optimization: Optimization of unused state.
	2. Retiming: splitting logic equally for possible combinations and improving the overall timing. use of 'useful slack' to reduce the delay somewhere else
	3. Sequential Logic Cloning (Floor Plan Aware Synthesis): Aviod the slack, ensure meeting timing requirements.

### 1 Sequential Constant Propagation:

For a flop to become sequential constant the Q (in a DFF) pin should always have a contant value.

### Optimization Lab:
> Combinational:

for file: opt_check, opt_check2, opt_check3, opt_check4, multiple_module_opt
```
ls *opt*
ls *opt_check*
yosys
read_liberty -lib <lib_path>
read_verilog <*opt_check.v>
synth -top <top_module_name>
flatten <for multiple_modules_opt>
opt_clean -purge  <#command to do constant propagation and other optimization>
abc -liberty <lib_path>
write_verilog <*_opt_generated_netlist.v>
show
```

> Sequential:

files: dff_const1, dff_const2, dff_const3, dff_const4, dff_const5
```
ls *dff_const*
iverilog <dff_const*.v> <tb_dff_const*.v>
./a.out
gtkwave <tb_dff_const*.vcd>
yosys
read_liberty -lib <lib_path>
read_verilog <dff_const*.v>
synth -top <top_module_name>
dfflibmap -liberty <lib_path>
abc -liberty <lib_path>
write_verilog <dff_const*_generated_netlist.v>
show
```

> Unused output optimization:

files: counter_opt, 
```
yosys
read_liberty -lib <lib_path>
read_verilog <*_opt.v>
synth -top <top_module_name>
dfflibmap -liberty <lib_path>
abc -liberty <lib_path>
write_verilog <*_opt_generated_netlist.v>
show
```

counter_opt2:
>> assign q = (count[2:0] == 3'b100);
