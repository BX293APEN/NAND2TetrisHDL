from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    ram16k = Chip(name="RAM16K")
    ram16k.chip_io(["in[16]", "load", "address[14]"], ["out[16]"])

    ram16k.add_comment("アクセスするレジスタを決定する")

    
    ram16k.add_function(
        "DMux4Way", 
        [
            "in", 
            "sel[1]", "sel[0]"
        ], 
        [
            "true", 
            "address[13]", "address[12]",
        ],
        ["a", "b", "c", "d"], 
        ["rl0", "rl1", "rl2", "rl3"], 
        
    )

    ram16k.add_function(
        "And",
        ["a", "b"],
        ["rl", "load"],
        ["out"],
        ["rLoad"],
        lsb=0, msb=4, 
        directPin=["load"],
        internal=["rLoad" ,"rl"]
    )

    ram16k.add_function(
        "RAM4K", 
        [
            "in", "load", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "rLoad", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["rOut"], 
        lsb=0, msb=4, 
        directPin=[
            "in", 
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        internal=["rLoad", "rOut"]
    )

    ram16k.add_function(
        "Mux4Way16", 
        [
            "a", "b", "c", "d",
            "sel[1]", "sel[0]"
        ], 
        [
            "rOut0", "rOut1", "rOut2", "rOut3", 
            "address[13]", "address[12]",
        ], 
        ["out"], 
        ["out"]
    )

    ram16k.dump(f"{directory}/RAM16K.thdl")