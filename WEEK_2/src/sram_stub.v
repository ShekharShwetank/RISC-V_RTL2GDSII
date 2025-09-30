// sram_stub.v - An empty module definition for synthesis (black box)
module sram (
    input clk,
    input [9:0] addr,
    input [31:0] wdata,
    input [3:0] sel,
    input we,
    input cyc,
    input stb,
    output reg ack,
    output reg [31:0] rdata
);
endmodule
