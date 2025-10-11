(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc/STA$ sudo apt update
[sudo] password for ank: 
Get:1 https://packages.microsoft.com/repos/vscode stable InRelease [3,594 B]
Get:2 https://packages.microsoft.com/repos/code stable InRelease [3,590 B]                   
Get:3 https://download.docker.com/linux/ubuntu noble InRelease [48.5 kB]            
Get:4 https://packages.microsoft.com/repos/vscode stable/main amd64 Packages [27.8 kB]
Get:5 https://packages.microsoft.com/repos/code stable/main amd64 Packages [20.1 kB]
Get:6 https://download.docker.com/linux/ubuntu noble/stable amd64 Packages [32.7 kB]
Hit:7 http://in.archive.ubuntu.com/ubuntu noble InRelease                                    
Get:8 http://security.ubuntu.com/ubuntu noble-security InRelease [126 kB]                    
Hit:9 https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2404/x86_64  InRelease  
Get:10 http://in.archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]                  
Get:11 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble InRelease [17.8 kB]    
Hit:12 https://ppa.launchpadcontent.net/kicad/kicad-8.0-releases/ubuntu noble InRelease      
Get:13 http://security.ubuntu.com/ubuntu noble-security/main Sources [201 kB]
Get:14 http://in.archive.ubuntu.com/ubuntu noble-backports InRelease [126 kB]
Get:15 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main i386 Packages [16.9 kB]
Get:16 https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble/main amd64 Packages [28.7 kB]
Get:17 http://in.archive.ubuntu.com/ubuntu noble-updates/main Sources [467 kB]               
Get:18 http://security.ubuntu.com/ubuntu noble-security/restricted Sources [49.8 kB]
Get:19 http://security.ubuntu.com/ubuntu noble-security/main amd64 Packages [1,213 kB]
Get:20 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Packages [1,490 kB]    
Get:21 http://security.ubuntu.com/ubuntu noble-security/main i386 Packages [335 kB]       
Get:22 http://security.ubuntu.com/ubuntu noble-security/main Translation-en [202 kB]         
Get:23 http://security.ubuntu.com/ubuntu noble-security/main amd64 Components [21.6 kB]      
Get:24 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Packages [1,967 kB] 
Get:25 http://in.archive.ubuntu.com/ubuntu noble-updates/main i386 Packages [535 kB]         
Get:26 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 Components [175 kB]      
Get:27 http://in.archive.ubuntu.com/ubuntu noble-updates/main amd64 c-n-f Metadata [15.3 kB] 
Get:28 http://in.archive.ubuntu.com/ubuntu noble-updates/restricted amd64 Components [212 B] 
Get:29 http://in.archive.ubuntu.com/ubuntu noble-updates/universe i386 Packages [983 kB]
Get:30 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Packages [1,487 kB]  
Get:31 http://security.ubuntu.com/ubuntu noble-security/restricted Translation-en [448 kB]   
Get:32 http://security.ubuntu.com/ubuntu noble-security/restricted amd64 Components [212 B]  
Get:33 http://security.ubuntu.com/ubuntu noble-security/universe amd64 Components [52.3 kB]  
Get:34 http://security.ubuntu.com/ubuntu noble-security/multiverse amd64 Components [212 B]  
Get:35 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 Components [377 kB]  
Get:36 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 c-n-f Metadata [31.1 kB]
Get:37 http://in.archive.ubuntu.com/ubuntu noble-updates/multiverse amd64 Components [940 B] 
Get:38 http://in.archive.ubuntu.com/ubuntu noble-backports/main amd64 Components [7,124 B]   
Get:39 http://in.archive.ubuntu.com/ubuntu noble-backports/restricted amd64 Components [216 B]
Get:40 http://in.archive.ubuntu.com/ubuntu noble-backports/universe amd64 Components [11.0 kB]
Get:41 http://in.archive.ubuntu.com/ubuntu noble-backports/multiverse amd64 Components [212 B]
Fetched 10.6 MB in 7s (1,607 kB/s)                                                           
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
31 packages can be upgraded. Run 'apt list --upgradable' to see them.
W: https://packages.microsoft.com/repos/vscode/dists/stable/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
W: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Packages (main/binary-i386/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Translations (main/i18n/Translation-en_IN) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'https://packages.microsoft.com/repos/vscode stable InRelease' doesn't support architecture 'i386'
W: Target Packages (main/binary-amd64/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Packages (main/binary-i386/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Packages (main/binary-all/Packages) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Translations (main/i18n/Translation-en_IN) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target Translations (main/i18n/Translation-en) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11 (main/dep11/Components-amd64.yml) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11 (main/dep11/Components-all.yml) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons-small (main/dep11/icons-48x48.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons (main/dep11/icons-64x64.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target DEP-11-icons-hidpi (main/dep11/icons-64x64@2.tar) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target CNF (main/cnf/Commands-amd64) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
W: Target CNF (main/cnf/Commands-all) is configured multiple times in /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-jammy.sources:1 and /etc/apt/sources.list.d/archive_uri-https_packages_microsoft_com_repos_vscode-noble.list:1
N: Missing Signed-By in the sources.list(5) entry for 'https://packages.microsoft.com/repos/vscode'
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc/STA$ sudo apt install opensta
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Package opensta is not available, but is referred to by another package.
This may mean that the package is missing, has been obsoleted, or
is only available from another source

E: Package 'opensta' has no installation candidate
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc/STA$ sudo apt install -y build-essential cmake swig tcl-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
build-essential is already the newest version (12.10ubuntu1).
cmake is already the newest version (3.28.3-1build7).
tcl-dev is already the newest version (8.6.14build1).
Suggested packages:
  swig-doc swig-examples
The following NEW packages will be installed:
  swig
0 upgraded, 1 newly installed, 0 to remove and 31 not upgraded.
Need to get 1,187 kB of archives.
After this operation, 5,672 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu noble/universe amd64 swig amd64 4.2.0-2ubuntu1 [1,187 kB]
Fetched 1,187 kB in 3s (420 kB/s)
Selecting previously unselected package swig.
(Reading database ... 314080 files and directories currently installed.)
Preparing to unpack .../swig_4.2.0-2ubuntu1_amd64.deb ...
Unpacking swig (4.2.0-2ubuntu1) ...
Setting up swig (4.2.0-2ubuntu1) ...
Processing triggers for man-db (2.12.0-4build2) ...
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc/STA$ cd ../../..
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ ls
Documents  ngspice-45.2  soc_env	WEEK_1	WEEK_3
magic	   OpenLane	 verilog_files	WEEK_2	yosys
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd ~/Desktop/SoC_Shwetank
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ git clone https://github.com/The-OpenROAD-Project/OpenSTA.git
Cloning into 'OpenSTA'...
remote: Enumerating objects: 19232, done.
remote: Counting objects: 100% (4164/4164), done.
remote: Compressing objects: 100% (638/638), done.
remote: Total 19232 (delta 3803), reused 3559 (delta 3518), pack-reused 15068 (from 3)
Receiving objects: 100% (19232/19232), 52.59 MiB | 4.88 MiB/s, done.
Resolving deltas: 100% (15115/15115), done.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd OpenSTA
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA$ mkdir build
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA$ cd build
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cmake ..
-- The CXX compiler identification is GNU 13.3.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- STA version: 2.7.0
-- STA git sha: 05b292c379c9f3a74d23c67adb6f937e0206b374
-- System name: Linux
-- Compiler: GNU 13.3.0
-- Build type: RELEASE
-- Build CXX_FLAGS: -O3 -DNDEBUG
-- Install prefix: /usr/local
-- Found FLEX: /usr/bin/flex (found version "2.6.4") 
-- Found BISON: /usr/bin/bison (found version "3.8.2") 
-- TCL library: /usr/lib/x86_64-linux-gnu/libtcl.so
-- TCL header: /usr/include/tcl/tcl.h
-- TCL readline library: NOT FOUND
-- TCL readline header: NOT FOUND
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.3")  
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
CMake Error at CMakeLists.txt:382 (find_package):
  By not providing "FindEigen3.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "Eigen3", but
  CMake did not find one.

  Could not find a package configuration file provided by "Eigen3" with any
  of the following names:

    Eigen3Config.cmake
    eigen3-config.cmake

  Add the installation prefix of "Eigen3" to CMAKE_PREFIX_PATH or set
  "Eigen3_DIR" to a directory containing one of the above files.  If "Eigen3"
  provides a separate development package or SDK, be sure it has been
  installed.


-- Configuring incomplete, errors occurred!
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ ls
CMakeCache.txt	CMakeFiles
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ sudo apt install libeigen3-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Suggested packages:
  libeigen3-doc libmpfrc++-dev
The following NEW packages will be installed:
  libeigen3-dev
0 upgraded, 1 newly installed, 0 to remove and 31 not upgraded.
Need to get 1,057 kB of archives.
After this operation, 9,076 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu noble-updates/universe amd64 libeigen3-dev all 3.4.0-4build0.1 [1,057 kB]
Fetched 1,057 kB in 5s (230 kB/s)                        
Selecting previously unselected package libeigen3-dev.
(Reading database ... 314932 files and directories currently installed.)
Preparing to unpack .../libeigen3-dev_3.4.0-4build0.1_all.deb ...
Unpacking libeigen3-dev (3.4.0-4build0.1) ...
Setting up libeigen3-dev (3.4.0-4build0.1) ...
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cd ~/Desktop/SoC_Shwetank/OpenSTA/build/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cmake ..
-- STA version: 2.7.0
-- STA git sha: 05b292c379c9f3a74d23c67adb6f937e0206b374
-- System name: Linux
-- Compiler: GNU 13.3.0
-- Build type: RELEASE
-- Build CXX_FLAGS: -O3 -DNDEBUG
-- Install prefix: /usr/local
-- TCL library: /usr/lib/x86_64-linux-gnu/libtcl.so
-- TCL header: /usr/include/tcl/tcl.h
-- TCL readline library: NOT FOUND
-- TCL readline header: NOT FOUND
-- CUDD library: not found
-- SSTA: 0
-- Found SWIG: /usr/bin/swig4.0 (found suitable version "4.2.0", minimum required is "3.0")  
-- STA library: /home/ank/Desktop/SoC_Shwetank/OpenSTA/build/libOpenSTA.a
-- STA executable: /home/ank/Desktop/SoC_Shwetank/OpenSTA/build/sta
-- Configuring done (0.1s)
CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
Please set them or make sure they are set and tested correctly in the CMake files:
CUDD_LIB
    linked by target "OpenSTA" in directory /home/ank/Desktop/SoC_Shwetank/OpenSTA

-- Generating done (0.0s)
CMake Generate step failed.  Build files cannot be regenerated correctly.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ sudo apt install libcudd-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package libcudd-dev
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cd ~/Desktop/SoC_Shwetank
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ git clone https://github.com/ivmai/cudd.git
Cloning into 'cudd'...
remote: Enumerating objects: 1007, done.
remote: Counting objects: 100% (157/157), done.
remote: Compressing objects: 100% (72/72), done.
remote: Total 1007 (delta 97), reused 85 (delta 85), pack-reused 850 (from 1)
Receiving objects: 100% (1007/1007), 2.38 MiB | 1.54 MiB/s, done.
Resolving deltas: 100% (575/575), done.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank$ cd cudd
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make
make: *** No targets specified and no makefile found.  Stop.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ ls
aclocal.m4   configure	   cudd   Doxyfile.in  LICENSE	    Makefile.in  README		util
build-aux    configure.ac  dddmp  epd	       m4	    mtr		 RELEASE.NOTES
config.h.in  cplusplus	   doc	  groups.dox   Makefile.am  nanotrav	 st
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make
make: *** No targets specified and no makefile found.  Stop.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ ./configure
checking build system type... x86_64-unknown-linux-gnu
checking host system type... x86_64-unknown-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a thread-safe mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking whether gcc understands -c and -o together... yes
checking for style of include used by make... GNU
checking dependency style of gcc... gcc3
checking for g++... g++
checking whether we are using the GNU C++ compiler... yes
checking whether g++ accepts -g... yes
checking dependency style of g++... gcc3
checking for ar... ar
checking the archiver (ar) interface... ar
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking whether the shell understands some XSI constructs... yes
checking whether the shell understands "+="... yes
checking how to convert x86_64-unknown-linux-gnu file names to x86_64-unknown-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-unknown-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /usr/bin/ld option to reload object files... -r
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for archiver @FILE support... @
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for mt... mt
checking if mt is a manifest tool... no
checking how to run the C preprocessor... gcc -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... no
checking for gcc option to produce PIC... -fPIC -DPIC
checking if gcc PIC flag -fPIC -DPIC works... yes
checking if gcc static flag -static works... yes
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /usr/bin/ld -m elf_x86_64
checking if the linker (/usr/bin/ld -m elf_x86_64) is GNU ld... yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking for g++ option to produce PIC... -fPIC -DPIC
checking if g++ PIC flag -fPIC -DPIC works... yes
checking if g++ static flag -static works... yes
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether byte ordering is bigendian... no
checking for doxygen... no
configure: WARNING: Doxygen not found - continuing without Doxygen support
checking for pdflatex... no
configure: WARNING: pdflatex not found - unable to compile manual to PDF
checking for makeindex... no
configure: WARNING: makeindex not found - unable to compile manual to PDF
checking for library containing pow... -lm
checking for pthread_create in -lpthread... yes
checking for library containing WSAStartup... no
checking for library containing GetProcessMemoryInfo... no
checking float.h usability... yes
checking float.h presence... yes
checking for float.h... yes
checking for inttypes.h... (cached) yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking assert.h usability... yes
checking assert.h presence... yes
checking for assert.h... yes
checking math.h usability... yes
checking math.h presence... yes
checking for math.h... yes
checking for unistd.h... (cached) yes
checking sys/time.h usability... yes
checking sys/time.h presence... yes
checking for sys/time.h... yes
checking sys/times.h usability... yes
checking sys/times.h presence... yes
checking for sys/times.h... yes
checking sys/resource.h usability... yes
checking sys/resource.h presence... yes
checking for sys/resource.h... yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking for working C++ thread header... yes
checking for stdbool.h that conforms to C99... yes
checking for _Bool... yes
checking for inline... inline
checking for size_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for ptrdiff_t... yes
checking size of int... 4
checking size of long... 8
checking size of void *... 8
checking size of long double... 16
checking whether we are building for a Win32 host... no
checking whether enough of C++11 is supported... yes
checking for pow... yes
checking for sqrt... yes
checking for strchr... yes
checking for strstr... yes
checking for powl... yes
checking for gethostname... yes
checking for getrlimit... yes
checking for getrusage... yes
checking for sysconf... yes
checking for +Infinity (IEEE 754 floating point)... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating dddmp/exp/test1.sh
config.status: creating dddmp/exp/test2.sh
config.status: creating dddmp/exp/test3.sh
config.status: creating dddmp/exp/test4.sh
config.status: creating dddmp/exp/test5.sh
config.status: creating dddmp/exp/test6.sh
config.status: creating dddmp/exp/test7.sh
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
--------------------------------------------------
Configuration summary for cudd 3.0.0

Build system   : x86_64-unknown-linux-gnu
Host system    : x86_64-unknown-linux-gnu
Prefix         : '/usr/local'
Compilers      : 'gcc    -Wall -Wextra -g -O3'
               : 'g++    -Wall -Wextra -std=c++0x -g -O3'
Shared library : no
 dddmp enabled : no
 obj enabled   : no
--------------------------------------------------
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ ls
aclocal.m4   config.log     cplusplus  Doxyfile.in  LICENSE	 Makefile.in  RELEASE.NOTES
build-aux    config.status  cudd       epd	    m4		 mtr	      st
config.h     configure	    dddmp      groups.dox   Makefile	 nanotrav     stamp-h1
config.h.in  configure.ac   doc        libtool	    Makefile.am  README       util
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing aclocal-1.14 -I m4
/home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing: line 81: aclocal-1.14: command not found
WARNING: 'aclocal-1.14' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <http://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <http://www.gnu.org/software/autoconf>
         <http://www.gnu.org/software/m4/>
         <http://www.perl.org/>
make: *** [Makefile:983: aclocal.m4] Error 127
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ sudo apt install automake autoconf libtool
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
automake is already the newest version (1:1.16.5-1.3ubuntu1).
autoconf is already the newest version (2.71-3).
libtool is already the newest version (2.4.7-7build1).
0 upgraded, 0 newly installed, 0 to remove and 31 not upgraded.
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make clean
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing aclocal-1.14 -I m4
/home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing: line 81: aclocal-1.14: command not found
WARNING: 'aclocal-1.14' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <http://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <http://www.gnu.org/software/autoconf>
         <http://www.gnu.org/software/m4/>
         <http://www.perl.org/>
make: *** [Makefile:983: aclocal.m4] Error 127
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make clean
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing aclocal-1.14 -I m4
/home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing: line 81: aclocal-1.14: command not found
WARNING: 'aclocal-1.14' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <http://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <http://www.gnu.org/software/autoconf>
         <http://www.gnu.org/software/m4/>
         <http://www.perl.org/>
make: *** [Makefile:983: aclocal.m4] Error 127
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make
CDPATH="${ZSH_VERSION+.}:" && cd . && /bin/bash /home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing aclocal-1.14 -I m4
/home/ank/Desktop/SoC_Shwetank/cudd/build-aux/missing: line 81: aclocal-1.14: command not found
WARNING: 'aclocal-1.14' is missing on your system.
         You should only need it if you modified 'acinclude.m4' or
         'configure.ac' or m4 files included by 'configure.ac'.
         The 'aclocal' program is part of the GNU Automake package:
         <http://www.gnu.org/software/automake>
         It also requires GNU Autoconf, GNU m4 and Perl in order to run:
         <http://www.gnu.org/software/autoconf>
         <http://www.gnu.org/software/m4/>
         <http://www.perl.org/>
make: *** [Makefile:983: aclocal.m4] Error 127
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ autoreconf -fi
libtoolize: putting auxiliary files in AC_CONFIG_AUX_DIR, 'build-aux'.
libtoolize: copying file 'build-aux/ltmain.sh'
libtoolize: putting macros in AC_CONFIG_MACRO_DIRS, 'm4'.
libtoolize: copying file 'm4/libtool.m4'
libtoolize: copying file 'm4/ltoptions.m4'
libtoolize: copying file 'm4/ltsugar.m4'
libtoolize: copying file 'm4/ltversion.m4'
libtoolize: copying file 'm4/lt~obsolete.m4'
configure.ac:131: warning: The macro `AC_TRY_RUN' is obsolete.
configure.ac:131: You should run autoupdate.
./lib/autoconf/general.m4:2997: AC_TRY_RUN is expanded from...
lib/m4sugar/m4sh.m4:692: _AS_IF_ELSE is expanded from...
lib/m4sugar/m4sh.m4:699: AS_IF is expanded from...
./lib/autoconf/general.m4:2249: AC_CACHE_VAL is expanded from...
configure.ac:131: the top level
configure.ac:34: installing 'build-aux/compile'
configure.ac:9: installing 'build-aux/missing'
Makefile.am: installing 'build-aux/depcomp'
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ ./configure
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... yes
checking for a race-free mkdir -p... /usr/bin/mkdir -p
checking for gawk... gawk
checking whether make sets $(MAKE)... yes
checking whether make supports nested variables... yes
checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether the compiler supports GNU C... yes
checking whether gcc accepts -g... yes
checking for gcc option to enable C11 features... none needed
checking whether gcc understands -c and -o together... yes
checking whether make supports the include directive... yes (GNU style)
checking dependency style of gcc... gcc3
checking for g++... g++
checking whether the compiler supports GNU C++... yes
checking whether g++ accepts -g... yes
checking for g++ option to enable C++11 features... none needed
checking dependency style of g++... gcc3
checking for ar... ar
checking the archiver (ar) interface... ar
checking how to print strings... printf
checking for a sed that does not truncate output... /usr/bin/sed
checking for grep that handles long lines and -e... /usr/bin/grep
checking for egrep... /usr/bin/grep -E
checking for fgrep... /usr/bin/grep -F
checking for ld used by gcc... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for BSD- or MS-compatible name lister (nm)... /usr/bin/nm -B
checking the name lister (/usr/bin/nm -B) interface... BSD nm
checking whether ln -s works... yes
checking the maximum length of command line arguments... 1572864
checking how to convert x86_64-pc-linux-gnu file names to x86_64-pc-linux-gnu format... func_convert_file_noop
checking how to convert x86_64-pc-linux-gnu file names to toolchain format... func_convert_file_noop
checking for /usr/bin/ld option to reload object files... -r
checking for file... file
checking for objdump... objdump
checking how to recognize dependent libraries... pass_all
checking for dlltool... no
checking how to associate runtime and link libraries... printf %s\n
checking for archiver @FILE support... @
checking for strip... strip
checking for ranlib... ranlib
checking command to parse /usr/bin/nm -B output from gcc object... ok
checking for sysroot... no
checking for a working dd... /usr/bin/dd
checking how to truncate binary pipes... /usr/bin/dd bs=4096 count=1
checking for mt... mt
checking if mt is a manifest tool... no
checking for stdio.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for strings.h... yes
checking for sys/stat.h... yes
checking for sys/types.h... yes
checking for unistd.h... yes
checking for dlfcn.h... yes
checking for objdir... .libs
checking if gcc supports -fno-rtti -fno-exceptions... no
checking for gcc option to produce PIC... -fPIC -DPIC
checking if gcc PIC flag -fPIC -DPIC works... yes
checking if gcc static flag -static works... yes
checking if gcc supports -c -o file.o... yes
checking if gcc supports -c -o file.o... (cached) yes
checking whether the gcc linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether stripping libraries is possible... yes
checking if libtool supports shared libraries... yes
checking whether to build shared libraries... no
checking whether to build static libraries... yes
checking how to run the C++ preprocessor... g++ -E
checking for ld used by g++... /usr/bin/ld -m elf_x86_64
checking if the linker (/usr/bin/ld -m elf_x86_64) is GNU ld... yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking for g++ option to produce PIC... -fPIC -DPIC
checking if g++ PIC flag -fPIC -DPIC works... yes
checking if g++ static flag -static works... yes
checking if g++ supports -c -o file.o... yes
checking if g++ supports -c -o file.o... (cached) yes
checking whether the g++ linker (/usr/bin/ld -m elf_x86_64) supports shared libraries... yes
checking dynamic linker characteristics... (cached) GNU/Linux ld.so
checking how to hardcode library paths into programs... immediate
checking whether byte ordering is bigendian... no
checking for doxygen... no
configure: WARNING: Doxygen not found - continuing without Doxygen support
checking for pdflatex... no
configure: WARNING: pdflatex not found - unable to compile manual to PDF
checking for makeindex... no
configure: WARNING: makeindex not found - unable to compile manual to PDF
checking for library containing pow... -lm
checking for pthread_create in -lpthread... yes
checking for library containing WSAStartup... no
checking for library containing GetProcessMemoryInfo... no
checking for float.h... yes
checking for inttypes.h... (cached) yes
checking for limits.h... yes
checking for stddef.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for assert.h... yes
checking for math.h... yes
checking for unistd.h... (cached) yes
checking for sys/time.h... yes
checking for sys/times.h... yes
checking for sys/resource.h... yes
checking for sys/wait.h... yes
checking for working C++ thread header... yes
checking for _Bool... yes
checking for stdbool.h that conforms to C99... yes
checking for inline... inline
checking for size_t... yes
checking for uint16_t... yes
checking for uint32_t... yes
checking for ptrdiff_t... yes
checking size of int... 4
checking size of long... 8
checking size of void *... 8
checking size of long double... 16
checking whether we are building for a Win32 host... no
checking whether enough of C++11 is supported... yes
checking for pow... yes
checking for sqrt... yes
checking for strchr... yes
checking for strstr... yes
checking for powl... yes
checking for gethostname... yes
checking for getrlimit... yes
checking for getrusage... yes
checking for sysconf... yes
checking for +Infinity (IEEE 754 floating point)... yes
checking that generated files are newer than configure... done
configure: creating ./config.status
config.status: creating Makefile
config.status: creating dddmp/exp/test1.sh
config.status: creating dddmp/exp/test2.sh
config.status: creating dddmp/exp/test3.sh
config.status: creating dddmp/exp/test4.sh
config.status: creating dddmp/exp/test5.sh
config.status: creating dddmp/exp/test6.sh
config.status: creating dddmp/exp/test7.sh
config.status: creating config.h
config.status: executing depfiles commands
config.status: executing libtool commands
--------------------------------------------------
Configuration summary for cudd 3.0.0

Build system   : x86_64-pc-linux-gnu
Host system    : x86_64-pc-linux-gnu
Prefix         : '/usr/local'
Compilers      : 'gcc    -Wall -Wextra -g -O3'
               : 'g++    -Wall -Wextra -std=c++0x -g -O3'
Shared library : no
 dddmp enabled : no
 obj enabled   : no
--------------------------------------------------
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make clean
 rm -f cudd/testcudd cudd/testextra st/testst mtr/testmtr dddmp/testdddmp cplusplus/testobj cplusplus/testmulti nanotrav/nanotrav
test -z "cudd/r7x8.1.tst cudd/extra.tst mtr/test.tst dddmp/exp/test1.sh dddmp/exp/test2.sh dddmp/exp/test3.sh dddmp/exp/test4.sh dddmp/exp/test5.sh dddmp/exp/test6.sh dddmp/exp/test7.sh cplusplus/test.tst cplusplus/multi.tst nanotrav/adj49.tst nanotrav/C17.tst nanotrav/C880.tst nanotrav/closest.tst nanotrav/ham01.tst nanotrav/mult32a.tst nanotrav/rcn25.tst nanotrav/s27.tst nanotrav/s27b.tst nanotrav/s27c.tst nanotrav/s382.tst nanotrav/s641.tst nanotrav/miniFirst.tst  cudd/test_cudd.test st/test_st.test mtr/test_mtr.test dddmp/test_dddmp.test cplusplus/test_obj.test nanotrav/test_ntrv.test" || rm -f cudd/r7x8.1.tst cudd/extra.tst mtr/test.tst dddmp/exp/test1.sh dddmp/exp/test2.sh dddmp/exp/test3.sh dddmp/exp/test4.sh dddmp/exp/test5.sh dddmp/exp/test6.sh dddmp/exp/test7.sh cplusplus/test.tst cplusplus/multi.tst nanotrav/adj49.tst nanotrav/C17.tst nanotrav/C880.tst nanotrav/closest.tst nanotrav/ham01.tst nanotrav/mult32a.tst nanotrav/rcn25.tst nanotrav/s27.tst nanotrav/s27b.tst nanotrav/s27c.tst nanotrav/s382.tst nanotrav/s641.tst nanotrav/miniFirst.tst  cudd/test_cudd.test st/test_st.test mtr/test_mtr.test dddmp/test_dddmp.test cplusplus/test_obj.test nanotrav/test_ntrv.test
test -z "cudd/libcudd.la" || rm -f cudd/libcudd.la
rm -f cudd/so_locations
rm -rf .libs _libs
rm -rf cplusplus/.libs cplusplus/_libs
rm -rf cudd/.libs cudd/_libs
rm -rf dddmp/.libs dddmp/_libs
rm -rf epd/.libs epd/_libs
rm -rf mtr/.libs mtr/_libs
rm -rf nanotrav/.libs nanotrav/_libs
rm -rf st/.libs st/_libs
rm -rf util/.libs util/_libs
test -z "dddmp/libdddmp.la cplusplus/libobj.la" || rm -f dddmp/libdddmp.la cplusplus/libobj.la
rm -f cplusplus/so_locations dddmp/so_locations
rm -f *.o
rm -f cplusplus/*.o
rm -f cplusplus/*.lo
rm -f cudd/*.o
rm -f cudd/*.lo
rm -f dddmp/*.o
rm -f dddmp/*.lo
rm -f epd/*.o
rm -f epd/*.lo
rm -f mtr/*.o
rm -f mtr/*.lo
rm -f nanotrav/*.o
rm -f st/*.o
rm -f st/*.lo
rm -f util/*.o
rm -f util/*.lo
test -z "cudd/test_cudd.log st/test_st.log mtr/test_mtr.log dddmp/test_dddmp.log cplusplus/test_obj.log nanotrav/test_ntrv.log" || rm -f cudd/test_cudd.log st/test_st.log mtr/test_mtr.log dddmp/test_dddmp.log cplusplus/test_obj.log nanotrav/test_ntrv.log
test -z "cudd/test_cudd.trs st/test_st.trs mtr/test_mtr.trs dddmp/test_dddmp.trs cplusplus/test_obj.trs nanotrav/test_ntrv.trs" || rm -f cudd/test_cudd.trs st/test_st.trs mtr/test_mtr.trs dddmp/test_dddmp.trs cplusplus/test_obj.trs nanotrav/test_ntrv.trs
test -z "test-suite.log" || rm -f test-suite.log
rm -f *.lo
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ make
make  all-am
make[1]: Entering directory '/home/ank/Desktop/SoC_Shwetank/cudd'
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddAbs.Tpo -c -o cudd/libcudd_la-cuddAddAbs.lo `test -f 'cudd/cuddAddAbs.c' || echo './'`cudd/cuddAddAbs.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddAbs.Tpo -c cudd/cuddAddAbs.c -o cudd/libcudd_la-cuddAddAbs.o
mv -f cudd/.deps/libcudd_la-cuddAddAbs.Tpo cudd/.deps/libcudd_la-cuddAddAbs.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddApply.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddApply.Tpo -c -o cudd/libcudd_la-cuddAddApply.lo `test -f 'cudd/cuddAddApply.c' || echo './'`cudd/cuddAddApply.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddApply.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddApply.Tpo -c cudd/cuddAddApply.c -o cudd/libcudd_la-cuddAddApply.o
mv -f cudd/.deps/libcudd_la-cuddAddApply.Tpo cudd/.deps/libcudd_la-cuddAddApply.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddFind.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddFind.Tpo -c -o cudd/libcudd_la-cuddAddFind.lo `test -f 'cudd/cuddAddFind.c' || echo './'`cudd/cuddAddFind.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddFind.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddFind.Tpo -c cudd/cuddAddFind.c -o cudd/libcudd_la-cuddAddFind.o
mv -f cudd/.deps/libcudd_la-cuddAddFind.Tpo cudd/.deps/libcudd_la-cuddAddFind.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddInv.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddInv.Tpo -c -o cudd/libcudd_la-cuddAddInv.lo `test -f 'cudd/cuddAddInv.c' || echo './'`cudd/cuddAddInv.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddInv.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddInv.Tpo -c cudd/cuddAddInv.c -o cudd/libcudd_la-cuddAddInv.o
mv -f cudd/.deps/libcudd_la-cuddAddInv.Tpo cudd/.deps/libcudd_la-cuddAddInv.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddIte.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddIte.Tpo -c -o cudd/libcudd_la-cuddAddIte.lo `test -f 'cudd/cuddAddIte.c' || echo './'`cudd/cuddAddIte.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddIte.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddIte.Tpo -c cudd/cuddAddIte.c -o cudd/libcudd_la-cuddAddIte.o
cudd/cuddAddIte.c: In function 'Cudd_addLeq':
cudd/cuddAddIte.c:377:31: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  377 |     tmp = cuddCacheLookup2(dd,(DD_CTFP)Cudd_addLeq,f,g);
      |                               ^
cudd/cuddAddIte.c:399:25: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  399 |     cuddCacheInsert2(dd,(DD_CTFP) Cudd_addLeq,f,g,
      |                         ^
mv -f cudd/.deps/libcudd_la-cuddAddIte.Tpo cudd/.deps/libcudd_la-cuddAddIte.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddNeg.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddNeg.Tpo -c -o cudd/libcudd_la-cuddAddNeg.lo `test -f 'cudd/cuddAddNeg.c' || echo './'`cudd/cuddAddNeg.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddNeg.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddNeg.Tpo -c cudd/cuddAddNeg.c -o cudd/libcudd_la-cuddAddNeg.o
cudd/cuddAddNeg.c: In function 'cuddAddRoundOffRecur':
cudd/cuddAddNeg.c:238:15: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, int)' to 'DdNode * (*)(DdManager *, DdNode *)' [-Wcast-function-type]
  238 |     cacheOp = (DD_CTFP1) Cudd_addRoundOff;
      |               ^
mv -f cudd/.deps/libcudd_la-cuddAddNeg.Tpo cudd/.deps/libcudd_la-cuddAddNeg.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddWalsh.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddWalsh.Tpo -c -o cudd/libcudd_la-cuddAddWalsh.lo `test -f 'cudd/cuddAddWalsh.c' || echo './'`cudd/cuddAddWalsh.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAddWalsh.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAddWalsh.Tpo -c cudd/cuddAddWalsh.c -o cudd/libcudd_la-cuddAddWalsh.o
mv -f cudd/.deps/libcudd_la-cuddAddWalsh.Tpo cudd/.deps/libcudd_la-cuddAddWalsh.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAndAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAndAbs.Tpo -c -o cudd/libcudd_la-cuddAndAbs.lo `test -f 'cudd/cuddAndAbs.c' || echo './'`cudd/cuddAndAbs.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAndAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAndAbs.Tpo -c cudd/cuddAndAbs.c -o cudd/libcudd_la-cuddAndAbs.o
mv -f cudd/.deps/libcudd_la-cuddAndAbs.Tpo cudd/.deps/libcudd_la-cuddAndAbs.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAnneal.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAnneal.Tpo -c -o cudd/libcudd_la-cuddAnneal.lo `test -f 'cudd/cuddAnneal.c' || echo './'`cudd/cuddAnneal.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAnneal.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAnneal.Tpo -c cudd/cuddAnneal.c -o cudd/libcudd_la-cuddAnneal.o
mv -f cudd/.deps/libcudd_la-cuddAnneal.Tpo cudd/.deps/libcudd_la-cuddAnneal.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddApa.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddApa.Tpo -c -o cudd/libcudd_la-cuddApa.lo `test -f 'cudd/cuddApa.c' || echo './'`cudd/cuddApa.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddApa.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddApa.Tpo -c cudd/cuddApa.c -o cudd/libcudd_la-cuddApa.o
mv -f cudd/.deps/libcudd_la-cuddApa.Tpo cudd/.deps/libcudd_la-cuddApa.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAPI.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAPI.Tpo -c -o cudd/libcudd_la-cuddAPI.lo `test -f 'cudd/cuddAPI.c' || echo './'`cudd/cuddAPI.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddAPI.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddAPI.Tpo -c cudd/cuddAPI.c -o cudd/libcudd_la-cuddAPI.o
mv -f cudd/.deps/libcudd_la-cuddAPI.Tpo cudd/.deps/libcudd_la-cuddAPI.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddApprox.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddApprox.Tpo -c -o cudd/libcudd_la-cuddApprox.lo `test -f 'cudd/cuddApprox.c' || echo './'`cudd/cuddApprox.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddApprox.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddApprox.Tpo -c cudd/cuddApprox.c -o cudd/libcudd_la-cuddApprox.o
mv -f cudd/.deps/libcudd_la-cuddApprox.Tpo cudd/.deps/libcudd_la-cuddApprox.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddAbs.Tpo -c -o cudd/libcudd_la-cuddBddAbs.lo `test -f 'cudd/cuddBddAbs.c' || echo './'`cudd/cuddBddAbs.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddAbs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddAbs.Tpo -c cudd/cuddBddAbs.c -o cudd/libcudd_la-cuddBddAbs.o
cudd/cuddBddAbs.c: In function 'Cudd_bddVarIsDependent':
cudd/cuddBddAbs.c:329:15: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  329 |     cacheOp = (DD_CTFP) Cudd_bddVarIsDependent;
      |               ^
mv -f cudd/.deps/libcudd_la-cuddBddAbs.Tpo cudd/.deps/libcudd_la-cuddBddAbs.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddCorr.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddCorr.Tpo -c -o cudd/libcudd_la-cuddBddCorr.lo `test -f 'cudd/cuddBddCorr.c' || echo './'`cudd/cuddBddCorr.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddCorr.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddCorr.Tpo -c cudd/cuddBddCorr.c -o cudd/libcudd_la-cuddBddCorr.o
mv -f cudd/.deps/libcudd_la-cuddBddCorr.Tpo cudd/.deps/libcudd_la-cuddBddCorr.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddIte.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddIte.Tpo -c -o cudd/libcudd_la-cuddBddIte.lo `test -f 'cudd/cuddBddIte.c' || echo './'`cudd/cuddBddIte.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBddIte.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBddIte.Tpo -c cudd/cuddBddIte.c -o cudd/libcudd_la-cuddBddIte.o
cudd/cuddBddIte.c: In function 'Cudd_bddLeq':
cudd/cuddBddIte.c:662:35: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  662 |         tmp = cuddCacheLookup2(dd,(DD_CTFP)Cudd_bddLeq,f,g);
      |                                   ^
cudd/cuddBddIte.c:695:29: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  695 |         cuddCacheInsert2(dd,(DD_CTFP)Cudd_bddLeq,f,g,(res ? one : zero));
      |                             ^
mv -f cudd/.deps/libcudd_la-cuddBddIte.Tpo cudd/.deps/libcudd_la-cuddBddIte.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBridge.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBridge.Tpo -c -o cudd/libcudd_la-cuddBridge.lo `test -f 'cudd/cuddBridge.c' || echo './'`cudd/cuddBridge.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddBridge.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddBridge.Tpo -c cudd/cuddBridge.c -o cudd/libcudd_la-cuddBridge.o
mv -f cudd/.deps/libcudd_la-cuddBridge.Tpo cudd/.deps/libcudd_la-cuddBridge.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCache.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCache.Tpo -c -o cudd/libcudd_la-cuddCache.lo `test -f 'cudd/cuddCache.c' || echo './'`cudd/cuddCache.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCache.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCache.Tpo -c cudd/cuddCache.c -o cudd/libcudd_la-cuddCache.o
mv -f cudd/.deps/libcudd_la-cuddCache.Tpo cudd/.deps/libcudd_la-cuddCache.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCheck.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCheck.Tpo -c -o cudd/libcudd_la-cuddCheck.lo `test -f 'cudd/cuddCheck.c' || echo './'`cudd/cuddCheck.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCheck.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCheck.Tpo -c cudd/cuddCheck.c -o cudd/libcudd_la-cuddCheck.o
mv -f cudd/.deps/libcudd_la-cuddCheck.Tpo cudd/.deps/libcudd_la-cuddCheck.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddClip.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddClip.Tpo -c -o cudd/libcudd_la-cuddClip.lo `test -f 'cudd/cuddClip.c' || echo './'`cudd/cuddClip.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddClip.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddClip.Tpo -c cudd/cuddClip.c -o cudd/libcudd_la-cuddClip.o
cudd/cuddClip.c: In function 'cuddBddClippingAndRecur':
cudd/cuddClip.c:285:15: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, DdNode *, int,  int)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  285 |     cacheOp = (DD_CTFP)
      |               ^
mv -f cudd/.deps/libcudd_la-cuddClip.Tpo cudd/.deps/libcudd_la-cuddClip.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCof.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCof.Tpo -c -o cudd/libcudd_la-cuddCof.lo `test -f 'cudd/cuddCof.c' || echo './'`cudd/cuddCof.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCof.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCof.Tpo -c cudd/cuddCof.c -o cudd/libcudd_la-cuddCof.o
mv -f cudd/.deps/libcudd_la-cuddCof.Tpo cudd/.deps/libcudd_la-cuddCof.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCompose.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCompose.Tpo -c -o cudd/libcudd_la-cuddCompose.lo `test -f 'cudd/cuddCompose.c' || echo './'`cudd/cuddCompose.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddCompose.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddCompose.Tpo -c cudd/cuddCompose.c -o cudd/libcudd_la-cuddCompose.o
mv -f cudd/.deps/libcudd_la-cuddCompose.Tpo cudd/.deps/libcudd_la-cuddCompose.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddDecomp.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddDecomp.Tpo -c -o cudd/libcudd_la-cuddDecomp.lo `test -f 'cudd/cuddDecomp.c' || echo './'`cudd/cuddDecomp.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddDecomp.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddDecomp.Tpo -c cudd/cuddDecomp.c -o cudd/libcudd_la-cuddDecomp.o
mv -f cudd/.deps/libcudd_la-cuddDecomp.Tpo cudd/.deps/libcudd_la-cuddDecomp.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddEssent.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddEssent.Tpo -c -o cudd/libcudd_la-cuddEssent.lo `test -f 'cudd/cuddEssent.c' || echo './'`cudd/cuddEssent.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddEssent.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddEssent.Tpo -c cudd/cuddEssent.c -o cudd/libcudd_la-cuddEssent.o
mv -f cudd/.deps/libcudd_la-cuddEssent.Tpo cudd/.deps/libcudd_la-cuddEssent.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddExact.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddExact.Tpo -c -o cudd/libcudd_la-cuddExact.lo `test -f 'cudd/cuddExact.c' || echo './'`cudd/cuddExact.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddExact.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddExact.Tpo -c cudd/cuddExact.c -o cudd/libcudd_la-cuddExact.o
mv -f cudd/.deps/libcudd_la-cuddExact.Tpo cudd/.deps/libcudd_la-cuddExact.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddExport.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddExport.Tpo -c -o cudd/libcudd_la-cuddExport.lo `test -f 'cudd/cuddExport.c' || echo './'`cudd/cuddExport.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddExport.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddExport.Tpo -c cudd/cuddExport.c -o cudd/libcudd_la-cuddExport.o
mv -f cudd/.deps/libcudd_la-cuddExport.Tpo cudd/.deps/libcudd_la-cuddExport.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGenCof.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGenCof.Tpo -c -o cudd/libcudd_la-cuddGenCof.lo `test -f 'cudd/cuddGenCof.c' || echo './'`cudd/cuddGenCof.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGenCof.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGenCof.Tpo -c cudd/cuddGenCof.c -o cudd/libcudd_la-cuddGenCof.o
mv -f cudd/.deps/libcudd_la-cuddGenCof.Tpo cudd/.deps/libcudd_la-cuddGenCof.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGenetic.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGenetic.Tpo -c -o cudd/libcudd_la-cuddGenetic.lo `test -f 'cudd/cuddGenetic.c' || echo './'`cudd/cuddGenetic.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGenetic.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGenetic.Tpo -c cudd/cuddGenetic.c -o cudd/libcudd_la-cuddGenetic.o
mv -f cudd/.deps/libcudd_la-cuddGenetic.Tpo cudd/.deps/libcudd_la-cuddGenetic.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGroup.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGroup.Tpo -c -o cudd/libcudd_la-cuddGroup.lo `test -f 'cudd/cuddGroup.c' || echo './'`cudd/cuddGroup.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddGroup.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddGroup.Tpo -c cudd/cuddGroup.c -o cudd/libcudd_la-cuddGroup.o
mv -f cudd/.deps/libcudd_la-cuddGroup.Tpo cudd/.deps/libcudd_la-cuddGroup.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddHarwell.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddHarwell.Tpo -c -o cudd/libcudd_la-cuddHarwell.lo `test -f 'cudd/cuddHarwell.c' || echo './'`cudd/cuddHarwell.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddHarwell.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddHarwell.Tpo -c cudd/cuddHarwell.c -o cudd/libcudd_la-cuddHarwell.o
mv -f cudd/.deps/libcudd_la-cuddHarwell.Tpo cudd/.deps/libcudd_la-cuddHarwell.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddInit.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddInit.Tpo -c -o cudd/libcudd_la-cuddInit.lo `test -f 'cudd/cuddInit.c' || echo './'`cudd/cuddInit.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddInit.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddInit.Tpo -c cudd/cuddInit.c -o cudd/libcudd_la-cuddInit.o
mv -f cudd/.deps/libcudd_la-cuddInit.Tpo cudd/.deps/libcudd_la-cuddInit.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddInteract.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddInteract.Tpo -c -o cudd/libcudd_la-cuddInteract.lo `test -f 'cudd/cuddInteract.c' || echo './'`cudd/cuddInteract.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddInteract.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddInteract.Tpo -c cudd/cuddInteract.c -o cudd/libcudd_la-cuddInteract.o
mv -f cudd/.deps/libcudd_la-cuddInteract.Tpo cudd/.deps/libcudd_la-cuddInteract.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLCache.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLCache.Tpo -c -o cudd/libcudd_la-cuddLCache.lo `test -f 'cudd/cuddLCache.c' || echo './'`cudd/cuddLCache.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLCache.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLCache.Tpo -c cudd/cuddLCache.c -o cudd/libcudd_la-cuddLCache.o
mv -f cudd/.deps/libcudd_la-cuddLCache.Tpo cudd/.deps/libcudd_la-cuddLCache.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLevelQ.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLevelQ.Tpo -c -o cudd/libcudd_la-cuddLevelQ.lo `test -f 'cudd/cuddLevelQ.c' || echo './'`cudd/cuddLevelQ.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLevelQ.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLevelQ.Tpo -c cudd/cuddLevelQ.c -o cudd/libcudd_la-cuddLevelQ.o
mv -f cudd/.deps/libcudd_la-cuddLevelQ.Tpo cudd/.deps/libcudd_la-cuddLevelQ.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLinear.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLinear.Tpo -c -o cudd/libcudd_la-cuddLinear.lo `test -f 'cudd/cuddLinear.c' || echo './'`cudd/cuddLinear.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLinear.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLinear.Tpo -c cudd/cuddLinear.c -o cudd/libcudd_la-cuddLinear.o
mv -f cudd/.deps/libcudd_la-cuddLinear.Tpo cudd/.deps/libcudd_la-cuddLinear.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLiteral.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLiteral.Tpo -c -o cudd/libcudd_la-cuddLiteral.lo `test -f 'cudd/cuddLiteral.c' || echo './'`cudd/cuddLiteral.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddLiteral.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddLiteral.Tpo -c cudd/cuddLiteral.c -o cudd/libcudd_la-cuddLiteral.o
mv -f cudd/.deps/libcudd_la-cuddLiteral.Tpo cudd/.deps/libcudd_la-cuddLiteral.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddMatMult.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddMatMult.Tpo -c -o cudd/libcudd_la-cuddMatMult.lo `test -f 'cudd/cuddMatMult.c' || echo './'`cudd/cuddMatMult.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddMatMult.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddMatMult.Tpo -c cudd/cuddMatMult.c -o cudd/libcudd_la-cuddMatMult.o
cudd/cuddMatMult.c: In function 'addMMRecur':
cudd/cuddMatMult.c:379:15: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, DdNode *, int,  int *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  379 |     cacheOp = (DD_CTFP) addMMRecur;
      |               ^
mv -f cudd/.deps/libcudd_la-cuddMatMult.Tpo cudd/.deps/libcudd_la-cuddMatMult.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddPriority.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddPriority.Tpo -c -o cudd/libcudd_la-cuddPriority.lo `test -f 'cudd/cuddPriority.c' || echo './'`cudd/cuddPriority.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddPriority.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddPriority.Tpo -c cudd/cuddPriority.c -o cudd/libcudd_la-cuddPriority.o
cudd/cuddPriority.c: In function 'cuddBddClosestCube':
cudd/cuddPriority.c:1637:35: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, DdNode *, int *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
 1637 |         res = cuddCacheLookup2(dd,(DD_CTFP) Cudd_bddClosestCube, f, g);
      |                                   ^
cudd/cuddPriority.c:1789:29: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, DdNode *, int *)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
 1789 |         cuddCacheInsert2(dd,(DD_CTFP) Cudd_bddClosestCube, f, g, res);
      |                             ^
mv -f cudd/.deps/libcudd_la-cuddPriority.Tpo cudd/.deps/libcudd_la-cuddPriority.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddRead.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddRead.Tpo -c -o cudd/libcudd_la-cuddRead.lo `test -f 'cudd/cuddRead.c' || echo './'`cudd/cuddRead.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddRead.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddRead.Tpo -c cudd/cuddRead.c -o cudd/libcudd_la-cuddRead.o
mv -f cudd/.deps/libcudd_la-cuddRead.Tpo cudd/.deps/libcudd_la-cuddRead.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddRef.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddRef.Tpo -c -o cudd/libcudd_la-cuddRef.lo `test -f 'cudd/cuddRef.c' || echo './'`cudd/cuddRef.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddRef.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddRef.Tpo -c cudd/cuddRef.c -o cudd/libcudd_la-cuddRef.o
mv -f cudd/.deps/libcudd_la-cuddRef.Tpo cudd/.deps/libcudd_la-cuddRef.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddReorder.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddReorder.Tpo -c -o cudd/libcudd_la-cuddReorder.lo `test -f 'cudd/cuddReorder.c' || echo './'`cudd/cuddReorder.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddReorder.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddReorder.Tpo -c cudd/cuddReorder.c -o cudd/libcudd_la-cuddReorder.o
mv -f cudd/.deps/libcudd_la-cuddReorder.Tpo cudd/.deps/libcudd_la-cuddReorder.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSat.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSat.Tpo -c -o cudd/libcudd_la-cuddSat.lo `test -f 'cudd/cuddSat.c' || echo './'`cudd/cuddSat.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSat.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSat.Tpo -c cudd/cuddSat.c -o cudd/libcudd_la-cuddSat.o
cudd/cuddSat.c: In function 'Cudd_Decreasing':
cudd/cuddSat.c:420:15: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, int)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  420 |     cacheOp = (DD_CTFP) Cudd_Decreasing;
      |               ^
cudd/cuddSat.c: In function 'Cudd_EqualSupNorm':
cudd/cuddSat.c:798:29: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *, CUDD_VALUE_TYPE,  int)' {aka 'int (*)(DdManager *, DdNode *, DdNode *, double,  int)'} to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  798 |     r = cuddCacheLookup2(dd,(DD_CTFP)Cudd_EqualSupNorm,f,g);
      |                             ^
cudd/cuddSat.c:813:25: warning: cast between incompatible function types from 'int (*)(DdManager *, DdNode *, DdNode *, CUDD_VALUE_TYPE,  int)' {aka 'int (*)(DdManager *, DdNode *, DdNode *, double,  int)'} to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  813 |     cuddCacheInsert2(dd,(DD_CTFP)Cudd_EqualSupNorm,f,g,DD_ONE(dd));
      |                         ^
mv -f cudd/.deps/libcudd_la-cuddSat.Tpo cudd/.deps/libcudd_la-cuddSat.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSign.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSign.Tpo -c -o cudd/libcudd_la-cuddSign.lo `test -f 'cudd/cuddSign.c' || echo './'`cudd/cuddSign.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSign.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSign.Tpo -c cudd/cuddSign.c -o cudd/libcudd_la-cuddSign.o
mv -f cudd/.deps/libcudd_la-cuddSign.Tpo cudd/.deps/libcudd_la-cuddSign.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSolve.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSolve.Tpo -c -o cudd/libcudd_la-cuddSolve.lo `test -f 'cudd/cuddSolve.c' || echo './'`cudd/cuddSolve.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSolve.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSolve.Tpo -c cudd/cuddSolve.c -o cudd/libcudd_la-cuddSolve.o
mv -f cudd/.deps/libcudd_la-cuddSolve.Tpo cudd/.deps/libcudd_la-cuddSolve.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSplit.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSplit.Tpo -c -o cudd/libcudd_la-cuddSplit.lo `test -f 'cudd/cuddSplit.c' || echo './'`cudd/cuddSplit.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSplit.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSplit.Tpo -c cudd/cuddSplit.c -o cudd/libcudd_la-cuddSplit.o
mv -f cudd/.deps/libcudd_la-cuddSplit.Tpo cudd/.deps/libcudd_la-cuddSplit.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSubsetHB.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSubsetHB.Tpo -c -o cudd/libcudd_la-cuddSubsetHB.lo `test -f 'cudd/cuddSubsetHB.c' || echo './'`cudd/cuddSubsetHB.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSubsetHB.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSubsetHB.Tpo -c cudd/cuddSubsetHB.c -o cudd/libcudd_la-cuddSubsetHB.o
mv -f cudd/.deps/libcudd_la-cuddSubsetHB.Tpo cudd/.deps/libcudd_la-cuddSubsetHB.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSubsetSP.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSubsetSP.Tpo -c -o cudd/libcudd_la-cuddSubsetSP.lo `test -f 'cudd/cuddSubsetSP.c' || echo './'`cudd/cuddSubsetSP.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSubsetSP.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSubsetSP.Tpo -c cudd/cuddSubsetSP.c -o cudd/libcudd_la-cuddSubsetSP.o
mv -f cudd/.deps/libcudd_la-cuddSubsetSP.Tpo cudd/.deps/libcudd_la-cuddSubsetSP.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSymmetry.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSymmetry.Tpo -c -o cudd/libcudd_la-cuddSymmetry.lo `test -f 'cudd/cuddSymmetry.c' || echo './'`cudd/cuddSymmetry.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddSymmetry.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddSymmetry.Tpo -c cudd/cuddSymmetry.c -o cudd/libcudd_la-cuddSymmetry.o
mv -f cudd/.deps/libcudd_la-cuddSymmetry.Tpo cudd/.deps/libcudd_la-cuddSymmetry.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddTable.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddTable.Tpo -c -o cudd/libcudd_la-cuddTable.lo `test -f 'cudd/cuddTable.c' || echo './'`cudd/cuddTable.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddTable.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddTable.Tpo -c cudd/cuddTable.c -o cudd/libcudd_la-cuddTable.o
mv -f cudd/.deps/libcudd_la-cuddTable.Tpo cudd/.deps/libcudd_la-cuddTable.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddUtil.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddUtil.Tpo -c -o cudd/libcudd_la-cuddUtil.lo `test -f 'cudd/cuddUtil.c' || echo './'`cudd/cuddUtil.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddUtil.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddUtil.Tpo -c cudd/cuddUtil.c -o cudd/libcudd_la-cuddUtil.o
mv -f cudd/.deps/libcudd_la-cuddUtil.Tpo cudd/.deps/libcudd_la-cuddUtil.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddWindow.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddWindow.Tpo -c -o cudd/libcudd_la-cuddWindow.lo `test -f 'cudd/cuddWindow.c' || echo './'`cudd/cuddWindow.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddWindow.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddWindow.Tpo -c cudd/cuddWindow.c -o cudd/libcudd_la-cuddWindow.o
cudd/cuddWindow.c: In function 'ddPermuteWindow3':
cudd/cuddWindow.c:386:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
  386 |     case BCA: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                  ^
cudd/cuddWindow.c:387:5: note: here
  387 |     case CBA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:387:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
  387 |     case CBA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                  ^
cudd/cuddWindow.c:388:5: note: here
  388 |     case ABC: if (!cuddSwapInPlace(table,y,z)) return(0);
      |     ^~~~
cudd/cuddWindow.c:390:18: warning: this statement may fall through [-Wimplicit-fallthrough=]
  390 |     case BAC: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                  ^
cudd/cuddWindow.c:391:5: note: here
  391 |     case CAB: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c: In function 'ddPermuteWindow4':
cudd/cuddWindow.c:759:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  759 |     case DBCA: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:760:5: note: here
  760 |     case BDCA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:760:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  760 |     case BDCA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:761:5: note: here
  761 |     case CDBA: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:761:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  761 |     case CDBA: if (!cuddSwapInPlace(table,w,x)) return(0);
      |                   ^
cudd/cuddWindow.c:762:5: note: here
  762 |     case ADBC: if (!cuddSwapInPlace(table,y,z)) return(0);
      |     ^~~~
cudd/cuddWindow.c:762:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  762 |     case ADBC: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:763:5: note: here
  763 |     case ABDC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:763:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  763 |     case ABDC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:764:5: note: here
  764 |     case ACDB: if (!cuddSwapInPlace(table,y,z)) return(0);
      |     ^~~~
cudd/cuddWindow.c:766:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  766 |     case DCBA: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:767:5: note: here
  767 |     case BCDA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:767:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  767 |     case BCDA: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:768:5: note: here
  768 |     case CBDA: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:772:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  772 |     case DBAC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:773:5: note: here
  773 |     case DCAB: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:773:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  773 |     case DCAB: if (!cuddSwapInPlace(table,w,x)) return(0);
      |                   ^
cudd/cuddWindow.c:774:5: note: here
  774 |     case DACB: if (!cuddSwapInPlace(table,y,z)) return(0);
      |     ^~~~
cudd/cuddWindow.c:774:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  774 |     case DACB: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:775:5: note: here
  775 |     case BACD: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:775:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  775 |     case BACD: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:776:5: note: here
  776 |     case CABD: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:778:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  778 |     case DABC: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:779:5: note: here
  779 |     case BADC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:779:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  779 |     case BADC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:780:5: note: here
  780 |     case CADB: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:783:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  783 |     case BDAC: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:784:5: note: here
  784 |     case CDAB: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
cudd/cuddWindow.c:784:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  784 |     case CDAB: if (!cuddSwapInPlace(table,w,x)) return(0);
      |                   ^
cudd/cuddWindow.c:785:5: note: here
  785 |     case ADCB: if (!cuddSwapInPlace(table,y,z)) return(0);
      |     ^~~~
cudd/cuddWindow.c:785:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  785 |     case ADCB: if (!cuddSwapInPlace(table,y,z)) return(0);
      |                   ^
cudd/cuddWindow.c:786:5: note: here
  786 |     case ABCD: if (!cuddSwapInPlace(table,x,y)) return(0);
      |     ^~~~
cudd/cuddWindow.c:788:19: warning: this statement may fall through [-Wimplicit-fallthrough=]
  788 |     case BCAD: if (!cuddSwapInPlace(table,x,y)) return(0);
      |                   ^
cudd/cuddWindow.c:789:5: note: here
  789 |     case CBAD: if (!cuddSwapInPlace(table,w,x)) return(0);
      |     ^~~~
mv -f cudd/.deps/libcudd_la-cuddWindow.Tpo cudd/.deps/libcudd_la-cuddWindow.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddCount.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddCount.Tpo -c -o cudd/libcudd_la-cuddZddCount.lo `test -f 'cudd/cuddZddCount.c' || echo './'`cudd/cuddZddCount.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddCount.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddCount.Tpo -c cudd/cuddZddCount.c -o cudd/libcudd_la-cuddZddCount.o
mv -f cudd/.deps/libcudd_la-cuddZddCount.Tpo cudd/.deps/libcudd_la-cuddZddCount.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddFuncs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddFuncs.Tpo -c -o cudd/libcudd_la-cuddZddFuncs.lo `test -f 'cudd/cuddZddFuncs.c' || echo './'`cudd/cuddZddFuncs.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddFuncs.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddFuncs.Tpo -c cudd/cuddZddFuncs.c -o cudd/libcudd_la-cuddZddFuncs.o
mv -f cudd/.deps/libcudd_la-cuddZddFuncs.Tpo cudd/.deps/libcudd_la-cuddZddFuncs.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddGroup.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddGroup.Tpo -c -o cudd/libcudd_la-cuddZddGroup.lo `test -f 'cudd/cuddZddGroup.c' || echo './'`cudd/cuddZddGroup.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddGroup.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddGroup.Tpo -c cudd/cuddZddGroup.c -o cudd/libcudd_la-cuddZddGroup.o
mv -f cudd/.deps/libcudd_la-cuddZddGroup.Tpo cudd/.deps/libcudd_la-cuddZddGroup.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddIsop.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddIsop.Tpo -c -o cudd/libcudd_la-cuddZddIsop.lo `test -f 'cudd/cuddZddIsop.c' || echo './'`cudd/cuddZddIsop.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddIsop.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddIsop.Tpo -c cudd/cuddZddIsop.c -o cudd/libcudd_la-cuddZddIsop.o
cudd/cuddZddIsop.c: In function 'cuddZddIsop':
cudd/cuddZddIsop.c:256:15: warning: cast between incompatible function types from 'DdNode * (*)(DdManager *, DdNode *, DdNode *, DdNode **)' to 'DdNode * (*)(DdManager *, DdNode *, DdNode *)' [-Wcast-function-type]
  256 |     cacheOp = (DD_CTFP) cuddZddIsop;
      |               ^
mv -f cudd/.deps/libcudd_la-cuddZddIsop.Tpo cudd/.deps/libcudd_la-cuddZddIsop.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddLin.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddLin.Tpo -c -o cudd/libcudd_la-cuddZddLin.lo `test -f 'cudd/cuddZddLin.c' || echo './'`cudd/cuddZddLin.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddLin.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddLin.Tpo -c cudd/cuddZddLin.c -o cudd/libcudd_la-cuddZddLin.o
mv -f cudd/.deps/libcudd_la-cuddZddLin.Tpo cudd/.deps/libcudd_la-cuddZddLin.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddMisc.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddMisc.Tpo -c -o cudd/libcudd_la-cuddZddMisc.lo `test -f 'cudd/cuddZddMisc.c' || echo './'`cudd/cuddZddMisc.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddMisc.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddMisc.Tpo -c cudd/cuddZddMisc.c -o cudd/libcudd_la-cuddZddMisc.o
mv -f cudd/.deps/libcudd_la-cuddZddMisc.Tpo cudd/.deps/libcudd_la-cuddZddMisc.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddPort.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddPort.Tpo -c -o cudd/libcudd_la-cuddZddPort.lo `test -f 'cudd/cuddZddPort.c' || echo './'`cudd/cuddZddPort.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddPort.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddPort.Tpo -c cudd/cuddZddPort.c -o cudd/libcudd_la-cuddZddPort.o
mv -f cudd/.deps/libcudd_la-cuddZddPort.Tpo cudd/.deps/libcudd_la-cuddZddPort.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddReord.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddReord.Tpo -c -o cudd/libcudd_la-cuddZddReord.lo `test -f 'cudd/cuddZddReord.c' || echo './'`cudd/cuddZddReord.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddReord.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddReord.Tpo -c cudd/cuddZddReord.c -o cudd/libcudd_la-cuddZddReord.o
mv -f cudd/.deps/libcudd_la-cuddZddReord.Tpo cudd/.deps/libcudd_la-cuddZddReord.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddSetop.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddSetop.Tpo -c -o cudd/libcudd_la-cuddZddSetop.lo `test -f 'cudd/cuddZddSetop.c' || echo './'`cudd/cuddZddSetop.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddSetop.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddSetop.Tpo -c cudd/cuddZddSetop.c -o cudd/libcudd_la-cuddZddSetop.o
mv -f cudd/.deps/libcudd_la-cuddZddSetop.Tpo cudd/.deps/libcudd_la-cuddZddSetop.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddSymm.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddSymm.Tpo -c -o cudd/libcudd_la-cuddZddSymm.lo `test -f 'cudd/cuddZddSymm.c' || echo './'`cudd/cuddZddSymm.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddSymm.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddSymm.Tpo -c cudd/cuddZddSymm.c -o cudd/libcudd_la-cuddZddSymm.o
mv -f cudd/.deps/libcudd_la-cuddZddSymm.Tpo cudd/.deps/libcudd_la-cuddZddSymm.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddUtil.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddUtil.Tpo -c -o cudd/libcudd_la-cuddZddUtil.lo `test -f 'cudd/cuddZddUtil.c' || echo './'`cudd/cuddZddUtil.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT cudd/libcudd_la-cuddZddUtil.lo -MD -MP -MF cudd/.deps/libcudd_la-cuddZddUtil.Tpo -c cudd/cuddZddUtil.c -o cudd/libcudd_la-cuddZddUtil.o
mv -f cudd/.deps/libcudd_la-cuddZddUtil.Tpo cudd/.deps/libcudd_la-cuddZddUtil.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cpu_stats.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cpu_stats.Tpo -c -o util/cudd_libcudd_la-cpu_stats.lo `test -f 'util/cpu_stats.c' || echo './'`util/cpu_stats.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cpu_stats.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cpu_stats.Tpo -c util/cpu_stats.c -o util/cudd_libcudd_la-cpu_stats.o
In file included from /usr/include/assert.h:35,
                 from util/util.h:70,
                 from util/cpu_stats.c:66:
/usr/include/features.h:196:3: warning: #warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE" [-Wcpp]
  196 | # warning "_BSD_SOURCE and _SVID_SOURCE are deprecated, use _DEFAULT_SOURCE"
      |   ^~~~~~~
mv -f util/.deps/cudd_libcudd_la-cpu_stats.Tpo util/.deps/cudd_libcudd_la-cpu_stats.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cpu_time.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cpu_time.Tpo -c -o util/cudd_libcudd_la-cpu_time.lo `test -f 'util/cpu_time.c' || echo './'`util/cpu_time.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cpu_time.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cpu_time.Tpo -c util/cpu_time.c -o util/cudd_libcudd_la-cpu_time.o
mv -f util/.deps/cudd_libcudd_la-cpu_time.Tpo util/.deps/cudd_libcudd_la-cpu_time.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cstringstream.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cstringstream.Tpo -c -o util/cudd_libcudd_la-cstringstream.lo `test -f 'util/cstringstream.c' || echo './'`util/cstringstream.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-cstringstream.lo -MD -MP -MF util/.deps/cudd_libcudd_la-cstringstream.Tpo -c util/cstringstream.c -o util/cudd_libcudd_la-cstringstream.o
util/cstringstream.c: In function 'appendStringStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
util/cstringstream.c: In function 'appendIntStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
In function 'appendStringStringStream',
    inlined from 'appendIntStringStream' at util/cstringstream.c:151:10:
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
util/cstringstream.c: In function 'appendUnsignedStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
In function 'appendStringStringStream',
    inlined from 'appendUnsignedStringStream' at util/cstringstream.c:158:10:
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
util/cstringstream.c: In function 'appendLongStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
In function 'appendStringStringStream',
    inlined from 'appendLongStringStream' at util/cstringstream.c:165:10:
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
util/cstringstream.c: In function 'appendUnsignedLongStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
In function 'appendStringStringStream',
    inlined from 'appendUnsignedLongStringStream' at util/cstringstream.c:172:10:
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
util/cstringstream.c: In function 'appendDoubleStringStream':
util/cstringstream.c:143:3: warning: '__builtin_strncpy' output truncated before terminating nul copying as many bytes from a string as its length [-Wstringop-truncation]
  143 |   strncpy(ss->data + ss->inUse - len, s, len);
      |   ^
In function 'appendStringStringStream',
    inlined from 'appendDoubleStringStream' at util/cstringstream.c:179:10:
util/cstringstream.c:140:16: note: length computed here
  140 |   size_t len = strlen(s);
      |                ^~~~~~~~~
mv -f util/.deps/cudd_libcudd_la-cstringstream.Tpo util/.deps/cudd_libcudd_la-cstringstream.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-datalimit.lo -MD -MP -MF util/.deps/cudd_libcudd_la-datalimit.Tpo -c -o util/cudd_libcudd_la-datalimit.lo `test -f 'util/datalimit.c' || echo './'`util/datalimit.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-datalimit.lo -MD -MP -MF util/.deps/cudd_libcudd_la-datalimit.Tpo -c util/datalimit.c -o util/cudd_libcudd_la-datalimit.o
mv -f util/.deps/cudd_libcudd_la-datalimit.Tpo util/.deps/cudd_libcudd_la-datalimit.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-pathsearch.lo -MD -MP -MF util/.deps/cudd_libcudd_la-pathsearch.Tpo -c -o util/cudd_libcudd_la-pathsearch.lo `test -f 'util/pathsearch.c' || echo './'`util/pathsearch.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-pathsearch.lo -MD -MP -MF util/.deps/cudd_libcudd_la-pathsearch.Tpo -c util/pathsearch.c -o util/cudd_libcudd_la-pathsearch.o
mv -f util/.deps/cudd_libcudd_la-pathsearch.Tpo util/.deps/cudd_libcudd_la-pathsearch.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-pipefork.lo -MD -MP -MF util/.deps/cudd_libcudd_la-pipefork.Tpo -c -o util/cudd_libcudd_la-pipefork.lo `test -f 'util/pipefork.c' || echo './'`util/pipefork.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-pipefork.lo -MD -MP -MF util/.deps/cudd_libcudd_la-pipefork.Tpo -c util/pipefork.c -o util/cudd_libcudd_la-pipefork.o
mv -f util/.deps/cudd_libcudd_la-pipefork.Tpo util/.deps/cudd_libcudd_la-pipefork.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-prtime.lo -MD -MP -MF util/.deps/cudd_libcudd_la-prtime.Tpo -c -o util/cudd_libcudd_la-prtime.lo `test -f 'util/prtime.c' || echo './'`util/prtime.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-prtime.lo -MD -MP -MF util/.deps/cudd_libcudd_la-prtime.Tpo -c util/prtime.c -o util/cudd_libcudd_la-prtime.o
mv -f util/.deps/cudd_libcudd_la-prtime.Tpo util/.deps/cudd_libcudd_la-prtime.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-safe_mem.lo -MD -MP -MF util/.deps/cudd_libcudd_la-safe_mem.Tpo -c -o util/cudd_libcudd_la-safe_mem.lo `test -f 'util/safe_mem.c' || echo './'`util/safe_mem.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-safe_mem.lo -MD -MP -MF util/.deps/cudd_libcudd_la-safe_mem.Tpo -c util/safe_mem.c -o util/cudd_libcudd_la-safe_mem.o
mv -f util/.deps/cudd_libcudd_la-safe_mem.Tpo util/.deps/cudd_libcudd_la-safe_mem.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-strsav.lo -MD -MP -MF util/.deps/cudd_libcudd_la-strsav.Tpo -c -o util/cudd_libcudd_la-strsav.lo `test -f 'util/strsav.c' || echo './'`util/strsav.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-strsav.lo -MD -MP -MF util/.deps/cudd_libcudd_la-strsav.Tpo -c util/strsav.c -o util/cudd_libcudd_la-strsav.o
mv -f util/.deps/cudd_libcudd_la-strsav.Tpo util/.deps/cudd_libcudd_la-strsav.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-texpand.lo -MD -MP -MF util/.deps/cudd_libcudd_la-texpand.Tpo -c -o util/cudd_libcudd_la-texpand.lo `test -f 'util/texpand.c' || echo './'`util/texpand.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-texpand.lo -MD -MP -MF util/.deps/cudd_libcudd_la-texpand.Tpo -c util/texpand.c -o util/cudd_libcudd_la-texpand.o
mv -f util/.deps/cudd_libcudd_la-texpand.Tpo util/.deps/cudd_libcudd_la-texpand.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-ucbqsort.lo -MD -MP -MF util/.deps/cudd_libcudd_la-ucbqsort.Tpo -c -o util/cudd_libcudd_la-ucbqsort.lo `test -f 'util/ucbqsort.c' || echo './'`util/ucbqsort.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT util/cudd_libcudd_la-ucbqsort.lo -MD -MP -MF util/.deps/cudd_libcudd_la-ucbqsort.Tpo -c util/ucbqsort.c -o util/cudd_libcudd_la-ucbqsort.o
mv -f util/.deps/cudd_libcudd_la-ucbqsort.Tpo util/.deps/cudd_libcudd_la-ucbqsort.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT st/cudd_libcudd_la-st.lo -MD -MP -MF st/.deps/cudd_libcudd_la-st.Tpo -c -o st/cudd_libcudd_la-st.lo `test -f 'st/st.c' || echo './'`st/st.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT st/cudd_libcudd_la-st.lo -MD -MP -MF st/.deps/cudd_libcudd_la-st.Tpo -c st/st.c -o st/cudd_libcudd_la-st.o
mv -f st/.deps/cudd_libcudd_la-st.Tpo st/.deps/cudd_libcudd_la-st.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT epd/cudd_libcudd_la-epd.lo -MD -MP -MF epd/.deps/cudd_libcudd_la-epd.Tpo -c -o epd/cudd_libcudd_la-epd.lo `test -f 'epd/epd.c' || echo './'`epd/epd.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT epd/cudd_libcudd_la-epd.lo -MD -MP -MF epd/.deps/cudd_libcudd_la-epd.Tpo -c epd/epd.c -o epd/cudd_libcudd_la-epd.o
mv -f epd/.deps/cudd_libcudd_la-epd.Tpo epd/.deps/cudd_libcudd_la-epd.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT mtr/cudd_libcudd_la-mtrBasic.lo -MD -MP -MF mtr/.deps/cudd_libcudd_la-mtrBasic.Tpo -c -o mtr/cudd_libcudd_la-mtrBasic.lo `test -f 'mtr/mtrBasic.c' || echo './'`mtr/mtrBasic.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT mtr/cudd_libcudd_la-mtrBasic.lo -MD -MP -MF mtr/.deps/cudd_libcudd_la-mtrBasic.Tpo -c mtr/mtrBasic.c -o mtr/cudd_libcudd_la-mtrBasic.o
mv -f mtr/.deps/cudd_libcudd_la-mtrBasic.Tpo mtr/.deps/cudd_libcudd_la-mtrBasic.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./cudd -I./st -I./epd -I./mtr -I./util   -Wall -Wextra -g -O3 -MT mtr/cudd_libcudd_la-mtrGroup.lo -MD -MP -MF mtr/.deps/cudd_libcudd_la-mtrGroup.Tpo -c -o mtr/cudd_libcudd_la-mtrGroup.lo `test -f 'mtr/mtrGroup.c' || echo './'`mtr/mtrGroup.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./cudd -I./st -I./epd -I./mtr -I./util -Wall -Wextra -g -O3 -MT mtr/cudd_libcudd_la-mtrGroup.lo -MD -MP -MF mtr/.deps/cudd_libcudd_la-mtrGroup.Tpo -c mtr/mtrGroup.c -o mtr/cudd_libcudd_la-mtrGroup.o
mv -f mtr/.deps/cudd_libcudd_la-mtrGroup.Tpo mtr/.deps/cudd_libcudd_la-mtrGroup.Plo
/bin/bash ./libtool  --tag=CXX   --mode=link g++  -Wall -Wextra -std=c++0x -g -O3 -release 3.0.0 -version-info 0:0:0 -no-undefined  -o cudd/libcudd.la -rpath /usr/local/lib cudd/libcudd_la-cuddAddAbs.lo cudd/libcudd_la-cuddAddApply.lo cudd/libcudd_la-cuddAddFind.lo cudd/libcudd_la-cuddAddInv.lo cudd/libcudd_la-cuddAddIte.lo cudd/libcudd_la-cuddAddNeg.lo cudd/libcudd_la-cuddAddWalsh.lo cudd/libcudd_la-cuddAndAbs.lo cudd/libcudd_la-cuddAnneal.lo cudd/libcudd_la-cuddApa.lo cudd/libcudd_la-cuddAPI.lo cudd/libcudd_la-cuddApprox.lo cudd/libcudd_la-cuddBddAbs.lo cudd/libcudd_la-cuddBddCorr.lo cudd/libcudd_la-cuddBddIte.lo cudd/libcudd_la-cuddBridge.lo cudd/libcudd_la-cuddCache.lo cudd/libcudd_la-cuddCheck.lo cudd/libcudd_la-cuddClip.lo cudd/libcudd_la-cuddCof.lo cudd/libcudd_la-cuddCompose.lo cudd/libcudd_la-cuddDecomp.lo cudd/libcudd_la-cuddEssent.lo cudd/libcudd_la-cuddExact.lo cudd/libcudd_la-cuddExport.lo cudd/libcudd_la-cuddGenCof.lo cudd/libcudd_la-cuddGenetic.lo cudd/libcudd_la-cuddGroup.lo cudd/libcudd_la-cuddHarwell.lo cudd/libcudd_la-cuddInit.lo cudd/libcudd_la-cuddInteract.lo cudd/libcudd_la-cuddLCache.lo cudd/libcudd_la-cuddLevelQ.lo cudd/libcudd_la-cuddLinear.lo cudd/libcudd_la-cuddLiteral.lo cudd/libcudd_la-cuddMatMult.lo cudd/libcudd_la-cuddPriority.lo cudd/libcudd_la-cuddRead.lo cudd/libcudd_la-cuddRef.lo cudd/libcudd_la-cuddReorder.lo cudd/libcudd_la-cuddSat.lo cudd/libcudd_la-cuddSign.lo cudd/libcudd_la-cuddSolve.lo cudd/libcudd_la-cuddSplit.lo cudd/libcudd_la-cuddSubsetHB.lo cudd/libcudd_la-cuddSubsetSP.lo cudd/libcudd_la-cuddSymmetry.lo cudd/libcudd_la-cuddTable.lo cudd/libcudd_la-cuddUtil.lo cudd/libcudd_la-cuddWindow.lo cudd/libcudd_la-cuddZddCount.lo cudd/libcudd_la-cuddZddFuncs.lo cudd/libcudd_la-cuddZddGroup.lo cudd/libcudd_la-cuddZddIsop.lo cudd/libcudd_la-cuddZddLin.lo cudd/libcudd_la-cuddZddMisc.lo cudd/libcudd_la-cuddZddPort.lo cudd/libcudd_la-cuddZddReord.lo cudd/libcudd_la-cuddZddSetop.lo cudd/libcudd_la-cuddZddSymm.lo cudd/libcudd_la-cuddZddUtil.lo util/cudd_libcudd_la-cpu_stats.lo util/cudd_libcudd_la-cpu_time.lo util/cudd_libcudd_la-cstringstream.lo util/cudd_libcudd_la-datalimit.lo util/cudd_libcudd_la-pathsearch.lo util/cudd_libcudd_la-pipefork.lo util/cudd_libcudd_la-prtime.lo util/cudd_libcudd_la-safe_mem.lo util/cudd_libcudd_la-strsav.lo util/cudd_libcudd_la-texpand.lo util/cudd_libcudd_la-ucbqsort.lo st/cudd_libcudd_la-st.lo epd/cudd_libcudd_la-epd.lo mtr/cudd_libcudd_la-mtrBasic.lo mtr/cudd_libcudd_la-mtrGroup.lo    -lm 
libtool: link: ar cr cudd/.libs/libcudd.a  cudd/libcudd_la-cuddAddAbs.o cudd/libcudd_la-cuddAddApply.o cudd/libcudd_la-cuddAddFind.o cudd/libcudd_la-cuddAddInv.o cudd/libcudd_la-cuddAddIte.o cudd/libcudd_la-cuddAddNeg.o cudd/libcudd_la-cuddAddWalsh.o cudd/libcudd_la-cuddAndAbs.o cudd/libcudd_la-cuddAnneal.o cudd/libcudd_la-cuddApa.o cudd/libcudd_la-cuddAPI.o cudd/libcudd_la-cuddApprox.o cudd/libcudd_la-cuddBddAbs.o cudd/libcudd_la-cuddBddCorr.o cudd/libcudd_la-cuddBddIte.o cudd/libcudd_la-cuddBridge.o cudd/libcudd_la-cuddCache.o cudd/libcudd_la-cuddCheck.o cudd/libcudd_la-cuddClip.o cudd/libcudd_la-cuddCof.o cudd/libcudd_la-cuddCompose.o cudd/libcudd_la-cuddDecomp.o cudd/libcudd_la-cuddEssent.o cudd/libcudd_la-cuddExact.o cudd/libcudd_la-cuddExport.o cudd/libcudd_la-cuddGenCof.o cudd/libcudd_la-cuddGenetic.o cudd/libcudd_la-cuddGroup.o cudd/libcudd_la-cuddHarwell.o cudd/libcudd_la-cuddInit.o cudd/libcudd_la-cuddInteract.o cudd/libcudd_la-cuddLCache.o cudd/libcudd_la-cuddLevelQ.o cudd/libcudd_la-cuddLinear.o cudd/libcudd_la-cuddLiteral.o cudd/libcudd_la-cuddMatMult.o cudd/libcudd_la-cuddPriority.o cudd/libcudd_la-cuddRead.o cudd/libcudd_la-cuddRef.o cudd/libcudd_la-cuddReorder.o cudd/libcudd_la-cuddSat.o cudd/libcudd_la-cuddSign.o cudd/libcudd_la-cuddSolve.o cudd/libcudd_la-cuddSplit.o cudd/libcudd_la-cuddSubsetHB.o cudd/libcudd_la-cuddSubsetSP.o cudd/libcudd_la-cuddSymmetry.o cudd/libcudd_la-cuddTable.o cudd/libcudd_la-cuddUtil.o cudd/libcudd_la-cuddWindow.o cudd/libcudd_la-cuddZddCount.o cudd/libcudd_la-cuddZddFuncs.o cudd/libcudd_la-cuddZddGroup.o cudd/libcudd_la-cuddZddIsop.o cudd/libcudd_la-cuddZddLin.o cudd/libcudd_la-cuddZddMisc.o cudd/libcudd_la-cuddZddPort.o cudd/libcudd_la-cuddZddReord.o cudd/libcudd_la-cuddZddSetop.o cudd/libcudd_la-cuddZddSymm.o cudd/libcudd_la-cuddZddUtil.o util/cudd_libcudd_la-cpu_stats.o util/cudd_libcudd_la-cpu_time.o util/cudd_libcudd_la-cstringstream.o util/cudd_libcudd_la-datalimit.o util/cudd_libcudd_la-pathsearch.o util/cudd_libcudd_la-pipefork.o util/cudd_libcudd_la-prtime.o util/cudd_libcudd_la-safe_mem.o util/cudd_libcudd_la-strsav.o util/cudd_libcudd_la-texpand.o util/cudd_libcudd_la-ucbqsort.o st/cudd_libcudd_la-st.o epd/cudd_libcudd_la-epd.o mtr/cudd_libcudd_la-mtrBasic.o mtr/cudd_libcudd_la-mtrGroup.o
libtool: link: ranlib cudd/.libs/libcudd.a
libtool: link: ( cd "cudd/.libs" && rm -f "libcudd.la" && ln -s "../libcudd.la" "libcudd.la" )
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpBinary.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpBinary.Tpo -c -o dddmp/libdddmp_la-dddmpBinary.lo `test -f 'dddmp/dddmpBinary.c' || echo './'`dddmp/dddmpBinary.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpBinary.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpBinary.Tpo -c dddmp/dddmpBinary.c -o dddmp/libdddmp_la-dddmpBinary.o
mv -f dddmp/.deps/libdddmp_la-dddmpBinary.Tpo dddmp/.deps/libdddmp_la-dddmpBinary.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpConvert.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpConvert.Tpo -c -o dddmp/libdddmp_la-dddmpConvert.lo `test -f 'dddmp/dddmpConvert.c' || echo './'`dddmp/dddmpConvert.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpConvert.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpConvert.Tpo -c dddmp/dddmpConvert.c -o dddmp/libdddmp_la-dddmpConvert.o
mv -f dddmp/.deps/libdddmp_la-dddmpConvert.Tpo dddmp/.deps/libdddmp_la-dddmpConvert.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpDbg.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpDbg.Tpo -c -o dddmp/libdddmp_la-dddmpDbg.lo `test -f 'dddmp/dddmpDbg.c' || echo './'`dddmp/dddmpDbg.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpDbg.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpDbg.Tpo -c dddmp/dddmpDbg.c -o dddmp/libdddmp_la-dddmpDbg.o
mv -f dddmp/.deps/libdddmp_la-dddmpDbg.Tpo dddmp/.deps/libdddmp_la-dddmpDbg.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpLoad.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpLoad.Tpo -c -o dddmp/libdddmp_la-dddmpLoad.lo `test -f 'dddmp/dddmpLoad.c' || echo './'`dddmp/dddmpLoad.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpLoad.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpLoad.Tpo -c dddmp/dddmpLoad.c -o dddmp/libdddmp_la-dddmpLoad.o
mv -f dddmp/.deps/libdddmp_la-dddmpLoad.Tpo dddmp/.deps/libdddmp_la-dddmpLoad.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpLoadCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpLoadCnf.Tpo -c -o dddmp/libdddmp_la-dddmpLoadCnf.lo `test -f 'dddmp/dddmpLoadCnf.c' || echo './'`dddmp/dddmpLoadCnf.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpLoadCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpLoadCnf.Tpo -c dddmp/dddmpLoadCnf.c -o dddmp/libdddmp_la-dddmpLoadCnf.o
mv -f dddmp/.deps/libdddmp_la-dddmpLoadCnf.Tpo dddmp/.deps/libdddmp_la-dddmpLoadCnf.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeAdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeAdd.Tpo -c -o dddmp/libdddmp_la-dddmpNodeAdd.lo `test -f 'dddmp/dddmpNodeAdd.c' || echo './'`dddmp/dddmpNodeAdd.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeAdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeAdd.Tpo -c dddmp/dddmpNodeAdd.c -o dddmp/libdddmp_la-dddmpNodeAdd.o
mv -f dddmp/.deps/libdddmp_la-dddmpNodeAdd.Tpo dddmp/.deps/libdddmp_la-dddmpNodeAdd.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeBdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeBdd.Tpo -c -o dddmp/libdddmp_la-dddmpNodeBdd.lo `test -f 'dddmp/dddmpNodeBdd.c' || echo './'`dddmp/dddmpNodeBdd.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeBdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeBdd.Tpo -c dddmp/dddmpNodeBdd.c -o dddmp/libdddmp_la-dddmpNodeBdd.o
mv -f dddmp/.deps/libdddmp_la-dddmpNodeBdd.Tpo dddmp/.deps/libdddmp_la-dddmpNodeBdd.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeCnf.Tpo -c -o dddmp/libdddmp_la-dddmpNodeCnf.lo `test -f 'dddmp/dddmpNodeCnf.c' || echo './'`dddmp/dddmpNodeCnf.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpNodeCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpNodeCnf.Tpo -c dddmp/dddmpNodeCnf.c -o dddmp/libdddmp_la-dddmpNodeCnf.o
mv -f dddmp/.deps/libdddmp_la-dddmpNodeCnf.Tpo dddmp/.deps/libdddmp_la-dddmpNodeCnf.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreAdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreAdd.Tpo -c -o dddmp/libdddmp_la-dddmpStoreAdd.lo `test -f 'dddmp/dddmpStoreAdd.c' || echo './'`dddmp/dddmpStoreAdd.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreAdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreAdd.Tpo -c dddmp/dddmpStoreAdd.c -o dddmp/libdddmp_la-dddmpStoreAdd.o
mv -f dddmp/.deps/libdddmp_la-dddmpStoreAdd.Tpo dddmp/.deps/libdddmp_la-dddmpStoreAdd.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreBdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreBdd.Tpo -c -o dddmp/libdddmp_la-dddmpStoreBdd.lo `test -f 'dddmp/dddmpStoreBdd.c' || echo './'`dddmp/dddmpStoreBdd.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreBdd.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreBdd.Tpo -c dddmp/dddmpStoreBdd.c -o dddmp/libdddmp_la-dddmpStoreBdd.o
mv -f dddmp/.deps/libdddmp_la-dddmpStoreBdd.Tpo dddmp/.deps/libdddmp_la-dddmpStoreBdd.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreCnf.Tpo -c -o dddmp/libdddmp_la-dddmpStoreCnf.lo `test -f 'dddmp/dddmpStoreCnf.c' || echo './'`dddmp/dddmpStoreCnf.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreCnf.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreCnf.Tpo -c dddmp/dddmpStoreCnf.c -o dddmp/libdddmp_la-dddmpStoreCnf.o
In file included from dddmp/dddmpInt.h:39,
                 from dddmp/dddmpStoreCnf.c:29:
dddmp/dddmpStoreCnf.c: In function 'DddmpCuddBddArrayStoreCnf':
dddmp/dddmp.h:242:5: warning: this statement may fall through [-Wimplicit-fallthrough=]
  242 |     fflush (stderr); \
      |     ^~~~~~~~~~~~~~~
dddmp/dddmpStoreCnf.c:599:7: note: in expansion of macro 'Dddmp_Warning'
  599 |       Dddmp_Warning (1, "Wrong DDDMP Store Mode. Force DDDMP_MODE_BEST.");
      |       ^~~~~~~~~~~~~
dddmp/dddmpStoreCnf.c:600:5: note: here
  600 |     case DDDMP_CNF_MODE_BEST:
      |     ^~~~
dddmp/dddmp.h:242:5: warning: this statement may fall through [-Wimplicit-fallthrough=]
  242 |     fflush (stderr); \
      |     ^~~~~~~~~~~~~~~
dddmp/dddmpStoreCnf.c:645:7: note: in expansion of macro 'Dddmp_Warning'
  645 |       Dddmp_Warning (1, "Wrong DDDMP Store Mode. Force DDDMP_MODE_BEST.");
      |       ^~~~~~~~~~~~~
dddmp/dddmpStoreCnf.c:646:5: note: here
  646 |     case DDDMP_CNF_MODE_BEST:
      |     ^~~~
mv -f dddmp/.deps/libdddmp_la-dddmpStoreCnf.Tpo dddmp/.deps/libdddmp_la-dddmpStoreCnf.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreMisc.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreMisc.Tpo -c -o dddmp/libdddmp_la-dddmpStoreMisc.lo `test -f 'dddmp/dddmpStoreMisc.c' || echo './'`dddmp/dddmpStoreMisc.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpStoreMisc.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpStoreMisc.Tpo -c dddmp/dddmpStoreMisc.c -o dddmp/libdddmp_la-dddmpStoreMisc.o
mv -f dddmp/.deps/libdddmp_la-dddmpStoreMisc.Tpo dddmp/.deps/libdddmp_la-dddmpStoreMisc.Plo
/bin/bash ./libtool  --tag=CC   --mode=compile gcc -DHAVE_CONFIG_H -I.  -I./util -I./mtr -I./epd -I./cudd -I./st   -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpUtil.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpUtil.Tpo -c -o dddmp/libdddmp_la-dddmpUtil.lo `test -f 'dddmp/dddmpUtil.c' || echo './'`dddmp/dddmpUtil.c
libtool: compile:  gcc -DHAVE_CONFIG_H -I. -I./util -I./mtr -I./epd -I./cudd -I./st -Wall -Wextra -g -O3 -MT dddmp/libdddmp_la-dddmpUtil.lo -MD -MP -MF dddmp/.deps/libdddmp_la-dddmpUtil.Tpo -c dddmp/dddmpUtil.c -o dddmp/libdddmp_la-dddmpUtil.o
mv -f dddmp/.deps/libdddmp_la-dddmpUtil.Tpo dddmp/.deps/libdddmp_la-dddmpUtil.Plo
/bin/bash ./libtool  --tag=CC   --mode=link gcc  -Wall -Wextra -g -O3   -o dddmp/libdddmp.la  dddmp/libdddmp_la-dddmpBinary.lo dddmp/libdddmp_la-dddmpConvert.lo dddmp/libdddmp_la-dddmpDbg.lo dddmp/libdddmp_la-dddmpLoad.lo dddmp/libdddmp_la-dddmpLoadCnf.lo dddmp/libdddmp_la-dddmpNodeAdd.lo dddmp/libdddmp_la-dddmpNodeBdd.lo dddmp/libdddmp_la-dddmpNodeCnf.lo dddmp/libdddmp_la-dddmpStoreAdd.lo dddmp/libdddmp_la-dddmpStoreBdd.lo dddmp/libdddmp_la-dddmpStoreCnf.lo dddmp/libdddmp_la-dddmpStoreMisc.lo dddmp/libdddmp_la-dddmpUtil.lo  -lm 
libtool: link: ar cr dddmp/.libs/libdddmp.a  dddmp/libdddmp_la-dddmpBinary.o dddmp/libdddmp_la-dddmpConvert.o dddmp/libdddmp_la-dddmpDbg.o dddmp/libdddmp_la-dddmpLoad.o dddmp/libdddmp_la-dddmpLoadCnf.o dddmp/libdddmp_la-dddmpNodeAdd.o dddmp/libdddmp_la-dddmpNodeBdd.o dddmp/libdddmp_la-dddmpNodeCnf.o dddmp/libdddmp_la-dddmpStoreAdd.o dddmp/libdddmp_la-dddmpStoreBdd.o dddmp/libdddmp_la-dddmpStoreCnf.o dddmp/libdddmp_la-dddmpStoreMisc.o dddmp/libdddmp_la-dddmpUtil.o
libtool: link: ranlib dddmp/.libs/libdddmp.a
libtool: link: ( cd "dddmp/.libs" && rm -f "libdddmp.la" && ln -s "../libdddmp.la" "libdddmp.la" )
/bin/bash ./libtool  --tag=CXX   --mode=compile g++ -DHAVE_CONFIG_H -I.  -I./cudd -I./mtr -I./epd -I./st   -Wall -Wextra -std=c++0x -g -O3 -MT cplusplus/libobj_la-cuddObj.lo -MD -MP -MF cplusplus/.deps/libobj_la-cuddObj.Tpo -c -o cplusplus/libobj_la-cuddObj.lo `test -f 'cplusplus/cuddObj.cc' || echo './'`cplusplus/cuddObj.cc
libtool: compile:  g++ -DHAVE_CONFIG_H -I. -I./cudd -I./mtr -I./epd -I./st -Wall -Wextra -std=c++0x -g -O3 -MT cplusplus/libobj_la-cuddObj.lo -MD -MP -MF cplusplus/.deps/libobj_la-cuddObj.Tpo -c cplusplus/cuddObj.cc -o cplusplus/libobj_la-cuddObj.o
mv -f cplusplus/.deps/libobj_la-cuddObj.Tpo cplusplus/.deps/libobj_la-cuddObj.Plo
/bin/bash ./libtool  --tag=CXX   --mode=link g++  -Wall -Wextra -std=c++0x -g -O3   -o cplusplus/libobj.la  cplusplus/libobj_la-cuddObj.lo  -lm 
libtool: link: ar cr cplusplus/.libs/libobj.a  cplusplus/libobj_la-cuddObj.o
libtool: link: ranlib cplusplus/.libs/libobj.a
libtool: link: ( cd "cplusplus/.libs" && rm -f "libobj.la" && ln -s "../libobj.la" "libobj.la" )
make[1]: Leaving directory '/home/ank/Desktop/SoC_Shwetank/cudd'
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ sudo make install
make[1]: Entering directory '/home/ank/Desktop/SoC_Shwetank/cudd'
 /usr/bin/mkdir -p '/usr/local/lib'
 /bin/bash ./libtool   --mode=install /usr/bin/install -c   cudd/libcudd.la '/usr/local/lib'
libtool: install: /usr/bin/install -c cudd/.libs/libcudd.lai /usr/local/lib/libcudd.la
libtool: install: /usr/bin/install -c cudd/.libs/libcudd.a /usr/local/lib/libcudd.a
libtool: install: chmod 644 /usr/local/lib/libcudd.a
libtool: install: ranlib /usr/local/lib/libcudd.a
libtool: finish: PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/sbin" ldconfig -n /usr/local/lib
----------------------------------------------------------------------
Libraries have been installed in:
   /usr/local/lib

If you ever happen to want to link against installed libraries
in a given directory, LIBDIR, you must either use libtool, and
specify the full pathname of the library, or use the '-LLIBDIR'
flag during linking and do at least one of the following:
   - add LIBDIR to the 'LD_LIBRARY_PATH' environment variable
     during execution
   - add LIBDIR to the 'LD_RUN_PATH' environment variable
     during linking
   - use the '-Wl,-rpath -Wl,LIBDIR' linker flag
   - have your system administrator add LIBDIR to '/etc/ld.so.conf'

See any operating system documentation about shared libraries for
more information, such as the ld(1) and ld.so(8) manual pages.
----------------------------------------------------------------------
 /usr/bin/mkdir -p '/usr/local/include'
 /usr/bin/install -c -m 644 cudd/cudd.h '/usr/local/include'
make[1]: Leaving directory '/home/ank/Desktop/SoC_Shwetank/cudd'
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/cudd$ cd ~/Desktop/SoC_Shwetank/OpenSTA/build/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ rm -rf *
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cmake ..
-- The CXX compiler identification is GNU 13.3.0
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- STA version: 2.7.0
-- STA git sha: 05b292c379c9f3a74d23c67adb6f937e0206b374
-- System name: Linux
-- Compiler: GNU 13.3.0
-- Build type: RELEASE
-- Build CXX_FLAGS: -O3 -DNDEBUG
-- Install prefix: /usr/local
-- Found FLEX: /usr/bin/flex (found version "2.6.4") 
-- Found BISON: /usr/bin/bison (found version "3.8.2") 
-- TCL library: /usr/lib/x86_64-linux-gnu/libtcl.so
-- TCL header: /usr/include/tcl/tcl.h
-- TCL readline library: NOT FOUND
-- TCL readline header: NOT FOUND
-- Found ZLIB: /usr/lib/x86_64-linux-gnu/libz.so (found version "1.3")  
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE  
-- CUDD library: /usr/local/lib/libcudd.a
-- CUDD header: /usr/local/include/cudd.h
-- SSTA: 0
-- Found SWIG: /usr/bin/swig4.0 (found suitable version "4.2.0", minimum required is "3.0")  
-- STA library: /home/ank/Desktop/SoC_Shwetank/OpenSTA/build/libOpenSTA.a
-- STA executable: /home/ank/Desktop/SoC_Shwetank/OpenSTA/build/sta
-- Configuring done (0.6s)
-- Generating done (0.0s)
-- Build files have been written to: /home/ank/Desktop/SoC_Shwetank/OpenSTA/build
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ make
[  0%] [BISON][VerilogParse] Building parser with bison 3.8.2
[  0%] [FLEX][LibExprLex] Building scanner with flex 2.6.4
[  1%] [BISON][LibExprParse] Building parser with bison 3.8.2
[  1%] [FLEX][LibertyLex] Building scanner with flex 2.6.4
[  2%] [BISON][LibertyParse] Building parser with bison 3.8.2
[  3%] [FLEX][SaifLex] Building scanner with flex 2.6.4
[  3%] [BISON][SaifParse] Building parser with bison 3.8.2
[  4%] [FLEX][SdfLex] Building scanner with flex 2.6.4
[  5%] [BISON][SdfParse] Building parser with bison 3.8.2
[  5%] [FLEX][SpefLex] Building scanner with flex 2.6.4
[  6%] [BISON][SpefParse] Building parser with bison 3.8.2
[  6%] Generating StaTclInitVar.cc
[  7%] [FLEX][VerilogLex] Building scanner with flex 2.6.4
[  7%] Building CXX object CMakeFiles/OpenSTA.dir/app/StaMain.cc.o
[  8%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/ArcDelayCalc.cc.o
[  8%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/ArcDcalcWaveforms.cc.o
[  9%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/ArnoldiDelayCalc.cc.o
[ 10%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/ArnoldiReduce.cc.o
[ 10%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/CcsCeffDelayCalc.cc.o
[ 11%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/DcalcAnalysisPt.cc.o
[ 11%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/DelayCalc.cc.o
[ 12%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/DelayCalcBase.cc.o
[ 12%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/DmpCeff.cc.o
[ 13%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/DmpDelayCalc.cc.o
[ 13%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/FindRoot.cc.o
[ 14%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/GraphDelayCalc.cc.o
[ 15%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/LumpedCapDelayCalc.cc.o
[ 15%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/NetCaps.cc.o
[ 16%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/ParallelDelayCalc.cc.o
[ 16%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/PrimaDelayCalc.cc.o
[ 17%] Building CXX object CMakeFiles/OpenSTA.dir/dcalc/UnitDelayCalc.cc.o
[ 17%] Building CXX object CMakeFiles/OpenSTA.dir/graph/DelayFloat.cc.o
[ 18%] Building CXX object CMakeFiles/OpenSTA.dir/graph/DelayNormal1.cc.o
[ 18%] Building CXX object CMakeFiles/OpenSTA.dir/graph/DelayNormal2.cc.o
[ 19%] Building CXX object CMakeFiles/OpenSTA.dir/graph/Graph.cc.o
[ 20%] Building CXX object CMakeFiles/OpenSTA.dir/graph/GraphCmp.cc.o
[ 20%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/EquivCells.cc.o
[ 21%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/FuncExpr.cc.o
[ 21%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/InternalPower.cc.o
[ 22%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LeakagePower.cc.o
[ 22%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/Liberty.cc.o
[ 23%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LibertyBuilder.cc.o
[ 23%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LibExprReader.cc.o
[ 24%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LibertyParser.cc.o
[ 25%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LibertyReader.cc.o
[ 25%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LibertyWriter.cc.o
[ 26%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/LinearModel.cc.o
[ 26%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/Sequential.cc.o
[ 27%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/TableModel.cc.o
[ 27%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/TimingArc.cc.o
[ 28%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/TimingModel.cc.o
[ 28%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/TimingRole.cc.o
[ 29%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/Units.cc.o
[ 30%] Building CXX object CMakeFiles/OpenSTA.dir/liberty/Wireload.cc.o
[ 30%] Building CXX object CMakeFiles/OpenSTA.dir/network/ConcreteLibrary.cc.o
[ 31%] Building CXX object CMakeFiles/OpenSTA.dir/network/ConcreteNetwork.cc.o
[ 31%] Building CXX object CMakeFiles/OpenSTA.dir/network/HpinDrvrLoad.cc.o
[ 32%] Building CXX object CMakeFiles/OpenSTA.dir/network/Network.cc.o
[ 32%] Building CXX object CMakeFiles/OpenSTA.dir/network/NetworkCmp.cc.o
[ 33%] Building CXX object CMakeFiles/OpenSTA.dir/network/ParseBus.cc.o
[ 33%] Building CXX object CMakeFiles/OpenSTA.dir/network/PortDirection.cc.o
[ 34%] Building CXX object CMakeFiles/OpenSTA.dir/network/SdcNetwork.cc.o
[ 35%] Building CXX object CMakeFiles/OpenSTA.dir/network/VerilogNamespace.cc.o
[ 35%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/ConcreteParasitics.cc.o
[ 36%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/EstimateParasitics.cc.o
[ 36%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/Parasitics.cc.o
[ 37%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/ReduceParasitics.cc.o
[ 37%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/ReportParasiticAnnotation.cc.o
[ 38%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/SpefNamespace.cc.o
[ 38%] Building CXX object CMakeFiles/OpenSTA.dir/parasitics/SpefReader.cc.o
[ 39%] Building CXX object CMakeFiles/OpenSTA.dir/power/Power.cc.o
[ 40%] Building CXX object CMakeFiles/OpenSTA.dir/power/VcdReader.cc.o
[ 40%] Building CXX object CMakeFiles/OpenSTA.dir/power/SaifReader.cc.o
[ 41%] Building CXX object CMakeFiles/OpenSTA.dir/power/VcdParse.cc.o
[ 41%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/Clock.cc.o
[ 42%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/ClockGatingCheck.cc.o
[ 42%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/ClockGroups.cc.o
[ 43%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/ClockInsertion.cc.o
[ 43%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/ClockLatency.cc.o
[ 44%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/CycleAccting.cc.o
[ 45%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/DataCheck.cc.o
[ 45%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/DeratingFactors.cc.o
[ 46%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/DisabledPorts.cc.o
[ 46%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/ExceptionPath.cc.o
[ 47%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/InputDrive.cc.o
[ 47%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/PinPair.cc.o
[ 48%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/PortDelay.cc.o
[ 48%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/PortExtCap.cc.o
[ 49%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/Sdc.cc.o
[ 50%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/SdcGraph.cc.o
[ 50%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/SdcCmdComment.cc.o
[ 51%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/Variables.cc.o
[ 51%] Building CXX object CMakeFiles/OpenSTA.dir/sdc/WriteSdc.cc.o
[ 52%] Building CXX object CMakeFiles/OpenSTA.dir/sdf/ReportAnnotation.cc.o
[ 52%] Building CXX object CMakeFiles/OpenSTA.dir/sdf/SdfReader.cc.o
[ 53%] Building CXX object CMakeFiles/OpenSTA.dir/sdf/SdfWriter.cc.o
[ 53%] Building CXX object CMakeFiles/OpenSTA.dir/search/Bdd.cc.o
[ 54%] Building CXX object CMakeFiles/OpenSTA.dir/search/Bfs.cc.o
[ 55%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckMaxSkews.cc.o
[ 55%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckMinPeriods.cc.o
[ 56%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckMinPulseWidths.cc.o
[ 56%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckCapacitanceLimits.cc.o
[ 57%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckFanoutLimits.cc.o
[ 57%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckSlewLimits.cc.o
[ 58%] Building CXX object CMakeFiles/OpenSTA.dir/search/CheckTiming.cc.o
[ 58%] Building CXX object CMakeFiles/OpenSTA.dir/search/ClkInfo.cc.o
[ 59%] Building CXX object CMakeFiles/OpenSTA.dir/search/ClkLatency.cc.o
[ 60%] Building CXX object CMakeFiles/OpenSTA.dir/search/ClkNetwork.cc.o
[ 60%] Building CXX object CMakeFiles/OpenSTA.dir/search/ClkSkew.cc.o
[ 61%] Building CXX object CMakeFiles/OpenSTA.dir/search/Corner.cc.o
[ 61%] Building CXX object CMakeFiles/OpenSTA.dir/search/Crpr.cc.o
[ 62%] Building CXX object CMakeFiles/OpenSTA.dir/search/FindRegister.cc.o
[ 62%] Building CXX object CMakeFiles/OpenSTA.dir/search/GatedClk.cc.o
[ 63%] Building CXX object CMakeFiles/OpenSTA.dir/search/Genclks.cc.o
[ 63%] Building CXX object CMakeFiles/OpenSTA.dir/search/Latches.cc.o
[ 64%] Building CXX object CMakeFiles/OpenSTA.dir/search/Levelize.cc.o
[ 65%] Building CXX object CMakeFiles/OpenSTA.dir/search/MakeTimingModel.cc.o
[ 65%] Building CXX object CMakeFiles/OpenSTA.dir/search/Path.cc.o
[ 66%] Building CXX object CMakeFiles/OpenSTA.dir/search/PathAnalysisPt.cc.o
[ 66%] Building CXX object CMakeFiles/OpenSTA.dir/search/PathEnd.cc.o
[ 67%] Building CXX object CMakeFiles/OpenSTA.dir/search/PathEnum.cc.o
[ 67%] Building CXX object CMakeFiles/OpenSTA.dir/search/PathExpanded.cc.o
[ 68%] Building CXX object CMakeFiles/OpenSTA.dir/search/PathGroup.cc.o
[ 68%] Building CXX object CMakeFiles/OpenSTA.dir/search/Property.cc.o
[ 69%] Building CXX object CMakeFiles/OpenSTA.dir/search/ReportPath.cc.o
[ 70%] Building CXX object CMakeFiles/OpenSTA.dir/search/Search.cc.o
[ 70%] Building CXX object CMakeFiles/OpenSTA.dir/search/SearchPred.cc.o
[ 71%] Building CXX object CMakeFiles/OpenSTA.dir/search/Sim.cc.o
[ 71%] Building CXX object CMakeFiles/OpenSTA.dir/search/Sta.cc.o
[ 72%] Building CXX object CMakeFiles/OpenSTA.dir/search/StaState.cc.o
[ 72%] Building CXX object CMakeFiles/OpenSTA.dir/search/Tag.cc.o
[ 73%] Building CXX object CMakeFiles/OpenSTA.dir/search/TagGroup.cc.o
[ 73%] Building CXX object CMakeFiles/OpenSTA.dir/search/VertexVisitor.cc.o
[ 74%] Building CXX object CMakeFiles/OpenSTA.dir/search/VisitPathEnds.cc.o
[ 75%] Building CXX object CMakeFiles/OpenSTA.dir/search/VisitPathGroupVertices.cc.o
[ 75%] Building CXX object CMakeFiles/OpenSTA.dir/search/WorstSlack.cc.o
[ 76%] Building CXX object CMakeFiles/OpenSTA.dir/spice/WritePathSpice.cc.o
[ 76%] Building CXX object CMakeFiles/OpenSTA.dir/spice/WriteSpice.cc.o
[ 77%] Building CXX object CMakeFiles/OpenSTA.dir/spice/Xyce.cc.o
[ 77%] Building CXX object CMakeFiles/OpenSTA.dir/tcl/TclTypeHelpers.cc.o
[ 78%] Building CXX object CMakeFiles/OpenSTA.dir/util/Debug.cc.o
[ 78%] Building CXX object CMakeFiles/OpenSTA.dir/util/DispatchQueue.cc.o
[ 79%] Building CXX object CMakeFiles/OpenSTA.dir/util/Error.cc.o
[ 80%] Building CXX object CMakeFiles/OpenSTA.dir/util/Fuzzy.cc.o
[ 80%] Building CXX object CMakeFiles/OpenSTA.dir/util/Hash.cc.o
[ 81%] Building CXX object CMakeFiles/OpenSTA.dir/util/Machine.cc.o
[ 81%] Building CXX object CMakeFiles/OpenSTA.dir/util/MinMax.cc.o
[ 82%] Building CXX object CMakeFiles/OpenSTA.dir/util/PatternMatch.cc.o
[ 82%] Building CXX object CMakeFiles/OpenSTA.dir/util/Report.cc.o
[ 83%] Building CXX object CMakeFiles/OpenSTA.dir/util/ReportStd.cc.o
[ 83%] Building CXX object CMakeFiles/OpenSTA.dir/util/ReportTcl.cc.o
[ 84%] Building CXX object CMakeFiles/OpenSTA.dir/util/RiseFallMinMax.cc.o
[ 85%] Building CXX object CMakeFiles/OpenSTA.dir/util/RiseFallValues.cc.o
[ 85%] Building CXX object CMakeFiles/OpenSTA.dir/util/Stats.cc.o
[ 86%] Building CXX object CMakeFiles/OpenSTA.dir/util/StringSeq.cc.o
[ 86%] Building CXX object CMakeFiles/OpenSTA.dir/util/StringSet.cc.o
[ 87%] Building CXX object CMakeFiles/OpenSTA.dir/util/StringUtil.cc.o
[ 87%] Building CXX object CMakeFiles/OpenSTA.dir/util/TokenParser.cc.o
[ 88%] Building CXX object CMakeFiles/OpenSTA.dir/util/Transition.cc.o
[ 88%] Building CXX object CMakeFiles/OpenSTA.dir/verilog/VerilogReader.cc.o
[ 89%] Building CXX object CMakeFiles/OpenSTA.dir/verilog/VerilogWriter.cc.o
[ 90%] Building CXX object CMakeFiles/OpenSTA.dir/StaTclInitVar.cc.o
[ 90%] Building CXX object CMakeFiles/OpenSTA.dir/LibExprLex.cc.o
[ 91%] Building CXX object CMakeFiles/OpenSTA.dir/LibExprParse.cc.o
[ 91%] Building CXX object CMakeFiles/OpenSTA.dir/LibertyLex.cc.o
[ 92%] Building CXX object CMakeFiles/OpenSTA.dir/LibertyParse.cc.o
[ 92%] Building CXX object CMakeFiles/OpenSTA.dir/SpefLex.cc.o
[ 93%] Building CXX object CMakeFiles/OpenSTA.dir/SpefParse.cc.o
[ 93%] Building CXX object CMakeFiles/OpenSTA.dir/SdfLex.cc.o
[ 94%] Building CXX object CMakeFiles/OpenSTA.dir/SdfParse.cc.o
[ 95%] Building CXX object CMakeFiles/OpenSTA.dir/VerilogLex.cc.o
[ 95%] Building CXX object CMakeFiles/OpenSTA.dir/VerilogParse.cc.o
[ 96%] Building CXX object CMakeFiles/OpenSTA.dir/SaifLex.cc.o
[ 96%] Building CXX object CMakeFiles/OpenSTA.dir/SaifParse.cc.o
[ 97%] Linking CXX static library libOpenSTA.a
[ 97%] Built target OpenSTA
[ 98%] Swig compile app/StaApp.i for tcl
[ 98%] Built target sta_swig_swig_compilation
[ 98%] Building CXX object CMakeFiles/sta_swig.dir/CMakeFiles/sta_swig.dir/StaAppTCL_wrap.cxx.o
[ 99%] Linking CXX static library sta_swig.a
[ 99%] Built target sta_swig
[ 99%] Building CXX object CMakeFiles/sta.dir/app/Main.cc.o
[100%] Linking CXX executable sta
[100%] Built target sta
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ sudo make install
[ 97%] Built target OpenSTA
[ 98%] Built target sta_swig_swig_compilation
[ 99%] Built target sta_swig
[100%] Built target sta
Install the project...
-- Install configuration: "RELEASE"
-- Installing: /usr/local/bin/sta
-- Installing: /usr/local/lib/libOpenSTA.a
-- Installing: /usr/local/include/sta
-- Installing: /usr/local/include/sta/PortDirection.hh
-- Installing: /usr/local/include/sta/ReportTcl.hh
-- Installing: /usr/local/include/sta/Bdd.hh
-- Installing: /usr/local/include/sta/Bfs.hh
-- Installing: /usr/local/include/sta/Wireload.hh
-- Installing: /usr/local/include/sta/Delay.hh
-- Installing: /usr/local/include/sta/Hash.hh
-- Installing: /usr/local/include/sta/ObjectId.hh
-- Installing: /usr/local/include/sta/NetworkCmp.hh
-- Installing: /usr/local/include/sta/TimingModel.hh
-- Installing: /usr/local/include/sta/TimingArc.hh
-- Installing: /usr/local/include/sta/PatternMatch.hh
-- Installing: /usr/local/include/sta/Sta.hh
-- Installing: /usr/local/include/sta/ParasiticsClass.hh
-- Installing: /usr/local/include/sta/MinMaxValues.hh
-- Installing: /usr/local/include/sta/Network.hh
-- Installing: /usr/local/include/sta/SearchClass.hh
-- Installing: /usr/local/include/sta/Machine.hh
-- Installing: /usr/local/include/sta/VerilogWriter.hh
-- Installing: /usr/local/include/sta/MinMax.hh
-- Installing: /usr/local/include/sta/DispatchQueue.hh
-- Installing: /usr/local/include/sta/UnorderedSet.hh
-- Installing: /usr/local/include/sta/PortExtCap.hh
-- Installing: /usr/local/include/sta/GraphCmp.hh
-- Installing: /usr/local/include/sta/Vector.hh
-- Installing: /usr/local/include/sta/DcalcAnalysisPt.hh
-- Installing: /usr/local/include/sta/ArcDelayCalc.hh
-- Installing: /usr/local/include/sta/DelayNormal2.hh
-- Installing: /usr/local/include/sta/PortDelay.hh
-- Installing: /usr/local/include/sta/Report.hh
-- Installing: /usr/local/include/sta/ClkNetwork.hh
-- Installing: /usr/local/include/sta/PinPair.hh
-- Installing: /usr/local/include/sta/Stats.hh
-- Installing: /usr/local/include/sta/StringSeq.hh
-- Installing: /usr/local/include/sta/ReportStd.hh
-- Installing: /usr/local/include/sta/LibertyClass.hh
-- Installing: /usr/local/include/sta/LeakagePower.hh
-- Installing: /usr/local/include/sta/SdcClass.hh
-- Installing: /usr/local/include/sta/SearchPred.hh
-- Installing: /usr/local/include/sta/LibertyWriter.hh
-- Installing: /usr/local/include/sta/Transition.hh
-- Installing: /usr/local/include/sta/EnumNameMap.hh
-- Installing: /usr/local/include/sta/GraphClass.hh
-- Installing: /usr/local/include/sta/PathEnd.hh
-- Installing: /usr/local/include/sta/ClockInsertion.hh
-- Installing: /usr/local/include/sta/VerilogNamespace.hh
-- Installing: /usr/local/include/sta/StringSet.hh
-- Installing: /usr/local/include/sta/Property.hh
-- Installing: /usr/local/include/sta/VerilogReader.hh
-- Installing: /usr/local/include/sta/StaMain.hh
-- Installing: /usr/local/include/sta/TclTypeHelpers.hh
-- Installing: /usr/local/include/sta/LinearModel.hh
-- Installing: /usr/local/include/sta/TimingRole.hh
-- Installing: /usr/local/include/sta/GraphDelayCalc.hh
-- Installing: /usr/local/include/sta/MakeConcreteNetwork.hh
-- Installing: /usr/local/include/sta/NetworkClass.hh
-- Installing: /usr/local/include/sta/ConcreteNetwork.hh
-- Installing: /usr/local/include/sta/PathAnalysisPt.hh
-- Installing: /usr/local/include/sta/DataCheck.hh
-- Installing: /usr/local/include/sta/ConcreteLibrary.hh
-- Installing: /usr/local/include/sta/Path.hh
-- Installing: /usr/local/include/sta/Fuzzy.hh
-- Installing: /usr/local/include/sta/ParseBus.hh
-- Installing: /usr/local/include/sta/Debug.hh
-- Installing: /usr/local/include/sta/VertexVisitor.hh
-- Installing: /usr/local/include/sta/StaState.hh
-- Installing: /usr/local/include/sta/TokenParser.hh
-- Installing: /usr/local/include/sta/PowerClass.hh
-- Installing: /usr/local/include/sta/Parasitics.hh
-- Installing: /usr/local/include/sta/CircuitSim.hh
-- Installing: /usr/local/include/sta/Units.hh
-- Installing: /usr/local/include/sta/TableModel.hh
-- Installing: /usr/local/include/sta/Mutex.hh
-- Installing: /usr/local/include/sta/DisabledPorts.hh
-- Installing: /usr/local/include/sta/RiseFallMinMax.hh
-- Installing: /usr/local/include/sta/InternalPower.hh
-- Installing: /usr/local/include/sta/Variables.hh
-- Installing: /usr/local/include/sta/EquivCells.hh
-- Installing: /usr/local/include/sta/HpinDrvrLoad.hh
-- Installing: /usr/local/include/sta/ClockGatingCheck.hh
-- Installing: /usr/local/include/sta/SdcCmdComment.hh
-- Installing: /usr/local/include/sta/FuncExpr.hh
-- Installing: /usr/local/include/sta/DelayFloat.hh
-- Installing: /usr/local/include/sta/Sdc.hh
-- Installing: /usr/local/include/sta/ObjectTable.hh
-- Installing: /usr/local/include/sta/VisitPathEnds.hh
-- Installing: /usr/local/include/sta/Sequential.hh
-- Installing: /usr/local/include/sta/StringUtil.hh
-- Installing: /usr/local/include/sta/CycleAccting.hh
-- Installing: /usr/local/include/sta/ClockLatency.hh
-- Installing: /usr/local/include/sta/Clock.hh
-- Installing: /usr/local/include/sta/DelayNormal1.hh
-- Installing: /usr/local/include/sta/Zlib.hh
-- Installing: /usr/local/include/sta/DeratingFactors.hh
-- Installing: /usr/local/include/sta/UnorderedMap.hh
-- Installing: /usr/local/include/sta/RiseFallValues.hh
-- Installing: /usr/local/include/sta/Corner.hh
-- Installing: /usr/local/include/sta/PathExpanded.hh
-- Installing: /usr/local/include/sta/WriteSdc.hh
-- Installing: /usr/local/include/sta/Search.hh
-- Installing: /usr/local/include/sta/InputDrive.hh
-- Installing: /usr/local/include/sta/ClockGroups.hh
-- Installing: /usr/local/include/sta/Set.hh
-- Installing: /usr/local/include/sta/MakeConcreteParasitics.hh
-- Installing: /usr/local/include/sta/VertexId.hh
-- Installing: /usr/local/include/sta/Iterator.hh
-- Installing: /usr/local/include/sta/DelayCalc.hh
-- Installing: /usr/local/include/sta/ExceptionPath.hh
-- Installing: /usr/local/include/sta/Error.hh
-- Installing: /usr/local/include/sta/PathGroup.hh
-- Installing: /usr/local/include/sta/Graph.hh
-- Installing: /usr/local/include/sta/Liberty.hh
-- Installing: /usr/local/include/sta/SdcNetwork.hh
-- Installing: /usr/local/include/sta/Map.hh
-- Up-to-date: /usr/local/include/sta
-- Installing: /usr/local/include/sta/StaConfig.hh
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/OpenSTA/build$ cd ~/Desktop/SoC_Shwetank/WEEK_3/babysoc/
(soc_env) ank@ank-Victus-by-HP-Gaming-Laptop-15-fb0xxx:~/Desktop/SoC_Shwetank/WEEK_3/babysoc$ sta -no_splash STA/run_sta.tcl | tee STA/sta_run.log
