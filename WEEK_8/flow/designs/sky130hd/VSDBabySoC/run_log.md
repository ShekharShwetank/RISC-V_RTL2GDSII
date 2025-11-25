shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk clean_all
rm -f ./results/sky130hd/VSDBabySoC/base/1_* ./results/sky130hd/VSDBabySoC/base/mem*.json
rm -f ./reports/sky130hd/VSDBabySoC/base/synth_*
rm -f ./logs/sky130hd/VSDBabySoC/base/1_*
rm -f 
rm -f ./results/sky130hd/VSDBabySoC/base/clock_period.txt
rm -f ./results/sky130hd/VSDBabySoC/base/2_*floorplan*.odb ./results/sky130hd/VSDBabySoC/base/2_floorplan.sdc ./results/sky130hd/VSDBabySoC/base/2_*.v ./results/sky130hd/VSDBabySoC/base/2_*.def
rm -f ./reports/sky130hd/VSDBabySoC/base/2_*
rm -f ./logs/sky130hd/VSDBabySoC/base/2_*
rm -f ./results/sky130hd/VSDBabySoC/base/3_*place*.odb
rm -f ./results/sky130hd/VSDBabySoC/base/3_place.sdc
rm -f ./results/sky130hd/VSDBabySoC/base/3_*.def ./results/sky130hd/VSDBabySoC/base/3_*.v
rm -f ./reports/sky130hd/VSDBabySoC/base/3_*
rm -f ./logs/sky130hd/VSDBabySoC/base/3_*
rm -rf ./results/sky130hd/VSDBabySoC/base/4_*cts*.odb ./results/sky130hd/VSDBabySoC/base/4_cts.sdc ./results/sky130hd/VSDBabySoC/base/4_*.v ./results/sky130hd/VSDBabySoC/base/4_*.def
rm -f  ./reports/sky130hd/VSDBabySoC/base/4_*
rm -rf ./logs/sky130hd/VSDBabySoC/base/4_*
rm -rf ./results/sky130hd/VSDBabySoC/base/route.guide ./results/sky130hd/VSDBabySoC/base/output_guide.mod ./results/sky130hd/VSDBabySoC/base/updated_clks.sdc
rm -rf ./results/sky130hd/VSDBabySoC/base/5_*.odb ./results/sky130hd/VSDBabySoC/base/5_route.sdc ./results/sky130hd/VSDBabySoC/base/5_*.def ./results/sky130hd/VSDBabySoC/base/5_*.v
rm -f  ./reports/sky130hd/VSDBabySoC/base/5_*
rm -f  ./logs/sky130hd/VSDBabySoC/base/5_*
rm -rf ./results/sky130hd/VSDBabySoC/base/6_*.gds ./results/sky130hd/VSDBabySoC/base/6_*.oas ./results/sky130hd/VSDBabySoC/base/6_*.odb ./results/sky130hd/VSDBabySoC/base/6_*.v ./results/sky130hd/VSDBabySoC/base/6_*.def ./results/sky130hd/VSDBabySoC/base/6_*.sdc ./results/sky130hd/VSDBabySoC/base/6_*.spef
rm -rf ./reports/sky130hd/VSDBabySoC/base/6_*.rpt
rm -f  ./logs/sky130hd/VSDBabySoC/base/6_*
rm -f ./reports/sky130hd/VSDBabySoC/base/design-dir.txt
rm -f ./reports/sky130hd/VSDBabySoC/base/metadata*.*
rm -f ./results/sky130hd/VSDBabySoC/base/vsdbabysoc.lib ./results/sky130hd/VSDBabySoC/base/vsdbabysoc.lef
rm -rf ./objects/sky130hd/VSDBabySoC/base
<<<<<<< HEAD
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ YOSYS_EXE=~/OpenROAD-flow-scripts/tools/yosys/yosys OPENROAD_EXE=~/OpenROAD-flow-scripts/tools/OpenROAD/build/bin/openroad make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk finish
=======
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ export PDN_SCRIPT=/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/pdn_custom.tcl
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ echo $PDN_SCRIPT
/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/pdn_custom.tcl
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ YOSYS_EXE=~/OpenROAD-flow-scripts/tools/yosys/yosys OPENROAD_EXE=~/OpenROAD-flow-scripts/tools/OpenROAD/build/bin/openroad make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk
>>>>>>> 2e9d213 (added assets)
mkdir -p results/sky130hd/VSDBabySoC/base/
echo 11 > results/sky130hd/VSDBabySoC/base/clock_period.txt
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.sh /home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth_canonicalize.tcl ./logs/sky130hd/VSDBabySoC/base/1_1_yosys_canonicalize.log
Using ABC speed script.
Extracting clock period from SDC file: ./results/sky130hd/VSDBabySoC/base/clock_period.txt
Setting clock period to 11
1. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
2. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
3. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
4. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
5. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
6. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
7. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/vsdbabysoc.v
8. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v
9. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/clk_gate.v
10. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_clkgate_hd.v
11. Executing HIERARCHY pass (managing design hierarchy).
12. Executing AST frontend in derive mode using pre-parsed AST for module `\vsdbabysoc'.
12.1. Analyzing design hierarchy..
12.2. Executing AST frontend in derive mode using pre-parsed AST for module `\rvmyth'.
Warning: Replacing memory \CPU_Dmem_value_a4 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:308
Warning: Replacing memory \CPU_Xreg_value_a3 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:288
Warning: Replacing memory \CPU_Imem_instr_a1 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:273
Warning: Replacing memory \CPU_Xreg_value_a5 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:693
Warning: Replacing memory \CPU_Xreg_value_a4 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:692
Warning: Replacing memory \CPU_Dmem_value_a5 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:683
12.3. Analyzing design hierarchy..
12.4. Executing AST frontend in derive mode using pre-parsed AST for module `\clk_gate'.
12.5. Analyzing design hierarchy..
12.6. Analyzing design hierarchy..
13. Executing OPT_CLEAN pass (remove unused cells and wires).
Warning: Ignoring module rvmyth because it contains processes (run 'proc' command first).
14. Executing RTLIL backend.
Warnings: 7 unique messages, 7 total
<<<<<<< HEAD
End of script. Logfile hash: cff3327032, CPU: user 0.19s system 0.03s, MEM: 51.75 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 67% 8x read_liberty (0 sec), 17% 1x hierarchy (0 sec), ...
Elapsed time: 0:00.32[h:]min:sec. CPU time: user 0.27 sys 0.04 (100%). Peak memory: 55680KB.
=======
End of script. Logfile hash: cff3327032, CPU: user 0.21s system 0.04s, MEM: 52.00 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 68% 8x read_liberty (0 sec), 15% 1x hierarchy (0 sec), ...
Elapsed time: 0:00.35[h:]min:sec. CPU time: user 0.29 sys 0.05 (99%). Peak memory: 55808KB.
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.sh /home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.tcl ./logs/sky130hd/VSDBabySoC/base/1_2_yosys.log
Using ABC speed script.
Extracting clock period from SDC file: ./results/sky130hd/VSDBabySoC/base/clock_period.txt
Setting clock period to 11
1. Executing RTLIL frontend.
2. Executing HIERARCHY pass (managing design hierarchy).
2.1. Analyzing design hierarchy..
2.2. Analyzing design hierarchy..
3. Executing SYNTH pass.
3.1. Executing HIERARCHY pass (managing design hierarchy).
3.1.1. Analyzing design hierarchy..
3.1.2. Analyzing design hierarchy..
3.2. Executing PROC pass (convert processes to netlists).
3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
3.2.4. Executing PROC_INIT pass (extract init attributes).
3.2.5. Executing PROC_ARST pass (detect async resets in processes).
3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).
3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).
3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
3.2.12. Executing OPT_EXPR pass (perform const folding).
3.3. Executing FLATTEN pass (flatten design).
3.4. Executing OPT_EXPR pass (perform const folding).
3.5. Executing OPT_CLEAN pass (remove unused cells and wires).
3.6. Executing CHECK pass (checking for obvious problems).
3.7. Executing OPT pass (performing simple optimizations).
3.7.1. Executing OPT_EXPR pass (perform const folding).
3.7.2. Executing OPT_MERGE pass (detect identical cells).
3.7.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.7.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.7.5. Executing OPT_MERGE pass (detect identical cells).
3.7.6. Executing OPT_DFF pass (perform DFF optimizations).
3.7.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.7.8. Executing OPT_EXPR pass (perform const folding).
3.7.9. Rerunning OPT passes. (Maybe there is more to do..)
3.7.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.7.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.7.12. Executing OPT_MERGE pass (detect identical cells).
3.7.13. Executing OPT_DFF pass (perform DFF optimizations).
3.7.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.7.15. Executing OPT_EXPR pass (perform const folding).
3.7.16. Finished fast OPT passes. (There is nothing left to do.)
3.8. Executing FSM pass (extract and optimize FSM).
3.8.1. Executing FSM_DETECT pass (finding FSMs in design).
3.8.2. Executing FSM_EXTRACT pass (extracting FSM from design).
3.8.3. Executing FSM_OPT pass (simple optimizations of FSMs).
3.8.4. Executing OPT_CLEAN pass (remove unused cells and wires).
3.8.5. Executing FSM_OPT pass (simple optimizations of FSMs).
3.8.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).
3.8.7. Executing FSM_INFO pass (dumping all available information on FSM cells).
3.8.8. Executing FSM_MAP pass (mapping FSMs to basic logic).
3.9. Executing OPT pass (performing simple optimizations).
3.9.1. Executing OPT_EXPR pass (perform const folding).
3.9.2. Executing OPT_MERGE pass (detect identical cells).
3.9.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.5. Executing OPT_MERGE pass (detect identical cells).
3.9.6. Executing OPT_DFF pass (perform DFF optimizations).
3.9.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.8. Executing OPT_EXPR pass (perform const folding).
3.9.9. Rerunning OPT passes. (Maybe there is more to do..)
3.9.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.12. Executing OPT_MERGE pass (detect identical cells).
3.9.13. Executing OPT_DFF pass (perform DFF optimizations).
3.9.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.15. Executing OPT_EXPR pass (perform const folding).
3.9.16. Rerunning OPT passes. (Maybe there is more to do..)
3.9.17. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.18. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.19. Executing OPT_MERGE pass (detect identical cells).
3.9.20. Executing OPT_DFF pass (perform DFF optimizations).
3.9.21. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.22. Executing OPT_EXPR pass (perform const folding).
3.9.23. Finished fast OPT passes. (There is nothing left to do.)
3.10. Executing WREDUCE pass (reducing word size of cells).
3.11. Executing PEEPOPT pass (run peephole optimizers).
3.12. Executing OPT_CLEAN pass (remove unused cells and wires).
3.13. Executing ALUMACC pass (create $alu and $macc cells).
3.14. Executing SHARE pass (SAT-based resource sharing).
3.15. Executing OPT pass (performing simple optimizations).
3.15.1. Executing OPT_EXPR pass (perform const folding).
3.15.2. Executing OPT_MERGE pass (detect identical cells).
3.15.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.15.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.15.5. Executing OPT_MERGE pass (detect identical cells).
3.15.6. Executing OPT_DFF pass (perform DFF optimizations).
3.15.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.15.8. Executing OPT_EXPR pass (perform const folding).
3.15.9. Rerunning OPT passes. (Maybe there is more to do..)
3.15.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.15.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.15.12. Executing OPT_MERGE pass (detect identical cells).
3.15.13. Executing OPT_DFF pass (perform DFF optimizations).
3.15.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.15.15. Executing OPT_EXPR pass (perform const folding).
3.15.16. Finished fast OPT passes. (There is nothing left to do.)
3.16. Executing MEMORY pass.
3.16.1. Executing OPT_MEM pass (optimize memories).
3.16.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
3.16.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).
3.16.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).
3.16.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).
3.16.6. Executing OPT_CLEAN pass (remove unused cells and wires).
3.16.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).
3.16.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
3.16.9. Executing OPT_CLEAN pass (remove unused cells and wires).
3.16.10. Executing MEMORY_COLLECT pass (generating $mem cells).
3.17. Executing OPT_CLEAN pass (remove unused cells and wires).
4. Executing SYNTH pass.
4.1. Executing OPT pass (performing simple optimizations).
4.1.1. Executing OPT_EXPR pass (perform const folding).
4.1.2. Executing OPT_MERGE pass (detect identical cells).
4.1.3. Executing OPT_DFF pass (perform DFF optimizations).
4.1.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.1.5. Rerunning OPT passes. (Removed registers in this run.)
4.1.6. Executing OPT_EXPR pass (perform const folding).
4.1.7. Executing OPT_MERGE pass (detect identical cells).
4.1.8. Executing OPT_DFF pass (perform DFF optimizations).
4.1.9. Executing OPT_CLEAN pass (remove unused cells and wires).
4.1.10. Finished fast OPT passes.
4.2. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).
4.3. Executing OPT pass (performing simple optimizations).
4.3.1. Executing OPT_EXPR pass (perform const folding).
4.3.2. Executing OPT_MERGE pass (detect identical cells).
4.3.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.5. Executing OPT_MERGE pass (detect identical cells).
4.3.6. Executing OPT_SHARE pass.
4.3.7. Executing OPT_DFF pass (perform DFF optimizations).
4.3.8. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.9. Executing OPT_EXPR pass (perform const folding).
4.3.10. Rerunning OPT passes. (Maybe there is more to do..)
4.3.11. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.12. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.13. Executing OPT_MERGE pass (detect identical cells).
4.3.14. Executing OPT_SHARE pass.
4.3.15. Executing OPT_DFF pass (perform DFF optimizations).
4.3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.17. Executing OPT_EXPR pass (perform const folding).
4.3.18. Rerunning OPT passes. (Maybe there is more to do..)
4.3.19. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.20. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.21. Executing OPT_MERGE pass (detect identical cells).
4.3.22. Executing OPT_SHARE pass.
4.3.23. Executing OPT_DFF pass (perform DFF optimizations).
4.3.24. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.25. Executing OPT_EXPR pass (perform const folding).
4.3.26. Rerunning OPT passes. (Maybe there is more to do..)
4.3.27. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.28. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.29. Executing OPT_MERGE pass (detect identical cells).
4.3.30. Executing OPT_SHARE pass.
4.3.31. Executing OPT_DFF pass (perform DFF optimizations).
4.3.32. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.33. Executing OPT_EXPR pass (perform const folding).
4.3.34. Rerunning OPT passes. (Maybe there is more to do..)
4.3.35. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.36. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.37. Executing OPT_MERGE pass (detect identical cells).
4.3.38. Executing OPT_SHARE pass.
4.3.39. Executing OPT_DFF pass (perform DFF optimizations).
4.3.40. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.41. Executing OPT_EXPR pass (perform const folding).
4.3.42. Rerunning OPT passes. (Maybe there is more to do..)
4.3.43. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.44. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.45. Executing OPT_MERGE pass (detect identical cells).
4.3.46. Executing OPT_SHARE pass.
4.3.47. Executing OPT_DFF pass (perform DFF optimizations).
4.3.48. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.49. Executing OPT_EXPR pass (perform const folding).
4.3.50. Rerunning OPT passes. (Maybe there is more to do..)
4.3.51. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.52. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.53. Executing OPT_MERGE pass (detect identical cells).
4.3.54. Executing OPT_SHARE pass.
4.3.55. Executing OPT_DFF pass (perform DFF optimizations).
4.3.56. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.57. Executing OPT_EXPR pass (perform const folding).
4.3.58. Finished fast OPT passes. (There is nothing left to do.)
4.4. Executing TECHMAP pass (map to technology primitives).
4.4.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/tools/yosys/share/techmap.v
4.4.2. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/common/lcu_kogge_stone.v
4.4.3. Continuing TECHMAP pass.
4.5. Executing OPT pass (performing simple optimizations).
4.5.1. Executing OPT_EXPR pass (perform const folding).
4.5.2. Executing OPT_MERGE pass (detect identical cells).
4.5.3. Executing OPT_DFF pass (perform DFF optimizations).
4.5.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.5. Rerunning OPT passes. (Removed registers in this run.)
4.5.6. Executing OPT_EXPR pass (perform const folding).
4.5.7. Executing OPT_MERGE pass (detect identical cells).
4.5.8. Executing OPT_DFF pass (perform DFF optimizations).
4.5.9. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.10. Rerunning OPT passes. (Removed registers in this run.)
4.5.11. Executing OPT_EXPR pass (perform const folding).
4.5.12. Executing OPT_MERGE pass (detect identical cells).
4.5.13. Executing OPT_DFF pass (perform DFF optimizations).
4.5.14. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.15. Finished fast OPT passes.
4.6. Executing ABC pass (technology mapping using ABC).
4.6.1. Extracting gate netlist of module `\vsdbabysoc' to `<abc-temp-dir>/input.blif'..
4.7. Executing OPT pass (performing simple optimizations).
4.7.1. Executing OPT_EXPR pass (perform const folding).
4.7.2. Executing OPT_MERGE pass (detect identical cells).
4.7.3. Executing OPT_DFF pass (perform DFF optimizations).
4.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.7.5. Finished fast OPT passes.
4.8. Executing HIERARCHY pass (managing design hierarchy).
4.8.1. Analyzing design hierarchy..
4.8.2. Analyzing design hierarchy..
4.9. Printing statistics.
4.10. Executing CHECK pass (checking for obvious problems).
5. Executing OPT pass (performing simple optimizations).
5.1. Executing OPT_EXPR pass (perform const folding).
5.2. Executing OPT_MERGE pass (detect identical cells).
5.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
5.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
5.5. Executing OPT_MERGE pass (detect identical cells).
5.6. Executing OPT_DFF pass (perform DFF optimizations).
5.7. Executing OPT_CLEAN pass (remove unused cells and wires).
5.8. Executing OPT_EXPR pass (perform const folding).
5.9. Rerunning OPT passes. (Maybe there is more to do..)
5.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
5.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
5.12. Executing OPT_MERGE pass (detect identical cells).
5.13. Executing OPT_DFF pass (perform DFF optimizations).
5.14. Executing OPT_CLEAN pass (remove unused cells and wires).
5.15. Executing OPT_EXPR pass (perform const folding).
5.16. Finished fast OPT passes. (There is nothing left to do.)
6. Executing EXTRACT_FA pass (find and extract full/half adders).
7. Executing TECHMAP pass (map to technology primitives).
7.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_adders_hd.v
7.2. Continuing TECHMAP pass.
8. Executing TECHMAP pass (map to technology primitives).
8.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/tools/yosys/share/techmap.v
8.2. Continuing TECHMAP pass.
9. Executing OPT pass (performing simple optimizations).
9.1. Executing OPT_EXPR pass (perform const folding).
9.2. Executing OPT_MERGE pass (detect identical cells).
9.3. Executing OPT_DFF pass (perform DFF optimizations).
9.4. Executing OPT_CLEAN pass (remove unused cells and wires).
9.5. Finished fast OPT passes.
10. Executing TECHMAP pass (map to technology primitives).
10.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_latch_hd.v
10.2. Continuing TECHMAP pass.
11. Executing DFFLIBMAP pass (mapping DFF cells to sequential cells from liberty file).
11.1. Executing DFFLEGALIZE pass (convert FFs to types supported by the target).
12. Executing OPT pass (performing simple optimizations).
12.1. Executing OPT_EXPR pass (perform const folding).
12.2. Executing OPT_MERGE pass (detect identical cells).
12.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
12.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
12.5. Executing OPT_MERGE pass (detect identical cells).
12.6. Executing OPT_DFF pass (perform DFF optimizations).
12.7. Executing OPT_CLEAN pass (remove unused cells and wires).
12.8. Executing OPT_EXPR pass (perform const folding).
12.9. Finished fast OPT passes. (There is nothing left to do.)
13. Executing SETUNDEF pass (replace undef values with defined constants).
abc -script /home/shwetank/OpenROAD-flow-scripts/flow/scripts/abc_speed.script -liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib -dont_use sky130_fd_sc_hd__probe_p_8 -dont_use sky130_fd_sc_hd__probec_p_8 -dont_use sky130_fd_sc_hd__lpflow_bleeder_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_12 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_3 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_6 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_inputiso0n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso0p_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1p_1 -dont_use sky130_fd_sc_hd__lpflow_inputisolatch_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_16 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_2 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_4 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_8 -dont_use sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 -constr ./objects/sky130hd/VSDBabySoC/base/abc.constr -D 11
14. Executing ABC pass (technology mapping using ABC).
14.1. Extracting gate netlist of module `\vsdbabysoc' to `<abc-temp-dir>/input.blif'..
14.1.1. Executed ABC.
14.1.2. Re-integrating ABC results.
<<<<<<< HEAD
Took 6 seconds: abc -script /home/shwetank/OpenROAD-flow-scripts/flow/scripts/abc_speed.script -liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib -dont_use sky130_fd_sc_hd__probe_p_8 -dont_use sky130_fd_sc_hd__probec_p_8 -dont_use sky130_fd_sc_hd__lpflow_bleeder_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_12 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_3 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_6 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_inputiso0n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso0p_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1p_1 -dont_use sky130_fd_sc_hd__lpflow_inputisolatch_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_16 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_2 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_4 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_8 -dont_use sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 -constr ./objects/sky130hd/VSDBabySoC/base/abc.constr -D 11
=======
Took 7 seconds: abc -script /home/shwetank/OpenROAD-flow-scripts/flow/scripts/abc_speed.script -liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib -dont_use sky130_fd_sc_hd__probe_p_8 -dont_use sky130_fd_sc_hd__probec_p_8 -dont_use sky130_fd_sc_hd__lpflow_bleeder_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_12 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_3 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_6 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_inputiso0n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso0p_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1p_1 -dont_use sky130_fd_sc_hd__lpflow_inputisolatch_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_16 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_2 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_4 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_8 -dont_use sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 -constr ./objects/sky130hd/VSDBabySoC/base/abc.constr -D 11
>>>>>>> 2e9d213 (added assets)
15. Executing SPLITNETS pass (splitting up multi-bit signals).
16. Executing OPT_CLEAN pass (remove unused cells and wires).
17. Executing HILOMAP pass (mapping to constant drivers).
18. Executing INSBUF pass (insert buffer cells for connected wires).
19. Executing CHECK pass (checking for obvious problems).
20. Printing statistics.
21. Executing CHECK pass (checking for obvious problems).
22. Executing Verilog backend.
22.1. Executing BMUXMAP pass.
22.2. Executing DEMUXMAP pass.
exec cp /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/vsdbabysoc_synthesis.sdc ./results/sky130hd/VSDBabySoC/base/1_synth.sdc
<<<<<<< HEAD
End of script. Logfile hash: 527069a084, CPU: user 2.97s system 0.07s, MEM: 69.61 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 68% 2x abc (6 sec), 7% 34x opt_clean (0 sec), ...
Elapsed time: 0:09.42[h:]min:sec. CPU time: user 9.26 sys 0.16 (100%). Peak memory: 72692KB.
=======
End of script. Logfile hash: 87c92c58a4, CPU: user 3.37s system 0.08s, MEM: 69.49 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 66% 2x abc (6 sec), 7% 34x opt_clean (0 sec), ...
Elapsed time: 0:09.89[h:]min:sec. CPU time: user 9.72 sys 0.17 (100%). Peak memory: 72440KB.
>>>>>>> 2e9d213 (added assets)
mkdir -p ./results/sky130hd/VSDBabySoC/base ./logs/sky130hd/VSDBabySoC/base ./reports/sky130hd/VSDBabySoC/base
cp ./results/sky130hd/VSDBabySoC/base/1_2_yosys.v ./results/sky130hd/VSDBabySoC/base/1_synth.v
OpenROAD v2.0-26087-g3bcda7705d 
Features included (+) or not (-): +GPU +GUI +Python
This program is licensed under the BSD-3 license. See the LICENSE file for details.
Components of this program may be licensed under more restrictive licenses which must be honored.
[INFO ORD-0030] Using 10 thread(s).
mkdir -p ./objects/sky130hd/VSDBabySoC/base
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_1_floorplan floorplan
Running floorplan.tcl, stage 2_1_floorplan
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lef/sky130_fd_sc_hd.tlef, created 13 layers, 25 vias
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lef/sky130_fd_sc_hd_merged.lef, created 441 library cells
[WARNING ODB-0220] WARNING (LEFPARS-2008): NOWIREEXTENSIONATPIN statement is obsolete in version 5.6 or later.
The NOWIREEXTENSIONATPIN statement will be ignored. See file /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsddac.lef at line 2.

[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsddac.lef, created 1 library cells
[WARNING ODB-0220] WARNING (LEFPARS-2008): NOWIREEXTENSIONATPIN statement is obsolete in version 5.6 or later.
The NOWIREEXTENSIONATPIN statement will be ignored. See file /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsdpll.lef at line 2.

[WARNING ODB-0186] macro avsdpll references unknown site unithddb1
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsdpll.lef, created 1 library cells
link_design vsdbabysoc
Master sky130_ef_sc_hd__decap_12 is loaded but not used in the design

==========================================================================
Floorplan check_setup
--------------------------------------------------------------------------
Warning: There are 6 input ports missing set_input_delay.
Warning: There is 1 output port missing set_output_delay.
Warning: There are 2 unconstrained endpoints.
number instances in verilog is 6605
<<<<<<< HEAD
[WARNING IFP-0028] Core area lower left (50.000, 50.000) snapped to (50.140, 51.680).
[INFO IFP-0001] Added 881 rows of 5217 site unithd.
=======
[WARNING IFP-0028] Core area lower left (20.000, 20.000) snapped to (20.240, 21.760).
[INFO IFP-0001] Added 874 rows of 5173 site unithd.
>>>>>>> 2e9d213 (added assets)
source /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/make_tracks.tcl
source /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/fastroute.tcl
Repair tie lo fanout...
[INFO RSZ-0042] Inserted 4 tie sky130_fd_sc_hd__conb_1 instances.
Repair tie hi fanout...
[INFO RSZ-0026] Removed 595 buffers.
Default units for flow
 time 1ns
 capacitance 1pF
 resistance 1kohm
 voltage 1v
 current 1mA
 power 1nW
 distance 1um
Report metrics stage 2, floorplan final...

==========================================================================
floorplan final report_design_area
--------------------------------------------------------------------------
Design area 722267 um^2 13% utilization.
<<<<<<< HEAD
Elapsed time: 0:02.04[h:]min:sec. CPU time: user 2.25 sys 0.33 (126%). Peak memory: 140220KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_1_floorplan                      2            136 c65a11f5e946087b4d13
=======
Elapsed time: 0:02.10[h:]min:sec. CPU time: user 2.33 sys 0.32 (126%). Peak memory: 138940KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_1_floorplan                      2            135 d6734a29e94f5091b74e
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_2_floorplan_macro macro_place
Running macro_place.tcl, stage 2_2_floorplan_macro
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_1_floorplan.odb
<<<<<<< HEAD
rtl_macro_placer -max_num_level 2 -halo_width 40 -halo_height 40 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.3
Die Area: (0.00, 0.00) (2500.00, 2500.00),  Floorplan Area: (50.14, 51.68) (2449.96, 2448.00)
=======
rtl_macro_placer -max_num_level 2 -halo_width 100 -halo_height 100 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.35
Die Area: (0.00, 0.00) (2500.00, 2500.00),  Floorplan Area: (20.24, 21.76) (2399.82, 2399.04)
>>>>>>> 2e9d213 (added assets)
	Number of std cell instances: 6011
	Area of std cell instances: 50614.96
	Number of macros: 2
	Area of macros: 671652.31
<<<<<<< HEAD
	Halo width: 40.00
	Halo height: 40.00
	Area of macros with halos: 828913.94
	Area of std cell instances + Area of macros: 722267.25
	Floorplan area: 5750737.00
=======
	Halo width: 100.00
	Halo height: 100.00
	Area of macros with halos: 1112806.25
	Area of std cell instances + Area of macros: 722267.25
	Floorplan area: 5656928.00
>>>>>>> 2e9d213 (added assets)
	Design Utilization: 0.13
	Floorplan Utilization: 0.01
	Manufacturing Grid: 5

[WARNING MPL-0002] Couldn't align pin dac/D[0] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[1] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[2] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[4] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[5] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[6] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[7] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[8] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[9] from layer li1 to the track-grid.
<<<<<<< HEAD
[WARNING MPL-0002] Couldn't align pin dac/OUT from layer met4 to the track-grid.
=======
>>>>>>> 2e9d213 (added assets)
[WARNING MPL-0002] Couldn't align pin pll/CLK from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/ENb_CP from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/ENb_VCO from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/REF from layer li1 to the track-grid.
<<<<<<< HEAD
Took 18 seconds: rtl_macro_placer -max_num_level 2 -halo_width 40 -halo_height 40 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.3
Elapsed time: 0:18.06[h:]min:sec. CPU time: user 30.03 sys 21.89 (287%). Peak memory: 168680KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_2_floorplan_macro               18            164 cef9b1fd13273d7850eb
=======
Took 19 seconds: rtl_macro_placer -max_num_level 2 -halo_width 100 -halo_height 100 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.35
Elapsed time: 0:19.22[h:]min:sec. CPU time: user 33.25 sys 21.78 (286%). Peak memory: 163348KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_2_floorplan_macro               19            159 a324dd60a9c6c61e1ba0
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_3_floorplan_tapcell tapcell
Running tapcell.tcl, stage 2_3_floorplan_tapcell
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_2_floorplan_macro.odb
<<<<<<< HEAD
[INFO ODB-0303] The initial 881 rows (4596177 sites) were cut with 2 shapes for a total of 1098 rows (4051237 sites).
[INFO TAP-0005] Inserted 67622 tapcells.
Elapsed time: 0:00.73[h:]min:sec. CPU time: user 0.62 sys 0.11 (100%). Peak memory: 145936KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_3_floorplan_tapcell              0            142 7af13a514a5e794a0fd8
=======
[INFO ODB-0303] The initial 874 rows (4521202 sites) were cut with 2 shapes for a total of 1090 rows (3976350 sites).
[INFO TAP-0005] Inserted 66579 tapcells.
Elapsed time: 0:00.84[h:]min:sec. CPU time: user 0.71 sys 0.13 (100%). Peak memory: 143624KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_3_floorplan_tapcell              0            140 2afe6075f752fa45aa06
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_4_floorplan_pdn pdn
Running pdn.tcl, stage 2_4_floorplan_pdn
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_3_floorplan_tapcell.odb
<<<<<<< HEAD
[WARNING PDN-0007] GND on met1 is partially blocked (58.3%) by obstructions on met3 for pll
[WARNING PDN-0007] GND2 on met1 is partially blocked (7.0%) by obstructions on met2 for pll
[INFO PDN-0001] Inserting grid: Core
[INFO PDN-0001] Inserting grid: pll_grid - pll
[INFO PDN-0001] Inserting grid: dac_grid - dac
[WARNING PDN-0110] No via inserted between met4 and met5 at (179.3400, 180.8800) - (180.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (259.3400, 180.8800) - (260.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (339.3400, 180.8800) - (340.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (419.3400, 180.8800) - (420.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (499.3400, 180.8800) - (500.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (579.3400, 180.8800) - (580.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (659.3400, 180.8800) - (660.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (739.3400, 180.8800) - (740.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (819.3400, 180.8800) - (820.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (899.3400, 180.8800) - (900.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (979.3400, 180.8800) - (980.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1059.3400, 180.8800) - (1060.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1139.3400, 180.8800) - (1140.9400, 181.5500) on VDD
Elapsed time: 0:02.62[h:]min:sec. CPU time: user 2.36 sys 0.26 (100%). Peak memory: 375036KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_4_floorplan_pdn                  2            366 e6b4c53b2a8fd5ac00cf
=======
[WARNING PDN-0189] Supply pin pll/GND is not connected to any net.
[WARNING PDN-0189] Supply pin pll/GND2 is not connected to any net.
[WARNING PDN-0189] Supply pin pll/VDD2 is not connected to any net.
[WARNING PDN-0189] Supply pin pll/VDD3 is not connected to any net.
[WARNING PDN-0007] VDD on met1 is partially blocked (11.9%) by obstructions on met2, met3 for pll
[INFO PDN-0001] Inserting grid: grid
[INFO PDN-0001] Inserting grid: CORE_macro_grid_1 - dac
[INFO PDN-0001] Inserting grid: CORE_macro_grid_1 - pll
[WARNING PDN-0110] No via inserted between met4 and met5 at (128.0000, 864.6100) - (129.6000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (155.1400, 864.6100) - (156.7400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (182.2800, 864.6100) - (183.8800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (209.4200, 864.6100) - (211.0200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (236.5600, 864.6100) - (238.1600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (263.7000, 864.6100) - (265.3000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (290.8400, 864.6100) - (292.4400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (317.9800, 864.6100) - (319.5800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (345.1200, 864.6100) - (346.7200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (372.2600, 864.6100) - (373.8600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (399.4000, 864.6100) - (401.0000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (426.5400, 864.6100) - (428.1400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (453.6800, 864.6100) - (455.2800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (480.8200, 864.6100) - (482.4200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (507.9600, 864.6100) - (509.5600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (535.1000, 864.6100) - (536.7000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (562.2400, 864.6100) - (563.8400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (589.3800, 864.6100) - (590.9800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (616.5200, 864.6100) - (618.1200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (643.6600, 864.6100) - (645.2600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (670.8000, 864.6100) - (672.4000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (697.9400, 864.6100) - (699.5400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (725.0800, 864.6100) - (726.6800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (752.2200, 864.6100) - (753.8200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (779.3600, 864.6100) - (780.9600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (806.5000, 864.6100) - (808.1000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (833.6400, 864.6100) - (835.2400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (860.7800, 864.6100) - (862.3800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (887.9200, 864.6100) - (889.5200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (915.0600, 864.6100) - (916.6600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (942.2000, 864.6100) - (943.8000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (969.3400, 864.6100) - (970.9400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (996.4800, 864.6100) - (998.0800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1023.6200, 864.6100) - (1025.2200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1050.7600, 864.6100) - (1052.3600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1077.9000, 864.6100) - (1079.5000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1105.0400, 864.6100) - (1106.6400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1132.1800, 864.6100) - (1133.7800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1159.3200, 864.6100) - (1160.9200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (128.0000, 864.6100) - (129.6000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (155.1400, 864.6100) - (156.7400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (182.2800, 864.6100) - (183.8800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (209.4200, 864.6100) - (211.0200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (236.5600, 864.6100) - (238.1600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (263.7000, 864.6100) - (265.3000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (290.8400, 864.6100) - (292.4400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (317.9800, 864.6100) - (319.5800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (345.1200, 864.6100) - (346.7200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (372.2600, 864.6100) - (373.8600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (399.4000, 864.6100) - (401.0000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (426.5400, 864.6100) - (428.1400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (453.6800, 864.6100) - (455.2800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (480.8200, 864.6100) - (482.4200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (507.9600, 864.6100) - (509.5600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (535.1000, 864.6100) - (536.7000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (562.2400, 864.6100) - (563.8400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (589.3800, 864.6100) - (590.9800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (616.5200, 864.6100) - (618.1200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (643.6600, 864.6100) - (645.2600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (670.8000, 864.6100) - (672.4000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (697.9400, 864.6100) - (699.5400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (725.0800, 864.6100) - (726.6800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (752.2200, 864.6100) - (753.8200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (779.3600, 864.6100) - (780.9600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (806.5000, 864.6100) - (808.1000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (833.6400, 864.6100) - (835.2400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (860.7800, 864.6100) - (862.3800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (887.9200, 864.6100) - (889.5200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (915.0600, 864.6100) - (916.6600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (942.2000, 864.6100) - (943.8000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (969.3400, 864.6100) - (970.9400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (996.4800, 864.6100) - (998.0800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1023.6200, 864.6100) - (1025.2200, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1050.7600, 864.6100) - (1052.3600, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1077.9000, 864.6100) - (1079.5000, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1105.0400, 864.6100) - (1106.6400, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1132.1800, 864.6100) - (1133.7800, 865.7600) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1159.3200, 864.6100) - (1160.9200, 865.7600) on VDD
Elapsed time: 0:04.11[h:]min:sec. CPU time: user 3.85 sys 0.26 (100%). Peak memory: 369500KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_4_floorplan_pdn                  4            360 1c6519b371b0e499d736
>>>>>>> 2e9d213 (added assets)
cp ./results/sky130hd/VSDBabySoC/base/2_4_floorplan_pdn.odb ./results/sky130hd/VSDBabySoC/base/2_floorplan.odb
cp ./results/sky130hd/VSDBabySoC/base/2_1_floorplan.sdc ./results/sky130hd/VSDBabySoC/base/2_floorplan.sdc
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_1_place_gp_skip_io global_place_skip_io
Running global_place_skip_io.tcl, stage 3_1_place_gp_skip_io
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_floorplan.odb
<<<<<<< HEAD
global_placement -skip_io -density "0.30   " -pad_left 0 -pad_right 0
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             76049
[INFO GPL-0007] Movable instances:                6011
[INFO GPL-0008] Fixed instances:                 67624
[INFO GPL-0009] Dummy instances:                  2414
[INFO GPL-0010] Number of nets:                   6123
[INFO GPL-0011] Number of pins:                  21871
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0016] Core area:                  5750736.662 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5750736.662 um^2
[INFO GPL-0017] Fixed instances area:       914400.733 um^2
[INFO GPL-0018] Movable instances area:      50614.794 um^2
[INFO GPL-0019] Utilization:                     1.047 %
[INFO GPL-0020] Standard cells area:         50614.794 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3000
[INFO GPL-0024] Movable insts average area:      8.420 um^2
[INFO GPL-0025] Ideal bin area:                 28.068 um^2
[INFO GPL-0026] Ideal bin count:                204886
[INFO GPL-0027] Total bin area:             5750736.662 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.374 *  9.361 um
=======
global_placement -skip_io -density "0.35   " -pad_left 0 -pad_right 0
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 20.240 21.760 ) ( 2399.820 2399.040 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             79008
[INFO GPL-0007] Movable instances:                6011
[INFO GPL-0008] Fixed instances:                 66581
[INFO GPL-0009] Dummy instances:                  6416
[INFO GPL-0010] Number of nets:                   6123
[INFO GPL-0011] Number of pins:                  21871
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 20.240 21.760 ) ( 2399.820 2399.040 ) um
[INFO GPL-0016] Core area:                  5656927.942 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5656927.942 um^2
[INFO GPL-0017] Fixed instances area:       1191465.210 um^2
[INFO GPL-0018] Movable instances area:      50614.794 um^2
[INFO GPL-0019] Utilization:                     1.133 %
[INFO GPL-0020] Standard cells area:         50614.794 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3500
[INFO GPL-0024] Movable insts average area:      8.420 um^2
[INFO GPL-0025] Ideal bin area:                 24.058 um^2
[INFO GPL-0026] Ideal bin count:                235135
[INFO GPL-0027] Total bin area:             5656927.942 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.295 *  9.286 um
>>>>>>> 2e9d213 (added assets)
[INFO GPL-0030] Number of bins:                  65536
[INFO GPL-0007] Execute nesterov global placement.
[INFO GPL-0031] HPWL: Half-Perimeter Wirelength
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
<<<<<<< HEAD
        0 |   0.9979 |  2.095375e+04 |   +0.00% |  9.09e-17 |      
       10 |   0.9902 |  2.545788e+04 |  +21.50% |  1.48e-16 |      
       20 |   0.9880 |  2.744306e+04 |   +7.80% |  2.41e-16 |      
       30 |   0.9875 |  2.826940e+04 |   +3.01% |  3.92e-16 |      
       40 |   0.9866 |  2.913294e+04 |   +3.05% |  6.39e-16 |      
       50 |   0.9854 |  2.991576e+04 |   +2.69% |  1.04e-15 |      
       60 |   0.9842 |  3.041927e+04 |   +1.68% |  1.69e-15 |      
       70 |   0.9828 |  3.059728e+04 |   +0.59% |  2.76e-15 |      
       80 |   0.9816 |  3.049286e+04 |   -0.34% |  4.50e-15 |      
       90 |   0.9798 |  3.023844e+04 |   -0.83% |  7.32e-15 |      
      100 |   0.9773 |  2.993773e+04 |   -0.99% |  1.19e-14 |      
      110 |   0.9750 |  2.959752e+04 |   -1.14% |  1.94e-14 |      
      120 |   0.9736 |  2.920040e+04 |   -1.34% |  3.17e-14 |      
      130 |   0.9722 |  2.876079e+04 |   -1.51% |  5.16e-14 |      
      140 |   0.9698 |  2.831981e+04 |   -1.53% |  8.40e-14 |      
      150 |   0.9682 |  2.792712e+04 |   -1.39% |  1.37e-13 |      
      160 |   0.9667 |  2.769282e+04 |   -0.84% |  2.23e-13 |      
      170 |   0.9663 |  2.778445e+04 |   +0.33% |  3.63e-13 |      
      180 |   0.9660 |  2.845621e+04 |   +2.42% |  5.91e-13 |      
      190 |   0.9654 |  3.006494e+04 |   +5.65% |  9.63e-13 |      
      200 |   0.9627 |  3.359092e+04 |  +11.73% |  1.57e-12 |      
      210 |   0.9605 |  4.128114e+04 |  +22.89% |  2.55e-12 |      
      220 |   0.9556 |  5.389911e+04 |  +30.57% |  4.15e-12 |      
      230 |   0.9554 |  7.518514e+04 |  +39.49% |  6.75e-12 |      
      240 |   0.9570 |  1.078004e+05 |  +43.38% |  1.10e-11 |      
      250 |   0.9726 |  1.475729e+05 |  +36.89% |  1.78e-11 |      
      260 |   0.9839 |  1.474293e+05 |   -0.10% |  2.89e-11 |      
      270 |   0.9896 |  1.372298e+05 |   -6.92% |  4.70e-11 |      
      280 |   0.9896 |  2.173756e+05 |  +58.40% |  7.59e-11 |      
      290 |   0.9867 |  1.945761e+05 |  -10.49% |  1.24e-10 |      
      300 |   0.9563 |  2.266253e+05 |  +16.47% |  2.00e-10 |      
      310 |   0.9036 |  2.594064e+05 |  +14.46% |  3.25e-10 |      
      320 |   0.8321 |  2.645941e+05 |   +2.00% |  5.29e-10 |      
      330 |   0.7308 |  2.401286e+05 |   -9.25% |  8.61e-10 |      
      340 |   0.6261 |  2.367808e+05 |   -1.39% |  1.40e-09 |      
      350 |   0.5688 |  2.484760e+05 |   +4.94% |  2.28e-09 |      
      360 |   0.4950 |  2.590026e+05 |   +4.24% |  3.70e-09 |      
      370 |   0.4367 |  2.726512e+05 |   +5.27% |  6.02e-09 |      
      380 |   0.3735 |  2.802581e+05 |   +2.79% |  9.75e-09 |      
      390 |   0.3306 |  2.778399e+05 |   -0.86% |  1.54e-08 |      
      400 |   0.3052 |  2.638243e+05 |   -5.04% |  2.27e-08 |      
      410 |   0.2771 |  2.504232e+05 |   -5.08% |  3.34e-08 |      
      420 |   0.2391 |  2.493461e+05 |   -0.43% |  4.92e-08 |      
      430 |   0.2017 |  2.460936e+05 |   -1.30% |  7.25e-08 |      
      440 |   0.1772 |  2.412782e+05 |   -1.96% |  1.07e-07 |      
      450 |   0.1506 |  2.411547e+05 |   -0.05% |  1.57e-07 |      
      460 |   0.1305 |  2.354898e+05 |   -2.35% |  2.32e-07 |      
      470 |   0.1101 |  2.347046e+05 |   -0.33% |  3.41e-07 |      
      478 |   0.0981 |  2.313246e+05 |          |  4.84e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 478
[INFO GPL-1002] Placed Cell Area            50614.7936
[INFO GPL-1003] Available Free Area         4836335.9296
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0116
[INFO GPL-1008]     - For 80% usage of free space: 0.0131
[INFO GPL-1009]     - For 50% usage of free space: 0.0209
[INFO GPL-1014] Final placement area: 50614.79 (+0.00%)
Took 24 seconds: global_placement -skip_io -density "0.30   " -pad_left 0 -pad_right 0
Elapsed time: 0:24.76[h:]min:sec. CPU time: user 94.87 sys 0.56 (385%). Peak memory: 235608KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_1_place_gp_skip_io              24            230 f12c09e2a298dbca3568
=======
        0 |   0.9998 |  2.120251e+04 |   +0.00% |  8.52e-17 |      
       10 |   0.9965 |  2.752583e+04 |  +29.82% |  1.39e-16 |      
       20 |   0.9962 |  2.974628e+04 |   +8.07% |  2.26e-16 |      
       30 |   0.9959 |  3.085248e+04 |   +3.72% |  3.68e-16 |      
       40 |   0.9956 |  3.199463e+04 |   +3.70% |  5.99e-16 |      
       50 |   0.9950 |  3.296396e+04 |   +3.03% |  9.76e-16 |      
       60 |   0.9946 |  3.356710e+04 |   +1.83% |  1.59e-15 |      
       70 |   0.9943 |  3.377393e+04 |   +0.62% |  2.59e-15 |      
       80 |   0.9940 |  3.365488e+04 |   -0.35% |  4.22e-15 |      
       90 |   0.9937 |  3.337232e+04 |   -0.84% |  6.87e-15 |      
      100 |   0.9932 |  3.304125e+04 |   -0.99% |  1.12e-14 |      
      110 |   0.9927 |  3.266136e+04 |   -1.15% |  1.82e-14 |      
      120 |   0.9917 |  3.219377e+04 |   -1.43% |  2.97e-14 |      
      130 |   0.9904 |  3.165576e+04 |   -1.67% |  4.83e-14 |      
      140 |   0.9883 |  3.109557e+04 |   -1.77% |  7.88e-14 |      
      150 |   0.9861 |  3.057767e+04 |   -1.67% |  1.28e-13 |      
      160 |   0.9838 |  3.018440e+04 |   -1.29% |  2.09e-13 |      
      170 |   0.9774 |  3.006197e+04 |   -0.41% |  3.40e-13 |      
      180 |   0.9696 |  3.047429e+04 |   +1.37% |  5.54e-13 |      
      190 |   0.9655 |  3.179110e+04 |   +4.32% |  9.03e-13 |      
      200 |   0.9578 |  3.473274e+04 |   +9.25% |  1.47e-12 |      
      210 |   0.9512 |  4.165985e+04 |  +19.94% |  2.39e-12 |      
      220 |   0.9443 |  5.318363e+04 |  +27.66% |  3.89e-12 |      
      230 |   0.9312 |  7.443238e+04 |  +39.95% |  6.33e-12 |      
      240 |   0.9135 |  1.118449e+05 |  +50.26% |  1.03e-11 |      
      250 |   0.8886 |  2.018674e+05 |  +80.49% |  1.66e-11 |      
      260 |   0.8745 |  2.118636e+05 |   +4.95% |  2.69e-11 |      
      270 |   0.8625 |  1.610257e+05 |  -24.00% |  4.38e-11 |      
      280 |   0.8206 |  2.434265e+05 |  +51.17% |  7.08e-11 |      
      290 |   0.7836 |  3.162244e+05 |  +29.91% |  1.14e-10 |      
      300 |   0.7464 |  2.773986e+05 |  -12.28% |  1.86e-10 |      
      310 |   0.7053 |  2.856162e+05 |   +2.96% |  3.01e-10 |      
      320 |   0.6460 |  3.274001e+05 |  +14.63% |  4.87e-10 |      
      330 |   0.6396 |  2.552076e+05 |  -22.05% |  7.89e-10 |      
      340 |   0.5793 |  2.655565e+05 |   +4.06% |  1.27e-09 |      
      350 |   0.5422 |  2.526233e+05 |   -4.87% |  2.06e-09 |      
      360 |   0.4781 |  2.448540e+05 |   -3.08% |  3.34e-09 |      
      370 |   0.4355 |  2.357241e+05 |   -3.73% |  5.42e-09 |      
      380 |   0.3859 |  2.278432e+05 |   -3.34% |  8.81e-09 |      
      390 |   0.3398 |  2.158486e+05 |   -5.26% |  1.37e-08 |      
      400 |   0.3012 |  2.118594e+05 |   -1.85% |  2.02e-08 |      
      410 |   0.2659 |  2.068951e+05 |   -2.34% |  2.98e-08 |      
      420 |   0.2330 |  1.986935e+05 |   -3.96% |  4.38e-08 |      
      430 |   0.2009 |  1.928986e+05 |   -2.92% |  6.45e-08 |      
      440 |   0.1751 |  1.866400e+05 |   -3.24% |  9.50e-08 |      
      450 |   0.1481 |  1.829250e+05 |   -1.99% |  1.40e-07 |      
      460 |   0.1284 |  1.803021e+05 |   -1.43% |  2.06e-07 |      
      470 |   0.1083 |  1.777042e+05 |   -1.44% |  3.04e-07 |      
      474 |   0.0997 |  1.766204e+05 |          |  3.69e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 474
[INFO GPL-1002] Placed Cell Area            50614.7936
[INFO GPL-1003] Available Free Area         4465462.7328
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0126
[INFO GPL-1008]     - For 80% usage of free space: 0.0142
[INFO GPL-1009]     - For 50% usage of free space: 0.0227
[INFO GPL-1014] Final placement area: 50614.79 (+0.00%)
Took 32 seconds: global_placement -skip_io -density "0.35   " -pad_left 0 -pad_right 0
Elapsed time: 0:33.34[h:]min:sec. CPU time: user 111.60 sys 0.58 (336%). Peak memory: 247816KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_1_place_gp_skip_io              33            242 79d6ed7c3bab88d508f2
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_2_place_iop io_placement
Running io_placement.tcl, stage 3_2_place_iop
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_1_place_gp_skip_io.odb
place_pins -hor_layers met3 -ver_layers met2
Found 2 macro blocks.
Using 2 tracks default min distance between IO pins.
[INFO PPL-0001] Number of available slots 9100
[INFO PPL-0002] Number of I/O             7
[INFO PPL-0003] Number of I/O w/sink      7
[INFO PPL-0004] Number of I/O w/o sink    0
[INFO PPL-0005] Slots per section         200
[INFO PPL-0008] Successfully assigned pins to sections.
<<<<<<< HEAD
[INFO PPL-0012] I/O nets HPWL: 773.24 um.
Elapsed time: 0:00.83[h:]min:sec. CPU time: user 0.68 sys 0.15 (100%). Peak memory: 195880KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_2_place_iop                      0            191 4ed86b7d412b3a698a4a
=======
[INFO PPL-0012] I/O nets HPWL: 1036.25 um.
Elapsed time: 0:01.16[h:]min:sec. CPU time: user 0.95 sys 0.21 (99%). Peak memory: 203160KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_2_place_iop                      1            198 9e5a03a46f9265d68b07
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_3_place_gp global_place
Running global_place.tcl, stage 3_3_place_gp
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_2_place_iop.odb
[INFO RSZ-0026] Removed 0 buffers.
Perform port buffering...
[INFO RSZ-0027] Inserted 6 sky130_fd_sc_hd__clkdlybuf4s50_1 input buffers.
[INFO RSZ-0028] Inserted 1 sky130_fd_sc_hd__clkdlybuf4s50_1 output buffers.
<<<<<<< HEAD
global_placement -density "0.30   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             76056
[INFO GPL-0007] Movable instances:                6018
[INFO GPL-0008] Fixed instances:                 67624
[INFO GPL-0009] Dummy instances:                  2414
[INFO GPL-0010] Number of nets:                   6130
[INFO GPL-0011] Number of pins:                  21892
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0016] Core area:                  5750736.662 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5750736.662 um^2
[INFO GPL-0017] Fixed instances area:       914400.733 um^2
[INFO GPL-0018] Movable instances area:      50684.861 um^2
[INFO GPL-0019] Utilization:                     1.048 %
[INFO GPL-0020] Standard cells area:         50684.861 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[InitialPlace]  Iter: 1 conjugate gradient residual: 0.00653910 HPWL: 287675213
[InitialPlace]  Iter: 2 conjugate gradient residual: 0.23018758 HPWL: 78558390
[InitialPlace]  Iter: 3 conjugate gradient residual: 0.00563520 HPWL: 92486771
[InitialPlace]  Iter: 4 conjugate gradient residual: 0.02219049 HPWL: 87530313
[InitialPlace]  Iter: 5 conjugate gradient residual: 0.32454821 HPWL: 76060515
[InitialPlace]  Iter: 6 conjugate gradient residual: 0.00563520 HPWL: 92632074
[InitialPlace]  Iter: 7 conjugate gradient residual: 0.02219049 HPWL: 87615072
[InitialPlace]  Iter: 8 conjugate gradient residual: 0.32454821 HPWL: 76123289
[InitialPlace]  Iter: 9 conjugate gradient residual: 0.00563520 HPWL: 92666915
[InitialPlace]  Iter: 10 conjugate gradient residual: 0.02219049 HPWL: 87650955
[InitialPlace]  Iter: 11 conjugate gradient residual: 0.32454821 HPWL: 76134881
[InitialPlace]  Iter: 12 conjugate gradient residual: 0.00563520 HPWL: 92683112
[InitialPlace]  Iter: 13 conjugate gradient residual: 0.02219049 HPWL: 87656430
[InitialPlace]  Iter: 14 conjugate gradient residual: 0.32454821 HPWL: 76147280
[InitialPlace]  Iter: 15 conjugate gradient residual: 0.00563520 HPWL: 92682789
[InitialPlace]  Iter: 16 conjugate gradient residual: 0.02219049 HPWL: 87663060
[InitialPlace]  Iter: 17 conjugate gradient residual: 0.32454821 HPWL: 76146091
[InitialPlace]  Iter: 18 conjugate gradient residual: 0.00563520 HPWL: 92696022
[InitialPlace]  Iter: 19 conjugate gradient residual: 0.02219049 HPWL: 87658091
[InitialPlace]  Iter: 20 conjugate gradient residual: 0.32454821 HPWL: 76156010
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3000
[INFO GPL-0024] Movable insts average area:      8.422 um^2
[INFO GPL-0025] Ideal bin area:                 28.074 um^2
[INFO GPL-0026] Ideal bin count:                204841
[INFO GPL-0027] Total bin area:             5750736.662 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.374 *  9.361 um
=======
global_placement -density "0.35   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 20.240 21.760 ) ( 2399.820 2399.040 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             79015
[INFO GPL-0007] Movable instances:                6018
[INFO GPL-0008] Fixed instances:                 66581
[INFO GPL-0009] Dummy instances:                  6416
[INFO GPL-0010] Number of nets:                   6130
[INFO GPL-0011] Number of pins:                  21892
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 20.240 21.760 ) ( 2399.820 2399.040 ) um
[INFO GPL-0016] Core area:                  5656927.942 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5656927.942 um^2
[INFO GPL-0017] Fixed instances area:       1191465.210 um^2
[INFO GPL-0018] Movable instances area:      50684.861 um^2
[INFO GPL-0019] Utilization:                     1.135 %
[INFO GPL-0020] Standard cells area:         50684.861 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[InitialPlace]  Iter: 1 conjugate gradient residual: 0.00725655 HPWL: 235496996
[InitialPlace]  Iter: 2 conjugate gradient residual: 0.03389857 HPWL: 76528751
[InitialPlace]  Iter: 3 conjugate gradient residual: 0.00158494 HPWL: 73532509
[InitialPlace]  Iter: 4 conjugate gradient residual: 0.00158494 HPWL: 73778479
[InitialPlace]  Iter: 5 conjugate gradient residual: 0.00158494 HPWL: 73833695
[InitialPlace]  Iter: 6 conjugate gradient residual: 0.00158494 HPWL: 73903974
[InitialPlace]  Iter: 7 conjugate gradient residual: 0.00158494 HPWL: 73884910
[InitialPlace]  Iter: 8 conjugate gradient residual: 0.00158494 HPWL: 73924196
[InitialPlace]  Iter: 9 conjugate gradient residual: 0.00158494 HPWL: 73918202
[InitialPlace]  Iter: 10 conjugate gradient residual: 0.00158494 HPWL: 73945436
[InitialPlace]  Iter: 11 conjugate gradient residual: 0.00158494 HPWL: 73926964
[InitialPlace]  Iter: 12 conjugate gradient residual: 0.00158494 HPWL: 73949644
[InitialPlace]  Iter: 13 conjugate gradient residual: 0.00158494 HPWL: 73948052
[InitialPlace]  Iter: 14 conjugate gradient residual: 0.00158494 HPWL: 73956849
[InitialPlace]  Iter: 15 conjugate gradient residual: 0.00158494 HPWL: 73943427
[InitialPlace]  Iter: 16 conjugate gradient residual: 0.00158494 HPWL: 73970016
[InitialPlace]  Iter: 17 conjugate gradient residual: 0.00158494 HPWL: 73953860
[InitialPlace]  Iter: 18 conjugate gradient residual: 0.00158494 HPWL: 73972995
[InitialPlace]  Iter: 19 conjugate gradient residual: 0.00158494 HPWL: 73959516
[InitialPlace]  Iter: 20 conjugate gradient residual: 0.00158494 HPWL: 73977079
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3500
[INFO GPL-0024] Movable insts average area:      8.422 um^2
[INFO GPL-0025] Ideal bin area:                 24.063 um^2
[INFO GPL-0026] Ideal bin count:                235083
[INFO GPL-0027] Total bin area:             5656927.942 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.295 *  9.286 um
>>>>>>> 2e9d213 (added assets)
[INFO GPL-0030] Number of bins:                  65536
[INFO GPL-0007] Execute nesterov global placement.
[INFO GPL-0031] HPWL: Half-Perimeter Wirelength
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
<<<<<<< HEAD
        0 |   0.9908 |  4.976842e+04 |   +0.00% |  9.77e-17 |      
       10 |   0.9618 |  6.724293e+04 |  +35.11% |  1.59e-16 |      
       20 |   0.9440 |  7.854263e+04 |  +16.80% |  2.58e-16 |      
       30 |   0.9292 |  8.500514e+04 |   +8.23% |  4.20e-16 |      
       40 |   0.9218 |  8.791584e+04 |   +3.42% |  6.84e-16 |      
       50 |   0.9188 |  8.963614e+04 |   +1.96% |  1.11e-15 |      
       60 |   0.9139 |  9.111692e+04 |   +1.65% |  1.82e-15 |      
       70 |   0.9138 |  9.180305e+04 |   +0.75% |  2.96e-15 |      
       80 |   0.9120 |  9.180828e+04 |   +0.01% |  4.82e-15 |      
       90 |   0.9148 |  9.165874e+04 |   -0.16% |  7.84e-15 |      
      100 |   0.9146 |  9.163052e+04 |   -0.03% |  1.28e-14 |      
      110 |   0.9117 |  9.158849e+04 |   -0.05% |  2.08e-14 |      
      120 |   0.9165 |  9.106959e+04 |   -0.57% |  3.39e-14 |      
      130 |   0.9165 |  9.026998e+04 |   -0.88% |  5.52e-14 |      
      140 |   0.9160 |  8.925345e+04 |   -1.13% |  8.99e-14 |      
      150 |   0.9150 |  8.801194e+04 |   -1.39% |  1.47e-13 |      
      160 |   0.9163 |  8.702879e+04 |   -1.12% |  2.39e-13 |      
      170 |   0.9157 |  8.629281e+04 |   -0.85% |  3.89e-13 |      
      180 |   0.9164 |  8.580975e+04 |   -0.56% |  6.33e-13 |      
      190 |   0.9175 |  8.558260e+04 |   -0.26% |  1.03e-12 |      
      200 |   0.9171 |  8.609151e+04 |   +0.59% |  1.68e-12 |      
      210 |   0.9154 |  8.751491e+04 |   +1.65% |  2.74e-12 |      
      220 |   0.9098 |  9.191582e+04 |   +5.03% |  4.45e-12 |      
      230 |   0.9006 |  1.017777e+05 |  +10.73% |  7.25e-12 |      
      240 |   0.8832 |  1.221720e+05 |  +20.04% |  1.18e-11 |      
      250 |   0.8586 |  1.667123e+05 |  +36.46% |  1.91e-11 |      
      260 |   0.8432 |  1.887292e+05 |  +13.21% |  3.10e-11 |      
      270 |   0.8324 |  1.605502e+05 |  -14.93% |  5.05e-11 |      
      280 |   0.8011 |  1.955534e+05 |  +21.80% |  8.20e-11 |      
      290 |   0.8059 |  2.404736e+05 |  +22.97% |  1.33e-10 |      
      300 |   0.7883 |  2.306181e+05 |   -4.10% |  2.16e-10 |      
      310 |   0.7346 |  2.455045e+05 |   +6.46% |  3.50e-10 |      
      320 |   0.6631 |  2.801927e+05 |  +14.13% |  5.67e-10 |      
      330 |   0.6328 |  2.490522e+05 |  -11.11% |  9.22e-10 |      
[INFO GPL-0100] Timing-driven iteration 1/2, virtual: false.
[INFO GPL-0101]    Iter: 331, overflow: 0.633, keep resizer changes at: 1, HPWL: 249052200
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6134
    final |     +0.3% |      87 |     122 |            86 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 88 slew violations.
[INFO RSZ-0036] Found 28 capacitance violations.
[INFO RSZ-0039] Resized 87 instances.
[INFO RSZ-0038] Inserted 122 buffers in 86 nets.
=======
        0 |   0.9903 |  2.097455e+04 |   +0.00% |  6.41e-17 |      
       10 |   0.9743 |  2.539897e+04 |  +21.09% |  1.04e-16 |      
       20 |   0.9694 |  2.739376e+04 |   +7.85% |  1.70e-16 |      
       30 |   0.9683 |  2.801395e+04 |   +2.26% |  2.77e-16 |      
       40 |   0.9670 |  2.885631e+04 |   +3.01% |  4.51e-16 |      
       50 |   0.9655 |  2.957352e+04 |   +2.49% |  7.34e-16 |      
       60 |   0.9632 |  3.004426e+04 |   +1.59% |  1.20e-15 |      
       70 |   0.9630 |  3.027443e+04 |   +0.77% |  1.95e-15 |      
       80 |   0.9641 |  3.028910e+04 |   +0.05% |  3.17e-15 |      
       90 |   0.9637 |  3.020206e+04 |   -0.29% |  5.17e-15 |      
      100 |   0.9635 |  3.011206e+04 |   -0.30% |  8.42e-15 |      
      110 |   0.9621 |  3.002035e+04 |   -0.30% |  1.37e-14 |      
      120 |   0.9620 |  2.990430e+04 |   -0.39% |  2.23e-14 |      
      130 |   0.9646 |  2.975749e+04 |   -0.49% |  3.64e-14 |      
      140 |   0.9638 |  2.959528e+04 |   -0.55% |  5.93e-14 |      
      150 |   0.9655 |  2.945200e+04 |   -0.48% |  9.65e-14 |      
      160 |   0.9631 |  2.939535e+04 |   -0.19% |  1.57e-13 |      
      170 |   0.9636 |  2.953635e+04 |   +0.48% |  2.56e-13 |      
      180 |   0.9649 |  3.001201e+04 |   +1.61% |  4.17e-13 |      
      190 |   0.9622 |  3.105117e+04 |   +3.46% |  6.80e-13 |      
      200 |   0.9614 |  3.308982e+04 |   +6.57% |  1.11e-12 |      
      210 |   0.9574 |  3.793376e+04 |  +14.64% |  1.80e-12 |      
      220 |   0.9494 |  4.638450e+04 |  +22.28% |  2.93e-12 |      
      230 |   0.9348 |  6.136334e+04 |  +32.29% |  4.77e-12 |      
      240 |   0.9163 |  8.804829e+04 |  +43.49% |  7.75e-12 |      
      250 |   0.8948 |  1.350500e+05 |  +53.38% |  1.26e-11 |      
      260 |   0.8777 |  1.939672e+05 |  +43.63% |  2.03e-11 |      
      270 |   0.8648 |  1.695725e+05 |  -12.58% |  3.31e-11 |      
      280 |   0.8440 |  1.679648e+05 |   -0.95% |  5.38e-11 |      
      290 |   0.7930 |  2.866529e+05 |  +70.66% |  8.65e-11 |      
      300 |   0.7725 |  2.873562e+05 |   +0.25% |  1.40e-10 |      
      310 |   0.7075 |  3.190044e+05 |  +11.01% |  2.28e-10 |      
      320 |   0.6912 |  2.646727e+05 |  -17.03% |  3.70e-10 |      
      330 |   0.6371 |  3.319682e+05 |  +25.43% |  5.97e-10 |      
[INFO GPL-0100] Timing-driven iteration 1/2, virtual: false.
[INFO GPL-0101]    Iter: 336, overflow: 0.634, keep resizer changes at: 1, HPWL: 271905760
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6134
    final |     +0.3% |      68 |     110 |            77 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 69 slew violations.
[INFO RSZ-0036] Found 36 capacitance violations.
[INFO RSZ-0039] Resized 68 instances.
[INFO RSZ-0038] Inserted 110 buffers in 77 nets.
>>>>>>> 2e9d213 (added assets)
   Iter   |    Area   | Removed | Inserted |   Pins
          |           | Buffers | Buffers  | Remaining
-------------------------------------------------------
        0 |     +0.0% |       0 |        0 |      6119
<<<<<<< HEAD
      610 |     +0.0% |       1 |       20 |      5509
     1220 |     +0.0% |       1 |       30 |      4899
     1830 |     +0.0% |      14 |       55 |      4289
     2440 |     +0.0% |      21 |       59 |      3679
     3050 |     +0.0% |      21 |       61 |      3069
     3660 |     +0.0% |      21 |       68 |      2459
     4270 |     +0.0% |      21 |       84 |      1849
     4880 |     -0.0% |     104 |      147 |      1239
     5490 |     -0.1% |     122 |      175 |       629
     6100 |     -0.1% |     122 |      175 |        19
    final |     -0.1% |     122 |      176 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 5.56e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 1700.381 um^2 (+3.35%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 176 (+2.92%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 298, deleted: 122
[INFO GPL-0110] Timing-driven: new target density: 0.3003516
[INFO GPL-0038] Routability snapshot saved at iter = 340
      339 |   0.5898 |  2.017842e+05 |          |           |      
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      340 |   0.5836 |  1.921580e+05 |  -22.84% |  1.49e-09 |      
      350 |   0.5372 |  2.009130e+05 |   +4.56% |  2.43e-09 |      
      360 |   0.4893 |  1.994643e+05 |   -0.72% |  3.96e-09 |      
      370 |   0.4348 |  2.017182e+05 |   +1.13% |  6.44e-09 |      
      380 |   0.3812 |  2.021531e+05 |   +0.22% |  1.05e-08 |      
      390 |   0.3420 |  2.003572e+05 |   -0.89% |  1.69e-08 |      
      400 |   0.3000 |  1.992007e+05 |   -0.58% |  2.49e-08 |      
[INFO GPL-0040] Routability iteration: 1
[INFO GPL-0041] Total routing overflow: 43.4048
[INFO GPL-0042] Number of overflowed tiles: 10763 (8.21%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0322
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0193
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0119
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0062
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0257
[INFO GPL-0048] Routing congestion (1.0257) lower than previous minimum (1e+30). Updating minimum.
[INFO GPL-0051] Inflated area:                1610.268 um^2 (+3.07%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174978, After: 174777 (-0.11%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1400215.988, After: 1398607.500 (-0.11%)
[INFO GPL-0078] Removed fillers count: 201, area removed: 1608.450 um^2. Remaining area to be compensated by modifying density: 1.818 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1398607.500 um^2 (-0.11%)
[INFO GPL-0061] Total non-inflated area:    1452603.010 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1454213.278 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      410 |   0.5478 |  1.993159e+05 |   +0.06% |  2.04e-09 |      
      420 |   0.5262 |  1.983646e+05 |   -0.48% |  3.00e-09 |      
      430 |   0.4763 |  2.025039e+05 |   +2.09% |  4.41e-09 |      
      440 |   0.4359 |  2.034311e+05 |   +0.46% |  6.50e-09 |      
      450 |   0.3931 |  2.018617e+05 |   -0.77% |  9.57e-09 |      
      460 |   0.3598 |  1.998825e+05 |   -0.98% |  1.41e-08 |      
      470 |   0.3192 |  1.982064e+05 |   -0.84% |  2.08e-08 |      
[INFO GPL-0040] Routability iteration: 2
[INFO GPL-0041] Total routing overflow: 32.2107
[INFO GPL-0042] Number of overflowed tiles: 10716 (8.18%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0154
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0109
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0079
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0045
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0132
[INFO GPL-0048] Routing congestion (1.0132) lower than previous minimum (1.026). Updating minimum.
[INFO GPL-0051] Inflated area:                 471.126 um^2 (+0.87%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174777, After: 174719 (-0.03%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1398607.500, After: 1398143.371 (-0.03%)
[INFO GPL-0078] Removed fillers count: 58, area removed: 464.130 um^2. Remaining area to be compensated by modifying density: 6.996 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1398143.371 um^2 (-0.03%)
[INFO GPL-0061] Total non-inflated area:    1452610.007 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1453081.133 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      480 |   0.5712 |  1.975667e+05 |   -0.32% |  1.68e-09 |      
      490 |   0.5409 |  2.025809e+05 |   +2.54% |  2.47e-09 |      
      500 |   0.5009 |  2.027038e+05 |   +0.06% |  3.64e-09 |      
      510 |   0.4608 |  2.020927e+05 |   -0.30% |  5.36e-09 |      
      520 |   0.4207 |  2.016324e+05 |   -0.23% |  7.89e-09 |      
      530 |   0.3752 |  2.000371e+05 |   -0.79% |  1.16e-08 |      
      540 |   0.3382 |  2.000883e+05 |   +0.03% |  1.71e-08 |      
      550 |   0.3029 |  1.981472e+05 |   -0.97% |  2.52e-08 |      
[INFO GPL-0040] Routability iteration: 3
[INFO GPL-0041] Total routing overflow: 30.7762
[INFO GPL-0042] Number of overflowed tiles: 10706 (8.17%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0135
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0100
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0074
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0043
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0118
[INFO GPL-0048] Routing congestion (1.0118) lower than previous minimum (1.013). Updating minimum.
[INFO GPL-0051] Inflated area:                 365.972 um^2 (+0.67%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174719, After: 174674 (-0.03%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1398143.371, After: 1397783.270 (-0.03%)
[INFO GPL-0078] Removed fillers count: 45, area removed: 360.101 um^2. Remaining area to be compensated by modifying density: 5.871 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1397783.270 um^2 (-0.03%)
[INFO GPL-0061] Total non-inflated area:    1452615.878 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1452981.849 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      560 |   0.5475 |  2.011210e+05 |   +1.50% |  2.03e-09 |      
      570 |   0.5282 |  2.002228e+05 |   -0.45% |  3.00e-09 |      
      580 |   0.4769 |  2.045762e+05 |   +2.17% |  4.41e-09 |      
      590 |   0.4381 |  2.056135e+05 |   +0.51% |  6.50e-09 |      
      600 |   0.3929 |  2.042239e+05 |   -0.68% |  9.57e-09 |      
      610 |   0.3612 |  2.019504e+05 |   -1.11% |  1.41e-08 |      
      620 |   0.3175 |  2.011824e+05 |   -0.38% |  2.08e-08 |      
[INFO GPL-0040] Routability iteration: 4
[INFO GPL-0041] Total routing overflow: 28.9371
[INFO GPL-0042] Number of overflowed tiles: 10684 (8.15%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0108
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0086
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0067
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0040
=======
      610 |     +0.0% |       2 |       18 |      5509
     1220 |     +0.0% |       2 |       28 |      4899
     1830 |     +0.0% |      15 |       58 |      4289
     2440 |     +0.0% |      22 |       62 |      3679
     3050 |     +0.0% |      22 |       64 |      3069
     3660 |     +0.0% |      22 |       71 |      2459
     4270 |     +0.0% |      29 |       88 |      1849
     4880 |     -0.0% |      94 |      144 |      1239
     5490 |     -0.1% |     110 |      172 |       629
     6100 |     -0.1% |     110 |      172 |        19
    final |     -0.1% |     110 |      172 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 5.4e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 1614.048 um^2 (+3.18%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 172 (+2.86%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 282, deleted: 110
[INFO GPL-0110] Timing-driven: new target density: 0.35036144
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      340 |   0.6392 |  1.852033e+05 |  -44.21% |  9.70e-10 |      
[INFO GPL-0038] Routability snapshot saved at iter = 346
      345 |   0.5973 |  1.921652e+05 |          |           |      
      350 |   0.5658 |  1.862392e+05 |   +0.56% |  1.58e-09 |      
      360 |   0.5243 |  1.943059e+05 |   +4.33% |  2.56e-09 |      
      370 |   0.4748 |  1.921539e+05 |   -1.11% |  4.18e-09 |      
      380 |   0.4111 |  1.940483e+05 |   +0.99% |  6.80e-09 |      
      390 |   0.3676 |  1.945961e+05 |   +0.28% |  1.11e-08 |      
      400 |   0.3260 |  1.916011e+05 |   -1.54% |  1.71e-08 |      
[INFO GPL-0040] Routability iteration: 1
[INFO GPL-0041] Total routing overflow: 48.3675
[INFO GPL-0042] Number of overflowed tiles: 1457 (1.11%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0716
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0368
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0185
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0074
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0542
[INFO GPL-0048] Routing congestion (1.0542) lower than previous minimum (1e+30). Updating minimum.
[INFO GPL-0051] Inflated area:                4369.971 um^2 (+8.36%)
[INFO GPL-0052] Placement target density:       0.3504
[INFO GPL-0076] Removing fillers, count: Before: 188975, After: 188429 (-0.29%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1512226.973, After: 1507854.081 (-0.29%)
[INFO GPL-0078] Removed fillers count: 546, area removed: 4369.223 um^2. Remaining area to be compensated by modifying density: 0.748 um^2
[INFO GPL-0058] White space area:           4465462.733 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1564525.855 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1507854.081 um^2 (-0.29%)
[INFO GPL-0061] Total non-inflated area:    1564522.960 um^2 (-0.00%)
[INFO GPL-0062] Total inflated area:        1568892.931 um^2 (-0.00%)
[INFO GPL-0063] New Target Density:             0.3504
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      410 |   0.6189 |  1.910626e+05 |   -0.28% |  1.30e-09 |      
      420 |   0.5441 |  1.983916e+05 |   +3.84% |  1.91e-09 |      
      430 |   0.5272 |  1.977737e+05 |   -0.31% |  2.81e-09 |      
      440 |   0.4759 |  2.023660e+05 |   +2.32% |  4.14e-09 |      
      450 |   0.4332 |  1.994909e+05 |   -1.42% |  6.09e-09 |      
      460 |   0.3948 |  1.997112e+05 |   +0.11% |  8.97e-09 |      
      470 |   0.3535 |  1.979890e+05 |   -0.86% |  1.32e-08 |      
      480 |   0.3195 |  1.945380e+05 |   -1.74% |  1.95e-08 |      
[INFO GPL-0040] Routability iteration: 2
[INFO GPL-0041] Total routing overflow: 12.4250
[INFO GPL-0042] Number of overflowed tiles: 1617 (1.23%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0172
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0094
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0047
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0019
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0133
[INFO GPL-0048] Routing congestion (1.0133) lower than previous minimum (1.054). Updating minimum.
[INFO GPL-0051] Inflated area:                 791.639 um^2 (+1.40%)
[INFO GPL-0052] Placement target density:       0.3504
[INFO GPL-0076] Removing fillers, count: Before: 188429, After: 188331 (-0.05%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1507854.081, After: 1507069.861 (-0.05%)
[INFO GPL-0078] Removed fillers count: 98, area removed: 784.220 um^2. Remaining area to be compensated by modifying density: 7.419 um^2
[INFO GPL-0058] White space area:           4465462.733 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1564525.855 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1507069.861 um^2 (-0.05%)
[INFO GPL-0061] Total non-inflated area:    1564530.379 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1565322.018 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3504
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      490 |   0.5793 |  1.980697e+05 |   +1.82% |  1.51e-09 |      
      500 |   0.5325 |  2.057876e+05 |   +3.90% |  2.23e-09 |      
      510 |   0.5136 |  1.989810e+05 |   -3.31% |  3.28e-09 |      
      520 |   0.4550 |  2.015320e+05 |   +1.28% |  4.83e-09 |      
      530 |   0.4218 |  2.004022e+05 |   -0.56% |  7.11e-09 |      
      540 |   0.3738 |  2.015339e+05 |   +0.56% |  1.05e-08 |      
      550 |   0.3451 |  1.983232e+05 |   -1.59% |  1.54e-08 |      
      560 |   0.3050 |  1.961703e+05 |   -1.09% |  2.27e-08 |      
[INFO GPL-0040] Routability iteration: 3
[INFO GPL-0041] Total routing overflow: 9.2577
[INFO GPL-0042] Number of overflowed tiles: 1600 (1.22%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0124
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0070
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0035
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0014
>>>>>>> 2e9d213 (added assets)
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0097
[INFO GPL-0050] Weighted routing congestion is lower than target routing congestion(1.0100), end routability optimization.
[INFO GPL-0090] Routability finished. Target routing congestion achieved succesfully.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
<<<<<<< HEAD
      630 |   0.2867 |  2.001494e+05 |   -0.51% |  3.06e-08 |      
      640 |   0.2503 |  1.999111e+05 |   -0.12% |  4.50e-08 |      
      650 |   0.2183 |  1.992322e+05 |   -0.34% |  6.63e-08 |      
[INFO GPL-0100] Timing-driven iteration 2/2, virtual: false.
[INFO GPL-0101]    Iter: 660, overflow: 0.194, keep resizer changes at: 1, HPWL: 198892194
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6310
    final |     +0.0% |      12 |       3 |             6 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 12 slew violations.
[INFO RSZ-0039] Resized 12 instances.
[INFO RSZ-0038] Inserted 3 buffers in 6 nets.
=======
      570 |   0.2704 |  1.944843e+05 |   -0.86% |  3.35e-08 |      
      580 |   0.2414 |  1.920159e+05 |   -1.27% |  4.93e-08 |      
      590 |   0.2087 |  1.911771e+05 |   -0.44% |  7.26e-08 |      
[INFO GPL-0100] Timing-driven iteration 2/2, virtual: false.
[INFO GPL-0101]    Iter: 597, overflow: 0.193, keep resizer changes at: 1, HPWL: 191330084
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6306
    final |     +0.0% |      10 |       2 |             8 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 10 slew violations.
[INFO RSZ-0039] Resized 10 instances.
[INFO RSZ-0038] Inserted 2 buffers in 8 nets.
>>>>>>> 2e9d213 (added assets)
   Iter   |    Area   | Removed | Inserted |   Pins
          |           | Buffers | Buffers  | Remaining
-------------------------------------------------------
        0 |     +0.0% |       0 |        0 |      6119
<<<<<<< HEAD
      610 |     +0.0% |      20 |       22 |      5509
     1220 |     +0.0% |      32 |       35 |      4899
     1830 |     +0.0% |      58 |       64 |      4289
     2440 |     +0.0% |      62 |       68 |      3679
     3050 |     +0.0% |      64 |       70 |      3069
     3660 |     +0.0% |      71 |       75 |      2459
     4270 |     +0.0% |      87 |       91 |      1849
     4880 |     +0.0% |     150 |      177 |      1239
     5490 |     +0.1% |     178 |      243 |       629
     6100 |     +0.1% |     178 |      243 |        19
    final |     +0.1% |     179 |      244 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 6.05e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 485.851 um^2 (+0.89%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 68 (+1.10%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 247, deleted: 179
[INFO GPL-0110] Timing-driven: new target density: 0.30045506
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      660 |   0.1965 |  2.080790e+05 |   +4.44% |  9.77e-08 |      
      670 |   0.1688 |  2.077660e+05 |   -0.15% |  1.44e-07 |      
      680 |   0.1468 |  2.065307e+05 |   -0.59% |  2.12e-07 |      
      690 |   0.1264 |  2.071016e+05 |   +0.28% |  3.12e-07 |      
      700 |   0.1071 |  2.114310e+05 |   +2.09% |  4.59e-07 |      
      704 |   0.0971 |  2.140167e+05 |          |  5.57e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 704
[INFO GPL-1003] Routability mode iteration count: 284
[INFO GPL-1005] Routability final weighted congestion: 1.0108
[INFO GPL-1002] Placed Cell Area            55318.4590
[INFO GPL-1003] Available Free Area         4836335.9296
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0127
[INFO GPL-1008]     - For 80% usage of free space: 0.0143
[INFO GPL-1009]     - For 50% usage of free space: 0.0229
[INFO GPL-1011] Original area (um^2): 50684.86
[INFO GPL-1012] Total routability artificial inflation: 4147.75 (+8.18%)
[INFO GPL-1013] Total timing-driven delta area: 2186.23 (+4.31%)
[INFO GPL-1014] Final placement area: 55318.46 (+9.14%)
Took 40 seconds: global_placement -density "0.30   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
=======
      610 |     +0.0% |      18 |       24 |      5509
     1220 |     +0.0% |      29 |       42 |      4899
     1830 |     +0.0% |      60 |       82 |      4289
     2440 |     +0.0% |      64 |       87 |      3679
     3050 |     +0.0% |      66 |       90 |      3069
     3660 |     +0.0% |      73 |       94 |      2459
     4270 |     +0.0% |      90 |      114 |      1849
     4880 |     +0.1% |     146 |      195 |      1239
     5490 |     +0.1% |     174 |      249 |       629
     6100 |     +0.1% |     174 |      249 |        19
    final |     +0.1% |     174 |      249 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 5.81e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 477.369 um^2 (+0.83%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 77 (+1.24%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 251, deleted: 174
[INFO GPL-0110] Timing-driven: new target density: 0.35046935
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      600 |   0.1844 |  2.033670e+05 |   +6.38% |  1.07e-07 |      
      610 |   0.1554 |  2.101974e+05 |   +3.36% |  1.57e-07 |      
      620 |   0.1349 |  2.133411e+05 |   +1.50% |  2.32e-07 |      
      630 |   0.1143 |  2.121498e+05 |   -0.56% |  3.41e-07 |      
      639 |   0.0966 |  2.107162e+05 |          |  5.02e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 639
[INFO GPL-1003] Routability mode iteration count: 214
[INFO GPL-1005] Routability final weighted congestion: 1.0043
[INFO GPL-1002] Placed Cell Area            57937.8871
[INFO GPL-1003] Available Free Area         4465462.7328
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0144
[INFO GPL-1008]     - For 80% usage of free space: 0.0162
[INFO GPL-1009]     - For 50% usage of free space: 0.0259
[INFO GPL-1011] Original area (um^2): 50684.86
[INFO GPL-1012] Total routability artificial inflation: 6775.66 (+13.37%)
[INFO GPL-1013] Total timing-driven delta area: 2091.42 (+4.13%)
[INFO GPL-1014] Final placement area: 57937.89 (+14.31%)
Took 48 seconds: global_placement -density "0.35   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
>>>>>>> 2e9d213 (added assets)
Report metrics stage 3, global place...

==========================================================================
global place report_design_area
--------------------------------------------------------------------------
<<<<<<< HEAD
Design area 724551 um^2 13% utilization.
Elapsed time: 0:43.87[h:]min:sec. CPU time: user 155.28 sys 2.41 (359%). Peak memory: 520412KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_3_place_gp                      43            508 cde10683da242de538fe
=======
Design area 724563 um^2 13% utilization.
Elapsed time: 0:52.00[h:]min:sec. CPU time: user 163.13 sys 2.64 (318%). Peak memory: 565032KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_3_place_gp                      52            551 7d0ed6f726713a1d7592
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_4_place_resized resize
Running resize.tcl, stage 3_4_place_resized
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_3_place_gp.odb
Perform buffer insertion and gate resizing...
repair_design -verbose -match_cell_footprint
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
<<<<<<< HEAD
        0 |     +0.0% |       0 |       0 |             0 |      6378
     1000 |     +0.0% |       0 |       0 |             0 |      5378
     2000 |     +0.0% |       0 |       0 |             0 |      4378
     3000 |     +0.0% |       0 |       0 |             0 |      3378
     4000 |     +0.0% |       0 |       0 |             0 |      2378
     5000 |     +0.0% |       0 |       0 |             0 |      1378
     6000 |     +0.0% |       0 |       0 |             0 |       378
    final |     +0.0% |       0 |       0 |             0 |         0
---------------------------------------------------------------------
=======
        0 |     +0.0% |       0 |       0 |             0 |      6383
     1000 |     +0.0% |       0 |       0 |             0 |      5383
     2000 |     +0.0% |       1 |       1 |             1 |      4383
     3000 |     +0.0% |       1 |       1 |             1 |      3383
     4000 |     +0.0% |       1 |       1 |             1 |      2383
     5000 |     +0.0% |       1 |       1 |             1 |      1383
     6000 |     +0.0% |       1 |       1 |             1 |       383
    final |     +0.0% |       1 |       1 |             1 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 1 slew violations.
[INFO RSZ-0039] Resized 1 instances.
[INFO RSZ-0038] Inserted 1 buffers in 1 nets.
>>>>>>> 2e9d213 (added assets)
Floating nets: 
[WARNING RSZ-0020] found 2 floating nets.
Report metrics stage 3, resizer...

==========================================================================
resizer report_design_area
--------------------------------------------------------------------------
<<<<<<< HEAD
Design area 724551 um^2 13% utilization.
Instance count before 73886, after 73886
Pin count before 22377, after 22377
Elapsed time: 0:04.26[h:]min:sec. CPU time: user 4.62 sys 0.67 (124%). Peak memory: 217600KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_4_place_resized                  4            212 cde10683da242de538fe
=======
Design area 724569 um^2 13% utilization.
Instance count before 72848, after 72849
Pin count before 22387, after 22389
Elapsed time: 0:04.90[h:]min:sec. CPU time: user 5.64 sys 0.81 (131%). Peak memory: 224184KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_4_place_resized                  4            218 ddf1cb35eaa9f5dc0184
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_5_place_dp detail_place
Running detail_place.tcl, stage 3_5_place_dp
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_4_place_resized.odb
Placement Analysis
---------------------------------
<<<<<<< HEAD
total displacement      10840.6 u
average displacement        0.1 u
max displacement            9.0 u
original HPWL          211175.5 u
legalized HPWL         217739.8 u
delta HPWL                    3 %
=======
total displacement      10222.6 u
average displacement        0.1 u
max displacement            6.8 u
original HPWL          214719.8 u
legalized HPWL         219704.7 u
delta HPWL                    2 %
>>>>>>> 2e9d213 (added assets)

Detailed placement improvement.
[INFO DPL-0401] Setting random seed to 1.
[INFO DPL-0402] Setting maximum displacement 5 1 to 13600 2720 units.
<<<<<<< HEAD
[INFO DPL-0320] Collected 67848 fixed cells.
[INFO DPL-0318] Collected 6262 single height cells.
[INFO DPL-0321] Collected 0 wide cells.
[INFO DPL-0322] Image (50140, 51680) - (2449960, 2448000)
[INFO DPL-0310] Assigned 6262 cells into segments.  Movement in X-direction is 0.000000, movement in Y-direction is 0.000000.
=======
[INFO DPL-0320] Collected 66804 fixed cells.
[INFO DPL-0318] Collected 6268 single height cells.
[INFO DPL-0321] Collected 0 wide cells.
[INFO DPL-0322] Image (20240, 21760) - (2399820, 2399040)
[INFO DPL-0310] Assigned 6268 cells into segments.  Movement in X-direction is 0.000000, movement in Y-direction is 0.000000.
>>>>>>> 2e9d213 (added assets)
[INFO DPL-0313] Found 0 cells in wrong regions.
[INFO DPL-0315] Found 0 row alignment problems.
[INFO DPL-0314] Found 0 site alignment problems.
[INFO DPL-0311] Found 0 overlaps between adjacent cells.
[INFO DPL-0312] Found 0 edge spacing violations and 0 padding violations.
[INFO DPL-0303] Running algorithm for independent set matching.
[INFO DPL-0300] Set matching objective is wirelength.
<<<<<<< HEAD
[INFO DPL-0301] Pass   1 of matching; objective is 2.163510e+08.
[INFO DPL-0302] End of matching; objective is 2.160306e+08, improvement is 0.15 percent.
[INFO DPL-0303] Running algorithm for global swaps.
[INFO DPL-0306] Pass   1 of global swaps; hpwl is 2.057131e+08.
[INFO DPL-0306] Pass   2 of global swaps; hpwl is 2.039531e+08.
[INFO DPL-0307] End of global swaps; objective is 2.039531e+08, improvement is 5.59 percent.
[INFO DPL-0303] Running algorithm for vertical swaps.
[INFO DPL-0308] Pass   1 of vertical swaps; hpwl is 2.026880e+08.
[INFO DPL-0309] End of vertical swaps; objective is 2.026880e+08, improvement is 0.62 percent.
[INFO DPL-0303] Running algorithm for reordering.
[INFO DPL-0304] Pass   1 of reordering; objective is 2.025227e+08.
[INFO DPL-0305] End of reordering; objective is 2.025227e+08, improvement is 0.08 percent.
=======
[INFO DPL-0301] Pass   1 of matching; objective is 2.280733e+08.
[INFO DPL-0302] End of matching; objective is 2.276109e+08, improvement is 0.20 percent.
[INFO DPL-0303] Running algorithm for global swaps.
[INFO DPL-0306] Pass   1 of global swaps; hpwl is 2.136158e+08.
[INFO DPL-0306] Pass   2 of global swaps; hpwl is 2.116882e+08.
[INFO DPL-0307] End of global swaps; objective is 2.116882e+08, improvement is 7.00 percent.
[INFO DPL-0303] Running algorithm for vertical swaps.
[INFO DPL-0308] Pass   1 of vertical swaps; hpwl is 2.100952e+08.
[INFO DPL-0309] End of vertical swaps; objective is 2.100952e+08, improvement is 0.75 percent.
[INFO DPL-0303] Running algorithm for reordering.
[INFO DPL-0304] Pass   1 of reordering; objective is 2.099013e+08.
[INFO DPL-0305] End of reordering; objective is 2.099013e+08, improvement is 0.09 percent.
>>>>>>> 2e9d213 (added assets)
[INFO DPL-0303] Running algorithm for random improvement.
[INFO DPL-0324] Random improver is using random generator.
[INFO DPL-0325] Random improver is using hpwl objective.
[INFO DPL-0326] Random improver cost string is (a).
<<<<<<< HEAD
[INFO DPL-0332] End of pass, Generator random called 125240 times.
[INFO DPL-0335] Generator random, Cumulative attempts 125240, swaps 8748, moves 49341 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 2.001760e+08, Scratch cost 1.961087e+08, Incremental cost 1.961087e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 1.961087e+08.
[INFO DPL-0327] Pass   1 of random improver; improvement in cost is 2.03 percent.
[INFO DPL-0332] End of pass, Generator random called 125240 times.
[INFO DPL-0335] Generator random, Cumulative attempts 250480, swaps 17086, moves 98360 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 1.961087e+08, Scratch cost 1.947561e+08, Incremental cost 1.947561e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 1.947561e+08.
[INFO DPL-0327] Pass   2 of random improver; improvement in cost is 0.69 percent.
[INFO DPL-0328] End of random improver; improvement is 2.707606 percent.
[INFO DPL-0380] Cell flipping.
[INFO DPL-0382] Changed 0 cell orientations for row compatibility.
[INFO DPL-0383] Performed 1763 cell flips.
[INFO DPL-0384] End of flipping; objective is 1.945031e+08, improvement is 1.32 percent.
=======
[INFO DPL-0332] End of pass, Generator random called 125360 times.
[INFO DPL-0335] Generator random, Cumulative attempts 125360, swaps 9218, moves 47682 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 2.069736e+08, Scratch cost 2.028784e+08, Incremental cost 2.028784e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 2.028784e+08.
[INFO DPL-0327] Pass   1 of random improver; improvement in cost is 1.98 percent.
[INFO DPL-0332] End of pass, Generator random called 125360 times.
[INFO DPL-0335] Generator random, Cumulative attempts 250720, swaps 17998, moves 94940 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 2.028784e+08, Scratch cost 2.015927e+08, Incremental cost 2.015927e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 2.015927e+08.
[INFO DPL-0327] Pass   2 of random improver; improvement in cost is 0.63 percent.
[INFO DPL-0328] End of random improver; improvement is 2.599830 percent.
[INFO DPL-0380] Cell flipping.
[INFO DPL-0382] Changed 0 cell orientations for row compatibility.
[INFO DPL-0383] Performed 1774 cell flips.
[INFO DPL-0384] End of flipping; objective is 2.017500e+08, improvement is 1.35 percent.
>>>>>>> 2e9d213 (added assets)
[INFO DPL-0313] Found 0 cells in wrong regions.
[INFO DPL-0315] Found 0 row alignment problems.
[INFO DPL-0314] Found 0 site alignment problems.
[INFO DPL-0311] Found 0 overlaps between adjacent cells.
[INFO DPL-0312] Found 0 edge spacing violations and 0 padding violations.
Detailed Improvement Results
------------------------------------------
<<<<<<< HEAD
Original HPWL           217739.8 u (  101704.9,   116034.8)
Final HPWL              195899.7 u (   88380.5,   107519.2)
Delta HPWL                 -10.0 % (     -13.1,       -7.3)

[INFO DPL-0020] Mirrored 235 instances
[INFO DPL-0021] HPWL before          195899.7 u
[INFO DPL-0022] HPWL after           195825.4 u
[INFO DPL-0023] HPWL delta               -0.0 %
[WARNING DPL-0010] Blocked layers check failed (1).
 pll
[ERROR DPL-0033] detailed placement checks failed.
Error: detail_place.tcl, 37 DPL-0033
Command exited with non-zero status 1
Elapsed time: 0:03.35[h:]min:sec. CPU time: user 3.04 sys 0.29 (99%). Peak memory: 393768KB.
make[1]: *** [Makefile:469: do-3_5_place_dp] Error 1
make: *** [Makefile:469: results/sky130hd/VSDBabySoC/base/3_5_place_dp.odb] Error 2
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk clean_all
rm -f ./results/sky130hd/VSDBabySoC/base/1_* ./results/sky130hd/VSDBabySoC/base/mem*.json
rm -f ./reports/sky130hd/VSDBabySoC/base/synth_*
rm -f ./logs/sky130hd/VSDBabySoC/base/1_*
rm -f 
rm -f ./results/sky130hd/VSDBabySoC/base/clock_period.txt
rm -f ./results/sky130hd/VSDBabySoC/base/2_*floorplan*.odb ./results/sky130hd/VSDBabySoC/base/2_floorplan.sdc ./results/sky130hd/VSDBabySoC/base/2_*.v ./results/sky130hd/VSDBabySoC/base/2_*.def
rm -f ./reports/sky130hd/VSDBabySoC/base/2_*
rm -f ./logs/sky130hd/VSDBabySoC/base/2_*
rm -f ./results/sky130hd/VSDBabySoC/base/3_*place*.odb
rm -f ./results/sky130hd/VSDBabySoC/base/3_place.sdc
rm -f ./results/sky130hd/VSDBabySoC/base/3_*.def ./results/sky130hd/VSDBabySoC/base/3_*.v
rm -f ./reports/sky130hd/VSDBabySoC/base/3_*
rm -f ./logs/sky130hd/VSDBabySoC/base/3_*
rm -rf ./results/sky130hd/VSDBabySoC/base/4_*cts*.odb ./results/sky130hd/VSDBabySoC/base/4_cts.sdc ./results/sky130hd/VSDBabySoC/base/4_*.v ./results/sky130hd/VSDBabySoC/base/4_*.def
rm -f  ./reports/sky130hd/VSDBabySoC/base/4_*
rm -rf ./logs/sky130hd/VSDBabySoC/base/4_*
rm -rf ./results/sky130hd/VSDBabySoC/base/route.guide ./results/sky130hd/VSDBabySoC/base/output_guide.mod ./results/sky130hd/VSDBabySoC/base/updated_clks.sdc
rm -rf ./results/sky130hd/VSDBabySoC/base/5_*.odb ./results/sky130hd/VSDBabySoC/base/5_route.sdc ./results/sky130hd/VSDBabySoC/base/5_*.def ./results/sky130hd/VSDBabySoC/base/5_*.v
rm -f  ./reports/sky130hd/VSDBabySoC/base/5_*
rm -f  ./logs/sky130hd/VSDBabySoC/base/5_*
rm -rf ./results/sky130hd/VSDBabySoC/base/6_*.gds ./results/sky130hd/VSDBabySoC/base/6_*.oas ./results/sky130hd/VSDBabySoC/base/6_*.odb ./results/sky130hd/VSDBabySoC/base/6_*.v ./results/sky130hd/VSDBabySoC/base/6_*.def ./results/sky130hd/VSDBabySoC/base/6_*.sdc ./results/sky130hd/VSDBabySoC/base/6_*.spef
rm -rf ./reports/sky130hd/VSDBabySoC/base/6_*.rpt
rm -f  ./logs/sky130hd/VSDBabySoC/base/6_*
rm -f ./reports/sky130hd/VSDBabySoC/base/design-dir.txt
rm -f ./reports/sky130hd/VSDBabySoC/base/metadata*.*
rm -f ./results/sky130hd/VSDBabySoC/base/vsdbabysoc.lib ./results/sky130hd/VSDBabySoC/base/vsdbabysoc.lef
rm -rf ./objects/sky130hd/VSDBabySoC/base
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ YOSYS_EXE=~/OpenROAD-flow-scripts/tools/yosys/yosys OPENROAD_EXE=~/OpenROAD-flow-scripts/tools/OpenROAD/build/bin/openroad make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk finish
mkdir -p results/sky130hd/VSDBabySoC/base/
echo 11 > results/sky130hd/VSDBabySoC/base/clock_period.txt
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.sh /home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth_canonicalize.tcl ./logs/sky130hd/VSDBabySoC/base/1_1_yosys_canonicalize.log
Using ABC speed script.
Extracting clock period from SDC file: ./results/sky130hd/VSDBabySoC/base/clock_period.txt
Setting clock period to 11
1. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
2. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
3. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
4. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
5. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
6. Executing Liberty frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
7. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/vsdbabysoc.v
8. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v
9. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/clk_gate.v
10. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_clkgate_hd.v
11. Executing HIERARCHY pass (managing design hierarchy).
12. Executing AST frontend in derive mode using pre-parsed AST for module `\vsdbabysoc'.
12.1. Analyzing design hierarchy..
12.2. Executing AST frontend in derive mode using pre-parsed AST for module `\rvmyth'.
Warning: Replacing memory \CPU_Dmem_value_a4 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:308
Warning: Replacing memory \CPU_Xreg_value_a3 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:288
Warning: Replacing memory \CPU_Imem_instr_a1 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth.v:273
Warning: Replacing memory \CPU_Xreg_value_a5 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:693
Warning: Replacing memory \CPU_Xreg_value_a4 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:692
Warning: Replacing memory \CPU_Dmem_value_a5 with list of registers. See /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/src/module/rvmyth_gen.v:683
12.3. Analyzing design hierarchy..
12.4. Executing AST frontend in derive mode using pre-parsed AST for module `\clk_gate'.
12.5. Analyzing design hierarchy..
12.6. Analyzing design hierarchy..
13. Executing OPT_CLEAN pass (remove unused cells and wires).
Warning: Ignoring module rvmyth because it contains processes (run 'proc' command first).
14. Executing RTLIL backend.
Warnings: 7 unique messages, 7 total
End of script. Logfile hash: cff3327032, CPU: user 0.19s system 0.04s, MEM: 52.00 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 68% 8x read_liberty (0 sec), 14% 1x hierarchy (0 sec), ...
Elapsed time: 0:00.32[h:]min:sec. CPU time: user 0.27 sys 0.04 (100%). Peak memory: 55808KB.
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.sh /home/shwetank/OpenROAD-flow-scripts/flow/scripts/synth.tcl ./logs/sky130hd/VSDBabySoC/base/1_2_yosys.log
Using ABC speed script.
Extracting clock period from SDC file: ./results/sky130hd/VSDBabySoC/base/clock_period.txt
Setting clock period to 11
1. Executing RTLIL frontend.
2. Executing HIERARCHY pass (managing design hierarchy).
2.1. Analyzing design hierarchy..
2.2. Analyzing design hierarchy..
3. Executing SYNTH pass.
3.1. Executing HIERARCHY pass (managing design hierarchy).
3.1.1. Analyzing design hierarchy..
3.1.2. Analyzing design hierarchy..
3.2. Executing PROC pass (convert processes to netlists).
3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
3.2.4. Executing PROC_INIT pass (extract init attributes).
3.2.5. Executing PROC_ARST pass (detect async resets in processes).
3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).
3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).
3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).
3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
3.2.12. Executing OPT_EXPR pass (perform const folding).
3.3. Executing FLATTEN pass (flatten design).
3.4. Executing OPT_EXPR pass (perform const folding).
3.5. Executing OPT_CLEAN pass (remove unused cells and wires).
3.6. Executing CHECK pass (checking for obvious problems).
3.7. Executing OPT pass (performing simple optimizations).
3.7.1. Executing OPT_EXPR pass (perform const folding).
3.7.2. Executing OPT_MERGE pass (detect identical cells).
3.7.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.7.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.7.5. Executing OPT_MERGE pass (detect identical cells).
3.7.6. Executing OPT_DFF pass (perform DFF optimizations).
3.7.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.7.8. Executing OPT_EXPR pass (perform const folding).
3.7.9. Rerunning OPT passes. (Maybe there is more to do..)
3.7.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.7.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.7.12. Executing OPT_MERGE pass (detect identical cells).
3.7.13. Executing OPT_DFF pass (perform DFF optimizations).
3.7.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.7.15. Executing OPT_EXPR pass (perform const folding).
3.7.16. Finished fast OPT passes. (There is nothing left to do.)
3.8. Executing FSM pass (extract and optimize FSM).
3.8.1. Executing FSM_DETECT pass (finding FSMs in design).
3.8.2. Executing FSM_EXTRACT pass (extracting FSM from design).
3.8.3. Executing FSM_OPT pass (simple optimizations of FSMs).
3.8.4. Executing OPT_CLEAN pass (remove unused cells and wires).
3.8.5. Executing FSM_OPT pass (simple optimizations of FSMs).
3.8.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).
3.8.7. Executing FSM_INFO pass (dumping all available information on FSM cells).
3.8.8. Executing FSM_MAP pass (mapping FSMs to basic logic).
3.9. Executing OPT pass (performing simple optimizations).
3.9.1. Executing OPT_EXPR pass (perform const folding).
3.9.2. Executing OPT_MERGE pass (detect identical cells).
3.9.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.5. Executing OPT_MERGE pass (detect identical cells).
3.9.6. Executing OPT_DFF pass (perform DFF optimizations).
3.9.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.8. Executing OPT_EXPR pass (perform const folding).
3.9.9. Rerunning OPT passes. (Maybe there is more to do..)
3.9.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.12. Executing OPT_MERGE pass (detect identical cells).
3.9.13. Executing OPT_DFF pass (perform DFF optimizations).
3.9.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.15. Executing OPT_EXPR pass (perform const folding).
3.9.16. Rerunning OPT passes. (Maybe there is more to do..)
3.9.17. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.9.18. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.9.19. Executing OPT_MERGE pass (detect identical cells).
3.9.20. Executing OPT_DFF pass (perform DFF optimizations).
3.9.21. Executing OPT_CLEAN pass (remove unused cells and wires).
3.9.22. Executing OPT_EXPR pass (perform const folding).
3.9.23. Finished fast OPT passes. (There is nothing left to do.)
3.10. Executing WREDUCE pass (reducing word size of cells).
3.11. Executing PEEPOPT pass (run peephole optimizers).
3.12. Executing OPT_CLEAN pass (remove unused cells and wires).
3.13. Executing ALUMACC pass (create $alu and $macc cells).
3.14. Executing SHARE pass (SAT-based resource sharing).
3.15. Executing OPT pass (performing simple optimizations).
3.15.1. Executing OPT_EXPR pass (perform const folding).
3.15.2. Executing OPT_MERGE pass (detect identical cells).
3.15.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.15.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.15.5. Executing OPT_MERGE pass (detect identical cells).
3.15.6. Executing OPT_DFF pass (perform DFF optimizations).
3.15.7. Executing OPT_CLEAN pass (remove unused cells and wires).
3.15.8. Executing OPT_EXPR pass (perform const folding).
3.15.9. Rerunning OPT passes. (Maybe there is more to do..)
3.15.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
3.15.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
3.15.12. Executing OPT_MERGE pass (detect identical cells).
3.15.13. Executing OPT_DFF pass (perform DFF optimizations).
3.15.14. Executing OPT_CLEAN pass (remove unused cells and wires).
3.15.15. Executing OPT_EXPR pass (perform const folding).
3.15.16. Finished fast OPT passes. (There is nothing left to do.)
3.16. Executing MEMORY pass.
3.16.1. Executing OPT_MEM pass (optimize memories).
3.16.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
3.16.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).
3.16.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).
3.16.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).
3.16.6. Executing OPT_CLEAN pass (remove unused cells and wires).
3.16.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).
3.16.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
3.16.9. Executing OPT_CLEAN pass (remove unused cells and wires).
3.16.10. Executing MEMORY_COLLECT pass (generating $mem cells).
3.17. Executing OPT_CLEAN pass (remove unused cells and wires).
4. Executing SYNTH pass.
4.1. Executing OPT pass (performing simple optimizations).
4.1.1. Executing OPT_EXPR pass (perform const folding).
4.1.2. Executing OPT_MERGE pass (detect identical cells).
4.1.3. Executing OPT_DFF pass (perform DFF optimizations).
4.1.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.1.5. Rerunning OPT passes. (Removed registers in this run.)
4.1.6. Executing OPT_EXPR pass (perform const folding).
4.1.7. Executing OPT_MERGE pass (detect identical cells).
4.1.8. Executing OPT_DFF pass (perform DFF optimizations).
4.1.9. Executing OPT_CLEAN pass (remove unused cells and wires).
4.1.10. Finished fast OPT passes.
4.2. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).
4.3. Executing OPT pass (performing simple optimizations).
4.3.1. Executing OPT_EXPR pass (perform const folding).
4.3.2. Executing OPT_MERGE pass (detect identical cells).
4.3.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.5. Executing OPT_MERGE pass (detect identical cells).
4.3.6. Executing OPT_SHARE pass.
4.3.7. Executing OPT_DFF pass (perform DFF optimizations).
4.3.8. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.9. Executing OPT_EXPR pass (perform const folding).
4.3.10. Rerunning OPT passes. (Maybe there is more to do..)
4.3.11. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.12. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.13. Executing OPT_MERGE pass (detect identical cells).
4.3.14. Executing OPT_SHARE pass.
4.3.15. Executing OPT_DFF pass (perform DFF optimizations).
4.3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.17. Executing OPT_EXPR pass (perform const folding).
4.3.18. Rerunning OPT passes. (Maybe there is more to do..)
4.3.19. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.20. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.21. Executing OPT_MERGE pass (detect identical cells).
4.3.22. Executing OPT_SHARE pass.
4.3.23. Executing OPT_DFF pass (perform DFF optimizations).
4.3.24. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.25. Executing OPT_EXPR pass (perform const folding).
4.3.26. Rerunning OPT passes. (Maybe there is more to do..)
4.3.27. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.28. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.29. Executing OPT_MERGE pass (detect identical cells).
4.3.30. Executing OPT_SHARE pass.
4.3.31. Executing OPT_DFF pass (perform DFF optimizations).
4.3.32. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.33. Executing OPT_EXPR pass (perform const folding).
4.3.34. Rerunning OPT passes. (Maybe there is more to do..)
4.3.35. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.36. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.37. Executing OPT_MERGE pass (detect identical cells).
4.3.38. Executing OPT_SHARE pass.
4.3.39. Executing OPT_DFF pass (perform DFF optimizations).
4.3.40. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.41. Executing OPT_EXPR pass (perform const folding).
4.3.42. Rerunning OPT passes. (Maybe there is more to do..)
4.3.43. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.44. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.45. Executing OPT_MERGE pass (detect identical cells).
4.3.46. Executing OPT_SHARE pass.
4.3.47. Executing OPT_DFF pass (perform DFF optimizations).
4.3.48. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.49. Executing OPT_EXPR pass (perform const folding).
4.3.50. Rerunning OPT passes. (Maybe there is more to do..)
4.3.51. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
4.3.52. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
4.3.53. Executing OPT_MERGE pass (detect identical cells).
4.3.54. Executing OPT_SHARE pass.
4.3.55. Executing OPT_DFF pass (perform DFF optimizations).
4.3.56. Executing OPT_CLEAN pass (remove unused cells and wires).
4.3.57. Executing OPT_EXPR pass (perform const folding).
4.3.58. Finished fast OPT passes. (There is nothing left to do.)
4.4. Executing TECHMAP pass (map to technology primitives).
4.4.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/tools/yosys/share/techmap.v
4.4.2. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/common/lcu_kogge_stone.v
4.4.3. Continuing TECHMAP pass.
4.5. Executing OPT pass (performing simple optimizations).
4.5.1. Executing OPT_EXPR pass (perform const folding).
4.5.2. Executing OPT_MERGE pass (detect identical cells).
4.5.3. Executing OPT_DFF pass (perform DFF optimizations).
4.5.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.5. Rerunning OPT passes. (Removed registers in this run.)
4.5.6. Executing OPT_EXPR pass (perform const folding).
4.5.7. Executing OPT_MERGE pass (detect identical cells).
4.5.8. Executing OPT_DFF pass (perform DFF optimizations).
4.5.9. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.10. Rerunning OPT passes. (Removed registers in this run.)
4.5.11. Executing OPT_EXPR pass (perform const folding).
4.5.12. Executing OPT_MERGE pass (detect identical cells).
4.5.13. Executing OPT_DFF pass (perform DFF optimizations).
4.5.14. Executing OPT_CLEAN pass (remove unused cells and wires).
4.5.15. Finished fast OPT passes.
4.6. Executing ABC pass (technology mapping using ABC).
4.6.1. Extracting gate netlist of module `\vsdbabysoc' to `<abc-temp-dir>/input.blif'..
4.7. Executing OPT pass (performing simple optimizations).
4.7.1. Executing OPT_EXPR pass (perform const folding).
4.7.2. Executing OPT_MERGE pass (detect identical cells).
4.7.3. Executing OPT_DFF pass (perform DFF optimizations).
4.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
4.7.5. Finished fast OPT passes.
4.8. Executing HIERARCHY pass (managing design hierarchy).
4.8.1. Analyzing design hierarchy..
4.8.2. Analyzing design hierarchy..
4.9. Printing statistics.
4.10. Executing CHECK pass (checking for obvious problems).
5. Executing OPT pass (performing simple optimizations).
5.1. Executing OPT_EXPR pass (perform const folding).
5.2. Executing OPT_MERGE pass (detect identical cells).
5.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
5.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
5.5. Executing OPT_MERGE pass (detect identical cells).
5.6. Executing OPT_DFF pass (perform DFF optimizations).
5.7. Executing OPT_CLEAN pass (remove unused cells and wires).
5.8. Executing OPT_EXPR pass (perform const folding).
5.9. Rerunning OPT passes. (Maybe there is more to do..)
5.10. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
5.11. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
5.12. Executing OPT_MERGE pass (detect identical cells).
5.13. Executing OPT_DFF pass (perform DFF optimizations).
5.14. Executing OPT_CLEAN pass (remove unused cells and wires).
5.15. Executing OPT_EXPR pass (perform const folding).
5.16. Finished fast OPT passes. (There is nothing left to do.)
6. Executing EXTRACT_FA pass (find and extract full/half adders).
7. Executing TECHMAP pass (map to technology primitives).
7.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_adders_hd.v
7.2. Continuing TECHMAP pass.
8. Executing TECHMAP pass (map to technology primitives).
8.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/tools/yosys/share/techmap.v
8.2. Continuing TECHMAP pass.
9. Executing OPT pass (performing simple optimizations).
9.1. Executing OPT_EXPR pass (perform const folding).
9.2. Executing OPT_MERGE pass (detect identical cells).
9.3. Executing OPT_DFF pass (perform DFF optimizations).
9.4. Executing OPT_CLEAN pass (remove unused cells and wires).
9.5. Finished fast OPT passes.
10. Executing TECHMAP pass (map to technology primitives).
10.1. Executing Verilog-2005 frontend: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/cells_latch_hd.v
10.2. Continuing TECHMAP pass.
11. Executing DFFLIBMAP pass (mapping DFF cells to sequential cells from liberty file).
11.1. Executing DFFLEGALIZE pass (convert FFs to types supported by the target).
12. Executing OPT pass (performing simple optimizations).
12.1. Executing OPT_EXPR pass (perform const folding).
12.2. Executing OPT_MERGE pass (detect identical cells).
12.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
12.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
12.5. Executing OPT_MERGE pass (detect identical cells).
12.6. Executing OPT_DFF pass (perform DFF optimizations).
12.7. Executing OPT_CLEAN pass (remove unused cells and wires).
12.8. Executing OPT_EXPR pass (perform const folding).
12.9. Finished fast OPT passes. (There is nothing left to do.)
13. Executing SETUNDEF pass (replace undef values with defined constants).
abc -script /home/shwetank/OpenROAD-flow-scripts/flow/scripts/abc_speed.script -liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib -dont_use sky130_fd_sc_hd__probe_p_8 -dont_use sky130_fd_sc_hd__probec_p_8 -dont_use sky130_fd_sc_hd__lpflow_bleeder_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_12 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_3 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_6 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_inputiso0n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso0p_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1p_1 -dont_use sky130_fd_sc_hd__lpflow_inputisolatch_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_16 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_2 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_4 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_8 -dont_use sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 -constr ./objects/sky130hd/VSDBabySoC/base/abc.constr -D 11
14. Executing ABC pass (technology mapping using ABC).
14.1. Extracting gate netlist of module `\vsdbabysoc' to `<abc-temp-dir>/input.blif'..
14.1.1. Executed ABC.
14.1.2. Re-integrating ABC results.
Took 6 seconds: abc -script /home/shwetank/OpenROAD-flow-scripts/flow/scripts/abc_speed.script -liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib -liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib -dont_use sky130_fd_sc_hd__probe_p_8 -dont_use sky130_fd_sc_hd__probec_p_8 -dont_use sky130_fd_sc_hd__lpflow_bleeder_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkbufkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_1 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_16 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_2 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_clkinvkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_12 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_3 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_4 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_6 -dont_use sky130_fd_sc_hd__lpflow_decapkapwr_8 -dont_use sky130_fd_sc_hd__lpflow_inputiso0n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso0p_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1n_1 -dont_use sky130_fd_sc_hd__lpflow_inputiso1p_1 -dont_use sky130_fd_sc_hd__lpflow_inputisolatch_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_1 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_16 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_2 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_4 -dont_use sky130_fd_sc_hd__lpflow_isobufsrc_8 -dont_use sky130_fd_sc_hd__lpflow_isobufsrckapwr_16 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_hl_isowell_tap_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_4 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_1 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_2 -dont_use sky130_fd_sc_hd__lpflow_lsbuf_lh_isowell_tap_4 -constr ./objects/sky130hd/VSDBabySoC/base/abc.constr -D 11
15. Executing SPLITNETS pass (splitting up multi-bit signals).
16. Executing OPT_CLEAN pass (remove unused cells and wires).
17. Executing HILOMAP pass (mapping to constant drivers).
18. Executing INSBUF pass (insert buffer cells for connected wires).
19. Executing CHECK pass (checking for obvious problems).
20. Printing statistics.
21. Executing CHECK pass (checking for obvious problems).
22. Executing Verilog backend.
22.1. Executing BMUXMAP pass.
22.2. Executing DEMUXMAP pass.
exec cp /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/vsdbabysoc_synthesis.sdc ./results/sky130hd/VSDBabySoC/base/1_synth.sdc
End of script. Logfile hash: a1c820cb07, CPU: user 3.07s system 0.08s, MEM: 69.62 MB peak
Yosys 0.59+0 (git sha1 26b51148a, g++ 11.4.0-1ubuntu1~22.04.2 -fPIC -O3)
Time spent: 67% 2x abc (6 sec), 7% 34x opt_clean (0 sec), ...
Elapsed time: 0:09.48[h:]min:sec. CPU time: user 9.31 sys 0.17 (100%). Peak memory: 72568KB.
mkdir -p ./results/sky130hd/VSDBabySoC/base ./logs/sky130hd/VSDBabySoC/base ./reports/sky130hd/VSDBabySoC/base
cp ./results/sky130hd/VSDBabySoC/base/1_2_yosys.v ./results/sky130hd/VSDBabySoC/base/1_synth.v
OpenROAD v2.0-26087-g3bcda7705d 
Features included (+) or not (-): +GPU +GUI +Python
This program is licensed under the BSD-3 license. See the LICENSE file for details.
Components of this program may be licensed under more restrictive licenses which must be honored.
[INFO ORD-0030] Using 10 thread(s).
mkdir -p ./objects/sky130hd/VSDBabySoC/base
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_1_floorplan floorplan
Running floorplan.tcl, stage 2_1_floorplan
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lef/sky130_fd_sc_hd.tlef, created 13 layers, 25 vias
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lef/sky130_fd_sc_hd_merged.lef, created 441 library cells
[WARNING ODB-0220] WARNING (LEFPARS-2008): NOWIREEXTENSIONATPIN statement is obsolete in version 5.6 or later.
The NOWIREEXTENSIONATPIN statement will be ignored. See file /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsddac.lef at line 2.

[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsddac.lef, created 1 library cells
[WARNING ODB-0220] WARNING (LEFPARS-2008): NOWIREEXTENSIONATPIN statement is obsolete in version 5.6 or later.
The NOWIREEXTENSIONATPIN statement will be ignored. See file /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsdpll.lef at line 2.

[WARNING ODB-0186] macro avsdpll references unknown site unithddb1
[INFO ODB-0227] LEF file: /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsdpll.lef, created 1 library cells
link_design vsdbabysoc
Master sky130_ef_sc_hd__decap_12 is loaded but not used in the design

==========================================================================
Floorplan check_setup
--------------------------------------------------------------------------
Warning: There are 6 input ports missing set_input_delay.
Warning: There is 1 output port missing set_output_delay.
Warning: There are 2 unconstrained endpoints.
number instances in verilog is 6605
[WARNING IFP-0028] Core area lower left (50.000, 50.000) snapped to (50.140, 51.680).
[INFO IFP-0001] Added 881 rows of 5217 site unithd.
source /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/make_tracks.tcl
source /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/fastroute.tcl
Repair tie lo fanout...
[INFO RSZ-0042] Inserted 4 tie sky130_fd_sc_hd__conb_1 instances.
Repair tie hi fanout...
[INFO RSZ-0026] Removed 595 buffers.
Default units for flow
 time 1ns
 capacitance 1pF
 resistance 1kohm
 voltage 1v
 current 1mA
 power 1nW
 distance 1um
Report metrics stage 2, floorplan final...

==========================================================================
floorplan final report_design_area
--------------------------------------------------------------------------
Design area 722267 um^2 13% utilization.
Elapsed time: 0:02.00[h:]min:sec. CPU time: user 2.25 sys 0.30 (127%). Peak memory: 140520KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_1_floorplan                      2            137 c65a11f5e946087b4d13
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_2_floorplan_macro macro_place
Running macro_place.tcl, stage 2_2_floorplan_macro
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_1_floorplan.odb
rtl_macro_placer -max_num_level 2 -halo_width 40 -halo_height 40 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.3
Die Area: (0.00, 0.00) (2500.00, 2500.00),  Floorplan Area: (50.14, 51.68) (2449.96, 2448.00)
	Number of std cell instances: 6011
	Area of std cell instances: 50614.96
	Number of macros: 2
	Area of macros: 671652.31
	Halo width: 40.00
	Halo height: 40.00
	Area of macros with halos: 828913.94
	Area of std cell instances + Area of macros: 722267.25
	Floorplan area: 5750737.00
	Design Utilization: 0.13
	Floorplan Utilization: 0.01
	Manufacturing Grid: 5

[WARNING MPL-0002] Couldn't align pin dac/D[0] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[1] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[2] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[4] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[5] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[6] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[7] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[8] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/D[9] from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin dac/OUT from layer met4 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/CLK from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/ENb_CP from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/ENb_VCO from layer li1 to the track-grid.
[WARNING MPL-0002] Couldn't align pin pll/REF from layer li1 to the track-grid.
Took 17 seconds: rtl_macro_placer -max_num_level 2 -halo_width 40 -halo_height 40 -min_ar 0.33 -area_weight 0.1 -wirelength_weight 100.0 -outline_weight 100.0 -boundary_weight 50.0 -notch_weight 10.0 -target_dead_space 0.05 -report_directory ./objects/sky130hd/VSDBabySoC/base/rtlmp -fence_lx 0.0 -fence_ly 0.0 -fence_ux 100000000.0 -fence_uy 100000000.0 -target_util 0.3
Elapsed time: 0:18.21[h:]min:sec. CPU time: user 29.88 sys 22.06 (285%). Peak memory: 166484KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_2_floorplan_macro               18            162 cef9b1fd13273d7850eb
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_3_floorplan_tapcell tapcell
Running tapcell.tcl, stage 2_3_floorplan_tapcell
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_2_floorplan_macro.odb
[INFO ODB-0303] The initial 881 rows (4596177 sites) were cut with 2 shapes for a total of 1098 rows (4051237 sites).
[INFO TAP-0005] Inserted 67622 tapcells.
Elapsed time: 0:00.75[h:]min:sec. CPU time: user 0.65 sys 0.09 (100%). Peak memory: 146064KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_3_floorplan_tapcell              0            142 7af13a514a5e794a0fd8
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 2_4_floorplan_pdn pdn
Running pdn.tcl, stage 2_4_floorplan_pdn
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_3_floorplan_tapcell.odb
[WARNING PDN-0007] GND on met1 is partially blocked (58.3%) by obstructions on met3 for pll
[WARNING PDN-0007] GND2 on met1 is partially blocked (7.0%) by obstructions on met2 for pll
[INFO PDN-0001] Inserting grid: Core
[INFO PDN-0001] Inserting grid: pll_grid - pll
[INFO PDN-0001] Inserting grid: dac_grid - dac
[WARNING PDN-0110] No via inserted between met4 and met5 at (179.3400, 180.8800) - (180.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (259.3400, 180.8800) - (260.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (339.3400, 180.8800) - (340.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (419.3400, 180.8800) - (420.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (499.3400, 180.8800) - (500.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (579.3400, 180.8800) - (580.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (659.3400, 180.8800) - (660.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (739.3400, 180.8800) - (740.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (819.3400, 180.8800) - (820.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (899.3400, 180.8800) - (900.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (979.3400, 180.8800) - (980.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1059.3400, 180.8800) - (1060.9400, 181.5500) on VDD
[WARNING PDN-0110] No via inserted between met4 and met5 at (1139.3400, 180.8800) - (1140.9400, 181.5500) on VDD
Elapsed time: 0:02.53[h:]min:sec. CPU time: user 2.25 sys 0.28 (100%). Peak memory: 375212KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
2_4_floorplan_pdn                  2            366 55b399cb075841cd9b67
cp ./results/sky130hd/VSDBabySoC/base/2_4_floorplan_pdn.odb ./results/sky130hd/VSDBabySoC/base/2_floorplan.odb
cp ./results/sky130hd/VSDBabySoC/base/2_1_floorplan.sdc ./results/sky130hd/VSDBabySoC/base/2_floorplan.sdc
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_1_place_gp_skip_io global_place_skip_io
Running global_place_skip_io.tcl, stage 3_1_place_gp_skip_io
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/2_floorplan.odb
global_placement -skip_io -density "0.30   " -pad_left 0 -pad_right 0
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             76049
[INFO GPL-0007] Movable instances:                6011
[INFO GPL-0008] Fixed instances:                 67624
[INFO GPL-0009] Dummy instances:                  2414
[INFO GPL-0010] Number of nets:                   6123
[INFO GPL-0011] Number of pins:                  21871
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0016] Core area:                  5750736.662 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5750736.662 um^2
[INFO GPL-0017] Fixed instances area:       914400.733 um^2
[INFO GPL-0018] Movable instances area:      50614.794 um^2
[INFO GPL-0019] Utilization:                     1.047 %
[INFO GPL-0020] Standard cells area:         50614.794 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3000
[INFO GPL-0024] Movable insts average area:      8.420 um^2
[INFO GPL-0025] Ideal bin area:                 28.068 um^2
[INFO GPL-0026] Ideal bin count:                204886
[INFO GPL-0027] Total bin area:             5750736.662 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.374 *  9.361 um
[INFO GPL-0030] Number of bins:                  65536
[INFO GPL-0007] Execute nesterov global placement.
[INFO GPL-0031] HPWL: Half-Perimeter Wirelength
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
        0 |   0.9979 |  2.095375e+04 |   +0.00% |  9.09e-17 |      
       10 |   0.9902 |  2.545788e+04 |  +21.50% |  1.48e-16 |      
       20 |   0.9880 |  2.744306e+04 |   +7.80% |  2.41e-16 |      
       30 |   0.9875 |  2.826940e+04 |   +3.01% |  3.92e-16 |      
       40 |   0.9866 |  2.913294e+04 |   +3.05% |  6.39e-16 |      
       50 |   0.9854 |  2.991576e+04 |   +2.69% |  1.04e-15 |      
       60 |   0.9842 |  3.041927e+04 |   +1.68% |  1.69e-15 |      
       70 |   0.9828 |  3.059728e+04 |   +0.59% |  2.76e-15 |      
       80 |   0.9816 |  3.049286e+04 |   -0.34% |  4.50e-15 |      
       90 |   0.9798 |  3.023844e+04 |   -0.83% |  7.32e-15 |      
      100 |   0.9773 |  2.993773e+04 |   -0.99% |  1.19e-14 |      
      110 |   0.9750 |  2.959752e+04 |   -1.14% |  1.94e-14 |      
      120 |   0.9736 |  2.920040e+04 |   -1.34% |  3.17e-14 |      
      130 |   0.9722 |  2.876079e+04 |   -1.51% |  5.16e-14 |      
      140 |   0.9698 |  2.831981e+04 |   -1.53% |  8.40e-14 |      
      150 |   0.9682 |  2.792712e+04 |   -1.39% |  1.37e-13 |      
      160 |   0.9667 |  2.769282e+04 |   -0.84% |  2.23e-13 |      
      170 |   0.9663 |  2.778445e+04 |   +0.33% |  3.63e-13 |      
      180 |   0.9660 |  2.845621e+04 |   +2.42% |  5.91e-13 |      
      190 |   0.9654 |  3.006494e+04 |   +5.65% |  9.63e-13 |      
      200 |   0.9627 |  3.359092e+04 |  +11.73% |  1.57e-12 |      
      210 |   0.9605 |  4.128114e+04 |  +22.89% |  2.55e-12 |      
      220 |   0.9556 |  5.389911e+04 |  +30.57% |  4.15e-12 |      
      230 |   0.9554 |  7.518514e+04 |  +39.49% |  6.75e-12 |      
      240 |   0.9570 |  1.078004e+05 |  +43.38% |  1.10e-11 |      
      250 |   0.9726 |  1.475729e+05 |  +36.89% |  1.78e-11 |      
      260 |   0.9839 |  1.474293e+05 |   -0.10% |  2.89e-11 |      
      270 |   0.9896 |  1.372298e+05 |   -6.92% |  4.70e-11 |      
      280 |   0.9896 |  2.173756e+05 |  +58.40% |  7.59e-11 |      
      290 |   0.9867 |  1.945761e+05 |  -10.49% |  1.24e-10 |      
      300 |   0.9563 |  2.266253e+05 |  +16.47% |  2.00e-10 |      
      310 |   0.9036 |  2.594064e+05 |  +14.46% |  3.25e-10 |      
      320 |   0.8321 |  2.645941e+05 |   +2.00% |  5.29e-10 |      
      330 |   0.7308 |  2.401286e+05 |   -9.25% |  8.61e-10 |      
      340 |   0.6261 |  2.367808e+05 |   -1.39% |  1.40e-09 |      
      350 |   0.5688 |  2.484760e+05 |   +4.94% |  2.28e-09 |      
      360 |   0.4950 |  2.590026e+05 |   +4.24% |  3.70e-09 |      
      370 |   0.4367 |  2.726512e+05 |   +5.27% |  6.02e-09 |      
      380 |   0.3735 |  2.802581e+05 |   +2.79% |  9.75e-09 |      
      390 |   0.3306 |  2.778399e+05 |   -0.86% |  1.54e-08 |      
      400 |   0.3052 |  2.638243e+05 |   -5.04% |  2.27e-08 |      
      410 |   0.2771 |  2.504232e+05 |   -5.08% |  3.34e-08 |      
      420 |   0.2391 |  2.493461e+05 |   -0.43% |  4.92e-08 |      
      430 |   0.2017 |  2.460936e+05 |   -1.30% |  7.25e-08 |      
      440 |   0.1772 |  2.412782e+05 |   -1.96% |  1.07e-07 |      
      450 |   0.1506 |  2.411547e+05 |   -0.05% |  1.57e-07 |      
      460 |   0.1305 |  2.354898e+05 |   -2.35% |  2.32e-07 |      
      470 |   0.1101 |  2.347046e+05 |   -0.33% |  3.41e-07 |      
      478 |   0.0981 |  2.313246e+05 |          |  4.84e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 478
[INFO GPL-1002] Placed Cell Area            50614.7936
[INFO GPL-1003] Available Free Area         4836335.9296
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0116
[INFO GPL-1008]     - For 80% usage of free space: 0.0131
[INFO GPL-1009]     - For 50% usage of free space: 0.0209
[INFO GPL-1014] Final placement area: 50614.79 (+0.00%)
Took 24 seconds: global_placement -skip_io -density "0.30   " -pad_left 0 -pad_right 0
Elapsed time: 0:24.99[h:]min:sec. CPU time: user 98.37 sys 0.50 (395%). Peak memory: 235680KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_1_place_gp_skip_io              24            230 7c4942a594db15ca773a
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_2_place_iop io_placement
Running io_placement.tcl, stage 3_2_place_iop
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_1_place_gp_skip_io.odb
place_pins -hor_layers met3 -ver_layers met2
Found 2 macro blocks.
Using 2 tracks default min distance between IO pins.
[INFO PPL-0001] Number of available slots 9100
[INFO PPL-0002] Number of I/O             7
[INFO PPL-0003] Number of I/O w/sink      7
[INFO PPL-0004] Number of I/O w/o sink    0
[INFO PPL-0005] Slots per section         200
[INFO PPL-0008] Successfully assigned pins to sections.
[INFO PPL-0012] I/O nets HPWL: 773.24 um.
Elapsed time: 0:00.82[h:]min:sec. CPU time: user 0.66 sys 0.16 (100%). Peak memory: 196284KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_2_place_iop                      0            191 0de6cb30b7417d70ecbf
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_3_place_gp global_place
Running global_place.tcl, stage 3_3_place_gp
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_2_place_iop.odb
[INFO RSZ-0026] Removed 0 buffers.
Perform port buffering...
[INFO RSZ-0027] Inserted 6 sky130_fd_sc_hd__clkdlybuf4s50_1 input buffers.
[INFO RSZ-0028] Inserted 1 sky130_fd_sc_hd__clkdlybuf4s50_1 output buffers.
global_placement -density "0.30   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
[INFO GPL-0005] Execute conjugate gradient initial placement.
[INFO GPL-0002] DBU: 1000
[INFO GPL-0003] SiteSize: (  0.460  2.720 ) um
[INFO GPL-0004] CoreBBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0032] Initializing region: Top-level
[INFO GPL-0006] Number of instances:             76056
[INFO GPL-0007] Movable instances:                6018
[INFO GPL-0008] Fixed instances:                 67624
[INFO GPL-0009] Dummy instances:                  2414
[INFO GPL-0010] Number of nets:                   6130
[INFO GPL-0011] Number of pins:                  21892
[INFO GPL-0012] Die BBox:  (  0.000  0.000 ) ( 2500.000 2500.000 ) um
[INFO GPL-0013] Core BBox: ( 50.140 51.680 ) ( 2449.960 2448.000 ) um
[INFO GPL-0016] Core area:                  5750736.662 um^2
[INFO GPL-0014] Region name: top-level.
[INFO GPL-0015] Region area:                5750736.662 um^2
[INFO GPL-0017] Fixed instances area:       914400.733 um^2
[INFO GPL-0018] Movable instances area:      50684.861 um^2
[INFO GPL-0019] Utilization:                     1.048 %
[INFO GPL-0020] Standard cells area:         50684.861 um^2
[INFO GPL-0021] Large instances area:            0.000 um^2
[InitialPlace]  Iter: 1 conjugate gradient residual: 0.00653910 HPWL: 287675213
[InitialPlace]  Iter: 2 conjugate gradient residual: 0.23018758 HPWL: 78558390
[InitialPlace]  Iter: 3 conjugate gradient residual: 0.00563520 HPWL: 92486771
[InitialPlace]  Iter: 4 conjugate gradient residual: 0.02219049 HPWL: 87530313
[InitialPlace]  Iter: 5 conjugate gradient residual: 0.32454821 HPWL: 76060515
[InitialPlace]  Iter: 6 conjugate gradient residual: 0.00563520 HPWL: 92632074
[InitialPlace]  Iter: 7 conjugate gradient residual: 0.02219049 HPWL: 87615072
[InitialPlace]  Iter: 8 conjugate gradient residual: 0.32454821 HPWL: 76123289
[InitialPlace]  Iter: 9 conjugate gradient residual: 0.00563520 HPWL: 92666915
[InitialPlace]  Iter: 10 conjugate gradient residual: 0.02219049 HPWL: 87650955
[InitialPlace]  Iter: 11 conjugate gradient residual: 0.32454821 HPWL: 76134881
[InitialPlace]  Iter: 12 conjugate gradient residual: 0.00563520 HPWL: 92683112
[InitialPlace]  Iter: 13 conjugate gradient residual: 0.02219049 HPWL: 87656430
[InitialPlace]  Iter: 14 conjugate gradient residual: 0.32454821 HPWL: 76147280
[InitialPlace]  Iter: 15 conjugate gradient residual: 0.00563520 HPWL: 92682789
[InitialPlace]  Iter: 16 conjugate gradient residual: 0.02219049 HPWL: 87663060
[InitialPlace]  Iter: 17 conjugate gradient residual: 0.32454821 HPWL: 76146091
[InitialPlace]  Iter: 18 conjugate gradient residual: 0.00563520 HPWL: 92696022
[InitialPlace]  Iter: 19 conjugate gradient residual: 0.02219049 HPWL: 87658091
[InitialPlace]  Iter: 20 conjugate gradient residual: 0.32454821 HPWL: 76156010
[INFO GPL-0033] Initializing Nesterov region: Top-level
[INFO GPL-0023] Placement target density:       0.3000
[INFO GPL-0024] Movable insts average area:      8.422 um^2
[INFO GPL-0025] Ideal bin area:                 28.074 um^2
[INFO GPL-0026] Ideal bin count:                204841
[INFO GPL-0027] Total bin area:             5750736.662 um^2
[INFO GPL-0028] Bin count (X, Y):         256 ,    256
[INFO GPL-0029] Bin size (W * H):       9.374 *  9.361 um
[INFO GPL-0030] Number of bins:                  65536
[INFO GPL-0007] Execute nesterov global placement.
[INFO GPL-0031] HPWL: Half-Perimeter Wirelength
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
        0 |   0.9908 |  4.976842e+04 |   +0.00% |  9.77e-17 |      
       10 |   0.9618 |  6.724293e+04 |  +35.11% |  1.59e-16 |      
       20 |   0.9440 |  7.854263e+04 |  +16.80% |  2.58e-16 |      
       30 |   0.9292 |  8.500514e+04 |   +8.23% |  4.20e-16 |      
       40 |   0.9218 |  8.791584e+04 |   +3.42% |  6.84e-16 |      
       50 |   0.9188 |  8.963614e+04 |   +1.96% |  1.11e-15 |      
       60 |   0.9139 |  9.111692e+04 |   +1.65% |  1.82e-15 |      
       70 |   0.9138 |  9.180305e+04 |   +0.75% |  2.96e-15 |      
       80 |   0.9120 |  9.180828e+04 |   +0.01% |  4.82e-15 |      
       90 |   0.9148 |  9.165874e+04 |   -0.16% |  7.84e-15 |      
      100 |   0.9146 |  9.163052e+04 |   -0.03% |  1.28e-14 |      
      110 |   0.9117 |  9.158849e+04 |   -0.05% |  2.08e-14 |      
      120 |   0.9165 |  9.106959e+04 |   -0.57% |  3.39e-14 |      
      130 |   0.9165 |  9.026998e+04 |   -0.88% |  5.52e-14 |      
      140 |   0.9160 |  8.925345e+04 |   -1.13% |  8.99e-14 |      
      150 |   0.9150 |  8.801194e+04 |   -1.39% |  1.47e-13 |      
      160 |   0.9163 |  8.702879e+04 |   -1.12% |  2.39e-13 |      
      170 |   0.9157 |  8.629281e+04 |   -0.85% |  3.89e-13 |      
      180 |   0.9164 |  8.580975e+04 |   -0.56% |  6.33e-13 |      
      190 |   0.9175 |  8.558260e+04 |   -0.26% |  1.03e-12 |      
      200 |   0.9171 |  8.609151e+04 |   +0.59% |  1.68e-12 |      
      210 |   0.9154 |  8.751491e+04 |   +1.65% |  2.74e-12 |      
      220 |   0.9098 |  9.191582e+04 |   +5.03% |  4.45e-12 |      
      230 |   0.9006 |  1.017777e+05 |  +10.73% |  7.25e-12 |      
      240 |   0.8832 |  1.221720e+05 |  +20.04% |  1.18e-11 |      
      250 |   0.8586 |  1.667123e+05 |  +36.46% |  1.91e-11 |      
      260 |   0.8432 |  1.887292e+05 |  +13.21% |  3.10e-11 |      
      270 |   0.8324 |  1.605502e+05 |  -14.93% |  5.05e-11 |      
      280 |   0.8011 |  1.955534e+05 |  +21.80% |  8.20e-11 |      
      290 |   0.8059 |  2.404736e+05 |  +22.97% |  1.33e-10 |      
      300 |   0.7883 |  2.306181e+05 |   -4.10% |  2.16e-10 |      
      310 |   0.7346 |  2.455045e+05 |   +6.46% |  3.50e-10 |      
      320 |   0.6631 |  2.801927e+05 |  +14.13% |  5.67e-10 |      
      330 |   0.6328 |  2.490522e+05 |  -11.11% |  9.22e-10 |      
[INFO GPL-0100] Timing-driven iteration 1/2, virtual: false.
[INFO GPL-0101]    Iter: 331, overflow: 0.633, keep resizer changes at: 1, HPWL: 249052200
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6134
    final |     +0.3% |      87 |     122 |            86 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 88 slew violations.
[INFO RSZ-0036] Found 28 capacitance violations.
[INFO RSZ-0039] Resized 87 instances.
[INFO RSZ-0038] Inserted 122 buffers in 86 nets.
   Iter   |    Area   | Removed | Inserted |   Pins
          |           | Buffers | Buffers  | Remaining
-------------------------------------------------------
        0 |     +0.0% |       0 |        0 |      6119
      610 |     +0.0% |       1 |       20 |      5509
     1220 |     +0.0% |       1 |       30 |      4899
     1830 |     +0.0% |      14 |       55 |      4289
     2440 |     +0.0% |      21 |       59 |      3679
     3050 |     +0.0% |      21 |       61 |      3069
     3660 |     +0.0% |      21 |       68 |      2459
     4270 |     +0.0% |      21 |       84 |      1849
     4880 |     -0.0% |     104 |      147 |      1239
     5490 |     -0.1% |     122 |      175 |       629
     6100 |     -0.1% |     122 |      175 |        19
    final |     -0.1% |     122 |      176 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 5.56e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 1700.381 um^2 (+3.35%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 176 (+2.92%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 298, deleted: 122
[INFO GPL-0110] Timing-driven: new target density: 0.3003516
[INFO GPL-0038] Routability snapshot saved at iter = 340
      339 |   0.5898 |  2.017842e+05 |          |           |      
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      340 |   0.5836 |  1.921580e+05 |  -22.84% |  1.49e-09 |      
      350 |   0.5372 |  2.009130e+05 |   +4.56% |  2.43e-09 |      
      360 |   0.4893 |  1.994643e+05 |   -0.72% |  3.96e-09 |      
      370 |   0.4348 |  2.017182e+05 |   +1.13% |  6.44e-09 |      
      380 |   0.3812 |  2.021531e+05 |   +0.22% |  1.05e-08 |      
      390 |   0.3420 |  2.003572e+05 |   -0.89% |  1.69e-08 |      
      400 |   0.3000 |  1.992007e+05 |   -0.58% |  2.49e-08 |      
[INFO GPL-0040] Routability iteration: 1
[INFO GPL-0041] Total routing overflow: 43.4048
[INFO GPL-0042] Number of overflowed tiles: 10763 (8.21%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0322
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0193
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0119
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0062
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0257
[INFO GPL-0048] Routing congestion (1.0257) lower than previous minimum (1e+30). Updating minimum.
[INFO GPL-0051] Inflated area:                1610.268 um^2 (+3.07%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174978, After: 174777 (-0.11%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1400215.988, After: 1398607.500 (-0.11%)
[INFO GPL-0078] Removed fillers count: 201, area removed: 1608.450 um^2. Remaining area to be compensated by modifying density: 1.818 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1398607.500 um^2 (-0.11%)
[INFO GPL-0061] Total non-inflated area:    1452603.010 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1454213.278 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      410 |   0.5478 |  1.993159e+05 |   +0.06% |  2.04e-09 |      
      420 |   0.5262 |  1.983646e+05 |   -0.48% |  3.00e-09 |      
      430 |   0.4763 |  2.025039e+05 |   +2.09% |  4.41e-09 |      
      440 |   0.4359 |  2.034311e+05 |   +0.46% |  6.50e-09 |      
      450 |   0.3931 |  2.018617e+05 |   -0.77% |  9.57e-09 |      
      460 |   0.3598 |  1.998825e+05 |   -0.98% |  1.41e-08 |      
      470 |   0.3192 |  1.982064e+05 |   -0.84% |  2.08e-08 |      
[INFO GPL-0040] Routability iteration: 2
[INFO GPL-0041] Total routing overflow: 32.2107
[INFO GPL-0042] Number of overflowed tiles: 10716 (8.18%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0154
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0109
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0079
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0045
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0132
[INFO GPL-0048] Routing congestion (1.0132) lower than previous minimum (1.026). Updating minimum.
[INFO GPL-0051] Inflated area:                 471.126 um^2 (+0.87%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174777, After: 174719 (-0.03%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1398607.500, After: 1398143.371 (-0.03%)
[INFO GPL-0078] Removed fillers count: 58, area removed: 464.130 um^2. Remaining area to be compensated by modifying density: 6.996 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1398143.371 um^2 (-0.03%)
[INFO GPL-0061] Total non-inflated area:    1452610.007 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1453081.133 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      480 |   0.5712 |  1.975667e+05 |   -0.32% |  1.68e-09 |      
      490 |   0.5409 |  2.025809e+05 |   +2.54% |  2.47e-09 |      
      500 |   0.5009 |  2.027038e+05 |   +0.06% |  3.64e-09 |      
      510 |   0.4608 |  2.020927e+05 |   -0.30% |  5.36e-09 |      
      520 |   0.4207 |  2.016324e+05 |   -0.23% |  7.89e-09 |      
      530 |   0.3752 |  2.000371e+05 |   -0.79% |  1.16e-08 |      
      540 |   0.3382 |  2.000883e+05 |   +0.03% |  1.71e-08 |      
      550 |   0.3029 |  1.981472e+05 |   -0.97% |  2.52e-08 |      
[INFO GPL-0040] Routability iteration: 3
[INFO GPL-0041] Total routing overflow: 30.7762
[INFO GPL-0042] Number of overflowed tiles: 10706 (8.17%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0135
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0100
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0074
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0043
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0118
[INFO GPL-0048] Routing congestion (1.0118) lower than previous minimum (1.013). Updating minimum.
[INFO GPL-0051] Inflated area:                 365.972 um^2 (+0.67%)
[INFO GPL-0052] Placement target density:       0.3004
[INFO GPL-0076] Removing fillers, count: Before: 174719, After: 174674 (-0.03%)
[INFO GPL-0077] Filler area (um^2)     : Before: 1398143.371, After: 1397783.270 (-0.03%)
[INFO GPL-0078] Removed fillers count: 45, area removed: 360.101 um^2. Remaining area to be compensated by modifying density: 5.871 um^2
[INFO GPL-0058] White space area:           4836335.930 um^2 (+0.00%)
[INFO GPL-0059] Movable instances area:     1452601.246 um^2 (+0.00%)
[INFO GPL-0060] Total filler area:          1397783.270 um^2 (-0.03%)
[INFO GPL-0061] Total non-inflated area:    1452615.878 um^2 (+0.00%)
[INFO GPL-0062] Total inflated area:        1452981.849 um^2 (+0.00%)
[INFO GPL-0063] New Target Density:             0.3004
[INFO GPL-0087] Routability end iteration: increase inflation and revert back to snapshot.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      560 |   0.5475 |  2.011210e+05 |   +1.50% |  2.03e-09 |      
      570 |   0.5282 |  2.002228e+05 |   -0.45% |  3.00e-09 |      
      580 |   0.4769 |  2.045762e+05 |   +2.17% |  4.41e-09 |      
      590 |   0.4381 |  2.056135e+05 |   +0.51% |  6.50e-09 |      
      600 |   0.3929 |  2.042239e+05 |   -0.68% |  9.57e-09 |      
      610 |   0.3612 |  2.019504e+05 |   -1.11% |  1.41e-08 |      
      620 |   0.3175 |  2.011824e+05 |   -0.38% |  2.08e-08 |      
[INFO GPL-0040] Routability iteration: 4
[INFO GPL-0041] Total routing overflow: 28.9371
[INFO GPL-0042] Number of overflowed tiles: 10684 (8.15%)
[INFO GPL-0043] Average top 0.5% routing congestion: 1.0108
[INFO GPL-0044] Average top 1.0% routing congestion: 1.0086
[INFO GPL-0045] Average top 2.0% routing congestion: 1.0067
[INFO GPL-0046] Average top 5.0% routing congestion: 1.0040
[INFO GPL-0047] Routability iteration weighted routing congestion: 1.0097
[INFO GPL-0050] Weighted routing congestion is lower than target routing congestion(1.0100), end routability optimization.
[INFO GPL-0090] Routability finished. Target routing congestion achieved succesfully.
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      630 |   0.2867 |  2.001494e+05 |   -0.51% |  3.06e-08 |      
      640 |   0.2503 |  1.999111e+05 |   -0.12% |  4.50e-08 |      
      650 |   0.2183 |  1.992322e+05 |   -0.34% |  6.63e-08 |      
[INFO GPL-0100] Timing-driven iteration 2/2, virtual: false.
[INFO GPL-0101]    Iter: 660, overflow: 0.194, keep resizer changes at: 1, HPWL: 198892194
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6310
    final |     +0.0% |      12 |       3 |             6 |         0
---------------------------------------------------------------------
[INFO RSZ-0034] Found 12 slew violations.
[INFO RSZ-0039] Resized 12 instances.
[INFO RSZ-0038] Inserted 3 buffers in 6 nets.
   Iter   |    Area   | Removed | Inserted |   Pins
          |           | Buffers | Buffers  | Remaining
-------------------------------------------------------
        0 |     +0.0% |       0 |        0 |      6119
      610 |     +0.0% |      20 |       22 |      5509
     1220 |     +0.0% |      32 |       35 |      4899
     1830 |     +0.0% |      58 |       64 |      4289
     2440 |     +0.0% |      62 |       68 |      3679
     3050 |     +0.0% |      64 |       70 |      3069
     3660 |     +0.0% |      71 |       75 |      2459
     4270 |     +0.0% |      87 |       91 |      1849
     4880 |     +0.0% |     150 |      177 |      1239
     5490 |     +0.1% |     178 |      243 |       629
     6100 |     +0.1% |     178 |      243 |        19
    final |     +0.1% |     179 |      244 |         0
-------------------------------------------------------
[INFO GPL-0106] Timing-driven: worst slack 6.05e-09
[INFO GPL-0107] Timing-driven: repair_design delta area: 485.851 um^2 (+0.89%)
[INFO GPL-0108] Timing-driven: repair_design, gpl delta gcells: 68 (+1.10%)
[INFO GPL-0109] Timing-driven: repair_design, gcells created: 247, deleted: 179
[INFO GPL-0110] Timing-driven: new target density: 0.30045506
Iteration | Overflow |     HPWL (um) |  HPWL(%) |   Penalty | Group
---------------------------------------------------------------
      660 |   0.1965 |  2.080790e+05 |   +4.44% |  9.77e-08 |      
      670 |   0.1688 |  2.077660e+05 |   -0.15% |  1.44e-07 |      
      680 |   0.1468 |  2.065307e+05 |   -0.59% |  2.12e-07 |      
      690 |   0.1264 |  2.071016e+05 |   +0.28% |  3.12e-07 |      
      700 |   0.1071 |  2.114310e+05 |   +2.09% |  4.59e-07 |      
      704 |   0.0971 |  2.140167e+05 |          |  5.57e-07 |      
---------------------------------------------------------------
[INFO GPL-1001] Global placement finished at iteration 704
[INFO GPL-1003] Routability mode iteration count: 284
[INFO GPL-1005] Routability final weighted congestion: 1.0108
[INFO GPL-1002] Placed Cell Area            55318.4590
[INFO GPL-1003] Available Free Area         4836335.9296
[INFO GPL-1004] Minimum Feasible Density        0.0200 (cell_area / free_area)
[INFO GPL-1006]   Suggested Target Densities:
[INFO GPL-1007]     - For 90% usage of free space: 0.0127
[INFO GPL-1008]     - For 80% usage of free space: 0.0143
[INFO GPL-1009]     - For 50% usage of free space: 0.0229
[INFO GPL-1011] Original area (um^2): 50684.86
[INFO GPL-1012] Total routability artificial inflation: 4147.75 (+8.18%)
[INFO GPL-1013] Total timing-driven delta area: 2186.23 (+4.31%)
[INFO GPL-1014] Final placement area: 55318.46 (+9.14%)
Took 39 seconds: global_placement -density "0.30   " -pad_left 0 -pad_right 0 -routability_driven -timing_driven
Report metrics stage 3, global place...

==========================================================================
global place report_design_area
--------------------------------------------------------------------------
Design area 724551 um^2 13% utilization.
Elapsed time: 0:43.03[h:]min:sec. CPU time: user 152.35 sys 2.23 (359%). Peak memory: 520140KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_3_place_gp                      43            507 46ca107c3fb8bcdd36e7
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_4_place_resized resize
Running resize.tcl, stage 3_4_place_resized
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_3_place_gp.odb
Perform buffer insertion and gate resizing...
repair_design -verbose -match_cell_footprint
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6378
     1000 |     +0.0% |       0 |       0 |             0 |      5378
     2000 |     +0.0% |       0 |       0 |             0 |      4378
     3000 |     +0.0% |       0 |       0 |             0 |      3378
     4000 |     +0.0% |       0 |       0 |             0 |      2378
     5000 |     +0.0% |       0 |       0 |             0 |      1378
     6000 |     +0.0% |       0 |       0 |             0 |       378
    final |     +0.0% |       0 |       0 |             0 |         0
---------------------------------------------------------------------
Floating nets: 
[WARNING RSZ-0020] found 2 floating nets.
Report metrics stage 3, resizer...

==========================================================================
resizer report_design_area
--------------------------------------------------------------------------
Design area 724551 um^2 13% utilization.
Instance count before 73886, after 73886
Pin count before 22377, after 22377
Elapsed time: 0:04.30[h:]min:sec. CPU time: user 4.62 sys 0.71 (123%). Peak memory: 217452KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_4_place_resized                  4            212 46ca107c3fb8bcdd36e7
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 3_5_place_dp detail_place
Running detail_place.tcl, stage 3_5_place_dp
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_4_place_resized.odb
Placement Analysis
---------------------------------
total displacement      10840.6 u
average displacement        0.1 u
max displacement            9.0 u
original HPWL          211175.5 u
legalized HPWL         217739.8 u
delta HPWL                    3 %

Detailed placement improvement.
[INFO DPL-0401] Setting random seed to 1.
[INFO DPL-0402] Setting maximum displacement 5 1 to 13600 2720 units.
[INFO DPL-0320] Collected 67848 fixed cells.
[INFO DPL-0318] Collected 6262 single height cells.
[INFO DPL-0321] Collected 0 wide cells.
[INFO DPL-0322] Image (50140, 51680) - (2449960, 2448000)
[INFO DPL-0310] Assigned 6262 cells into segments.  Movement in X-direction is 0.000000, movement in Y-direction is 0.000000.
[INFO DPL-0313] Found 0 cells in wrong regions.
[INFO DPL-0315] Found 0 row alignment problems.
[INFO DPL-0314] Found 0 site alignment problems.
[INFO DPL-0311] Found 0 overlaps between adjacent cells.
[INFO DPL-0312] Found 0 edge spacing violations and 0 padding violations.
[INFO DPL-0303] Running algorithm for independent set matching.
[INFO DPL-0300] Set matching objective is wirelength.
[INFO DPL-0301] Pass   1 of matching; objective is 2.163510e+08.
[INFO DPL-0302] End of matching; objective is 2.160306e+08, improvement is 0.15 percent.
[INFO DPL-0303] Running algorithm for global swaps.
[INFO DPL-0306] Pass   1 of global swaps; hpwl is 2.057131e+08.
[INFO DPL-0306] Pass   2 of global swaps; hpwl is 2.039531e+08.
[INFO DPL-0307] End of global swaps; objective is 2.039531e+08, improvement is 5.59 percent.
[INFO DPL-0303] Running algorithm for vertical swaps.
[INFO DPL-0308] Pass   1 of vertical swaps; hpwl is 2.026880e+08.
[INFO DPL-0309] End of vertical swaps; objective is 2.026880e+08, improvement is 0.62 percent.
[INFO DPL-0303] Running algorithm for reordering.
[INFO DPL-0304] Pass   1 of reordering; objective is 2.025227e+08.
[INFO DPL-0305] End of reordering; objective is 2.025227e+08, improvement is 0.08 percent.
[INFO DPL-0303] Running algorithm for random improvement.
[INFO DPL-0324] Random improver is using random generator.
[INFO DPL-0325] Random improver is using hpwl objective.
[INFO DPL-0326] Random improver cost string is (a).
[INFO DPL-0332] End of pass, Generator random called 125240 times.
[INFO DPL-0335] Generator random, Cumulative attempts 125240, swaps 8748, moves 49341 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 2.001760e+08, Scratch cost 1.961087e+08, Incremental cost 1.961087e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 1.961087e+08.
[INFO DPL-0327] Pass   1 of random improver; improvement in cost is 2.03 percent.
[INFO DPL-0332] End of pass, Generator random called 125240 times.
[INFO DPL-0335] Generator random, Cumulative attempts 250480, swaps 17086, moves 98360 since last reset.
[INFO DPL-0333] End of pass, Objective hpwl, Initial cost 1.961087e+08, Scratch cost 1.947561e+08, Incremental cost 1.947561e+08, Mismatch? N
[INFO DPL-0338] End of pass, Total cost is 1.947561e+08.
[INFO DPL-0327] Pass   2 of random improver; improvement in cost is 0.69 percent.
[INFO DPL-0328] End of random improver; improvement is 2.707606 percent.
[INFO DPL-0380] Cell flipping.
[INFO DPL-0382] Changed 0 cell orientations for row compatibility.
[INFO DPL-0383] Performed 1763 cell flips.
[INFO DPL-0384] End of flipping; objective is 1.945031e+08, improvement is 1.32 percent.
[INFO DPL-0313] Found 0 cells in wrong regions.
[INFO DPL-0315] Found 0 row alignment problems.
[INFO DPL-0314] Found 0 site alignment problems.
[INFO DPL-0311] Found 0 overlaps between adjacent cells.
[INFO DPL-0312] Found 0 edge spacing violations and 0 padding violations.
Detailed Improvement Results
------------------------------------------
Original HPWL           217739.8 u (  101704.9,   116034.8)
Final HPWL              195899.7 u (   88380.5,   107519.2)
Delta HPWL                 -10.0 % (     -13.1,       -7.3)

[INFO DPL-0020] Mirrored 235 instances
[INFO DPL-0021] HPWL before          195899.7 u
[INFO DPL-0022] HPWL after           195825.4 u
[INFO DPL-0023] HPWL delta               -0.0 %
=======
Original HPWL           219704.7 u (  123787.5,    95917.2)
Final HPWL              193272.1 u (  109110.4,    84161.7)
Delta HPWL                 -12.0 % (     -11.9,      -12.3)

[INFO DPL-0020] Mirrored 255 instances
[INFO DPL-0021] HPWL before          193272.1 u
[INFO DPL-0022] HPWL after           193163.1 u
[INFO DPL-0023] HPWL delta               -0.1 %
>>>>>>> 2e9d213 (added assets)
[INFO FLW-0012] Placement violations .
Report metrics stage 3, detailed place...

==========================================================================
detailed place report_design_area
--------------------------------------------------------------------------
<<<<<<< HEAD
Design area 724551 um^2 13% utilization.
Elapsed time: 0:06.27[h:]min:sec. CPU time: user 6.61 sys 0.66 (116%). Peak memory: 394640KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_5_place_dp                       6            385 b7784cb05a3f2858e7d1
=======
Design area 724569 um^2 13% utilization.
Elapsed time: 0:07.17[h:]min:sec. CPU time: user 7.60 sys 0.73 (116%). Peak memory: 398128KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
3_5_place_dp                       7            388 d18f5dba917ef0a72ffd
>>>>>>> 2e9d213 (added assets)
cp ./results/sky130hd/VSDBabySoC/base/3_5_place_dp.odb ./results/sky130hd/VSDBabySoC/base/3_place.odb
cp ./results/sky130hd/VSDBabySoC/base/2_floorplan.sdc ./results/sky130hd/VSDBabySoC/base/3_place.sdc
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 4_1_cts cts
Running cts.tcl, stage 4_1_cts
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/3_place.odb
clock_tree_synthesis -sink_clustering_enable -repair_clock_nets -distance_between_buffers 600
[INFO CTS-0050] Root buffer is sky130_fd_sc_hd__clkbuf_16.
[INFO CTS-0051] Sink buffer is sky130_fd_sc_hd__clkbuf_16.
[INFO CTS-0052] The following clock buffers will be used for CTS:
                    sky130_fd_sc_hd__clkbuf_16
[INFO CTS-0049] Characterization buffer is sky130_fd_sc_hd__clkbuf_16.
[INFO CTS-0007] Net "CLK" found for clock "clk".
[INFO CTS-0010]  Clock net "CLK" has 1144 sinks.
[INFO CTS-0008] TritonCTS found 1 clock nets.
[INFO CTS-0097] Characterization used 1 buffer(s) types.
[INFO CTS-0201] 2 blockages from hard placement blockages and placed macros will be used.
[INFO CTS-0027] Generating H-Tree topology for net CLK.
[INFO CTS-0028]  Total number of sinks: 1144.
[INFO CTS-0090]  Sinks will be clustered based on buffer max cap.
[INFO CTS-0030]  Number of static layers: 0.
[INFO CTS-0020]  Wire segment unit: 13600  dbu (13 um).
[INFO CTS-0021]  Distance between buffers: 22 units (600 um).
[INFO CTS-0206] Best clustering solution was found from clustering size of 10 and clustering diameter of 50.
<<<<<<< HEAD
[INFO CTS-0019]  Total number of sinks after clustering: 119.
[INFO CTS-0024]  Normalized sink region: [(19.9533, 8.90441), (76.9722, 109.992)].
[INFO CTS-0025]     Width:  57.0189.
[INFO CTS-0026]     Height: 101.0877.
 Level 1
    Direction: Vertical
    Sinks per sub-region: 60
    Sub-region size: 57.0189 X 50.5438
[INFO CTS-0034]     Segment length (rounded): 26.
 Level 2
    Direction: Horizontal
    Sinks per sub-region: 30
    Sub-region size: 28.5094 X 50.5438
[INFO CTS-0034]     Segment length (rounded): 14.
 Level 3
    Direction: Vertical
    Sinks per sub-region: 15
    Sub-region size: 28.5094 X 25.2719
[INFO CTS-0034]     Segment length (rounded): 12.
 Level 4
    Direction: Horizontal
    Sinks per sub-region: 8
    Sub-region size: 14.2547 X 25.2719
[INFO CTS-0034]     Segment length (rounded): 8.
[INFO CTS-0032]  Stop criterion found. Max number of sinks is 15.
[INFO CTS-0035]  Number of sinks covered: 119.
[INFO CTS-0018]     Created 142 clock buffers.
[INFO CTS-0012]     Minimum number of buffers in the clock path: 3.
[INFO CTS-0013]     Maximum number of buffers in the clock path: 4.
[INFO CTS-0015]     Created 142 clock nets.
[INFO CTS-0016]     Fanout distribution for the current clock = 2:1, 3:1, 4:4, 5:7, 6:4, 7:6, 8:8, 9:15, 10:41, 11:28, 12:14, 13:2, 14:2..
[INFO CTS-0017]     Max level of the clock tree: 4.
[INFO CTS-0098] Clock net "CLK"
[INFO CTS-0099]  Sinks 1238
[INFO CTS-0100]  Leaf buffers 117
[INFO CTS-0101]  Average sink wire length 2042.54 um
[INFO CTS-0102]  Path depth 3 - 4
[INFO CTS-0207]  Leaf load cells 94
Placement Analysis
---------------------------------
total displacement       1248.5 u
average displacement        0.0 u
max displacement            6.2 u
original HPWL          213161.0 u
legalized HPWL         216640.7 u
=======
[INFO CTS-0019]  Total number of sinks after clustering: 85.
[INFO CTS-0024]  Normalized sink region: [(22.8317, 2.1989), (132.489, 24.3869)].
[INFO CTS-0025]     Width:  109.6570.
[INFO CTS-0026]     Height: 22.1880.
 Level 1
    Direction: Horizontal
    Sinks per sub-region: 43
    Sub-region size: 54.8285 X 22.1880
[INFO CTS-0034]     Segment length (rounded): 28.
 Level 2
    Direction: Vertical
    Sinks per sub-region: 22
    Sub-region size: 54.8285 X 11.0940
[INFO CTS-0034]     Segment length (rounded): 6.
 Level 3
    Direction: Horizontal
    Sinks per sub-region: 11
    Sub-region size: 27.4143 X 11.0940
[INFO CTS-0034]     Segment length (rounded): 14.
[INFO CTS-0032]  Stop criterion found. Max number of sinks is 15.
[INFO CTS-0035]  Number of sinks covered: 85.
[INFO CTS-0018]     Created 94 clock buffers.
[INFO CTS-0012]     Minimum number of buffers in the clock path: 3.
[INFO CTS-0013]     Maximum number of buffers in the clock path: 3.
[INFO CTS-0015]     Created 94 clock nets.
[INFO CTS-0016]     Fanout distribution for the current clock = 3:1, 5:1, 6:1, 8:4, 10:6, 11:4, 12:10, 13:18, 14:15, 15:20, 16:8, 17:3, 18:2..
[INFO CTS-0017]     Max level of the clock tree: 3.
[INFO CTS-0098] Clock net "CLK"
[INFO CTS-0099]  Sinks 1224
[INFO CTS-0100]  Leaf buffers 85
[INFO CTS-0101]  Average sink wire length 1629.10 um
[INFO CTS-0102]  Path depth 2 - 3
[INFO CTS-0207]  Leaf load cells 80
Placement Analysis
---------------------------------
total displacement       1066.3 u
average displacement        0.0 u
max displacement           15.4 u
original HPWL          206450.9 u
legalized HPWL         209827.7 u
>>>>>>> 2e9d213 (added assets)
delta HPWL                    2 %

repair_timing -setup_margin 0 -hold_margin 0 -repair_tns 100 -skip_gate_cloning -match_cell_footprint -verbose
[INFO RSZ-0100] Repair move sequence: UnbufferMove SizeUpMove SwapPinsMove BufferMove SplitLoadMove 
[INFO RSZ-0098] No setup violations found
[INFO RSZ-0033] No hold violations found.
Placement Analysis
---------------------------------
total displacement          0.0 u
average displacement        0.0 u
max displacement            0.0 u
<<<<<<< HEAD
original HPWL          216640.7 u
legalized HPWL         216640.7 u
=======
original HPWL          209827.7 u
legalized HPWL         209827.7 u
>>>>>>> 2e9d213 (added assets)
delta HPWL                    0 %

Report metrics stage 4, cts final...

==========================================================================
cts final report_design_area
--------------------------------------------------------------------------
<<<<<<< HEAD
Design area 729026 um^2 13% utilization.
Elapsed time: 0:06.28[h:]min:sec. CPU time: user 7.09 sys 1.00 (128%). Peak memory: 388032KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
4_1_cts                            6            378 b0294b14c033bf4e2469
=======
Design area 727948 um^2 13% utilization.
Elapsed time: 0:06.71[h:]min:sec. CPU time: user 7.50 sys 1.04 (127%). Peak memory: 392544KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
4_1_cts                            6            383 e472cbf89ebd934e45ef
>>>>>>> 2e9d213 (added assets)
cp ./results/sky130hd/VSDBabySoC/base/4_1_cts.odb ./results/sky130hd/VSDBabySoC/base/4_cts.odb
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 5_1_grt global_route
Running global_route.tcl, stage 5_1_grt
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/4_cts.odb
[INFO DRT-0149] Reading tech and libs.
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4

Units:                1000
Number of layers:     13
Number of macros:     443
<<<<<<< HEAD
Number of vias:       35
Number of viarulegen: 25

[INFO DRT-0150] Reading design.
=======
Number of vias:       30
Number of viarulegen: 25

[INFO DRT-0150] Reading design.
[WARNING DRT-0120] Large net _02644_ has 121 pins which may impact routing performance. Consider optimization.
[WARNING DRT-0120] Large net net523 has 129 pins which may impact routing performance. Consider optimization.
>>>>>>> 2e9d213 (added assets)

Design:                   vsdbabysoc
Die area:                 ( 0 0 ) ( 2500000 2500000 )
Number of track patterns: 12
Number of DEF vias:       0
<<<<<<< HEAD
Number of components:     74122
Number of terminals:      7
Number of snets:          2
Number of nets:           6516

[INFO DRT-0167] List of default vias:
  Layer via
    default via: M1M2_PR
  Layer via2
    default via: M2M3_PR
  Layer via3
    default via: M3M4_PR
  Layer via4
    default via: M4M5_PR
[INFO DRT-0162] Library cell analysis.
[INFO DRT-0163] Instance analysis.
[INFO DRT-0164] Number of unique instances = 193.
[INFO DRT-0168] Init region query.
[INFO DRT-0024]   Complete FR_MASTERSLICE.
[INFO DRT-0024]   Complete Fr_VIA.
[INFO DRT-0024]   Complete li1.
[INFO DRT-0024]   Complete mcon.
[INFO DRT-0024]   Complete met1.
[INFO DRT-0024]   Complete via.
[INFO DRT-0024]   Complete met2.
[INFO DRT-0024]   Complete via2.
[INFO DRT-0024]   Complete met3.
[INFO DRT-0024]   Complete via3.
[INFO DRT-0024]   Complete met4.
[INFO DRT-0024]   Complete via4.
[INFO DRT-0024]   Complete met5.
[INFO DRT-0033] FR_MASTERSLICE shape region query size = 0.
[INFO DRT-0033] FR_VIA shape region query size = 0.
[INFO DRT-0033] li1 shape region query size = 447162.
[INFO DRT-0033] mcon shape region query size = 234892.
[INFO DRT-0033] met1 shape region query size = 183271.
[INFO DRT-0033] via shape region query size = 117220.
[INFO DRT-0033] met2 shape region query size = 70415.
[INFO DRT-0033] via2 shape region query size = 93758.
[INFO DRT-0033] met3 shape region query size = 70341.
[INFO DRT-0033] via3 shape region query size = 93752.
[INFO DRT-0033] met4 shape region query size = 25190.
[INFO DRT-0033] via4 shape region query size = 1656.
[INFO DRT-0033] met5 shape region query size = 1717.
[INFO DRT-0165] Start pin access.
[INFO DRT-0076]   Complete 1000 pins.
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[INFO DRT-0078]   Complete 1560 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 191 unique inst patterns.
[INFO DRT-0084]   Complete 4481 groups.
#scanned instances     = 74122
#unique  instances     = 193
#stdCellGenAp          = 6226
#stdCellValidPlanarAp  = 54
#stdCellValidViaAp     = 4492
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22734
#instTermValidViaApCnt = 0
#macroGenAp            = 2002
#macroValidPlanarAp    = 1693
#macroValidViaAp       = 82
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:03:10, elapsed time = 00:00:24, memory = 299.52 (MB), peak = 300.55 (MB)
global_route -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion.rpt -congestion_iterations 30 -congestion_report_iter_step 5 -verbose
[INFO GRT-0020] Min routing layer: met1
[INFO GRT-0021] Max routing layer: met5
[INFO GRT-0022] Global adjustment: 0%
[INFO GRT-0023] Grid origin: (0, 0)
[INFO GRT-0088] Layer li1     Track-Pitch = 0.4600  line-2-Via Pitch: 0.3400
[INFO GRT-0088] Layer met1    Track-Pitch = 0.3400  line-2-Via Pitch: 0.3400
[INFO GRT-0088] Layer met2    Track-Pitch = 0.4600  line-2-Via Pitch: 0.3500
[INFO GRT-0088] Layer met3    Track-Pitch = 0.6800  line-2-Via Pitch: 0.6150
[INFO GRT-0088] Layer met4    Track-Pitch = 0.9200  line-2-Via Pitch: 1.0400
[INFO GRT-0088] Layer met5    Track-Pitch = 3.4000  line-2-Via Pitch: 3.1100
[INFO GRT-0003] Macros: 2
[INFO GRT-0004] Blockages: 17242
[INFO GRT-0019] Found 143 clock nets.
[INFO GRT-0001] Minimum degree: 2
[INFO GRT-0002] Maximum degree: 92

[INFO GRT-0053] Routing resources analysis:
          Routing      Original      Derated      Resource
Layer     Direction    Resources     Resources    Reduction (%)
---------------------------------------------------------------
li1        Vertical            0             8          0.00%
met1       Horizontal    2623052       1392723          46.90%
met2       Vertical      1967108       1331481          32.31%
met3       Horizontal    1311526        917697          30.03%
met4       Vertical       787350        455844          42.10%
met5       Horizontal     262088        118918          54.63%
---------------------------------------------------------------

[INFO GRT-0101] Running extra iterations to remove overflow.
[INFO GRT-0197] Via related to pin nodes: 37795
[INFO GRT-0198] Via related Steiner nodes: 1274
[INFO GRT-0199] Via filling finished.
[INFO GRT-0111] Final number of vias: 48854
[INFO GRT-0112] Final usage 3D: 189145

[INFO GRT-0096] Final congestion report:
Layer         Resource        Demand        Usage (%)    Max H / Max V / Total Overflow
---------------------------------------------------------------------------------------
li1                  8             0            0.00%             0 /  0 /  0
met1           1392723         19027            1.37%             0 /  0 /  0
met2           1331481         20232            1.52%             0 /  0 /  0
met3            917697          1902            0.21%             0 /  0 /  0
met4            455844          1415            0.31%             0 /  0 /  0
met5            118918             7            0.01%             0 /  0 /  0
---------------------------------------------------------------------------------------
Total          4216671         42583            1.01%             0 /  0 /  0

[INFO GRT-0018] Total wirelength: 415276 um
[INFO GRT-0014] Routed nets: 6482
Perform buffer insertion and gate resizing...
repair_design -verbose
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6614
     1000 |     +0.0% |       0 |       0 |             0 |      5614
     2000 |     +0.0% |       0 |       0 |             0 |      4614
     3000 |     +0.0% |       0 |       0 |             0 |      3614
     4000 |     +0.0% |       0 |       0 |             0 |      2614
     5000 |     +0.0% |       0 |       0 |             0 |      1614
     6000 |     +0.0% |       0 |       0 |             0 |       614
    final |     +0.0% |       0 |       0 |             0 |         0
---------------------------------------------------------------------
global_route -start_incremental
detailed_placement
Placement Analysis
---------------------------------
total displacement          0.0 u
average displacement        0.0 u
max displacement            0.0 u
original HPWL          216640.7 u
legalized HPWL         216640.7 u
delta HPWL                    0 %

global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_repair_design.rpt
Repair setup and hold violations...
repair_timing -setup_margin 0 -hold_margin 0 -repair_tns 100 -skip_gate_cloning -verbose
[INFO RSZ-0100] Repair move sequence: UnbufferMove SizeUpMove SwapPinsMove BufferMove SplitLoadMove 
[INFO RSZ-0098] No setup violations found
[INFO RSZ-0033] No hold violations found.
global_route -start_incremental
detailed_placement
Placement Analysis
---------------------------------
total displacement          0.0 u
average displacement        0.0 u
max displacement            0.0 u
original HPWL          216640.7 u
legalized HPWL         216640.7 u
delta HPWL                    0 %

global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_repair_timing.rpt
global_route -start_incremental
global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_recover_power.rpt
Repair antennas...
[INFO GRT-0012] Found 27 antenna violations.
[INFO GRT-0302] Inserted 29 jumpers for 26 nets.
[INFO GRT-0012] Found 1 antenna violations.
[INFO GRT-0015] Inserted 1 diodes.
[INFO GRT-0012] Found 0 antenna violations.
[INFO ANT-0002] Found 0 net violations.
[INFO ANT-0001] Found 0 pin violations.
Estimate parasitics...
Report metrics stage 5, global route...

==========================================================================
global route report_design_area
--------------------------------------------------------------------------
Design area 729029 um^2 13% utilization.
[INFO FLW-0007] clock clk period 11.000000
[INFO FLW-0008] Clock clk period 5.308
[INFO FLW-0009] Clock clk slack 5.413
[INFO FLW-0011] Path endpoint path count 1285
Elapsed time: 0:38.09[h:]min:sec. CPU time: user 234.61 sys 2.13 (621%). Peak memory: 808184KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_1_grt                           38            789 71bc0231e162cf15ff52
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 5_2_route detail_route
Running detail_route.tcl, stage 5_2_route
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/5_1_grt.odb
detailed_route -output_drc ./reports/sky130hd/VSDBabySoC/base/5_route_drc.rpt -output_maze ./results/sky130hd/VSDBabySoC/base/maze.log -droute_end_iter 64 -verbose 1 -drc_report_iter_step 5
[INFO DRT-0149] Reading tech and libs.
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4

Units:                1000
Number of layers:     13
Number of macros:     443
Number of vias:       35
Number of viarulegen: 25

[INFO DRT-0150] Reading design.

Design:                   vsdbabysoc
Die area:                 ( 0 0 ) ( 2500000 2500000 )
Number of track patterns: 12
Number of DEF vias:       0
Number of components:     74123
Number of terminals:      7
Number of snets:          2
Number of nets:           6516
=======
Number of components:     73023
Number of terminals:      9
Number of snets:          2
Number of nets:           6474
>>>>>>> 2e9d213 (added assets)

[INFO DRT-0167] List of default vias:
  Layer via
    default via: M1M2_PR
  Layer via2
    default via: M2M3_PR
  Layer via3
    default via: M3M4_PR
  Layer via4
    default via: M4M5_PR
[INFO DRT-0162] Library cell analysis.
[INFO DRT-0163] Instance analysis.
[INFO DRT-0164] Number of unique instances = 194.
[INFO DRT-0168] Init region query.
[INFO DRT-0024]   Complete FR_MASTERSLICE.
[INFO DRT-0024]   Complete Fr_VIA.
[INFO DRT-0024]   Complete li1.
[INFO DRT-0024]   Complete mcon.
[INFO DRT-0024]   Complete met1.
[INFO DRT-0024]   Complete via.
[INFO DRT-0024]   Complete met2.
[INFO DRT-0024]   Complete via2.
[INFO DRT-0024]   Complete met3.
[INFO DRT-0024]   Complete via3.
[INFO DRT-0024]   Complete met4.
[INFO DRT-0024]   Complete via4.
[INFO DRT-0024]   Complete met5.
[INFO DRT-0033] FR_MASTERSLICE shape region query size = 0.
[INFO DRT-0033] FR_VIA shape region query size = 0.
<<<<<<< HEAD
[INFO DRT-0033] li1 shape region query size = 447165.
[INFO DRT-0033] mcon shape region query size = 234896.
[INFO DRT-0033] met1 shape region query size = 183273.
[INFO DRT-0033] via shape region query size = 117220.
[INFO DRT-0033] met2 shape region query size = 70415.
[INFO DRT-0033] via2 shape region query size = 93758.
[INFO DRT-0033] met3 shape region query size = 70341.
[INFO DRT-0033] via3 shape region query size = 93752.
[INFO DRT-0033] met4 shape region query size = 25190.
[INFO DRT-0033] via4 shape region query size = 1656.
[INFO DRT-0033] met5 shape region query size = 1717.
=======
[INFO DRT-0033] li1 shape region query size = 440765.
[INFO DRT-0033] mcon shape region query size = 231098.
[INFO DRT-0033] met1 shape region query size = 225050.
[INFO DRT-0033] via shape region query size = 337040.
[INFO DRT-0033] met2 shape region query size = 202307.
[INFO DRT-0033] via2 shape region query size = 269614.
[INFO DRT-0033] met3 shape region query size = 202233.
[INFO DRT-0033] via3 shape region query size = 269608.
[INFO DRT-0033] met4 shape region query size = 81613.
[INFO DRT-0033] via4 shape region query size = 13951.
[INFO DRT-0033] met5 shape region query size = 14302.
>>>>>>> 2e9d213 (added assets)
[INFO DRT-0165] Start pin access.
[INFO DRT-0076]   Complete 1000 pins.
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
<<<<<<< HEAD
[INFO DRT-0078]   Complete 1565 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 192 unique inst patterns.
[INFO DRT-0084]   Complete 4482 groups.
#scanned instances     = 74123
#unique  instances     = 194
#stdCellGenAp          = 6238
#stdCellValidPlanarAp  = 54
#stdCellValidViaAp     = 4504
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22734
#instTermValidViaApCnt = 0
#macroGenAp            = 2002
#macroValidPlanarAp    = 1693
#macroValidViaAp       = 82
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:03:11, elapsed time = 00:00:24, memory = 489.16 (MB), peak = 491.07 (MB)

[INFO DRT-0157] Number of guides:     54391

[INFO DRT-0169] Post process guides.
[INFO DRT-0176] GCELLGRID X 0 DO 362 STEP 6900 ;
[INFO DRT-0177] GCELLGRID Y 0 DO 362 STEP 6900 ;
[INFO DRT-0028]   Complete FR_MASTERSLICE.
[INFO DRT-0028]   Complete Fr_VIA.
[INFO DRT-0028]   Complete li1.
[INFO DRT-0028]   Complete mcon.
[INFO DRT-0028]   Complete met1.
[INFO DRT-0028]   Complete via.
[INFO DRT-0028]   Complete met2.
[INFO DRT-0028]   Complete via2.
[INFO DRT-0028]   Complete met3.
[INFO DRT-0028]   Complete via3.
[INFO DRT-0028]   Complete met4.
[INFO DRT-0028]   Complete via4.
[INFO DRT-0028]   Complete met5.
[INFO DRT-0178] Init guide query.
[INFO DRT-0035]   Complete FR_MASTERSLICE (guide).
[INFO DRT-0035]   Complete Fr_VIA (guide).
[INFO DRT-0035]   Complete li1 (guide).
[INFO DRT-0035]   Complete mcon (guide).
[INFO DRT-0035]   Complete met1 (guide).
[INFO DRT-0035]   Complete via (guide).
[INFO DRT-0035]   Complete met2 (guide).
[INFO DRT-0035]   Complete via2 (guide).
[INFO DRT-0035]   Complete met3 (guide).
[INFO DRT-0035]   Complete via3 (guide).
[INFO DRT-0035]   Complete met4 (guide).
[INFO DRT-0035]   Complete via4 (guide).
[INFO DRT-0035]   Complete met5 (guide).
[INFO DRT-0036] FR_MASTERSLICE guide region query size = 0.
[INFO DRT-0036] FR_VIA guide region query size = 0.
[INFO DRT-0036] li1 guide region query size = 18734.
[INFO DRT-0036] mcon guide region query size = 0.
[INFO DRT-0036] met1 guide region query size = 16344.
[INFO DRT-0036] via guide region query size = 0.
[INFO DRT-0036] met2 guide region query size = 8499.
[INFO DRT-0036] via2 guide region query size = 0.
[INFO DRT-0036] met3 guide region query size = 464.
[INFO DRT-0036] via3 guide region query size = 0.
[INFO DRT-0036] met4 guide region query size = 192.
[INFO DRT-0036] via4 guide region query size = 0.
[INFO DRT-0036] met5 guide region query size = 4.
[INFO DRT-0179] Init gr pin query.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 505.79 (MB), peak = 505.79 (MB)
[INFO DRT-0245] skipped writing guide updates to database.
[INFO DRT-0185] Post process initialize RPin region query.
[INFO DRT-0181] Start track assignment.
[INFO DRT-0184] Done with 27425 vertical wires in 8 frboxes and 16812 horizontal wires in 8 frboxes.
[INFO DRT-0186] Done with 2571 vertical wires in 8 frboxes and 5119 horizontal wires in 8 frboxes.
[INFO DRT-0182] Complete track assignment.
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:02, memory = 755.29 (MB), peak = 755.29 (MB)
[INFO DRT-0187] Start routing data preparation.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 755.29 (MB), peak = 755.29 (MB)
[INFO DRT-0194] Start detail routing.
[INFO DRT-0195] Start 0th optimization iteration.
    Completing 10% with 0 violations.
    elapsed time = 00:00:02, memory = 1013.46 (MB).
    Completing 20% with 0 violations.
    elapsed time = 00:00:03, memory = 1024.34 (MB).
    Completing 30% with 738 violations.
    elapsed time = 00:00:04, memory = 928.81 (MB).
    Completing 40% with 738 violations.
    elapsed time = 00:00:07, memory = 1183.56 (MB).
    Completing 50% with 738 violations.
    elapsed time = 00:00:10, memory = 1046.08 (MB).
    Completing 60% with 1498 violations.
    elapsed time = 00:00:14, memory = 1235.09 (MB).
    Completing 70% with 1498 violations.
    elapsed time = 00:00:14, memory = 1246.47 (MB).
    Completing 80% with 2425 violations.
    elapsed time = 00:00:17, memory = 1125.81 (MB).
    Completing 90% with 2425 violations.
    elapsed time = 00:00:20, memory = 1230.43 (MB).
    Completing 100% with 3182 violations.
    elapsed time = 00:00:24, memory = 1081.85 (MB).
[INFO DRT-0199]   Number of violations = 3726.
Viol/Layer         li1   mcon   met1    via   met2   met3
Cut Spacing          0     10      0      1      0      0
Metal Spacing        0      0    630      0     99      3
Min Hole             0      0      1      0      0      0
Recheck              7      0    383      0    150      4
Short                0      1   2231      3    199      4
[INFO DRT-0267] cpu time = 00:02:54, elapsed time = 00:00:24, memory = 1407.97 (MB), peak = 1407.97 (MB)
Total wire length = 303562 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 138637 um.
Total wire length on LAYER met2 = 142577 um.
Total wire length on LAYER met3 = 12773 um.
Total wire length on LAYER met4 = 9518 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49360.
Up-via summary (total 49360):

------------------------
 FR_MASTERSLICE        0
            li1    22891
           met1    25440
           met2      712
           met3      312
           met4        5
------------------------
               49360


[INFO DRT-0195] Start 1st optimization iteration.
    Completing 10% with 3726 violations.
    elapsed time = 00:00:02, memory = 1460.35 (MB).
    Completing 20% with 3726 violations.
    elapsed time = 00:00:03, memory = 1460.35 (MB).
    Completing 30% with 3420 violations.
    elapsed time = 00:00:05, memory = 1408.71 (MB).
    Completing 40% with 3420 violations.
    elapsed time = 00:00:07, memory = 1463.96 (MB).
    Completing 50% with 3420 violations.
    elapsed time = 00:00:10, memory = 1410.86 (MB).
    Completing 60% with 3183 violations.
    elapsed time = 00:00:14, memory = 1451.48 (MB).
    Completing 70% with 3183 violations.
    elapsed time = 00:00:14, memory = 1440.86 (MB).
    Completing 80% with 2581 violations.
    elapsed time = 00:00:16, memory = 1422.05 (MB).
    Completing 90% with 2581 violations.
    elapsed time = 00:00:20, memory = 1487.44 (MB).
    Completing 100% with 2145 violations.
    elapsed time = 00:00:22, memory = 1434.94 (MB).
[INFO DRT-0199]   Number of violations = 2145.
Viol/Layer        mcon   met1   met2   met3
Cut Spacing          1      0      0      0
Metal Spacing        0    380     32      3
Short                0   1663     66      0
[INFO DRT-0267] cpu time = 00:02:52, elapsed time = 00:00:23, memory = 1437.94 (MB), peak = 1487.44 (MB)
Total wire length = 302017 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 137639 um.
Total wire length on LAYER met2 = 141872 um.
Total wire length on LAYER met3 = 13024 um.
Total wire length on LAYER met4 = 9425 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49033.
Up-via summary (total 49033):

------------------------
 FR_MASTERSLICE        0
            li1    22849
           met1    25084
           met2      799
           met3      296
           met4        5
------------------------
               49033


[INFO DRT-0195] Start 2nd optimization iteration.
    Completing 10% with 2145 violations.
    elapsed time = 00:00:01, memory = 1470.94 (MB).
    Completing 20% with 2145 violations.
    elapsed time = 00:00:02, memory = 1440.81 (MB).
    Completing 30% with 2100 violations.
    elapsed time = 00:00:04, memory = 1440.81 (MB).
    Completing 40% with 2100 violations.
    elapsed time = 00:00:07, memory = 1466.06 (MB).
    Completing 50% with 2100 violations.
    elapsed time = 00:00:07, memory = 1466.06 (MB).
    Completing 60% with 1961 violations.
    elapsed time = 00:00:11, memory = 1465.70 (MB).
    Completing 70% with 1961 violations.
    elapsed time = 00:00:12, memory = 1495.32 (MB).
    Completing 80% with 1969 violations.
    elapsed time = 00:00:15, memory = 1442.32 (MB).
    Completing 90% with 1969 violations.
    elapsed time = 00:00:18, memory = 1468.45 (MB).
    Completing 100% with 1779 violations.
    elapsed time = 00:00:20, memory = 1442.32 (MB).
[INFO DRT-0199]   Number of violations = 1779.
Viol/Layer        mcon   met1   met2   met3
Cut Spacing          3      0      0      0
Metal Spacing        0    331     30      1
Min Hole             0      1      0      0
Short                0   1357     56      0
[INFO DRT-0267] cpu time = 00:02:30, elapsed time = 00:00:20, memory = 1442.32 (MB), peak = 1495.32 (MB)
Total wire length = 301367 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 137001 um.
Total wire length on LAYER met2 = 141882 um.
Total wire length on LAYER met3 = 12970 um.
Total wire length on LAYER met4 = 9458 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 48822.
Up-via summary (total 48822):

------------------------
 FR_MASTERSLICE        0
            li1    22871
           met1    24867
           met2      770
           met3      309
           met4        5
------------------------
               48822


[INFO DRT-0195] Start 3rd optimization iteration.
    Completing 10% with 1779 violations.
    elapsed time = 00:00:01, memory = 1442.32 (MB).
    Completing 20% with 1779 violations.
    elapsed time = 00:00:01, memory = 1442.32 (MB).
    Completing 30% with 1373 violations.
    elapsed time = 00:00:03, memory = 1442.32 (MB).
    Completing 40% with 1373 violations.
    elapsed time = 00:00:05, memory = 1475.95 (MB).
    Completing 50% with 1373 violations.
    elapsed time = 00:00:07, memory = 1443.38 (MB).
    Completing 60% with 1015 violations.
    elapsed time = 00:00:09, memory = 1472.62 (MB).
    Completing 70% with 1015 violations.
    elapsed time = 00:00:09, memory = 1472.62 (MB).
    Completing 80% with 574 violations.
    elapsed time = 00:00:12, memory = 1443.39 (MB).
    Completing 90% with 574 violations.
    elapsed time = 00:00:14, memory = 1529.02 (MB).
    Completing 100% with 158 violations.
    elapsed time = 00:00:18, memory = 1443.41 (MB).
[INFO DRT-0199]   Number of violations = 158.
Viol/Layer        met1    via   met2
Cut Spacing          0      1      0
Metal Spacing       50      0      6
Short               91      0     10
[INFO DRT-0267] cpu time = 00:01:52, elapsed time = 00:00:18, memory = 1443.41 (MB), peak = 1536.62 (MB)
Total wire length = 301136 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132047 um.
Total wire length on LAYER met2 = 142094 um.
Total wire length on LAYER met3 = 17356 um.
Total wire length on LAYER met4 = 9582 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49728.
Up-via summary (total 49728):

------------------------
 FR_MASTERSLICE        0
            li1    22873
           met1    25069
           met2     1461
           met3      320
           met4        5
------------------------
               49728


[INFO DRT-0195] Start 4th optimization iteration.
    Completing 10% with 158 violations.
    elapsed time = 00:00:00, memory = 1443.41 (MB).
    Completing 20% with 158 violations.
    elapsed time = 00:00:00, memory = 1443.41 (MB).
    Completing 30% with 135 violations.
    elapsed time = 00:00:00, memory = 1443.41 (MB).
    Completing 40% with 135 violations.
    elapsed time = 00:00:00, memory = 1443.41 (MB).
    Completing 50% with 135 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 72 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 72 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 33 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 33 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:13, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131850 um.
Total wire length on LAYER met2 = 142061 um.
Total wire length on LAYER met3 = 17517 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49739.
Up-via summary (total 49739):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1491
           met3      320
           met4        5
------------------------
               49739


[INFO DRT-0195] Start 5th stubborn tiles iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 7 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 7.
Viol/Layer        met1
Short                7
[INFO DRT-0267] cpu time = 00:00:32, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301065 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131817 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17550 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49739.
Up-via summary (total 49739):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1493
           met3      320
           met4        5
------------------------
               49739


[INFO DRT-0195] Start 6th stubborn tiles iteration.
    Completing 10% with 7 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 20% with 7 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 30% with 7 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 7 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 7 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 7 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 7 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:32, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131788 um.
Total wire length on LAYER met2 = 142058 um.
Total wire length on LAYER met3 = 17578 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49747.
Up-via summary (total 49747):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1497
           met3      320
           met4        5
------------------------
               49747


[INFO DRT-0195] Start 7th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:29, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301068 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131788 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17579 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49747.
Up-via summary (total 49747):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1497
           met3      320
           met4        5
------------------------
               49747


[INFO DRT-0200] Skipping iteration 8
[INFO DRT-0200] Skipping iteration 9
[INFO DRT-0195] Start 10th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:30, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301068 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131788 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17579 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49747.
Up-via summary (total 49747):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1497
           met3      320
           met4        5
------------------------
               49747


[INFO DRT-0200] Skipping iteration 11
[INFO DRT-0200] Skipping iteration 12
[INFO DRT-0200] Skipping iteration 13
[INFO DRT-0200] Skipping iteration 14
[INFO DRT-0195] Start 15th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:29, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301068 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131788 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17579 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49747.
Up-via summary (total 49747):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1497
           met3      320
           met4        5
------------------------
               49747


[INFO DRT-0200] Skipping iteration 16
[INFO DRT-0195] Start 17th optimization iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301073 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131842 um.
Total wire length on LAYER met2 = 142057 um.
Total wire length on LAYER met3 = 17528 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1493
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 18th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301075 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131841 um.
Total wire length on LAYER met2 = 142061 um.
Total wire length on LAYER met3 = 17528 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25053
           met2     1493
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 19th stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:29, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301072 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131841 um.
Total wire length on LAYER met2 = 142060 um.
Total wire length on LAYER met3 = 17528 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25053
           met2     1493
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 20th stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:29, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301072 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131841 um.
Total wire length on LAYER met2 = 142060 um.
Total wire length on LAYER met3 = 17528 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25053
           met2     1493
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0200] Skipping iteration 21
[INFO DRT-0200] Skipping iteration 22
[INFO DRT-0195] Start 23rd stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131806 um.
Total wire length on LAYER met2 = 142057 um.
Total wire length on LAYER met3 = 17561 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 24th stubborn tiles iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131806 um.
Total wire length on LAYER met2 = 142057 um.
Total wire length on LAYER met3 = 17561 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 25th optimization iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301072 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142056 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 26th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301074 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142060 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 27th stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:31, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0200] Skipping iteration 28
[INFO DRT-0200] Skipping iteration 29
[INFO DRT-0195] Start 30th stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:30, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0195] Start 31st stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:36, elapsed time = 00:00:04, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131811 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49745.
Up-via summary (total 49745):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25051
           met2     1495
           met3      320
           met4        5
------------------------
               49745


[INFO DRT-0200] Skipping iteration 32
[INFO DRT-0195] Start 33rd optimization iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 10 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 34th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301073 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131815 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 35th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301072 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142059 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 36th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142056 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 37th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142056 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 38th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142056 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 39th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142056 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 40th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 41st optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 42nd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 43rd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 44th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17555 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 45th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 46th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17555 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 47th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17555 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 48th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17555 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49743.
Up-via summary (total 49743):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25049
           met2     1495
           met3      320
           met4        5
------------------------
               49743


[INFO DRT-0195] Start 49th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 50th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 51st optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:06, elapsed time = 00:00:05, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17557 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 52nd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 53rd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 54th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 55th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 56th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301071 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 57th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 58th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301069 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131813 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 59th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:05, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:06, elapsed time = 00:00:05, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301070 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131814 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9589 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 60th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1443.66 (MB).
    Completing 30% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 40% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 50% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 60% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 70% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 80% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 90% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
    Completing 100% with 11 violations.
    elapsed time = 00:00:03, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 11.
Viol/Layer        met1
Short               11
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301066 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131812 um.
Total wire length on LAYER met2 = 142055 um.
Total wire length on LAYER met3 = 17556 um.
Total wire length on LAYER met4 = 9587 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49741.
Up-via summary (total 49741):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1495
           met3      320
           met4        5
------------------------
               49741


[INFO DRT-0195] Start 61st stubborn tiles iteration.
    Completing 10% with 11 violations.
    elapsed time = 00:00:15, memory = 1443.66 (MB).
    Completing 20% with 11 violations.
    elapsed time = 00:00:23, memory = 1443.66 (MB).
    Completing 30% with 11 violations.
    elapsed time = 00:00:24, memory = 1443.66 (MB).
    Completing 40% with 11 violations.
    elapsed time = 00:00:24, memory = 1443.66 (MB).
    Completing 50% with 11 violations.
    elapsed time = 00:00:25, memory = 1443.66 (MB).
    Completing 60% with 11 violations.
    elapsed time = 00:00:25, memory = 1443.66 (MB).
    Completing 70% with 11 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:04:23, elapsed time = 00:00:27, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131844 um.
Total wire length on LAYER met2 = 142058 um.
Total wire length on LAYER met3 = 17523 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49739.
Up-via summary (total 49739):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1493
           met3      320
           met4        5
------------------------
               49739


[INFO DRT-0195] Start 62nd stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:14, memory = 1443.66 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:23, memory = 1443.66 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:25, memory = 1443.66 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:26, memory = 1443.66 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:26, memory = 1443.66 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:27, memory = 1443.66 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:28, memory = 1443.66 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:28, memory = 1443.66 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:28, memory = 1443.66 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:04:35, elapsed time = 00:00:28, memory = 1443.66 (MB), peak = 1536.62 (MB)
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131844 um.
Total wire length on LAYER met2 = 142057 um.
Total wire length on LAYER met3 = 17523 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49739.
Up-via summary (total 49739):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1493
           met3      320
           met4        5
------------------------
               49739


[INFO DRT-0200] Skipping iteration 63
[INFO DRT-0200] Skipping iteration 64
[INFO DRT-0198] Complete detail routing.
Total wire length = 301067 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 131844 um.
Total wire length on LAYER met2 = 142057 um.
Total wire length on LAYER met3 = 17523 um.
Total wire length on LAYER met4 = 9586 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49739.
Up-via summary (total 49739):

------------------------
 FR_MASTERSLICE        0
            li1    22874
           met1    25047
           met2     1493
           met3      320
           met4        5
------------------------
               49739


[INFO DRT-0267] cpu time = 00:26:38, elapsed time = 00:03:54, memory = 1443.66 (MB), peak = 1536.62 (MB)

[INFO DRT-0180] Post processing.
Took 262 seconds: detailed_route -output_drc ./reports/sky130hd/VSDBabySoC/base/5_route_drc.rpt -output_maze ./results/sky130hd/VSDBabySoC/base/maze.log -droute_end_iter 64 -verbose 1 -drc_report_iter_step 5
[INFO GRT-0012] Found 6 antenna violations.
[INFO GRT-0015] Inserted 6 diodes.
=======
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[INFO DRT-0078]   Complete 1565 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 192 unique inst patterns.
[INFO DRT-0084]   Complete 4406 groups.
#scanned instances     = 73023
#unique  instances     = 194
#stdCellGenAp          = 6241
#stdCellValidPlanarAp  = 92
#stdCellValidViaAp     = 4511
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22636
#instTermValidViaApCnt = 0
#macroGenAp            = 2045
#macroValidPlanarAp    = 1725
#macroValidViaAp       = 84
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:03:54, elapsed time = 00:00:30, memory = 357.31 (MB), peak = 359.93 (MB)
global_route -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion.rpt -congestion_iterations 30 -congestion_report_iter_step 5 -verbose
[INFO GRT-0020] Min routing layer: met1
[INFO GRT-0021] Max routing layer: met5
[INFO GRT-0022] Global adjustment: 0%
[INFO GRT-0023] Grid origin: (0, 0)
[INFO GRT-0088] Layer li1     Track-Pitch = 0.4600  line-2-Via Pitch: 0.3400
[INFO GRT-0088] Layer met1    Track-Pitch = 0.3400  line-2-Via Pitch: 0.3400
[INFO GRT-0088] Layer met2    Track-Pitch = 0.4600  line-2-Via Pitch: 0.3500
[INFO GRT-0088] Layer met3    Track-Pitch = 0.6800  line-2-Via Pitch: 0.6150
[INFO GRT-0088] Layer met4    Track-Pitch = 0.9200  line-2-Via Pitch: 1.0400
[INFO GRT-0088] Layer met5    Track-Pitch = 3.4000  line-2-Via Pitch: 3.1100
[INFO GRT-0003] Macros: 2
[INFO GRT-0004] Blockages: 17242
[INFO GRT-0019] Found 95 clock nets.
[INFO GRT-0001] Minimum degree: 2
[INFO GRT-0002] Maximum degree: 129

[INFO GRT-0053] Routing resources analysis:
          Routing      Original      Derated      Resource
Layer     Direction    Resources     Resources    Reduction (%)
---------------------------------------------------------------
li1        Vertical            0             8          0.00%
met1       Horizontal    2623052       1402609          46.53%
met2       Vertical      1967108       1189145          39.55%
met3       Horizontal    1311526        871956          33.52%
met4       Vertical       787350        421111          46.52%
met5       Horizontal     262088        118918          54.63%
---------------------------------------------------------------

[INFO GRT-0101] Running extra iterations to remove overflow.
[INFO GRT-0197] Via related to pin nodes: 37911
[INFO GRT-0198] Via related Steiner nodes: 1265
[INFO GRT-0199] Via filling finished.
[INFO GRT-0111] Final number of vias: 48965
[INFO GRT-0112] Final usage 3D: 187330

[INFO GRT-0096] Final congestion report:
Layer         Resource        Demand        Usage (%)    Max H / Max V / Total Overflow
---------------------------------------------------------------------------------------
li1                  8             0            0.00%             0 /  0 /  0
met1           1402609         19007            1.36%             0 /  0 /  0
met2           1189145         16334            1.37%             0 /  0 /  0
met3            871956          3957            0.45%             0 /  0 /  0
met4            421111          1137            0.27%             0 /  0 /  0
met5            118918             0            0.00%             0 /  0 /  0
---------------------------------------------------------------------------------------
Total          4003747         40435            1.01%             0 /  0 /  0

[INFO GRT-0018] Total wirelength: 397895 um
[INFO GRT-0014] Routed nets: 6440
Perform buffer insertion and gate resizing...
repair_design -verbose
Iteration |   Area    | Resized | Buffers | Nets repaired | Remaining
---------------------------------------------------------------------
        0 |     +0.0% |       0 |       0 |             0 |      6558
     1000 |     +0.0% |       0 |       0 |             0 |      5558
     2000 |     +0.0% |       0 |       0 |             0 |      4558
     3000 |     +0.0% |       0 |       0 |             0 |      3558
     4000 |     +0.0% |       0 |       0 |             0 |      2558
     5000 |     +0.0% |       0 |       0 |             0 |      1558
     6000 |     +0.0% |       0 |       0 |             0 |       558
    final |     +0.0% |       0 |       0 |             0 |         0
---------------------------------------------------------------------
global_route -start_incremental
detailed_placement
Placement Analysis
---------------------------------
total displacement          0.0 u
average displacement        0.0 u
max displacement            0.0 u
original HPWL          209827.7 u
legalized HPWL         209827.7 u
delta HPWL                    0 %

global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_repair_design.rpt
Repair setup and hold violations...
repair_timing -setup_margin 0 -hold_margin 0 -repair_tns 100 -skip_gate_cloning -verbose
[INFO RSZ-0100] Repair move sequence: UnbufferMove SizeUpMove SwapPinsMove BufferMove SplitLoadMove 
[INFO RSZ-0098] No setup violations found
[INFO RSZ-0033] No hold violations found.
global_route -start_incremental
detailed_placement
Placement Analysis
---------------------------------
total displacement          0.0 u
average displacement        0.0 u
max displacement            0.0 u
original HPWL          209827.7 u
legalized HPWL         209827.7 u
delta HPWL                    0 %

global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_repair_timing.rpt
global_route -start_incremental
global_route -end_incremental -congestion_report_file ./reports/sky130hd/VSDBabySoC/base/congestion_post_recover_power.rpt
Repair antennas...
[INFO GRT-0012] Found 45 antenna violations.
[INFO GRT-0302] Inserted 47 jumpers for 43 nets.
[INFO GRT-0012] Found 2 antenna violations.
[INFO GRT-0015] Inserted 2 diodes.
[INFO GRT-0012] Found 0 antenna violations.
[INFO ANT-0002] Found 0 net violations.
[INFO ANT-0001] Found 0 pin violations.
Estimate parasitics...
Report metrics stage 5, global route...

==========================================================================
global route report_design_area
--------------------------------------------------------------------------
Design area 727953 um^2 13% utilization.
[INFO FLW-0007] clock clk period 11.000000
[INFO FLW-0008] Clock clk period 5.386
[INFO FLW-0009] Clock clk slack 5.331
[INFO FLW-0011] Path endpoint path count 1272
Elapsed time: 0:47.43[h:]min:sec. CPU time: user 288.72 sys 2.46 (613%). Peak memory: 911136KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_1_grt                           47            889 6e7a100bc8a27a03ffe9
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 5_2_route detail_route
Running detail_route.tcl, stage 5_2_route
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/5_1_grt.odb
detailed_route -output_drc ./reports/sky130hd/VSDBabySoC/base/5_route_drc.rpt -output_maze ./results/sky130hd/VSDBabySoC/base/maze.log -droute_end_iter 64 -verbose 1 -drc_report_iter_step 5
[INFO DRT-0149] Reading tech and libs.
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer mcon
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via2
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via3
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4
[WARNING DRT-0349] LEF58_ENCLOSURE with no CUTCLASS is not supported. Skipping for layer via4

Units:                1000
Number of layers:     13
Number of macros:     443
Number of vias:       30
Number of viarulegen: 25

[INFO DRT-0150] Reading design.
[WARNING DRT-0120] Large net _02644_ has 121 pins which may impact routing performance. Consider optimization.
[WARNING DRT-0120] Large net net523 has 129 pins which may impact routing performance. Consider optimization.

Design:                   vsdbabysoc
Die area:                 ( 0 0 ) ( 2500000 2500000 )
Number of track patterns: 12
Number of DEF vias:       0
Number of components:     73025
Number of terminals:      9
Number of snets:          2
Number of nets:           6474

[INFO DRT-0167] List of default vias:
  Layer via
    default via: M1M2_PR
  Layer via2
    default via: M2M3_PR
  Layer via3
    default via: M3M4_PR
  Layer via4
    default via: M4M5_PR
[INFO DRT-0162] Library cell analysis.
[INFO DRT-0163] Instance analysis.
[INFO DRT-0164] Number of unique instances = 196.
[INFO DRT-0168] Init region query.
>>>>>>> 2e9d213 (added assets)
[INFO DRT-0024]   Complete FR_MASTERSLICE.
[INFO DRT-0024]   Complete Fr_VIA.
[INFO DRT-0024]   Complete li1.
[INFO DRT-0024]   Complete mcon.
[INFO DRT-0024]   Complete met1.
[INFO DRT-0024]   Complete via.
[INFO DRT-0024]   Complete met2.
[INFO DRT-0024]   Complete via2.
[INFO DRT-0024]   Complete met3.
[INFO DRT-0024]   Complete via3.
[INFO DRT-0024]   Complete met4.
[INFO DRT-0024]   Complete via4.
[INFO DRT-0024]   Complete met5.
<<<<<<< HEAD
=======
[INFO DRT-0033] FR_MASTERSLICE shape region query size = 0.
[INFO DRT-0033] FR_VIA shape region query size = 0.
[INFO DRT-0033] li1 shape region query size = 440771.
[INFO DRT-0033] mcon shape region query size = 231106.
[INFO DRT-0033] met1 shape region query size = 225054.
[INFO DRT-0033] via shape region query size = 337040.
[INFO DRT-0033] met2 shape region query size = 202307.
[INFO DRT-0033] via2 shape region query size = 269614.
[INFO DRT-0033] met3 shape region query size = 202233.
[INFO DRT-0033] via3 shape region query size = 269608.
[INFO DRT-0033] met4 shape region query size = 81613.
[INFO DRT-0033] via4 shape region query size = 13951.
[INFO DRT-0033] met5 shape region query size = 14302.
>>>>>>> 2e9d213 (added assets)
[INFO DRT-0165] Start pin access.
[INFO DRT-0076]   Complete 1000 pins.
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
<<<<<<< HEAD
[INFO DRT-0078]   Complete 1570 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 193 unique inst patterns.
[INFO DRT-0084]   Complete 4481 groups.
#scanned instances     = 74129
#unique  instances     = 195
#stdCellGenAp          = 6250
#stdCellValidPlanarAp  = 54
#stdCellValidViaAp     = 4516
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22734
#instTermValidViaApCnt = 0
#macroGenAp            = 2002
#macroValidPlanarAp    = 1693
#macroValidViaAp       = 82
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:03:45, elapsed time = 00:00:28, memory = 1362.52 (MB), peak = 1536.62 (MB)

[INFO DRT-0157] Number of guides:     54381
=======
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[INFO DRT-0078]   Complete 1575 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 194 unique inst patterns.
[INFO DRT-0084]   Complete 4407 groups.
#scanned instances     = 73025
#unique  instances     = 196
#stdCellGenAp          = 6265
#stdCellValidPlanarAp  = 92
#stdCellValidViaAp     = 4535
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22636
#instTermValidViaApCnt = 0
#macroGenAp            = 2045
#macroValidPlanarAp    = 1725
#macroValidViaAp       = 84
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:03:52, elapsed time = 00:00:30, memory = 581.26 (MB), peak = 584.13 (MB)

[INFO DRT-0157] Number of guides:     53999
>>>>>>> 2e9d213 (added assets)

[INFO DRT-0169] Post process guides.
[INFO DRT-0176] GCELLGRID X 0 DO 362 STEP 6900 ;
[INFO DRT-0177] GCELLGRID Y 0 DO 362 STEP 6900 ;
[INFO DRT-0028]   Complete FR_MASTERSLICE.
[INFO DRT-0028]   Complete Fr_VIA.
[INFO DRT-0028]   Complete li1.
[INFO DRT-0028]   Complete mcon.
[INFO DRT-0028]   Complete met1.
[INFO DRT-0028]   Complete via.
[INFO DRT-0028]   Complete met2.
[INFO DRT-0028]   Complete via2.
[INFO DRT-0028]   Complete met3.
[INFO DRT-0028]   Complete via3.
[INFO DRT-0028]   Complete met4.
[INFO DRT-0028]   Complete via4.
[INFO DRT-0028]   Complete met5.
[INFO DRT-0178] Init guide query.
[INFO DRT-0035]   Complete FR_MASTERSLICE (guide).
[INFO DRT-0035]   Complete Fr_VIA (guide).
[INFO DRT-0035]   Complete li1 (guide).
[INFO DRT-0035]   Complete mcon (guide).
[INFO DRT-0035]   Complete met1 (guide).
[INFO DRT-0035]   Complete via (guide).
[INFO DRT-0035]   Complete met2 (guide).
[INFO DRT-0035]   Complete via2 (guide).
[INFO DRT-0035]   Complete met3 (guide).
[INFO DRT-0035]   Complete via3 (guide).
[INFO DRT-0035]   Complete met4 (guide).
[INFO DRT-0035]   Complete via4 (guide).
[INFO DRT-0035]   Complete met5 (guide).
[INFO DRT-0036] FR_MASTERSLICE guide region query size = 0.
[INFO DRT-0036] FR_VIA guide region query size = 0.
<<<<<<< HEAD
[INFO DRT-0036] li1 guide region query size = 18734.
[INFO DRT-0036] mcon guide region query size = 0.
[INFO DRT-0036] met1 guide region query size = 16345.
[INFO DRT-0036] via guide region query size = 0.
[INFO DRT-0036] met2 guide region query size = 8498.
[INFO DRT-0036] via2 guide region query size = 0.
[INFO DRT-0036] met3 guide region query size = 460.
[INFO DRT-0036] via3 guide region query size = 0.
[INFO DRT-0036] met4 guide region query size = 189.
[INFO DRT-0036] via4 guide region query size = 0.
[INFO DRT-0036] met5 guide region query size = 3.
[INFO DRT-0179] Init gr pin query.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1362.52 (MB), peak = 1536.62 (MB)
[INFO DRT-0245] skipped writing guide updates to database.
[INFO DRT-0185] Post process initialize RPin region query.
[INFO DRT-0181] Start track assignment.
[INFO DRT-0184] Done with 27421 vertical wires in 8 frboxes and 16808 horizontal wires in 8 frboxes.
[INFO DRT-0186] Done with 2557 vertical wires in 8 frboxes and 5103 horizontal wires in 8 frboxes.
[INFO DRT-0182] Complete track assignment.
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:01, memory = 1366.02 (MB), peak = 1536.62 (MB)
[INFO DRT-0187] Start routing data preparation.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1366.02 (MB), peak = 1536.62 (MB)
[INFO DRT-0194] Start detail routing.
[INFO DRT-0195] Start 0th optimization iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1503.88 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1503.88 (MB).
    Completing 30% with 11 violations.
    elapsed time = 00:00:01, memory = 1399.68 (MB).
    Completing 40% with 11 violations.
    elapsed time = 00:00:02, memory = 1475.18 (MB).
    Completing 50% with 11 violations.
    elapsed time = 00:00:02, memory = 1398.64 (MB).
    Completing 60% with 23 violations.
    elapsed time = 00:00:03, memory = 1568.01 (MB).
    Completing 70% with 23 violations.
    elapsed time = 00:00:03, memory = 1533.69 (MB).
    Completing 80% with 88 violations.
    elapsed time = 00:00:03, memory = 1398.67 (MB).
    Completing 90% with 88 violations.
    elapsed time = 00:00:04, memory = 1494.92 (MB).
    Completing 100% with 95 violations.
    elapsed time = 00:00:05, memory = 1424.14 (MB).
[INFO DRT-0199]   Number of violations = 116.
Viol/Layer        met1   met2
Metal Spacing        0      1
Recheck              8     13
Short               28     66
[INFO DRT-0267] cpu time = 00:00:41, elapsed time = 00:00:05, memory = 1685.64 (MB), peak = 1685.64 (MB)
Total wire length = 301042 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132270 um.
Total wire length on LAYER met2 = 142696 um.
Total wire length on LAYER met3 = 17044 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49762.
Up-via summary (total 49762):

------------------------
 FR_MASTERSLICE        0
            li1    22885
           met1    25063
           met2     1491
           met3      318
           met4        5
------------------------
               49762


[INFO DRT-0195] Start 1st optimization iteration.
    Completing 10% with 116 violations.
    elapsed time = 00:00:00, memory = 1717.02 (MB).
    Completing 20% with 116 violations.
    elapsed time = 00:00:01, memory = 1688.52 (MB).
    Completing 30% with 116 violations.
    elapsed time = 00:00:01, memory = 1688.52 (MB).
    Completing 40% with 116 violations.
    elapsed time = 00:00:02, memory = 1688.52 (MB).
    Completing 50% with 116 violations.
    elapsed time = 00:00:02, memory = 1688.52 (MB).
    Completing 60% with 110 violations.
    elapsed time = 00:00:03, memory = 1717.02 (MB).
    Completing 70% with 110 violations.
    elapsed time = 00:00:03, memory = 1722.14 (MB).
    Completing 80% with 70 violations.
    elapsed time = 00:00:03, memory = 1693.77 (MB).
    Completing 90% with 70 violations.
    elapsed time = 00:00:04, memory = 1721.52 (MB).
    Completing 100% with 26 violations.
    elapsed time = 00:00:05, memory = 1721.52 (MB).
[INFO DRT-0199]   Number of violations = 26.
Viol/Layer        met1   met2
Short               20      6
[INFO DRT-0267] cpu time = 00:00:42, elapsed time = 00:00:05, memory = 1721.52 (MB), peak = 1747.39 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132277 um.
Total wire length on LAYER met2 = 142683 um.
Total wire length on LAYER met3 = 17038 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49753.
Up-via summary (total 49753):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25055
           met2     1491
           met3      318
           met4        5
------------------------
               49753


[INFO DRT-0195] Start 2nd optimization iteration.
    Completing 10% with 26 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 20% with 26 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1   met2
Short               20      4
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.52 (MB), peak = 1747.39 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132277 um.
Total wire length on LAYER met2 = 142683 um.
Total wire length on LAYER met3 = 17038 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49753.
Up-via summary (total 49753):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25055
           met2     1491
           met3      318
           met4        5
------------------------
               49753


[INFO DRT-0195] Start 3rd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1721.52 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:01, memory = 1721.54 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:01, memory = 1721.54 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:01, memory = 1721.54 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132245 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17070 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1495
           met3      318
           met4        5
------------------------
               49761
=======
[INFO DRT-0036] li1 guide region query size = 18634.
[INFO DRT-0036] mcon guide region query size = 0.
[INFO DRT-0036] met1 guide region query size = 16317.
[INFO DRT-0036] via guide region query size = 0.
[INFO DRT-0036] met2 guide region query size = 8203.
[INFO DRT-0036] via2 guide region query size = 0.
[INFO DRT-0036] met3 guide region query size = 651.
[INFO DRT-0036] via3 guide region query size = 0.
[INFO DRT-0036] met4 guide region query size = 253.
[INFO DRT-0036] via4 guide region query size = 0.
[INFO DRT-0036] met5 guide region query size = 15.
[INFO DRT-0179] Init gr pin query.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 597.26 (MB), peak = 597.26 (MB)
[INFO DRT-0245] skipped writing guide updates to database.
[INFO DRT-0185] Post process initialize RPin region query.
[INFO DRT-0181] Start track assignment.
[INFO DRT-0184] Done with 27090 vertical wires in 8 frboxes and 16983 horizontal wires in 8 frboxes.
[INFO DRT-0186] Done with 2919 vertical wires in 8 frboxes and 5240 horizontal wires in 8 frboxes.
[INFO DRT-0182] Complete track assignment.
[INFO DRT-0267] cpu time = 00:00:09, elapsed time = 00:00:02, memory = 913.97 (MB), peak = 1041.29 (MB)
[INFO DRT-0187] Start routing data preparation.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 913.97 (MB), peak = 1041.29 (MB)
[INFO DRT-0194] Start detail routing.
[INFO DRT-0195] Start 0th optimization iteration.
    Completing 10% with 0 violations.
    elapsed time = 00:00:00, memory = 939.22 (MB).
    Completing 20% with 0 violations.
    elapsed time = 00:00:03, memory = 1166.30 (MB).
    Completing 30% with 850 violations.
    elapsed time = 00:00:10, memory = 1067.58 (MB).
    Completing 40% with 850 violations.
    elapsed time = 00:00:10, memory = 1188.58 (MB).
    Completing 50% with 850 violations.
    elapsed time = 00:00:18, memory = 1178.88 (MB).
    Completing 60% with 1623 violations.
    elapsed time = 00:00:18, memory = 1178.88 (MB).
    Completing 70% with 1623 violations.
    elapsed time = 00:00:23, memory = 1374.75 (MB).
    Completing 80% with 2451 violations.
    elapsed time = 00:00:26, memory = 1214.28 (MB).
    Completing 90% with 2451 violations.
    elapsed time = 00:00:27, memory = 1377.28 (MB).
    Completing 100% with 3251 violations.
    elapsed time = 00:00:35, memory = 1270.17 (MB).
[INFO DRT-0199]   Number of violations = 3790.
Viol/Layer         li1   mcon   met1   met2   met3   met4
Cut Spacing          0     15      0      0      0      0
Metal Spacing        0      0    493    131      1      2
Min Hole             0      0      1      0      0      0
Recheck              4      0    371    153      7      4
Short                0      0   2415    188      5      0
[INFO DRT-0267] cpu time = 00:03:56, elapsed time = 00:00:35, memory = 1552.15 (MB), peak = 1576.42 (MB)
Total wire length = 289791 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 139152 um.
Total wire length on LAYER met2 = 116582 um.
Total wire length on LAYER met3 = 26590 um.
Total wire length on LAYER met4 = 7282 um.
Total wire length on LAYER met5 = 182 um.
Total number of vias = 49603.
Up-via summary (total 49603):

------------------------
 FR_MASTERSLICE        0
            li1    22781
           met1    25400
           met2     1000
           met3      396
           met4       26
------------------------
               49603


[INFO DRT-0195] Start 1st optimization iteration.
    Completing 10% with 3790 violations.
    elapsed time = 00:00:00, memory = 1552.15 (MB).
    Completing 20% with 3790 violations.
    elapsed time = 00:00:04, memory = 1624.52 (MB).
    Completing 30% with 3346 violations.
    elapsed time = 00:00:08, memory = 1583.43 (MB).
    Completing 40% with 3346 violations.
    elapsed time = 00:00:09, memory = 1614.18 (MB).
    Completing 50% with 3346 violations.
    elapsed time = 00:00:15, memory = 1583.48 (MB).
    Completing 60% with 2978 violations.
    elapsed time = 00:00:16, memory = 1583.48 (MB).
    Completing 70% with 2978 violations.
    elapsed time = 00:00:20, memory = 1646.36 (MB).
    Completing 80% with 2707 violations.
    elapsed time = 00:00:25, memory = 1583.41 (MB).
    Completing 90% with 2707 violations.
    elapsed time = 00:00:26, memory = 1614.04 (MB).
    Completing 100% with 2431 violations.
    elapsed time = 00:00:33, memory = 1584.95 (MB).
[INFO DRT-0199]   Number of violations = 2431.
Viol/Layer        mcon   met1   met2   met3   met4
Cut Spacing          5      0      0      0      0
Metal Spacing        0    373     67      5      1
Short                0   1899     81      0      0
[INFO DRT-0267] cpu time = 00:03:37, elapsed time = 00:00:33, memory = 1587.95 (MB), peak = 1646.36 (MB)
Total wire length = 288138 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 138000 um.
Total wire length on LAYER met2 = 115942 um.
Total wire length on LAYER met3 = 26765 um.
Total wire length on LAYER met4 = 7273 um.
Total wire length on LAYER met5 = 156 um.
Total number of vias = 49314.
Up-via summary (total 49314):

------------------------
 FR_MASTERSLICE        0
            li1    22764
           met1    25087
           met2     1052
           met3      385
           met4       26
------------------------
               49314


[INFO DRT-0195] Start 2nd optimization iteration.
    Completing 10% with 2431 violations.
    elapsed time = 00:00:00, memory = 1587.95 (MB).
    Completing 20% with 2431 violations.
    elapsed time = 00:00:04, memory = 1665.57 (MB).
    Completing 30% with 2519 violations.
    elapsed time = 00:00:07, memory = 1601.83 (MB).
    Completing 40% with 2519 violations.
    elapsed time = 00:00:07, memory = 1601.83 (MB).
    Completing 50% with 2519 violations.
    elapsed time = 00:00:11, memory = 1631.83 (MB).
    Completing 60% with 2400 violations.
    elapsed time = 00:00:16, memory = 1601.89 (MB).
    Completing 70% with 2400 violations.
    elapsed time = 00:00:20, memory = 1634.91 (MB).
    Completing 80% with 2419 violations.
    elapsed time = 00:00:24, memory = 1602.46 (MB).
    Completing 90% with 2419 violations.
    elapsed time = 00:00:25, memory = 1633.21 (MB).
    Completing 100% with 2241 violations.
    elapsed time = 00:00:32, memory = 1602.83 (MB).
[INFO DRT-0199]   Number of violations = 2241.
Viol/Layer        mcon   met1    via   met2
Cut Spacing          1      0      1      0
Metal Spacing        0    331      0     84
Min Hole             0      0      0      1
Short                0   1727      0     96
[INFO DRT-0267] cpu time = 00:03:27, elapsed time = 00:00:32, memory = 1605.83 (MB), peak = 1665.57 (MB)
Total wire length = 287693 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 137650 um.
Total wire length on LAYER met2 = 115842 um.
Total wire length on LAYER met3 = 26794 um.
Total wire length on LAYER met4 = 7230 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 49318.
Up-via summary (total 49318):

------------------------
 FR_MASTERSLICE        0
            li1    22779
           met1    25089
           met2     1039
           met3      385
           met4       26
------------------------
               49318


[INFO DRT-0195] Start 3rd optimization iteration.
    Completing 10% with 2241 violations.
    elapsed time = 00:00:00, memory = 1605.83 (MB).
    Completing 20% with 2241 violations.
    elapsed time = 00:00:01, memory = 1681.98 (MB).
    Completing 30% with 1766 violations.
    elapsed time = 00:00:10, memory = 1614.91 (MB).
    Completing 40% with 1766 violations.
    elapsed time = 00:00:10, memory = 1614.91 (MB).
    Completing 50% with 1766 violations.
    elapsed time = 00:00:15, memory = 1616.53 (MB).
    Completing 60% with 1229 violations.
    elapsed time = 00:00:15, memory = 1616.53 (MB).
    Completing 70% with 1229 violations.
    elapsed time = 00:00:18, memory = 1648.82 (MB).
    Completing 80% with 777 violations.
    elapsed time = 00:00:22, memory = 1618.91 (MB).
    Completing 90% with 777 violations.
    elapsed time = 00:00:22, memory = 1684.91 (MB).
    Completing 100% with 310 violations.
    elapsed time = 00:00:30, memory = 1618.77 (MB).
[INFO DRT-0199]   Number of violations = 310.
Viol/Layer        met1    via   met2
Cut Spacing          0      1      0
Metal Spacing       89      0      9
Short              210      0      1
[INFO DRT-0267] cpu time = 00:02:38, elapsed time = 00:00:30, memory = 1618.77 (MB), peak = 1685.33 (MB)
Total wire length = 287263 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130937 um.
Total wire length on LAYER met2 = 116139 um.
Total wire length on LAYER met3 = 32612 um.
Total wire length on LAYER met4 = 7397 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50490.
Up-via summary (total 50490):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25354
           met2     1935
           met3      404
           met4       26
------------------------
               50490


[INFO DRT-0195] Start 4th optimization iteration.
    Completing 10% with 310 violations.
    elapsed time = 00:00:00, memory = 1618.77 (MB).
    Completing 20% with 310 violations.
    elapsed time = 00:00:00, memory = 1618.77 (MB).
    Completing 30% with 140 violations.
    elapsed time = 00:00:02, memory = 1618.77 (MB).
    Completing 40% with 140 violations.
    elapsed time = 00:00:02, memory = 1618.77 (MB).
    Completing 50% with 140 violations.
    elapsed time = 00:00:03, memory = 1618.77 (MB).
    Completing 60% with 110 violations.
    elapsed time = 00:00:03, memory = 1618.77 (MB).
    Completing 70% with 110 violations.
    elapsed time = 00:00:03, memory = 1618.77 (MB).
    Completing 80% with 86 violations.
    elapsed time = 00:00:04, memory = 1623.65 (MB).
    Completing 90% with 86 violations.
    elapsed time = 00:00:04, memory = 1623.65 (MB).
    Completing 100% with 27 violations.
    elapsed time = 00:00:05, memory = 1646.26 (MB).
[INFO DRT-0199]   Number of violations = 27.
Viol/Layer        met1   met2
Metal Spacing        5      2
Short               16      4
[INFO DRT-0267] cpu time = 00:00:22, elapsed time = 00:00:05, memory = 1646.26 (MB), peak = 1685.33 (MB)
Total wire length = 287270 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130808 um.
Total wire length on LAYER met2 = 116144 um.
Total wire length on LAYER met3 = 32742 um.
Total wire length on LAYER met4 = 7399 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50513.
Up-via summary (total 50513):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25353
           met2     1960
           met3      403
           met4       26
------------------------
               50513


[INFO DRT-0195] Start 5th optimization iteration.
    Completing 10% with 27 violations.
    elapsed time = 00:00:00, memory = 1646.26 (MB).
    Completing 20% with 27 violations.
    elapsed time = 00:00:00, memory = 1646.26 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:02, memory = 1646.26 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:02, memory = 1646.26 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:03, memory = 1648.01 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:03, memory = 1648.01 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:03, memory = 1648.01 (MB).
    Completing 80% with 10 violations.
    elapsed time = 00:00:04, memory = 1648.01 (MB).
    Completing 90% with 10 violations.
    elapsed time = 00:00:04, memory = 1648.01 (MB).
    Completing 100% with 10 violations.
    elapsed time = 00:00:04, memory = 1648.01 (MB).
[INFO DRT-0199]   Number of violations = 10.
Viol/Layer        met1
Metal Spacing        4
Short                6
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:04, memory = 1648.01 (MB), peak = 1685.33 (MB)
Total wire length = 287278 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130755 um.
Total wire length on LAYER met2 = 116153 um.
Total wire length on LAYER met3 = 32802 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50510.
Up-via summary (total 50510):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25342
           met2     1966
           met3      405
           met4       26
------------------------
               50510


[INFO DRT-0195] Start 6th stubborn tiles iteration.
    Completing 10% with 10 violations.
    elapsed time = 00:00:02, memory = 1895.87 (MB).
    Completing 20% with 10 violations.
    elapsed time = 00:00:08, memory = 2074.20 (MB).
    Completing 30% with 10 violations.
    elapsed time = 00:00:08, memory = 1982.38 (MB).
    Completing 40% with 10 violations.
    elapsed time = 00:00:08, memory = 2001.88 (MB).
    Completing 50% with 10 violations.
    elapsed time = 00:00:08, memory = 1944.66 (MB).
    Completing 60% with 10 violations.
    elapsed time = 00:00:11, memory = 1906.65 (MB).
    Completing 70% with 10 violations.
    elapsed time = 00:00:12, memory = 1909.53 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:23, memory = 1845.59 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:23, memory = 1845.59 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:23, memory = 1845.59 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:02:16, elapsed time = 00:00:23, memory = 1845.59 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116155 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 7th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:01, memory = 1845.59 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:01, memory = 1845.59 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:02, memory = 1845.59 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1845.59 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1845.59 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1845.59 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1845.59 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:32, elapsed time = 00:00:03, memory = 1845.59 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 8
[INFO DRT-0200] Skipping iteration 9
[INFO DRT-0195] Start 10th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1845.59 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:01, memory = 1845.59 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:02, memory = 1845.59 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:02, memory = 1845.59 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1845.59 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116155 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 11
[INFO DRT-0200] Skipping iteration 12
[INFO DRT-0200] Skipping iteration 13
[INFO DRT-0200] Skipping iteration 14
[INFO DRT-0195] Start 15th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 16
[INFO DRT-0195] Start 17th optimization iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 18th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116155 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 19
[INFO DRT-0195] Start 20th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116155 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 21
[INFO DRT-0200] Skipping iteration 22
[INFO DRT-0195] Start 23rd stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:32, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116156 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 24th stubborn tiles iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 20% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 30% with 6 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 40% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 50% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 60% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 6 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 6.
Viol/Layer        met1
Short                6
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130758 um.
Total wire length on LAYER met2 = 116155 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 25th optimization iteration.
    Completing 10% with 6 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 9.
Viol/Layer        met1
Short                9
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130761 um.
Total wire length on LAYER met2 = 116153 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 26th stubborn tiles iteration.
    Completing 10% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 9 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 9 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 9 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 60% with 9 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 9 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130760 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 27th stubborn tiles iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:33, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130760 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 28
[INFO DRT-0200] Skipping iteration 29
[INFO DRT-0195] Start 30th stubborn tiles iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:32, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130760 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0195] Start 31st stubborn tiles iteration.
    Completing 10% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 8 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 8 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 8 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 8 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 8 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 8.
Viol/Layer        met1
Short                8
[INFO DRT-0267] cpu time = 00:00:31, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287284 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130760 um.
Total wire length on LAYER met2 = 116154 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50509.
Up-via summary (total 50509):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25341
           met2     1966
           met3      405
           met4       26
------------------------
               50509


[INFO DRT-0200] Skipping iteration 32
[INFO DRT-0195] Start 33rd optimization iteration.
    Completing 10% with 10 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 10 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 10 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 10 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 10 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 34th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 35th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 36th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130765 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 37th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 38th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130765 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 39th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 40th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 41st optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 42nd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287280 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 43rd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287280 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 44th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287280 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 45th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 46th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 47th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 48th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 49th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 50th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 51st optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 52nd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130765 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 53rd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 54th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287283 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130765 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 55th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 56th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 57th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287280 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 58th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:04, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:04, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:05, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:05, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287280 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130762 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 59th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:01, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 60th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:02, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 61st optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287282 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130764 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 62nd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:03, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 63rd optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:04, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:04, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0195] Start 64th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 30% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 40% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 50% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 60% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 70% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 80% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 90% with 12 violations.
    elapsed time = 00:00:00, memory = 1842.43 (MB).
    Completing 100% with 12 violations.
    elapsed time = 00:00:04, memory = 1842.43 (MB).
[INFO DRT-0199]   Number of violations = 12.
Viol/Layer        met1
Short               12
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:04, memory = 1842.43 (MB), peak = 2107.73 (MB)
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0198] Complete detail routing.
Total wire length = 287281 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130763 um.
Total wire length on LAYER met2 = 116148 um.
Total wire length on LAYER met3 = 32803 um.
Total wire length on LAYER met4 = 7390 um.
Total wire length on LAYER met5 = 175 um.
Total number of vias = 50507.
Up-via summary (total 50507):

------------------------
 FR_MASTERSLICE        0
            li1    22771
           met1    25339
           met2     1966
           met3      405
           met4       26
------------------------
               50507


[INFO DRT-0267] cpu time = 00:23:33, elapsed time = 00:04:19, memory = 1842.43 (MB), peak = 2107.73 (MB)

[INFO DRT-0180] Post processing.
Took 295 seconds: detailed_route -output_drc ./reports/sky130hd/VSDBabySoC/base/5_route_drc.rpt -output_maze ./results/sky130hd/VSDBabySoC/base/maze.log -droute_end_iter 64 -verbose 1 -drc_report_iter_step 5
[INFO GRT-0012] Found 6 antenna violations.
[INFO GRT-0015] Inserted 15 diodes.
[WARNING DRT-0120] Large net _02644_ has 121 pins which may impact routing performance. Consider optimization.
[WARNING DRT-0120] Large net net523 has 129 pins which may impact routing performance. Consider optimization.
[INFO DRT-0024]   Complete FR_MASTERSLICE.
[INFO DRT-0024]   Complete Fr_VIA.
[INFO DRT-0024]   Complete li1.
[INFO DRT-0024]   Complete mcon.
[INFO DRT-0024]   Complete met1.
[INFO DRT-0024]   Complete via.
[INFO DRT-0024]   Complete met2.
[INFO DRT-0024]   Complete via2.
[INFO DRT-0024]   Complete met3.
[INFO DRT-0024]   Complete via3.
[INFO DRT-0024]   Complete met4.
[INFO DRT-0024]   Complete via4.
[INFO DRT-0024]   Complete met5.
[INFO DRT-0165] Start pin access.
[INFO DRT-0076]   Complete 1000 pins.
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] Macro pin has more than 1 polygon
[WARNING DRT-6000] message limit (1000) reached. This message will no longer print.
[INFO DRT-0078]   Complete 1575 pins.
[INFO DRT-0079]   Complete 100 unique inst patterns.
[INFO DRT-0081]   Complete 194 unique inst patterns.
[INFO DRT-0084]   Complete 4407 groups.
#scanned instances     = 73040
#unique  instances     = 196
#stdCellGenAp          = 6265
#stdCellValidPlanarAp  = 92
#stdCellValidViaAp     = 4535
#stdCellPinNoAp        = 6
#stdCellPinCnt         = 22636
#instTermValidViaApCnt = 0
#macroGenAp            = 2045
#macroValidPlanarAp    = 1725
#macroValidViaAp       = 84
#macroNoAp             = 0
[INFO DRT-0166] Complete pin access.
[INFO DRT-0267] cpu time = 00:04:52, elapsed time = 00:00:36, memory = 1627.32 (MB), peak = 2107.73 (MB)

[INFO DRT-0157] Number of guides:     53979

[INFO DRT-0169] Post process guides.
[INFO DRT-0176] GCELLGRID X 0 DO 362 STEP 6900 ;
[INFO DRT-0177] GCELLGRID Y 0 DO 362 STEP 6900 ;
[INFO DRT-0028]   Complete FR_MASTERSLICE.
[INFO DRT-0028]   Complete Fr_VIA.
[INFO DRT-0028]   Complete li1.
[INFO DRT-0028]   Complete mcon.
[INFO DRT-0028]   Complete met1.
[INFO DRT-0028]   Complete via.
[INFO DRT-0028]   Complete met2.
[INFO DRT-0028]   Complete via2.
[INFO DRT-0028]   Complete met3.
[INFO DRT-0028]   Complete via3.
[INFO DRT-0028]   Complete met4.
[INFO DRT-0028]   Complete via4.
[INFO DRT-0028]   Complete met5.
[INFO DRT-0178] Init guide query.
[INFO DRT-0035]   Complete FR_MASTERSLICE (guide).
[INFO DRT-0035]   Complete Fr_VIA (guide).
[INFO DRT-0035]   Complete li1 (guide).
[INFO DRT-0035]   Complete mcon (guide).
[INFO DRT-0035]   Complete met1 (guide).
[INFO DRT-0035]   Complete via (guide).
[INFO DRT-0035]   Complete met2 (guide).
[INFO DRT-0035]   Complete via2 (guide).
[INFO DRT-0035]   Complete met3 (guide).
[INFO DRT-0035]   Complete via3 (guide).
[INFO DRT-0035]   Complete met4 (guide).
[INFO DRT-0035]   Complete via4 (guide).
[INFO DRT-0035]   Complete met5 (guide).
[INFO DRT-0036] FR_MASTERSLICE guide region query size = 0.
[INFO DRT-0036] FR_VIA guide region query size = 0.
[INFO DRT-0036] li1 guide region query size = 18637.
[INFO DRT-0036] mcon guide region query size = 0.
[INFO DRT-0036] met1 guide region query size = 16320.
[INFO DRT-0036] via guide region query size = 0.
[INFO DRT-0036] met2 guide region query size = 8203.
[INFO DRT-0036] via2 guide region query size = 0.
[INFO DRT-0036] met3 guide region query size = 644.
[INFO DRT-0036] via3 guide region query size = 0.
[INFO DRT-0036] met4 guide region query size = 245.
[INFO DRT-0036] via4 guide region query size = 0.
[INFO DRT-0036] met5 guide region query size = 12.
[INFO DRT-0179] Init gr pin query.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1627.32 (MB), peak = 2107.73 (MB)
[INFO DRT-0245] skipped writing guide updates to database.
[INFO DRT-0185] Post process initialize RPin region query.
[INFO DRT-0181] Start track assignment.
[INFO DRT-0184] Done with 27085 vertical wires in 8 frboxes and 16976 horizontal wires in 8 frboxes.
[INFO DRT-0186] Done with 2949 vertical wires in 8 frboxes and 5277 horizontal wires in 8 frboxes.
[INFO DRT-0182] Complete track assignment.
[INFO DRT-0267] cpu time = 00:00:09, elapsed time = 00:00:02, memory = 1654.82 (MB), peak = 2107.73 (MB)
[INFO DRT-0187] Start routing data preparation.
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1654.82 (MB), peak = 2107.73 (MB)
[INFO DRT-0194] Start detail routing.
[INFO DRT-0195] Start 0th optimization iteration.
    Completing 10% with 12 violations.
    elapsed time = 00:00:00, memory = 1654.82 (MB).
    Completing 20% with 12 violations.
    elapsed time = 00:00:01, memory = 1702.57 (MB).
    Completing 30% with 28 violations.
    elapsed time = 00:00:01, memory = 1642.76 (MB).
    Completing 40% with 28 violations.
    elapsed time = 00:00:01, memory = 1719.63 (MB).
    Completing 50% with 28 violations.
    elapsed time = 00:00:03, memory = 1613.71 (MB).
    Completing 60% with 37 violations.
    elapsed time = 00:00:03, memory = 1613.71 (MB).
    Completing 70% with 37 violations.
    elapsed time = 00:00:04, memory = 1850.58 (MB).
    Completing 80% with 50 violations.
    elapsed time = 00:00:05, memory = 1613.65 (MB).
    Completing 90% with 50 violations.
    elapsed time = 00:00:05, memory = 1733.65 (MB).
    Completing 100% with 65 violations.
    elapsed time = 00:00:06, memory = 1672.48 (MB).
[INFO DRT-0199]   Number of violations = 73.
Viol/Layer        met1   met2   met3   met4
Metal Spacing        2      6      0      0
Recheck              3      1      3      1
Short               47      4      5      1
[INFO DRT-0267] cpu time = 00:00:55, elapsed time = 00:00:07, memory = 1931.85 (MB), peak = 2107.73 (MB)
Total wire length = 287320 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130746 um.
Total wire length on LAYER met2 = 116163 um.
Total wire length on LAYER met3 = 32872 um.
Total wire length on LAYER met4 = 7372 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50525.
Up-via summary (total 50525):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25346
           met2     1966
           met3      396
           met4       24
------------------------
               50525


[INFO DRT-0195] Start 1st optimization iteration.
    Completing 10% with 73 violations.
    elapsed time = 00:00:00, memory = 1931.85 (MB).
    Completing 20% with 73 violations.
    elapsed time = 00:00:01, memory = 1931.85 (MB).
    Completing 30% with 60 violations.
    elapsed time = 00:00:01, memory = 1931.85 (MB).
    Completing 40% with 60 violations.
    elapsed time = 00:00:01, memory = 1931.85 (MB).
    Completing 50% with 60 violations.
    elapsed time = 00:00:03, memory = 1931.85 (MB).
    Completing 60% with 51 violations.
    elapsed time = 00:00:03, memory = 1931.85 (MB).
    Completing 70% with 51 violations.
    elapsed time = 00:00:04, memory = 1931.98 (MB).
    Completing 80% with 53 violations.
    elapsed time = 00:00:04, memory = 1931.98 (MB).
    Completing 90% with 53 violations.
    elapsed time = 00:00:05, memory = 1931.98 (MB).
    Completing 100% with 43 violations.
    elapsed time = 00:00:06, memory = 1931.98 (MB).
[INFO DRT-0199]   Number of violations = 43.
Viol/Layer        met1   met2   met3
Metal Spacing        0      1      0
Short               34      7      1
[INFO DRT-0267] cpu time = 00:00:53, elapsed time = 00:00:06, memory = 1932.10 (MB), peak = 2107.73 (MB)
Total wire length = 287336 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130750 um.
Total wire length on LAYER met2 = 116169 um.
Total wire length on LAYER met3 = 32875 um.
Total wire length on LAYER met4 = 7375 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50523.
Up-via summary (total 50523):

------------------------
 FR_MASTERSLICE        0
            li1    22794
           met1    25344
           met2     1966
           met3      395
           met4       24
------------------------
               50523


[INFO DRT-0195] Start 2nd optimization iteration.
    Completing 10% with 43 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 20% with 43 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 30% with 44 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 40% with 44 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 50% with 44 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 60% with 43 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 70% with 43 violations.
    elapsed time = 00:00:00, memory = 1932.10 (MB).
    Completing 80% with 42 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 42 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 42 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 42.
Viol/Layer        met1   met2
Short               33      9
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287335 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130751 um.
Total wire length on LAYER met2 = 116169 um.
Total wire length on LAYER met3 = 32874 um.
Total wire length on LAYER met4 = 7375 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50523.
Up-via summary (total 50523):

------------------------
 FR_MASTERSLICE        0
            li1    22794
           met1    25344
           met2     1966
           met3      395
           met4       24
------------------------
               50523


[INFO DRT-0195] Start 3rd optimization iteration.
    Completing 10% with 42 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 42 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 37 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 37 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 37 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 37 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 37 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 31 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 31 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50544.
Up-via summary (total 50544):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25358
           met2     1972
           met3      397
           met4       24
------------------------
               50544
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 4th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132245 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17070 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1495
           met3      318
           met4        5
------------------------
               49761
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 5th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132245 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17070 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1495
           met3      318
           met4        5
------------------------
               49761
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 6th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132245 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17070 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1495
           met3      318
           met4        5
------------------------
               49761
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 7th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132245 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17070 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1495
           met3      318
           met4        5
------------------------
               49761
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 8th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132217 um.
Total wire length on LAYER met2 = 142687 um.
Total wire length on LAYER met3 = 17099 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49767.
Up-via summary (total 49767):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25061
           met2     1499
           met3      318
           met4        5
------------------------
               49767
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 9th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132216 um.
Total wire length on LAYER met2 = 142686 um.
Total wire length on LAYER met3 = 17099 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49767.
Up-via summary (total 49767):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25061
           met2     1499
           met3      318
           met4        5
------------------------
               49767
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 10th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132216 um.
Total wire length on LAYER met2 = 142686 um.
Total wire length on LAYER met3 = 17099 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49767.
Up-via summary (total 49767):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25061
           met2     1499
           met3      318
           met4        5
------------------------
               49767
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 11th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301030 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132181 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17132 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49767.
Up-via summary (total 49767):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25061
           met2     1499
           met3      318
           met4        5
------------------------
               49767


[INFO DRT-0195] Start 12th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301028 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132164 um.
Total wire length on LAYER met2 = 142683 um.
Total wire length on LAYER met3 = 17149 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49765.
Up-via summary (total 49765):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1499
           met3      318
           met4        5
------------------------
               49765


[INFO DRT-0195] Start 13th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301028 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132164 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17149 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49765.
Up-via summary (total 49765):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1499
           met3      318
           met4        5
------------------------
               49765


[INFO DRT-0195] Start 14th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301028 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132164 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17149 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49765.
Up-via summary (total 49765):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1499
           met3      318
           met4        5
------------------------
               49765


[INFO DRT-0195] Start 15th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301028 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132164 um.
Total wire length on LAYER met2 = 142683 um.
Total wire length on LAYER met3 = 17149 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49765.
Up-via summary (total 49765):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1499
           met3      318
           met4        5
------------------------
               49765


[INFO DRT-0195] Start 16th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 17.
Viol/Layer        met1
Short               17
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301028 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132164 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17149 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49765.
Up-via summary (total 49765):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1499
           met3      318
           met4        5
------------------------
               49765


[INFO DRT-0195] Start 17th optimization iteration.
    Completing 10% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 17 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132196 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763


[INFO DRT-0195] Start 18th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301036 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132195 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 12th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 13th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 14th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 15th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 16th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 17th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116127 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 18th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 19th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301036 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132195 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 20th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132194 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 21st optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132194 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 22nd optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132194 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116128 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 23rd optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132194 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287343 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116129 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 24th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132195 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17120 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49763.
Up-via summary (total 49763):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25059
           met2     1497
           met3      318
           met4        5
------------------------
               49763
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287343 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130726 um.
Total wire length on LAYER met2 = 116129 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 25th optimization iteration.
    Completing 10% with 18 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132184 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17134 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130729 um.
Total wire length on LAYER met2 = 116125 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542
>>>>>>> 2e9d213 (added assets)


[INFO DRT-0195] Start 26th optimization iteration.
    Completing 10% with 21 violations.
<<<<<<< HEAD
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301036 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132181 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 27th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301036 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132181 um.
Total wire length on LAYER met2 = 142685 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 28th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132180 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 29th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132180 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 30th optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132180 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 31st optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132181 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 32nd optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 18.
Viol/Layer        met1
Short               18
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132180 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 33rd optimization iteration.
    Completing 10% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 18 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 19 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132182 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17134 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 34th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132184 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 35th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132183 um.
Total wire length on LAYER met2 = 142684 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 36th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132182 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 37th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132183 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17134 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 38th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132182 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 39th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132184 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17134 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 40th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132183 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17135 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 41st optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 42nd optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17140 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 43rd optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 44th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 45th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 46th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 47th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 48th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 49th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 50th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17140 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 51st optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 52nd optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132177 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17140 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 53rd optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:01, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301033 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 54th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17140 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 55th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301035 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132179 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17139 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 56th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:02, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132178 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17140 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 57th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 58th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301032 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 59th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 40% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 50% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 60% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 70% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 80% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 90% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 100% with 21 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 21.
Viol/Layer        met1
Short               21
[INFO DRT-0267] cpu time = 00:00:06, elapsed time = 00:00:05, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301034 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132173 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8978 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 60th optimization iteration.
    Completing 10% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 61st optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:03, memory = 1721.66 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:04, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 62nd optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:04, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 63rd optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:04, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:05, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301030 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0195] Start 64th optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1721.66 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:05, memory = 1721.66 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:05, memory = 1721.66 (MB), peak = 1755.89 (MB)
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0198] Complete detail routing.
Total wire length = 301029 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 132172 um.
Total wire length on LAYER met2 = 142682 um.
Total wire length on LAYER met3 = 17144 um.
Total wire length on LAYER met4 = 8976 um.
Total wire length on LAYER met5 = 55 um.
Total number of vias = 49761.
Up-via summary (total 49761):

------------------------
 FR_MASTERSLICE        0
            li1    22884
           met1    25057
           met2     1497
           met3      318
           met4        5
------------------------
               49761


[INFO DRT-0267] cpu time = 00:03:07, elapsed time = 00:01:31, memory = 1721.66 (MB), peak = 1755.89 (MB)
=======
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 21 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116125 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 27th optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116125 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 28th optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116125 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 29th optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 30th optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287342 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 31st optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 32nd optimization iteration.
    Completing 10% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 20 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 20 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 20.
Viol/Layer        met1
Short               20
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287341 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130728 um.
Total wire length on LAYER met2 = 116126 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50542.
Up-via summary (total 50542):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25356
           met2     1972
           met3      397
           met4       24
------------------------
               50542


[INFO DRT-0195] Start 33rd optimization iteration.
    Completing 10% with 23 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 23 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 23 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 23 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 23 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116121 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 34th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 35th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 36th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 37th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 38th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 39th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 40th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 41st optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 42nd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 43rd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 44th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 45th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 46th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 47th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 48th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 49th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 50th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 51st optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 52nd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 53rd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:01, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 54th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287340 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 55th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 56th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 57th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:00, elapsed time = 00:00:00, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 58th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:04, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:05, elapsed time = 00:00:04, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 59th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:01, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:01, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 60th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:02, elapsed time = 00:00:02, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130730 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 61st optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:02, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:02, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287339 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130732 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 62nd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:03, elapsed time = 00:00:03, memory = 1932.20 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 63rd optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1932.20 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:03, memory = 1932.20 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:03, memory = 1934.95 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0195] Start 64th optimization iteration.
    Completing 10% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 20% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 30% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 40% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 50% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 60% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 70% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 80% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 90% with 24 violations.
    elapsed time = 00:00:00, memory = 1934.95 (MB).
    Completing 100% with 24 violations.
    elapsed time = 00:00:04, memory = 1934.95 (MB).
[INFO DRT-0199]   Number of violations = 24.
Viol/Layer        met1
Short               24
[INFO DRT-0267] cpu time = 00:00:04, elapsed time = 00:00:04, memory = 1934.95 (MB), peak = 2107.73 (MB)
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0198] Complete detail routing.
Total wire length = 287338 um.
Total wire length on LAYER li1 = 0 um.
Total wire length on LAYER met1 = 130731 um.
Total wire length on LAYER met2 = 116119 um.
Total wire length on LAYER met3 = 32903 um.
Total wire length on LAYER met4 = 7418 um.
Total wire length on LAYER met5 = 165 um.
Total number of vias = 50540.
Up-via summary (total 50540):

------------------------
 FR_MASTERSLICE        0
            li1    22793
           met1    25354
           met2     1972
           met3      397
           met4       24
------------------------
               50540


[INFO DRT-0267] cpu time = 00:03:27, elapsed time = 00:01:28, memory = 1934.95 (MB), peak = 2107.73 (MB)
>>>>>>> 2e9d213 (added assets)

[INFO DRT-0180] Post processing.
[INFO ANT-0002] Found 0 net violations.
[INFO ANT-0001] Found 0 pin violations.
[INFO ANT-0002] Found 0 net violations.
[INFO ANT-0001] Found 0 pin violations.
Report metrics stage 5, detailed route...

==========================================================================
detailed route report_design_area
--------------------------------------------------------------------------
<<<<<<< HEAD
Design area 729044 um^2 13% utilization.
Elapsed time: 6:31.98[h:]min:sec. CPU time: user 2242.70 sys 5.57 (573%). Peak memory: 1798036KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_2_route                        391           1755 c72253353bcaaadaa944
=======
Design area 727990 um^2 13% utilization.
Elapsed time: 7:12.82[h:]min:sec. CPU time: user 2202.16 sys 8.81 (510%). Peak memory: 2158320KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_2_route                        432           2107 bca927ff30ba2d98dda0
>>>>>>> 2e9d213 (added assets)
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 5_3_fillcell fillcell
Running fillcell.tcl, stage 5_3_fillcell
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/5_2_route.odb
filler_placement "sky130_fd_sc_hd__fill_1 sky130_fd_sc_hd__fill_2 sky130_fd_sc_hd__fill_4 sky130_fd_sc_hd__fill_8"
<<<<<<< HEAD
[INFO DPL-0001] Placed 604349 filler instances.
Elapsed time: 0:05.07[h:]min:sec. CPU time: user 4.36 sys 0.70 (100%). Peak memory: 822216KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_3_fillcell                       5            802 ca9f62e34798dbf27ef7
=======
[INFO DPL-0001] Placed 593753 filler instances.
Elapsed time: 0:05.04[h:]min:sec. CPU time: user 4.25 sys 0.78 (99%). Peak memory: 818264KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
5_3_fillcell                       5            799 e9979e84a0a53bf9315b
>>>>>>> 2e9d213 (added assets)
cp ./results/sky130hd/VSDBabySoC/base/5_3_fillcell.odb ./results/sky130hd/VSDBabySoC/base/5_route.odb
cp ./results/sky130hd/VSDBabySoC/base/5_1_grt.sdc ./results/sky130hd/VSDBabySoC/base/5_route.sdc
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 6_1_fill density_fill
Running density_fill.tcl, stage 6_1_fill
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/5_route.odb
exec cp ./results/sky130hd/VSDBabySoC/base/5_route.odb ./results/sky130hd/VSDBabySoC/base/6_1_fill.odb
<<<<<<< HEAD
Elapsed time: 0:02.45[h:]min:sec. CPU time: user 1.69 sys 0.61 (94%). Peak memory: 510644KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
6_1_fill                           2            498 ca9f62e34798dbf27ef7
=======
Elapsed time: 0:02.44[h:]min:sec. CPU time: user 1.67 sys 0.65 (95%). Peak memory: 512584KB.
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
6_1_fill                           2            500 e9979e84a0a53bf9315b
>>>>>>> 2e9d213 (added assets)
cp ./results/sky130hd/VSDBabySoC/base/5_route.sdc ./results/sky130hd/VSDBabySoC/base/6_1_fill.sdc
/home/shwetank/OpenROAD-flow-scripts/flow/scripts/flow.sh 6_report final_report
Running final_report.tcl, stage 6_report
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsddac.lib
read_liberty /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lib/avsdpll.lib
read_db ./results/sky130hd/VSDBabySoC/base/6_1_fill.odb
Deleted 0 routing obstructions
[INFO RCX-0431] Defined process_corner X with ext_model_index 0
[INFO RCX-0029] Defined extraction corner X
[INFO RCX-0435] Reading extraction model file /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/rcx_patterns.rules ...
[INFO RCX-0436] RC segment generation vsdbabysoc (max_merge_res 50.0) ...
<<<<<<< HEAD
[INFO RCX-0040] Final 29138 rc segments
[INFO RCX-0439] Coupling Cap extraction vsdbabysoc ...
[INFO RCX-0440] Coupling threshhold is 0.1000 fF, coupling capacitance less than 0.1000 fF will be grounded.
[INFO RCX-0442] 6% of 99670 wires extracted
[INFO RCX-0442] 13% of 99670 wires extracted
[INFO RCX-0442] 44% of 99670 wires extracted
[INFO RCX-0442] 60% of 99670 wires extracted
[INFO RCX-0442] 74% of 99670 wires extracted
[INFO RCX-0442] 94% of 99670 wires extracted
[INFO RCX-0442] 99% of 99670 wires extracted
[INFO RCX-0045] Extract 6516 nets, 35620 rsegs, 35620 caps, 62815 ccs
[INFO RCX-0443] 6516 nets finished
[WARNING PSM-0038] Unconnected node on net VDD at location (107.650um, 186.725um), layer: met4.
[WARNING PSM-0038] Unconnected node on net VDD at location (107.755um, 184.405um), layer: met5.
[WARNING PSM-0039] Unconnected instance dac/VPWR at location (107.702um, 185.962um).
[ERROR PSM-0069] Check connectivity failed on VDD.
Error: final_report.tcl, 60 PSM-0069
Command exited with non-zero status 1
Elapsed time: 0:22.92[h:]min:sec. CPU time: user 21.91 sys 1.00 (100%). Peak memory: 960436KB.
make[1]: *** [Makefile:618: do-6_report] Error 1
make: *** [Makefile:618: logs/sky130hd/VSDBabySoC/base/6_report.log] Error 2
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ 

=======
[INFO RCX-0040] Final 28655 rc segments
[INFO RCX-0439] Coupling Cap extraction vsdbabysoc ...
[INFO RCX-0440] Coupling threshhold is 0.1000 fF, coupling capacitance less than 0.1000 fF will be grounded.
[INFO RCX-0442] 27% of 189724 wires extracted
[INFO RCX-0442] 35% of 189724 wires extracted
[INFO RCX-0442] 51% of 189724 wires extracted
[INFO RCX-0442] 66% of 189724 wires extracted
[INFO RCX-0442] 85% of 189724 wires extracted
[INFO RCX-0442] 99% of 189724 wires extracted
[INFO RCX-0045] Extract 6474 nets, 35094 rsegs, 35094 caps, 64437 ccs
[INFO RCX-0443] 6474 nets finished
[WARNING PSM-0038] Unconnected node on net VDD at location (122.635um, 125.885um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (131.225um, 130.705um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (133.130um, 128.260um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (136.405um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (136.510um, 128.940um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (137.515um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (137.760um, 128.790um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (140.245um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (141.490um, 128.865um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (142.905um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (144.435um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (146.815um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (147.925um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (149.765um, 128.960um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (150.655um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (151.815um, 128.940um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (153.315um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (153.790um, 128.960um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (153.790um, 129.290um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (154.845um, 128.240um), layer: li1.
[WARNING PSM-0038] Unconnected node on net VDD at location (127.330um, 128.370um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (128.530um, 128.610um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (128.530um, 130.700um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (129.230um, 128.610um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (132.375um, 128.610um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (135.520um, 128.765um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (135.910um, 128.765um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (138.570um, 124.970um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (140.570um, 128.285um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (145.230um, 128.850um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (146.320um, 128.850um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (150.985um, 128.610um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (155.650um, 128.465um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (156.340um, 128.465um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (156.350um, 128.550um), layer: met1.
[WARNING PSM-0038] Unconnected node on net VDD at location (137.090um, 336.665um), layer: met4.
[WARNING PSM-0038] Unconnected node on net VDD at location (137.195um, 334.345um), layer: met5.
[WARNING PSM-0039] Unconnected instance dac/VPWR at location (137.142um, 335.902um).
[WARNING PSM-0039] Unconnected instance pll/VDD at location (140.119um, 128.580um).
[ERROR PSM-0069] Check connectivity failed on VDD.
Error: final_report.tcl, 60 PSM-0069
Command exited with non-zero status 1
Elapsed time: 0:24.67[h:]min:sec. CPU time: user 23.43 sys 1.16 (99%). Peak memory: 991112KB.
make[1]: *** [Makefile:618: do-6_report] Error 1
make: *** [Makefile:618: logs/sky130hd/VSDBabySoC/base/6_report.log] Error 2
shwetank@shwetank-VirtualBox:~/OpenROAD-flow-scripts/flow$ YOSYS_EXE=~/OpenROAD-flow-scripts/tools/yosys/yosys OPENROAD_EXE=~/OpenROAD-flow-scripts/tools/OpenROAD/build/bin/openroad make DESIGN_CONFIG=./designs/sky130hd/VSDBabySoC/config.mk
cp ./results/sky130hd/VSDBabySoC/base/5_route.sdc ./results/sky130hd/VSDBabySoC/base/6_final.sdc
cp /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/lef/sky130_fd_sc_hd.tlef ./objects/sky130hd/VSDBabySoC/base/klayout_tech.lef
SC_LEF_RELATIVE_PATH="../../../../platforms/sky130hd/lef/sky130_fd_sc_hd_merged.lef"; \
OTHER_LEFS_RELATIVE_PATHS=$(echo "<lef-files>$(realpath --relative-to=./results/sky130hd/VSDBabySoC/base ./objects/sky130hd/VSDBabySoC/base/klayout_tech.lef)</lef-files> <lef-files>$(realpath --relative-to=./results/sky130hd/VSDBabySoC/base /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsddac.lef)</lef-files> <lef-files>$(realpath --relative-to=./results/sky130hd/VSDBabySoC/base /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/lef/avsdpll.lef)</lef-files>"); \
sed 's,<lef-files>.*</lef-files>,<lef-files>'"$SC_LEF_RELATIVE_PATH"'</lef-files>'"$OTHER_LEFS_RELATIVE_PATHS"',g' /home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/sky130hd.lyt > ./objects/sky130hd/VSDBabySoC/base/klayout.lyt
sed -i 's,<map-file>.*</map-file>,<map-file>/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/*map</map-file>,g' ./objects/sky130hd/VSDBabySoC/base/klayout.lyt
(env time -f 'Elapsed time: %E[h:]min:sec. CPU time: user %U sys %S (%P). Peak memory: %MKB.' stdbuf -o L /home/shwetank/OpenROAD-flow-scripts/flow/scripts/klayout.sh -zz -rd design_name=vsdbabysoc \
        -rd in_def=./results/sky130hd/VSDBabySoC/base/6_final.def \
        -rd in_files="/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/gds/sky130_fd_sc_hd.gds /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/gds/avsddac.gds /home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/gds/avsdpll.gds " \
        -rd seal_file="" \
        -rd out_file=./results/sky130hd/VSDBabySoC/base/6_1_merged.gds \
        -rd tech_file=./objects/sky130hd/VSDBabySoC/base/klayout.lyt \
        -rd layer_map= \
        -r /home/shwetank/OpenROAD-flow-scripts/flow/util/def2stream.py) 2>&1 | tee /home/shwetank/OpenROAD-flow-scripts/flow/logs/sky130hd/VSDBabySoC/base/6_1_merge.log
KLayout 0.30.3
[INFO] Reporting cells prior to loading DEF ...
	/home/shwetank/OpenROAD-flow-scripts/flow/platforms/sky130hd/gds/sky130_fd_sc_hd.gds
	/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/gds/avsddac.gds
	/home/shwetank/OpenROAD-flow-scripts/flow/designs/sky130hd/VSDBabySoC/gds/avsdpll.gds
[INFO] All LEF cells have matching GDS/OAS cells
[INFO] No orphan cells in the final layout
Elapsed time: 0:08.29[h:]min:sec. CPU time: user 7.42 sys 0.78 (99%). Peak memory: 972900KB.
cp results/sky130hd/VSDBabySoC/base/6_1_merged.gds results/sky130hd/VSDBabySoC/base/6_final.gds
./logs/sky130hd/VSDBabySoC/base
Log                        Elapsed/s Peak Memory/MB  sha1sum .odb [0:20)
1_1_yosys_canonicalize             0             54 338db507fe989c92b160
1_2_yosys                          9             70 e5ee1f8010c8b37c294c
2_1_floorplan                      2            135 d6734a29e94f5091b74e
2_2_floorplan_macro               19            159 a324dd60a9c6c61e1ba0
2_3_floorplan_tapcell              0            140 2afe6075f752fa45aa06
2_4_floorplan_pdn                  4            360 1c6519b371b0e499d736
3_1_place_gp_skip_io              33            242 79d6ed7c3bab88d508f2
3_2_place_iop                      1            198 9e5a03a46f9265d68b07
3_3_place_gp                      52            551 7d0ed6f726713a1d7592
3_4_place_resized                  4            218 ddf1cb35eaa9f5dc0184
3_5_place_dp                       7            388 d18f5dba917ef0a72ffd
4_1_cts                            6            383 e472cbf89ebd934e45ef
5_1_grt                           47            889 6e7a100bc8a27a03ffe9
5_2_route                        432           2107 bca927ff30ba2d98dda0
5_3_fillcell                       5            799 e9979e84a0a53bf9315b
6_1_fill                           2            500 e9979e84a0a53bf9315b
6_1_merge                          8            950                  N/A
6_report                          24            967                  N/A
Total                            655           2107                     
>>>>>>> 2e9d213 (added assets)

