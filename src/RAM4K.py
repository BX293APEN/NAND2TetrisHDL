from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    ram4k = Chip(name="RAM4K")
    ram4k.chip_io(["in[16]", "load", "address[12]"], ["out[16]"])

    ram4k.add_comment("アクセスするレジスタを決定する")

    
    ram4k.add_function(
        "DMux8Way", 
        [
            "in", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "true", 
            "address[11]", "address[10]", "address[9]",
        ],
        ["a", "b", "c", "d", "e", "f", "g", "h"], 
        ["rl0", "rl1", "rl2", "rl3", "rl4", "rl5", "rl6", "rl7"], 
        
    )

    ram4k.add_function(
        "And",
        ["a", "b"],
        ["rl", "load"],
        ["out"],
        ["rLoad"],
        lsb=0, msb=8, 
        directPin=["load"],
        internal=["rLoad" ,"rl"]
    )

    ram4k.add_function(
        "RAM512", 
        [
            "in", "load", 
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "rLoad", 
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["rOut"], 
        lsb=0, msb=8, 
        directPin=[
            "in", 
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        internal=["rLoad", "rOut"]
    )

    ram4k.add_function(
        "Mux8Way16", 
        [
            "a", "b", "c", "d", "e", "f", "g", "h", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "rOut0", "rOut1", "rOut2", "rOut3", "rOut4", "rOut5", "rOut6", "rOut7", 
            "address[11]", "address[10]", "address[9]",
        ], 
        ["out"], 
        ["out"]
    )

    ram4k.dump(f"{directory}/RAM4K.thdl")