export DESIGN_NICKNAME = VSDBabySoC
export DESIGN_NAME     = vsdbabysoc
export PLATFORM        = sky130hd

export VSDBabySoC_DIR = $(DESIGN_HOME)/$(PLATFORM)/$(DESIGN_NICKNAME)

export VERILOG_FILES = \
    $(VSDBabySoC_DIR)/src/module/vsdbabysoc.v \
    $(VSDBabySoC_DIR)/src/module/rvmyth.v \
    $(VSDBabySoC_DIR)/src/module/clk_gate.v

export SDC_FILE = $(VSDBabySoC_DIR)/vsdbabysoc_synthesis.sdc
export VERILOG_INCLUDE_DIRS = $(wildcard $(VSDBabySoC_DIR)/include/)

export ADDITIONAL_LIBS = \
    $(VSDBabySoC_DIR)/lib/avsddac.lib \
    $(VSDBabySoC_DIR)/lib/avsdpll.lib

export ADDITIONAL_GDS  = $(wildcard $(VSDBabySoC_DIR)/gds/*.gds)
export ADDITIONAL_LEFS = $(wildcard $(VSDBabySoC_DIR)/lef/*.lef)

export ADDITIONAL_ROUTING_BLOCKAGES = $(VSDBabySoC_DIR)/route_blockages.tcl

export CLOCK_PORT = CLK
export CLOCK_NET  = CLK

export FP_PIN_ORDER_CFG = $(VSDBabySoC_DIR)/pin_order.cfg

export DIE_AREA  = 0   0   1600 1600
export CORE_AREA = 20  20  1580 1580

export FP_CORE_UTIL    = 40
export PLACE_DENSITY   = 0.30   # Changed from 0.48

export MACRO_PLACE_HALO    = 40 40  # Changed from 20 20
export MACRO_PLACE_CHANNEL = 40 40

export RTLMP_FLOW = 0
export MACRO_PLACEMENT = $(VSDBabySoC_DIR)/macro.cfg

# dac 320 900 N
# pll 40  40  N

export CTS_BUF_DISTANCE  = 600
export SKIP_GATE_CLONING = 1

# Normal congestion settings
export GRT_ALLOW_CONGESTION      = 1
export GRT_SKIP_CONGESTION_CHECK = 0
export GRT_CONGESTION_DRIVEN     = 1
export GRT_MAX_ITERATIONS        = 700
export GRT_ADJUSTMENT            = 0.15
export GRT_VIA_COST_ADJUSTMENT   = 3.0
# export GRT_LAYER_ADJUSTMENTS     = {met1:0.25,met2:0.20,met3:0.15,met4:0.10,met5:0.05}
export GRT_MAX_TIME              = 3600

# ---- REQUIRED FIXES FOR YOUR VERSION (prevents GRT-0116 stop) ----
export GRT_FAIL_ON_OVERFLOW = 1
export GRT_OVERFLOW_ITERS   = 50

export TNS_END_PERCENT      = 100
export REMOVE_ABC_BUFFERS   = 1
export MAGIC_ZEROIZE_ORIGIN = 0
export MAGIC_EXT_USE_GDS    = 1

export SPEF_OUTPUT_FILE = $(VSDBabySoC_DIR)/vsdbabysoc.spef