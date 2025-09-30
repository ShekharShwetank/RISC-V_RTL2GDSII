// SPDX-License-Identifier: ISC
/*
 * SoC Testbench
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

module soc_tb;

  reg clk;
  reg resetn;

  soc soc_i (
      .clk(clk),
      .resetn(resetn)
  );

  initial begin
    $dumpfile("waveforms/soc_tb.vcd");
    $dumpvars(0, soc_tb);

    clk = 0;
    forever #5 clk = ~clk;
  end

  initial begin
    resetn = 0;
    #20
    resetn = 1;

    #50000
    $finish;
  end

endmodule
