# This program will:
# 1. Load the value 0xDEADDEEF into register x5 (t0).
# 2. Store this value to memory address 0x100.

li  t0, 0xDEADDEEF      # Load Immediate value into t0
sw  t0, 256(x0)         # Store Word from t0 to address 256 (0x100) offset from register x0 (zero)
loop: j loop            # Infinite loop
