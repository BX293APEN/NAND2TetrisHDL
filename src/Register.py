from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))

    register = Chip(name="Register")
    register.chip_io(["in[16]", "load"], ["out[16]"])
    register.add_function(
        "Bit", 
        ["in", "load"], ["in", "load"], 
        ["out"], ["out"], 
        lsb=0, msb=16, 
        directPin=["load"]
    )
    register.dump(f"{directory}/Register.thdl")