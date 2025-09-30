// SPDX-License-Identifier: ISC
/*
 * Simple Behavioral SRAM Model (with Combinatorial Read)
 *
 * Copyright (C) 2021  VSD-PLL Team
 */

`timescale 1 ns / 1 ps

module sram (
    input clk,
    input [9:0] addr,
    input [31:0] wdata,
    input [3:0] sel,
    input we,
    input cyc,
    input stb,
    output reg ack,          // Changed to reg for procedural assignment
    output [31:0] rdata      // wire output driven combinationally
);

    reg [31:0] mem [0:1023]; // Memory array

    // Initialize memory from hex file
    initial begin
      $readmemh("/home/ank/Desktop/SoC_Shwetank/WEEK_2/firmware_ver_2_generated.hex", mem);
      $display("SRAM INFO: firmware_ver_2_generated.hex loaded at simulation time %0t.", $time);
      $display("SRAM INFO: Value at address 0x0 is: %h", mem[0]);
    end

    // Synchronous Write Logic
    always @(posedge clk) begin
        if (cyc && stb && we) begin
            if (sel[0]) mem[addr][7:0]   <= wdata[7:0];
            if (sel[1]) mem[addr][15:8]  <= wdata[15:8];
            if (sel[2]) mem[addr][23:16] <= wdata[23:16];
            if (sel[3]) mem[addr][31:24] <= wdata[31:24];
        end
    end

    // Synchronous Ack Logic: pulse ack while cyc and stb are high
    always @(posedge clk) begin
        if (cyc && stb)
            ack <= 1'b1;
        else
            ack <= 1'b0;
    end

    // Combinatorial Read Logic
    assign rdata = mem[addr];

endmodule

