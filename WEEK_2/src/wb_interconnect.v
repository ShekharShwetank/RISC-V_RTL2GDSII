// SPDX-License-Identifier: ISC
/*
 * Wishbone Interconnect (1 Master, 1 Slave)
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

module wb_interconnect (
    // Wishbone master interface
    input           wb_clk_i,
    input           wb_rst_i,
    input  [31:0]   wb_master_adr_i,
    output [31:0]   wb_master_dat_o,
    input  [31:0]   wb_master_dat_i,
    input  [3:0]    wb_master_sel_i,
    input           wb_master_we_i,
    input           wb_master_cyc_i,
    input           wb_master_stb_i,
    output          wb_master_ack_o,
    output          wb_master_err_o,
    output          wb_master_rty_o,

    // Wishbone slave interface (SRAM)
    output [31:0]   wb_slave0_adr_o,
    output [31:0]   wb_slave0_dat_o,
    input  [31:0]   wb_slave0_dat_i,
    output [3:0]    wb_slave0_sel_o,
    output          wb_slave0_we_o,
    output          wb_slave0_cyc_o,
    output          wb_slave0_stb_o,
    input           wb_slave0_ack_i,
    input           wb_slave0_err_i,
    input           wb_slave0_rty_i
);

    // Simple 1-to-1 connection
    assign wb_slave0_adr_o = wb_master_adr_i;
    assign wb_master_dat_o = wb_slave0_dat_i;
    assign wb_slave0_dat_o = wb_master_dat_i;
    assign wb_slave0_sel_o = wb_master_sel_i;
    assign wb_slave0_we_o = wb_master_we_i;
    assign wb_slave0_cyc_o = wb_master_cyc_i;
    assign wb_slave0_stb_o = wb_master_stb_i;
    assign wb_master_ack_o = wb_slave0_ack_i;
    assign wb_master_err_o = wb_slave0_err_i;
    assign wb_master_rty_o = wb_slave0_rty_i;

endmodule
