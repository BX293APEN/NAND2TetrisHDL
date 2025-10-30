from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    ram32k = Chip(name="RAM32K")
    ram32k.chip_io(["in[16]", "load", "address[15]"], ["out[16]"])

    ram32k.add_comment("アクセスするレジスタを決定する")

    
    ram32k.add_function(
        "DMux8Way", 
        [
            "in", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "load", 
            "address[14]", "address[13]", "address[12]",
        ],
        ["a", "b", "c", "d", "e", "f", "g", "h"], 
        ["rl0", "rl1", "rl2", "rl3", "rl4", "rl5", "rl6", "rl7"], 
        
    )

    ram32k.add_function(
        "RAM4K", 
        [
            "in", "load", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "rl", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["rOut"], 
        lsb=0, msb=8, 
        directPin=[
            "in", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        internal=["rl", "rOut"]
    )

    ram32k.add_function(
        "Mux8Way16", 
        [
            "a", "b", "c", "d", "e", "f", "g", "h", 
            "sel[2]", "sel[1]", "sel[0]"
        ], 
        [
            "rOut0", "rOut1", "rOut2", "rOut3", "rOut4", "rOut5", "rOut6", "rOut7", 
            "address[14]", "address[13]", "address[12]",
        ], 
        ["out"], 
        ["out"]
    )

    ram32k.dump(f"{directory}/RAM32K.thdl")