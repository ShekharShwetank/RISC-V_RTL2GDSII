PDN_SCRIPT := $(VSDBabySoC_DIR)/pdn_custom.tcl
export PDN_SCRIPT

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

export DIE_AREA  = 0   0   2500 2500
export CORE_AREA = 20  20  2400 2400

export FP_CORE_UTIL    = 35
export PLACE_DENSITY   = 0.35   # Changed from 0.48

export MACRO_PLACE_HALO    = 100 100  # Changed from 20 20
export MACRO_PLACE_CHANNEL = 120 120

export RTLMP_FLOW = 0
export MACRO_PLACEMENT = $(VSDBabySoC_DIR)/macro.cfg

# dac 320 900 N
# pll 40  40  N

export CTS_BUF_DISTANCE  = 600
export SKIP_GATE_CLONING = 1

# Normal congestion settings
export GRT_ALLOW_CONGESTION      = 1
export GRT_SKIP_CONGESTION_CHECK = 1 #set to 0
export GRT_CONGESTION_DRIVEN     = 1
export GRT_MAX_ITERATIONS        = 1000
export GRT_ADJUSTMENT            = 0.3
export GRT_VIA_COST_ADJUSTMENT   = 2.0
# export GRT_LAYER_ADJUSTMENTS     = {met1:0.25,met2:0.20,met3:0.15,met4:0.10,met5:0.05}
# export GRT_LAYER_ADJUSTMENTS     = {met1:0.5,met2:0.4,met3:0.3,met4:0.2,met5:0.1}
# export GRT_LAYER_ADJUSTMENTS     = {met1:0.15,met2:0.12,met3:0.10,met4:0.08,met5:0.05}
export GRT_MAX_TIME              = 3600

export GRT_FAIL_ON_OVERFLOW = 0
export GRT_OVERFLOW_ITERS   = 100

export TNS_END_PERCENT      = 100
export REMOVE_ABC_BUFFERS   = 1
export MAGIC_ZEROIZE_ORIGIN = 0
export MAGIC_EXT_USE_GDS    = 1
export PWR_ANALYSIS = 0

export SPEF_OUTPUT_FILE = $(VSDBabySoC_DIR)/vsdbabysoc.spef
