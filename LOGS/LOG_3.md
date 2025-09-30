# Pre-Synthesis:

ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ source soc_env/bin/activate
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd WEEK_2
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cd ~/Desktop/SoC_Shwetank/WEEK_2/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gedit firmware.hex
Gtk-Message: 11:23:50.350: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:255504): GLib-GIO-WARNING **: 11:23:51.688: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gedit src/sram.v
Gtk-Message: 11:24:25.713: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:255867): GLib-GIO-WARNING **: 11:24:26.226: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ iverilog -o simulation/baby_soc_sim testbench/soc_tb.v src/soc.v src/picorv32.v src/sram.v src/wb_interconnect.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:39: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
ERROR: src/sram.v:39: $readmemh(firmware.hex): Invalid input character: #
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gedit src/sram.v
Gtk-Message: 11:45:37.000: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:263608): GLib-GIO-WARNING **: 11:45:37.701: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gedit src/sram.v
Gtk-Message: 11:46:04.070: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:263899): GLib-GIO-WARNING **: 11:46:04.572: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ pwd
/home/ank/Desktop/SoC_Shwetank/WEEK_2
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls -a
.  ..  docs  firmware.hex  simulation  src  testbench  waveforms
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ iverilog -o simulation/baby_soc_sim testbench/soc_tb.v src/soc.v src/picorv32.v src/sram.v src/wb_interconnect.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
ERROR: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware.hex): Invalid input character: #
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: xxxxxxxx
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
WARNING: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware.hex): Not enough words in the file for the requested range [0:1023].
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: deadb2b7
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
GTKWAVE | Reloading waveform...
[0] start time.
[50020000] end time.
GTKWAVE | ...waveform reloaded
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
WARNING: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware.hex): Not enough words in the file for the requested range [0:1023].
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: deadb2b7
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
ERROR: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware.hex): Invalid input character: S
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: deadb2b7
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
WARNING: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware.hex): Not enough words in the file for the requested range [0:1023].
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: deadb2b7
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc --version
riscv64-unknown-elf-gcc (13.2.0-11ubuntu1+12) 13.2.0
Copyright (C) 2023 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gedit link.ld
Gtk-Message: 12:28:36.733: Not loading module "atk-bridge": The functionality is provided by GTK natively. Please try to not load it.

(gedit:279310): GLib-GIO-WARNING **: 12:28:37.451: Error creating IO channel for /proc/self/mountinfo: Permission denied (g-file-error-quark, 2)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cat link.ld
OUTPUT_ARCH( "riscv" )
ENTRY( _start )
SECTIONS
{
  . = 0x00000000;
  .text : { *(.text) }
}
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls -a
.  ..  docs  firmware.hex  firmware_ver_2.s  link.ld  simulation  src  testbench  waveforms
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc -march=rv32im -c -o firmware_ver_2.o firmware_ver_2.s
firmware_ver_2.s: Assembler messages:
firmware_ver_2.s:6: Error: can't have 64-bit ABI on 32-bit ISA
firmware_ver_2.s:6: Error: ilp32d/lp64d ABI can't be used when d extension isn't supported
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv32-unknown-elf-gcc --version
riscv32-unknown-elf-gcc: command not found
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -c -o firmware_ver_2.o firmware_ver_2.s
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls -a
.  ..  docs  firmware.hex  firmware_ver_2.o  firmware_ver_2.s  link.ld	simulation  src  testbench  waveforms
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -T link.ld -nostartfiles -o firmware_ver_2.elf firmware_ver_2.o
/usr/lib/gcc/riscv64-unknown-elf/13.2.0/../../../riscv64-unknown-elf/bin/ld: cannot find -lc: No such file or directory
/usr/lib/gcc/riscv64-unknown-elf/13.2.0/../../../riscv64-unknown-elf/bin/ld: cannot find -lgloss: No such file or directory
collect2: error: ld returned 1 exit status
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -T /home/ank/Desktop/SoC_Shwetank/WEEK_2/link.ld -nostartfiles -o firmware_ver_2.elf firmware_ver_2.o
/usr/lib/gcc/riscv64-unknown-elf/13.2.0/../../../riscv64-unknown-elf/bin/ld: cannot find -lc: No such file or directory
/usr/lib/gcc/riscv64-unknown-elf/13.2.0/../../../riscv64-unknown-elf/bin/ld: cannot find -lgloss: No such file or directory
collect2: error: ld returned 1 exit status
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -T link.ld -nostartfiles -nostdlib -o firmware_ver_2.elf firmware_ver_2.o
/usr/lib/gcc/riscv64-unknown-elf/13.2.0/../../../riscv64-unknown-elf/bin/ld: warning: cannot find entry symbol _start; defaulting to 00000000
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-objcopy -O verilog firmware_ver_2.elf firmware_generated.hex
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cat firmware_generated.hex
@00000000
B7 E2 AD DE 93 82 F2 EE 23 20 50 10 6F 00 00 00
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ riscv64-unknown-elf-objcopy -O binary firmware_ver_2.elf firmware_ver_2.bin
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ls
docs  firmware_generated.hex  firmware.hex  firmware_ver_2.bin	firmware_ver_2.elf  firmware_ver_2.o  firmware_ver_2.s	link.ld  simulation  src  testbench  waveforms
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ od -t x4 -An firmware.bin > firmware_ver_2_generated.hex
od: firmware.bin: No such file or directory
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ od -t x4 -An firmware_ver_2.bin > firmware_ver_2_generated.hex
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ sed -i 's/ //g' firmware_ver_2_generated.hex
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cat firmware_ver_2_generated.hex
deade2b7eef28293105020230000006f
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ od -t x4 -An firmware_ver_2.bin > firmware_ver_2_generated.hex
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cat firmware_ver_2_generated.hex
 deade2b7 eef28293 10502023 0000006f
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ od -t x4 -An firmware_ver_2.bin | xargs -n 1 > firmware_ver_2_1_generated.hex
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ cat firmware_ver_2_1_generated.hex
deade2b7
eef28293
10502023
0000006f
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ iverilog -o simulation/baby_soc_sim testbench/soc_tb.v src/soc.v src/picorv32.v src/sram.v src/wb_interconnect.v
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ ./simulation/baby_soc_sim
WARNING: src/sram.v:40: $readmemh: The behaviour for reg[...] mem[N:0]; $readmemh("...", mem); changed in the 1364-2005 standard. To avoid ambiguity, use mem[0:N] or explicit range parameters $readmemh("...", mem, start, stop);. Defaulting to 1364-2005 behavior.
WARNING: src/sram.v:40: $readmemh(/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware_ver_2_generated.hex): Not enough words in the file for the requested range [0:1023].
SRAM INFO: firmware.hex loaded at simulation time 0.
SRAM INFO: Value at address 0x0 is: deade2b7
VCD info: dumpfile waveforms/soc_tb.vcd opened for output.
testbench/soc_tb.v:46: $finish called at 50020000 (1ps)
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ gtkwave waveforms/soc_tb.vcd

GTKWave Analyzer v3.3.116 (w)1999-2023 BSI

[0] start time.
[50020000] end time.
WM Destroy
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_2$ 


