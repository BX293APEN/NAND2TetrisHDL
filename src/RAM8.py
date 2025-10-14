from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    ram8 = Chip(name="RAM8")
    ram8.chip_io(["in[16]", "load", "address[3]"], ["out[16]"])
    
    ram8.add_function(
        "DMux8Way", 
        ["in", "sel"], 
        ["true", "address"],
        ["a", "b", "c", "d", "e", "f", "g", "h"], 
        ["rl0", "rl1", "rl2", "rl3", "rl4", "rl5", "rl6", "rl7"], 
        
    )
    ram8.add_function(
        "Register", 
        ["in", "load"], 
        ["in", "rLoad"],
        ["out"], 
        ["rOut"],
        lsb=0, msb=8, 
        directPin=["in"],
        internal=["rLoad" ,"rOut"]
    )

    ram8.add_function(
        "Mux8Way16", 
        ["a", "b", "c", "d", "e", "f", "g", "h", "sel"], 
        ["rOut0", "rOut1", "rOut2", "rOut3", "rOut4", "rOut5", "rOut6", "rOut7", "address"], 
        ["out"], 
        ["out"]
    )
    

    ram8.dump(f"{directory}/RAM8.thdl")