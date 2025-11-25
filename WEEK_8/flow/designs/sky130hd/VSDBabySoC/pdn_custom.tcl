# pdn_custom.tcl - explicit global power mappings for VSDBabySoC

# 1) Global connections for standard cells and generic pins
add_global_connection -net VDD -inst_pattern {.*} -pin_pattern {^VPWR$|^VDD$|^VDD2$|^VDD3$|VDDPE|VDDCE|VPB} -power
add_global_connection -net VSS -inst_pattern {.*} -pin_pattern {^VGND$|^GND$|GND2|VNB|VSSE} -ground

# 2) Explicit cell-level mappings (strongest match)
# PLL cell (avsdpll) - connect all VDD/VSS variants
add_global_connection -net VDD -cell {avsdpll} -pin_pattern {^VDD$} -power
add_global_connection -net VDD -cell {avsdpll} -pin_pattern {^VDD2$} -power
add_global_connection -net VDD -cell {avsdpll} -pin_pattern {^VDD3$} -power
add_global_connection -net VSS -cell {avsdpll} -pin_pattern {^GND$} -ground
add_global_connection -net VSS -cell {avsdpll} -pin_pattern {^GND2$} -ground

# DAC cell (avsddac)
add_global_connection -net VDD -cell {avsddac} -pin_pattern {^VPWR$} -power
add_global_connection -net VSS -cell {avsddac} -pin_pattern {^VGND$} -ground

# 3) Fallback by instance names (in case instance is named 'pll' or 'dac')
add_global_connection -net VDD -inst_pattern {^pll$} -pin_pattern {^VDD$} -power
add_global_connection -net VSS -inst_pattern {^pll$} -pin_pattern {^GND$} -ground
add_global_connection -net VDD -inst_pattern {^dac$} -pin_pattern {^VPWR$} -power
add_global_connection -net VSS -inst_pattern {^dac$} -pin_pattern {^VGND$} -ground

# Apply global connections now
global_connect

# 4) Voltage domain
set_voltage_domain -name CORE -power VDD -ground VSS

# 5) Standard cell PDN grid (followpins & vertical/horizontal straps)
define_pdn_grid -name "Core" -voltage_domains CORE
add_pdn_stripe -grid "Core" -layer met1 -width 0.48 -followpins
add_pdn_stripe -grid "Core" -layer met4 -width 1.6 -pitch 80.0 -offset 10.0
add_pdn_stripe -grid "Core" -layer met5 -width 1.6 -pitch 80.0 -offset 10.0
add_pdn_connect -grid "Core" -layers {met1 met4}
add_pdn_connect -grid "Core" -layers {met4 met5}

# 6) PLL macro grid (explicitly expose low-layer connectivity)
define_pdn_grid -name "pll_grid" -voltage_domains CORE -macro -cells {avsdpll} -halo {100.0 100.0 100.0 100.0} -default_grid 0
# modest ring sizes to avoid blocking via insertion
add_pdn_ring -grid "pll_grid" -layers {met4 met5} -widths {2.0 2.0} -spacings {1.0 1.0} -pad_offsets {2.0 2.0} -add_connect
# make sure low-layer connectivity from pin to rings is allowed
add_pdn_connect -grid "pll_grid" -layers {li1 met1}
add_pdn_connect -grid "pll_grid" -layers {met1 met2}
add_pdn_connect -grid "pll_grid" -layers {met2 met3}
add_pdn_connect -grid "pll_grid" -layers {met3 met4}
add_pdn_connect -grid "pll_grid" -layers {met4 met5}

# 7) DAC macro grid
define_pdn_grid -name "dac_grid" -voltage_domains CORE -macro -cells {avsddac} -halo {100.0 100.0 100.0 100.0} -default_grid 0
add_pdn_ring -grid "dac_grid" -layers {met5} -widths {2.0} -spacings {1.0} -pad_offsets {2.0} -add_connect
# XPINs: VPWR in LEF uses met4+met5; allow met4<->met5 and lower-layer access for VGND in met2
add_pdn_connect -grid "dac_grid" -layers {met4 met5}
add_pdn_connect -grid "dac_grid" -layers {li1 met1}
add_pdn_connect -grid "dac_grid" -layers {met1 met2}
add_pdn_connect -grid "dac_grid" -layers {met2 met3}
add_pdn_connect -grid "dac_grid" -layers {met3 met4}
add_pdn_connect -grid "dac_grid" -layers {met4 met5}

