from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))

    pc = Chip(name="PC")
    pc.chip_io(["in[16]", "load", "inc", "reset"], ["out[16]"])

    pc.add_comment("値を変更するか決める")
    pc.add_function(
        "Or", 
        ["a", "b"],
        ["load", "inc"], 
        ["out"], 
        ["li"],
    )
    pc.add_function(
        "Or", 
        ["a", "b"],
        ["li", "reset"], 
        ["out"], 
        ["change"],
    )

    pc.add_function(
        "Add16", 
        ["a", "b[1..15]", "b[0]"], 
        ["rOut", "false", "inc"],
        ["out"], 
        ["counter"],
    )

    pc.add_function(
        "Mux16", 
        ["a", "b", "sel"], 
        ["counter", "in", "load"],
        ["out"], 
        ["ri"],
    )

    pc.add_function(
        "Mux16", 
        ["a", "b[0..15]", "sel"], 
        ["ri", "false", "reset"],
        ["out"], 
        ["inReset"],
    )
    
    pc.add_function(
        "Register", 
        ["in", "load"], 
        ["inReset", "change"],
        ["out", "out"], 
        ["rOut", "out"],
    )


    pc.dump(f"{directory}/PC.thdl")