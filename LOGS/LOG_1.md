(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ yosys

 /----------------------------------------------------------------------------\
 |  yosys -- Yosys Open SYnthesis Suite                                       |
 |  Copyright (C) 2012 - 2025  Claire Xenia Wolf <claire@yosyshq.com>         |
 |  Distributed under an ISC-like license, type "license" to see terms        |
 \----------------------------------------------------------------------------/
 Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)

yosys> read_liberty -lib /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

1. Executing Liberty frontend: /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
Imported 428 cell types from liberty file.

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v

2. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v' to AST representation.
Generating RTLIL representation for module `\sub_module2'.
Generating RTLIL representation for module `\sub_module1'.
Generating RTLIL representation for module `\multiple_modules'.
Successfully finished Verilog frontend.

yosys> synth -top multiple_modules

3. Executing SYNTH pass.

3.1. Executing HIERARCHY pass (managing design hierarchy).

3.1.1. Analyzing design hierarchy..
Top module:  \multiple_modules
Used module:     \sub_module2
Used module:     \sub_module1

3.1.2. Analyzing design hierarchy..
Top module:  \multiple_modules
Used module:     \sub_module2
Used module:     \sub_module1
Removed 0 unused modules.

3.2. Executing PROC pass (convert processes to netlists).

3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed a total of 0 dead cases.

3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 0 assignments to connections.

3.2.4. Executing PROC_INIT pass (extract init attributes).

3.2.5. Executing PROC_ARST pass (detect async resets in processes).

3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.

3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).

3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).

3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..
Removed 0 unused cells and 2 unused wires.
<suppressed ~2 debug messages>

3.5. Executing CHECK pass (checking for obvious problems).
Checking module multiple_modules...
Checking module sub_module1...
Checking module sub_module2...
Found and reported 0 problems.

3.6. Executing OPT pass (performing simple optimizations).

3.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \multiple_modules..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module2..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \multiple_modules.
  Optimizing cells in module \sub_module1.
  Optimizing cells in module \sub_module2.
Performed a total of 0 changes.

3.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.6.6. Executing OPT_DFF pass (perform DFF optimizations).

3.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.6.9. Finished fast OPT passes. (There is nothing left to do.)

3.7. Executing FSM pass (extract and optimize FSM).

3.7.1. Executing FSM_DETECT pass (finding FSMs in design).

3.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

3.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

3.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

3.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

3.8. Executing OPT pass (performing simple optimizations).

3.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \multiple_modules..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module2..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \multiple_modules.
  Optimizing cells in module \sub_module1.
  Optimizing cells in module \sub_module2.
Performed a total of 0 changes.

3.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.8.6. Executing OPT_DFF pass (perform DFF optimizations).

3.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.8.9. Finished fast OPT passes. (There is nothing left to do.)

3.9. Executing WREDUCE pass (reducing word size of cells).

3.10. Executing PEEPOPT pass (run peephole optimizers).

3.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module multiple_modules:
  created 0 $alu and 0 $macc cells.
Extracting $alu and $macc cells in module sub_module1:
  created 0 $alu and 0 $macc cells.
Extracting $alu and $macc cells in module sub_module2:
  created 0 $alu and 0 $macc cells.

3.13. Executing SHARE pass (SAT-based resource sharing).

3.14. Executing OPT pass (performing simple optimizations).

3.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \multiple_modules..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module2..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \multiple_modules.
  Optimizing cells in module \sub_module1.
  Optimizing cells in module \sub_module2.
Performed a total of 0 changes.

3.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.14.6. Executing OPT_DFF pass (perform DFF optimizations).

3.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.14.9. Finished fast OPT passes. (There is nothing left to do.)

3.15. Executing MEMORY pass.

3.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

3.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

3.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

3.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

3.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

3.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

3.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

3.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.17. Executing OPT pass (performing simple optimizations).

3.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.17.3. Executing OPT_DFF pass (perform DFF optimizations).

3.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.17.5. Finished fast OPT passes.

3.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

3.19. Executing OPT pass (performing simple optimizations).

3.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \multiple_modules..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Running muxtree optimizer on module \sub_module2..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \multiple_modules.
  Optimizing cells in module \sub_module1.
  Optimizing cells in module \sub_module2.
Performed a total of 0 changes.

3.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.19.6. Executing OPT_SHARE pass.

3.19.7. Executing OPT_DFF pass (perform DFF optimizations).

3.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.19.10. Finished fast OPT passes. (There is nothing left to do.)

3.20. Executing TECHMAP pass (map to technology primitives).

3.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

3.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $or.
Using extmapper simplemap for cells of type $and.
No more expansions possible.
<suppressed ~79 debug messages>

3.21. Executing OPT pass (performing simple optimizations).

3.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.21.3. Executing OPT_DFF pass (perform DFF optimizations).

3.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..

3.21.5. Finished fast OPT passes.

3.22. Executing ABC pass (technology mapping using ABC).

3.22.1. Extracting gate netlist of module `\multiple_modules' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

3.22.1.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.

3.22.2. Extracting gate netlist of module `\sub_module1' to `<abc-temp-dir>/input.blif'..

3.22.2.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-qnlBlt/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

3.22.2.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.

3.22.3. Extracting gate netlist of module `\sub_module2' to `<abc-temp-dir>/input.blif'..

3.22.3.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-qnlBlt/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

3.22.3.2. Re-integrating ABC results.
ABC RESULTS:                OR cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

3.23. Executing OPT pass (performing simple optimizations).

3.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module multiple_modules.
Optimizing module sub_module1.
Optimizing module sub_module2.

3.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\multiple_modules'.
Finding identical cells in module `\sub_module1'.
Finding identical cells in module `\sub_module2'.
Removed a total of 0 cells.

3.23.3. Executing OPT_DFF pass (perform DFF optimizations).

3.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \multiple_modules..
Finding unused cells or wires in module \sub_module1..
Finding unused cells or wires in module \sub_module2..
Removed 0 unused cells and 6 unused wires.
<suppressed ~2 debug messages>

3.23.5. Finished fast OPT passes.

3.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `multiple_modules'. Setting top module to multiple_modules.

3.24.1. Analyzing design hierarchy..
Top module:  \multiple_modules
Used module:     \sub_module1
Used module:     \sub_module2

3.24.2. Analyzing design hierarchy..
Top module:  \multiple_modules
Used module:     \sub_module1
Used module:     \sub_module2
Removed 0 unused modules.

3.25. Printing statistics.

=== multiple_modules ===

        +----------Local Count, excluding submodules.
        | 
        5 wires
        5 wire bits
        5 public wires
        5 public wire bits
        4 ports
        4 port bits
        2 submodules
        1   sub_module1
        1   sub_module2

=== sub_module1 ===

        +----------Local Count, excluding submodules.
        | 
        3 wires
        3 wire bits
        3 public wires
        3 public wire bits
        3 ports
        3 port bits
        1 cells
        1   $_AND_

=== sub_module2 ===

        +----------Local Count, excluding submodules.
        | 
        3 wires
        3 wire bits
        3 public wires
        3 public wire bits
        3 ports
        3 port bits
        1 cells
        1   $_OR_

=== design hierarchy ===

        +----------Count including submodules.
        | 
        2 multiple_modules
        1 sub_module1
        1 sub_module2

        +----------Count including submodules.
        | 
       11 wires
       11 wire bits
       11 public wires
       11 public wire bits
       10 ports
       10 port bits
        - memories
        - memory bits
        - processes
        2 cells
        1   $_AND_
        1   $_OR_
        2 submodules
        1   sub_module1
        1   sub_module2

3.26. Executing CHECK pass (checking for obvious problems).
Checking module multiple_modules...
Checking module sub_module1...
Checking module sub_module2...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

4. Executing ABC pass (technology mapping using ABC).

4.1. Extracting gate netlist of module `\multiple_modules' to `<abc-temp-dir>/input.blif'..
Don't call ABC as there is nothing to map.

4.1.1. Executed ABC.
Extracted 0 gates and 0 wires to a netlist network with 0 inputs and 0 outputs.
Removing temp directory.

4.2. Extracting gate netlist of module `\sub_module1' to `<abc-temp-dir>/input.blif'..

4.2.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

4.2.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__and2_0 cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.

4.3. Extracting gate netlist of module `\sub_module2' to `<abc-temp-dir>/input.blif'..

4.3.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.06 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.09 sec
ABC: Memory =   19.85 MB. Time =     0.09 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

4.3.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__lpflow_inputiso1p_1 cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

yosys> write_verilog multiple_modules_generated_netlist.v

5. Executing Verilog backend.

5.1. Executing BMUXMAP pass.

5.2. Executing DEMUXMAP pass.
Dumping module `\multiple_modules'.
Dumping module `\sub_module1'.
Dumping module `\sub_module2'.

yosys> write_verilog -noattr multiple_modules__natr_generated_netlist.v

6. Executing Verilog backend.

6.1. Executing BMUXMAP pass.

6.2. Executing DEMUXMAP pass.
Dumping module `\multiple_modules'.
Dumping module `\sub_module1'.
Dumping module `\sub_module2'.

yosys> show multiple_modules

7. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module multiple_modules to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)
/usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> flatten

8. Executing FLATTEN pass (flatten design).
Deleting now unused module sub_module1.
Deleting now unused module sub_module2.
<suppressed ~2 debug messages>

yosys> write_verilog -noattr multiple_modules_flattened_natr_generated_netlist.v

9. Executing Verilog backend.

9.1. Executing BMUXMAP pass.

9.2. Executing DEMUXMAP pass.
Dumping module `\multiple_modules'.

yosys> show

10. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module multiple_modules to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> synth -top sub_module1

11. Executing SYNTH pass.

11.1. Executing HIERARCHY pass (managing design hierarchy).
ERROR: Module `sub_module1' not found!

yosys> exit

End of script. Logfile hash: 38b8352fd9, CPU: user 0.14s system 0.06s, MEM: 49.00 MB peak
Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)
Time spent: 71% 2x abc (0 sec), 10% 2x read_liberty (0 sec), ...
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ yosys

 /----------------------------------------------------------------------------\
 |  yosys -- Yosys Open SYnthesis Suite                                       |
 |  Copyright (C) 2012 - 2025  Claire Xenia Wolf <claire@yosyshq.com>         |
 |  Distributed under an ISC-like license, type "license" to see terms        |
 \----------------------------------------------------------------------------/
 Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)

yosys> read_liberty -lib /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

1. Executing Liberty frontend: /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
Imported 428 cell types from liberty file.

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v

2. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/multiple_modules.v' to AST representation.
Generating RTLIL representation for module `\sub_module2'.
Generating RTLIL representation for module `\sub_module1'.
Generating RTLIL representation for module `\multiple_modules'.
Successfully finished Verilog frontend.

yosys> synth -top sub_module1

3. Executing SYNTH pass.

3.1. Executing HIERARCHY pass (managing design hierarchy).

3.1.1. Analyzing design hierarchy..
Top module:  \sub_module1

3.1.2. Analyzing design hierarchy..
Top module:  \sub_module1
Removing unused module `\multiple_modules'.
Removing unused module `\sub_module2'.
Removed 2 unused modules.

3.2. Executing PROC pass (convert processes to netlists).

3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Removed a total of 0 dead cases.

3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 0 redundant assignments.
Promoted 0 assignments to connections.

3.2.4. Executing PROC_INIT pass (extract init attributes).

3.2.5. Executing PROC_ARST pass (detect async resets in processes).

3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.

3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).

3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).

3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).

3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..
Removed 0 unused cells and 1 unused wires.
<suppressed ~1 debug messages>

3.5. Executing CHECK pass (checking for obvious problems).
Checking module sub_module1...
Found and reported 0 problems.

3.6. Executing OPT pass (performing simple optimizations).

3.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \sub_module1.
Performed a total of 0 changes.

3.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.6.6. Executing OPT_DFF pass (perform DFF optimizations).

3.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.6.9. Finished fast OPT passes. (There is nothing left to do.)

3.7. Executing FSM pass (extract and optimize FSM).

3.7.1. Executing FSM_DETECT pass (finding FSMs in design).

3.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

3.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

3.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

3.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

3.8. Executing OPT pass (performing simple optimizations).

3.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \sub_module1.
Performed a total of 0 changes.

3.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.8.6. Executing OPT_DFF pass (perform DFF optimizations).

3.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.8.9. Finished fast OPT passes. (There is nothing left to do.)

3.9. Executing WREDUCE pass (reducing word size of cells).

3.10. Executing PEEPOPT pass (run peephole optimizers).

3.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module sub_module1:
  created 0 $alu and 0 $macc cells.

3.13. Executing SHARE pass (SAT-based resource sharing).

3.14. Executing OPT pass (performing simple optimizations).

3.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \sub_module1.
Performed a total of 0 changes.

3.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.14.6. Executing OPT_DFF pass (perform DFF optimizations).

3.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.14.9. Finished fast OPT passes. (There is nothing left to do.)

3.15. Executing MEMORY pass.

3.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

3.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

3.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

3.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

3.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

3.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

3.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

3.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.17. Executing OPT pass (performing simple optimizations).

3.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.17.3. Executing OPT_DFF pass (perform DFF optimizations).

3.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.17.5. Finished fast OPT passes.

3.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

3.19. Executing OPT pass (performing simple optimizations).

3.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \sub_module1..
  Creating internal representation of mux trees.
  No muxes found in this module.
Removed 0 multiplexer ports.

3.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \sub_module1.
Performed a total of 0 changes.

3.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.19.6. Executing OPT_SHARE pass.

3.19.7. Executing OPT_DFF pass (perform DFF optimizations).

3.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.19.10. Finished fast OPT passes. (There is nothing left to do.)

3.20. Executing TECHMAP pass (map to technology primitives).

3.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

3.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $and.
No more expansions possible.
<suppressed ~78 debug messages>

3.21. Executing OPT pass (performing simple optimizations).

3.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.21.3. Executing OPT_DFF pass (perform DFF optimizations).

3.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..

3.21.5. Finished fast OPT passes.

3.22. Executing ABC pass (technology mapping using ABC).

3.22.1. Extracting gate netlist of module `\sub_module1' to `<abc-temp-dir>/input.blif'..

3.22.1.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-ZEoC1w/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

3.22.1.2. Re-integrating ABC results.
ABC RESULTS:               AND cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

3.23. Executing OPT pass (performing simple optimizations).

3.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module sub_module1.

3.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\sub_module1'.
Removed a total of 0 cells.

3.23.3. Executing OPT_DFF pass (perform DFF optimizations).

3.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \sub_module1..
Removed 0 unused cells and 3 unused wires.
<suppressed ~1 debug messages>

3.23.5. Finished fast OPT passes.

3.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `sub_module1'. Setting top module to sub_module1.

3.24.1. Analyzing design hierarchy..
Top module:  \sub_module1

3.24.2. Analyzing design hierarchy..
Top module:  \sub_module1
Removed 0 unused modules.

3.25. Printing statistics.

=== sub_module1 ===

        +----------Local Count, excluding submodules.
        | 
        3 wires
        3 wire bits
        3 public wires
        3 public wire bits
        3 ports
        3 port bits
        1 cells
        1   $_AND_

3.26. Executing CHECK pass (checking for obvious problems).
Checking module sub_module1...
Found and reported 0 problems.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

4. Executing ABC pass (technology mapping using ABC).

4.1. Extracting gate netlist of module `\sub_module1' to `<abc-temp-dir>/input.blif'..

4.1.1. Executed ABC.
Extracted 1 gates and 3 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.10 sec
ABC: Memory =   19.85 MB. Time =     0.10 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

4.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__and2_0 cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr multiple_modules_sub_module1_generated_netlist.v

5. Executing Verilog backend.

5.1. Executing BMUXMAP pass.

5.2. Executing DEMUXMAP pass.
Dumping module `\sub_module1'.

yosys> show

6. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module sub_module1 to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> exit

End of script. Logfile hash: c8a4222bfb, CPU: user 0.10s system 0.02s, MEM: 47.62 MB peak
Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)
Time spent: 61% 2x abc (0 sec), 16% 2x read_liberty (0 sec), ...
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ iverilog /home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v /home/ank/Desktop/SoC_Shwetank/verilog_files/tb_dff_asyncres_syncres.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ./a.out
VCD info: dumpfile tb_dff_asyncres_syncres.vcd opened for output.
/home/ank/Desktop/SoC_Shwetank/verilog_files/tb_dff_asyncres_syncres.v:25: $finish called at 3000000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ gtkwave tb_dff_asyncres_syncres.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[3000000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ yosys

 /----------------------------------------------------------------------------\
 |  yosys -- Yosys Open SYnthesis Suite                                       |
 |  Copyright (C) 2012 - 2025  Claire Xenia Wolf <claire@yosyshq.com>         |
 |  Distributed under an ISC-like license, type "license" to see terms        |
 \----------------------------------------------------------------------------/
 Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)

yosys> read_liberty -lib /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

1. Executing Liberty frontend: /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib
Imported 428 cell types from liberty file.

yosys> read_verilog /home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v

2. Executing Verilog-2005 frontend: /home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v
Parsing Verilog input from `/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v' to AST representation.
Generating RTLIL representation for module `\dff_asyncres_syncres'.
Successfully finished Verilog frontend.

yosys> synth -top dff_asyncres_syncres

3. Executing SYNTH pass.

3.1. Executing HIERARCHY pass (managing design hierarchy).

3.1.1. Analyzing design hierarchy..
Top module:  \dff_asyncres_syncres

3.1.2. Analyzing design hierarchy..
Top module:  \dff_asyncres_syncres
Removed 0 unused modules.

3.2. Executing PROC pass (convert processes to netlists).

3.2.1. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Cleaned up 0 empty switches.

3.2.2. Executing PROC_RMDEAD pass (remove dead branches from decision trees).
Marked 2 switch rules as full_case in process $proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1 in module dff_asyncres_syncres.
Removed a total of 0 dead cases.

3.2.3. Executing PROC_PRUNE pass (remove redundant assignments in processes).
Removed 1 redundant assignment.
Promoted 0 assignments to connections.

3.2.4. Executing PROC_INIT pass (extract init attributes).

3.2.5. Executing PROC_ARST pass (detect async resets in processes).
Found async reset \async_reset in `\dff_asyncres_syncres.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1'.

3.2.6. Executing PROC_ROM pass (convert switches to ROMs).
Converted 0 switches.
<suppressed ~1 debug messages>

3.2.7. Executing PROC_MUX pass (convert decision trees to multiplexers).
Creating decoders for process `\dff_asyncres_syncres.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1'.
     1/1: $0\q[0:0]

3.2.8. Executing PROC_DLATCH pass (convert process syncs to latches).

3.2.9. Executing PROC_DFF pass (convert process syncs to FFs).
Creating register for signal `\dff_asyncres_syncres.\q' using process `\dff_asyncres_syncres.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1'.
  created $adff cell `$procdff$7' with positive edge clock and positive level reset.

3.2.10. Executing PROC_MEMWR pass (convert process memory writes to cells).

3.2.11. Executing PROC_CLEAN pass (remove empty switches from decision trees).
Found and cleaned up 1 empty switch in `\dff_asyncres_syncres.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1'.
Removing empty process `dff_asyncres_syncres.$proc$/home/ank/Desktop/SoC_Shwetank/verilog_files/dff_asyncres_syncres.v:2$1'.
Cleaned up 1 empty switch.

3.2.12. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.
<suppressed ~1 debug messages>

3.3. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..
Removed 0 unused cells and 3 unused wires.
<suppressed ~1 debug messages>

3.5. Executing CHECK pass (checking for obvious problems).
Checking module dff_asyncres_syncres...
Found and reported 0 problems.

3.6. Executing OPT pass (performing simple optimizations).

3.6.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.6.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.6.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \dff_asyncres_syncres..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

3.6.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \dff_asyncres_syncres.
Performed a total of 0 changes.

3.6.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.6.6. Executing OPT_DFF pass (perform DFF optimizations).

3.6.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.6.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.6.9. Finished fast OPT passes. (There is nothing left to do.)

3.7. Executing FSM pass (extract and optimize FSM).

3.7.1. Executing FSM_DETECT pass (finding FSMs in design).

3.7.2. Executing FSM_EXTRACT pass (extracting FSM from design).

3.7.3. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.7.5. Executing FSM_OPT pass (simple optimizations of FSMs).

3.7.6. Executing FSM_RECODE pass (re-assigning FSM state encoding).

3.7.7. Executing FSM_INFO pass (dumping all available information on FSM cells).

3.7.8. Executing FSM_MAP pass (mapping FSMs to basic logic).

3.8. Executing OPT pass (performing simple optimizations).

3.8.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.8.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.8.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \dff_asyncres_syncres..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

3.8.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \dff_asyncres_syncres.
Performed a total of 0 changes.

3.8.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.8.6. Executing OPT_DFF pass (perform DFF optimizations).

3.8.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.8.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.8.9. Finished fast OPT passes. (There is nothing left to do.)

3.9. Executing WREDUCE pass (reducing word size of cells).

3.10. Executing PEEPOPT pass (run peephole optimizers).

3.11. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.12. Executing ALUMACC pass (create $alu and $macc cells).
Extracting $alu and $macc cells in module dff_asyncres_syncres:
  created 0 $alu and 0 $macc cells.

3.13. Executing SHARE pass (SAT-based resource sharing).

3.14. Executing OPT pass (performing simple optimizations).

3.14.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.14.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.14.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \dff_asyncres_syncres..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

3.14.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \dff_asyncres_syncres.
Performed a total of 0 changes.

3.14.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.14.6. Executing OPT_DFF pass (perform DFF optimizations).

3.14.7. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.14.8. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.14.9. Finished fast OPT passes. (There is nothing left to do.)

3.15. Executing MEMORY pass.

3.15.1. Executing OPT_MEM pass (optimize memories).
Performed a total of 0 transformations.

3.15.2. Executing OPT_MEM_PRIORITY pass (removing unnecessary memory write priority relations).
Performed a total of 0 transformations.

3.15.3. Executing OPT_MEM_FEEDBACK pass (finding memory read-to-write feedback paths).

3.15.4. Executing MEMORY_BMUX2ROM pass (converting muxes to ROMs).

3.15.5. Executing MEMORY_DFF pass (merging $dff cells to $memrd).

3.15.6. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.15.7. Executing MEMORY_SHARE pass (consolidating $memrd/$memwr cells).

3.15.8. Executing OPT_MEM_WIDEN pass (optimize memories where all ports are wide).
Performed a total of 0 transformations.

3.15.9. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.15.10. Executing MEMORY_COLLECT pass (generating $mem cells).

3.16. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.17. Executing OPT pass (performing simple optimizations).

3.17.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.17.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.17.3. Executing OPT_DFF pass (perform DFF optimizations).

3.17.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.17.5. Finished fast OPT passes.

3.18. Executing MEMORY_MAP pass (converting memories to logic and flip-flops).

3.19. Executing OPT pass (performing simple optimizations).

3.19.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.19.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.19.3. Executing OPT_MUXTREE pass (detect dead branches in mux trees).
Running muxtree optimizer on module \dff_asyncres_syncres..
  Creating internal representation of mux trees.
  Evaluating internal representation of mux trees.
  Analyzing evaluation results.
Removed 0 multiplexer ports.
<suppressed ~2 debug messages>

3.19.4. Executing OPT_REDUCE pass (consolidate $*mux and $reduce_* inputs).
  Optimizing cells in module \dff_asyncres_syncres.
Performed a total of 0 changes.

3.19.5. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.19.6. Executing OPT_SHARE pass.

3.19.7. Executing OPT_DFF pass (perform DFF optimizations).

3.19.8. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.19.9. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.19.10. Finished fast OPT passes. (There is nothing left to do.)

3.20. Executing TECHMAP pass (map to technology primitives).

3.20.1. Executing Verilog-2005 frontend: /usr/local/bin/../share/yosys/techmap.v
Parsing Verilog input from `/usr/local/bin/../share/yosys/techmap.v' to AST representation.
Generating RTLIL representation for module `\_90_simplemap_bool_ops'.
Generating RTLIL representation for module `\_90_simplemap_reduce_ops'.
Generating RTLIL representation for module `\_90_simplemap_logic_ops'.
Generating RTLIL representation for module `\_90_simplemap_compare_ops'.
Generating RTLIL representation for module `\_90_simplemap_various'.
Generating RTLIL representation for module `\_90_simplemap_registers'.
Generating RTLIL representation for module `\_90_shift_ops_shr_shl_sshl_sshr'.
Generating RTLIL representation for module `\_90_shift_shiftx'.
Generating RTLIL representation for module `\_90_fa'.
Generating RTLIL representation for module `\_90_lcu_brent_kung'.
Generating RTLIL representation for module `\_90_alu'.
Generating RTLIL representation for module `\_90_macc'.
Generating RTLIL representation for module `\_90_alumacc'.
Generating RTLIL representation for module `\$__div_mod_u'.
Generating RTLIL representation for module `\$__div_mod_trunc'.
Generating RTLIL representation for module `\_90_div'.
Generating RTLIL representation for module `\_90_mod'.
Generating RTLIL representation for module `\$__div_mod_floor'.
Generating RTLIL representation for module `\_90_divfloor'.
Generating RTLIL representation for module `\_90_modfloor'.
Generating RTLIL representation for module `\_90_pow'.
Generating RTLIL representation for module `\_90_pmux'.
Generating RTLIL representation for module `\_90_demux'.
Generating RTLIL representation for module `\_90_lut'.
Generating RTLIL representation for module `\$connect'.
Generating RTLIL representation for module `\$input_port'.
Successfully finished Verilog frontend.

3.20.2. Continuing TECHMAP pass.
Using extmapper simplemap for cells of type $mux.
Using extmapper simplemap for cells of type $adff.
No more expansions possible.
<suppressed ~79 debug messages>

3.21. Executing OPT pass (performing simple optimizations).

3.21.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.21.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.21.3. Executing OPT_DFF pass (perform DFF optimizations).

3.21.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..

3.21.5. Finished fast OPT passes.

3.22. Executing ABC pass (technology mapping using ABC).

3.22.1. Extracting gate netlist of module `\dff_asyncres_syncres' to `<abc-temp-dir>/input.blif'..

3.22.1.1. Executed ABC.
Extracted 1 gates and 4 wires to a netlist network with 2 inputs and 1 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_library /tmp/yosys-abc-7wYWC9/stdcells.genlib 
ABC: + strash 
ABC: + dretime 
ABC: + map 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: abc 04> echo "ABC_DONE"

3.22.1.2. Re-integrating ABC results.
ABC RESULTS:            ANDNOT cells:        1
ABC RESULTS:        internal signals:        1
ABC RESULTS:           input signals:        2
ABC RESULTS:          output signals:        1
Removing temp directory.
Removing global temp directory.

3.23. Executing OPT pass (performing simple optimizations).

3.23.1. Executing OPT_EXPR pass (perform const folding).
Optimizing module dff_asyncres_syncres.

3.23.2. Executing OPT_MERGE pass (detect identical cells).
Finding identical cells in module `\dff_asyncres_syncres'.
Removed a total of 0 cells.

3.23.3. Executing OPT_DFF pass (perform DFF optimizations).

3.23.4. Executing OPT_CLEAN pass (remove unused cells and wires).
Finding unused cells or wires in module \dff_asyncres_syncres..
Removed 0 unused cells and 3 unused wires.
<suppressed ~1 debug messages>

3.23.5. Finished fast OPT passes.

3.24. Executing HIERARCHY pass (managing design hierarchy).
Attribute `top' found on module `dff_asyncres_syncres'. Setting top module to dff_asyncres_syncres.

3.24.1. Analyzing design hierarchy..
Top module:  \dff_asyncres_syncres

3.24.2. Analyzing design hierarchy..
Top module:  \dff_asyncres_syncres
Removed 0 unused modules.

3.25. Printing statistics.

=== dff_asyncres_syncres ===

        +----------Local Count, excluding submodules.
        | 
        6 wires
        6 wire bits
        5 public wires
        5 public wire bits
        5 ports
        5 port bits
        2 cells
        1   $_ANDNOT_
        1   $_DFF_PP0_

3.26. Executing CHECK pass (checking for obvious problems).
Checking module dff_asyncres_syncres...
Found and reported 0 problems.

yosys> dfflibmap -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

4. Executing DFFLIBMAP pass (mapping DFF cells to sequential cells from liberty file).
  cell sky130_fd_sc_hd__dfxtp_1 (noninv, pins=3, area=20.02) is a direct match for cell type $_DFF_P_.
  cell sky130_fd_sc_hd__dfrtn_1 (noninv, pins=4, area=25.02) is a direct match for cell type $_DFF_NN0_.
  cell sky130_fd_sc_hd__dfrtp_1 (noninv, pins=4, area=25.02) is a direct match for cell type $_DFF_PN0_.
  cell sky130_fd_sc_hd__dfstp_2 (noninv, pins=4, area=26.28) is a direct match for cell type $_DFF_PN1_.
  cell sky130_fd_sc_hd__edfxtp_1 (noninv, pins=4, area=30.03) is a direct match for cell type $_DFFE_PP_.
  cell sky130_fd_sc_hd__dfbbn_1 (noninv, pins=6, area=32.53) is a direct match for cell type $_DFFSR_NNN_.
  cell sky130_fd_sc_hd__dfbbp_1 (noninv, pins=6, area=32.53) is a direct match for cell type $_DFFSR_PNN_.
  final dff cell mappings:
    unmapped dff cell: $_DFF_N_
    \sky130_fd_sc_hd__dfxtp_1 _DFF_P_ (.CLK( C), .D( D), .Q( Q));
    \sky130_fd_sc_hd__dfrtn_1 _DFF_NN0_ (.CLK_N( C), .D( D), .Q( Q), .RESET_B( R));
    unmapped dff cell: $_DFF_NN1_
    unmapped dff cell: $_DFF_NP0_
    unmapped dff cell: $_DFF_NP1_
    \sky130_fd_sc_hd__dfrtp_1 _DFF_PN0_ (.CLK( C), .D( D), .Q( Q), .RESET_B( R));
    \sky130_fd_sc_hd__dfstp_2 _DFF_PN1_ (.CLK( C), .D( D), .Q( Q), .SET_B( R));
    unmapped dff cell: $_DFF_PP0_
    unmapped dff cell: $_DFF_PP1_
    unmapped dff cell: $_DFFE_NN_
    unmapped dff cell: $_DFFE_NP_
    unmapped dff cell: $_DFFE_PN_
    \sky130_fd_sc_hd__edfxtp_1 _DFFE_PP_ (.CLK( C), .D( D), .DE( E), .Q( Q));
    \sky130_fd_sc_hd__dfbbn_1 _DFFSR_NNN_ (.CLK_N( C), .D( D), .Q( Q), .Q_N(~Q), .RESET_B( R), .SET_B( S));
    unmapped dff cell: $_DFFSR_NNP_
    unmapped dff cell: $_DFFSR_NPN_
    unmapped dff cell: $_DFFSR_NPP_
    \sky130_fd_sc_hd__dfbbp_1 _DFFSR_PNN_ (.CLK( C), .D( D), .Q( Q), .Q_N(~Q), .RESET_B( R), .SET_B( S));
    unmapped dff cell: $_DFFSR_PNP_
    unmapped dff cell: $_DFFSR_PPN_
    unmapped dff cell: $_DFFSR_PPP_

4.1. Executing DFFLEGALIZE pass (convert FFs to types supported by the target).
<suppressed ~24 debug messages>
Mapping DFF cells in module `\dff_asyncres_syncres':
  mapped 1 $_DFF_PN0_ cells to \sky130_fd_sc_hd__dfrtp_1 cells.

yosys> abc -liberty /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib

5. Executing ABC pass (technology mapping using ABC).

5.1. Extracting gate netlist of module `\dff_asyncres_syncres' to `<abc-temp-dir>/input.blif'..

5.1.1. Executed ABC.
Extracted 2 gates and 5 wires to a netlist network with 3 inputs and 2 outputs.
Running ABC script: <abc-temp-dir>/abc.script
ABC: UC Berkeley, ABC 1.01 (compiled Sep 19 2025 17:16:22)
ABC: abc 01> set abcout /dev/stdout
ABC: abc 01> empty
ABC: abc 01> source <abc-temp-dir>/abc.script
ABC: + read_blif <abc-temp-dir>/input.blif 
ABC: + read_lib -w /home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib 
ABC: Parsing finished successfully.  Parsing time =     0.07 sec
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__decap_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__diode_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__dlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtn_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__dlxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__ebufn_8".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__edfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped three-stat+ strash 
ABC: + &get -n 
ABC: + &fraig -x 
ABC: + &put 
ABC: + scorr 
ABC: + dc2 
ABC: + dretime 
ABC: + strash 
ABC: + &get -n 
ABC: + &dch -f 
ABC: + &nf 
ABC: + &put 
ABC: + write_blif <abc-temp-dir>/output.blif 
ABC: e cell "sky130_fd_sc_hd__einvn_0".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvn_8".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_1".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_2".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_4".
ABC: Scl_LibertyReadGenlib() skipped three-state cell "sky130_fd_sc_hd__einvp_8".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_bleeder_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_12" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_3" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_6" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__lpflow_decapkapwr_8" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__lpflow_inputisolatch_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbn_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfbbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtn_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfrtp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfsbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfstp_4".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sdfxtp_4".
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_1" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_2" without logic function.
ABC: Scl_LibertyReadGenlib() skipped cell "sky130_fd_sc_hd__sdlclkp_4" without logic function.
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxbp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_1".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_2".
ABC: Scl_LibertyReadGenlib() skipped sequential cell "sky130_fd_sc_hd__sedfxtp_4".
ABC: Library "sky130_fd_sc_hd__tt_025C_1v80" from "/home/ank/.ciel/ciel/sky130/versions/a80ed405766c5d4f21c8bfca84552a7478fe75b2/sky130A/libs.ref/sky130_fd_sc_hd/lib/sky130_fd_sc_hd__tt_025C_1v80.lib" has 334 cells (94 skipped: 63 seq; 13 tri-state; 18 no func; 0 dont_use; 0 with 2 outputs; 0 with 3+ outputs).  Time =     0.09 sec
ABC: Memory =   19.85 MB. Time =     0.09 sec
ABC: Warning: Detected 9 multi-output cells (for example, "sky130_fd_sc_hd__fa_1").
ABC: Warning: The network is combinational (run "fraig" or "fraig_sweep").
ABC: abc 07> echo "ABC_DONE"

5.1.2. Re-integrating ABC results.
ABC RESULTS:   sky130_fd_sc_hd__clkinv_1 cells:        1
ABC RESULTS:   sky130_fd_sc_hd__lpflow_isobufsrc_1 cells:        1
ABC RESULTS:        internal signals:        0
ABC RESULTS:           input signals:        3
ABC RESULTS:          output signals:        2
Removing temp directory.
Removing global temp directory.

yosys> write_verilog -noattr dff_asyncres_syncres_natr_generated_netlist.v

6. Executing Verilog backend.

6.1. Executing BMUXMAP pass.

6.2. Executing DEMUXMAP pass.
Dumping module `\dff_asyncres_syncres'.

yosys> flatten

7. Executing FLATTEN pass (flatten design).

yosys> write_verilog -noattr dff_asyncres_syncres_flatten_natr_generated_netlist.v

8. Executing Verilog backend.

8.1. Executing BMUXMAP pass.

8.2. Executing DEMUXMAP pass.
Dumping module `\dff_asyncres_syncres'.

yosys> show

9. Generating Graphviz representation of design.
Writing dot description to `/home/ank/.yosys_show.dot'.
Dumping module dff_asyncres_syncres to page 1.
Exec: { test -f '/home/ank/.yosys_show.dot.pid' && fuser -s '/home/ank/.yosys_show.dot.pid' 2> /dev/null; } || ( echo $$ >&3; exec xdot '/home/ank/.yosys_show.dot'; ) 3> '/home/ank/.yosys_show.dot.pid' &

yosys> /usr/lib/python3/dist-packages/xdot/ui/elements.py:174: UserWarning: Font family 'Times-Roman' is not available, using 'Ubuntu 11'
  warnings.warn(msg)


yosys> 

yosys> 

yosys> 

yosys> exit

End of script. Logfile hash: c4ed59d33a, CPU: user 0.15s system 0.03s, MEM: 48.38 MB peak
Yosys 0.57+148 (git sha1 259bd6fb3, g++ 13.3.0-6ubuntu2~24.04 -fPIC -O3)
Time spent: 57% 2x abc (0 sec), 14% 2x read_liberty (0 sec), ...
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ ls
a.out						       multiple_modules_flattened_natr_generated_netlist.v  multiple_modules_sub_module1_generated_netlist.v  WEEK_1_guide.txt
dff_asyncres_syncres_flatten_natr_generated_netlist.v  multiple_modules_generated_netlist.v		    tb_dff_asyncres_syncres.vcd
dff_asyncres_syncres_natr_generated_netlist.v	       multiple_modules__natr_generated_netlist.v	    W1D2.md
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_1$ 

