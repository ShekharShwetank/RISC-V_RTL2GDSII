// SPDX-License-Identifier: ISC
/*
 * SoC Top Level
 *
 * Copyright (C) 2021  VSD-PLL Team
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
 * ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
 * ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
 * OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
 */

`timescale 1 ns / 1 ps

/* 
module soc (
    input clk,
    input resetn
);
*/

module soc (
    input clk,
    input resetn,
    output [31:0] wb_adr_o,
    output wb_we_o,
    output [31:0] wb_dat_o,
    output wb_ack_i
);

  // Wishbone Signals
  // wire [31:0] wb_adr_o;
  wire [31:0] wb_dat_i;
  // wire [31:0] wb_dat_o;
  wire [3:0]  wb_sel_o;
  // wire        wb_we_o;
  wire        wb_cyc_o;
  wire        wb_stb_o;
  // wire        wb_ack_i;
  wire        wb_err_i;
  wire        wb_rty_i;

  // CPU mem_instr wire
  wire cpu_mem_instr;
  
  // Logic to generate Wishbone signals from PicoRV32 interface
  assign wb_cyc_o = wb_stb_o;
  assign wb_we_o  = |wb_sel_o;

  // SRAM signals
  wire [31:0] sram_addr;
  wire [31:0] sram_wdata;
  wire [31:0] sram_rdata;
  wire [3:0]  sram_sel;
  wire        sram_we;
  wire        sram_cyc;
  wire        sram_stb;
  wire        sram_ack;
  
  picorv32 #(
      .BARREL_SHIFTER(1),
      .COMPRESSED_ISA(1),
      .ENABLE_MUL(1)
  ) cpu (
      .clk(clk),
      .resetn(resetn),
      .mem_valid(wb_stb_o),
      .mem_instr(cpu_mem_instr),
      .mem_ready(wb_ack_i),
      .mem_addr(wb_adr_o),
      .mem_wdata(wb_dat_o),
      .mem_wstrb(wb_sel_o),
      .mem_rdata(wb_dat_i)
  );

  wb_interconnect wb_interconnect (
      .wb_clk_i(clk),
      .wb_rst_i(~resetn),

      .wb_master_adr_i(wb_adr_o),
      .wb_master_dat_o(wb_dat_i),
      .wb_master_dat_i(wb_dat_o),
      .wb_master_sel_i(wb_sel_o),
      .wb_master_we_i(wb_we_o),
      .wb_master_cyc_i(wb_cyc_o),
      .wb_master_stb_i(wb_stb_o),
      .wb_master_ack_o(wb_ack_i),
      .wb_master_err_o(wb_err_i),
      .wb_master_rty_o(wb_rty_i),

      // Slave (SRAM)
      .wb_slave0_adr_o(sram_addr),
      .wb_slave0_dat_i(sram_rdata),  // CORRECTED
      .wb_slave0_dat_o(sram_wdata),  // CORRECTED
      .wb_slave0_sel_o(sram_sel),
      .wb_slave0_we_o(sram_we),
      .wb_slave0_cyc_o(sram_cyc),
      .wb_slave0_stb_o(sram_stb),
      .wb_slave0_ack_i(sram_ack),
      .wb_slave0_err_i(1'b0),
      .wb_slave0_rty_i(1'b0)
  );

  sram sram (
      .clk(clk),
      .addr(sram_addr[11:2]),  // 1K words (4KB)
      .wdata(sram_wdata),
      .sel(sram_sel),
      .we(sram_we),
      .cyc(sram_cyc),
      .stb(sram_stb),
      .ack(sram_ack),
      .rdata(sram_rdata)
  );

endmodule
