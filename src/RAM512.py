from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    ram512 = Chip(name="RAM512")
    ram512.chip_io(["in[16]", "load", "address[9]"], ["out[16]"])

    ram512.add_comment("アクセスするレジスタを決定する")

    
    ram512.add_function(
        "DMux8Way", 
        [
            "in", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "true", 
            "address[8]", "address[7]", "address[6]"
        ],
        ["a", "b", "c", "d", "e", "f", "g", "h"], 
        ["rl0", "rl1", "rl2", "rl3", "rl4", "rl5", "rl6", "rl7"], 
        
    )

    ram512.add_function(
        "And",
        ["a", "b"],
        ["rl", "load"],
        ["out"],
        ["rLoad"],
        lsb=0, msb=8, 
        directPin=["load"],
        internal=["rLoad" ,"rl"]
    )

    ram512.add_function(
        "RAM64", 
        [
            "in", "load", 
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "rLoad", 
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["rOut"], 
        lsb=0, msb=8, 
        directPin=[
            "in", 
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]"
        ],
        internal=["rLoad", "rOut"]
    )

    ram512.add_function(
        "Mux8Way16", 
        [
            "a", "b", "c", "d", "e", "f", "g", "h", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "rOut0", "rOut1", "rOut2", "rOut3", "rOut4", "rOut5", "rOut6", "rOut7", 
            "address[8]", "address[7]", "address[6]"
        ], 
        ["out"], 
        ["out"]
    )

    ram512.dump(f"{directory}/RAM512.thdl")