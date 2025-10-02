from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    inc16 = Chip(name="Inc16")
    inc16.chip_io(["in[16]"], ["out[16]"])


    inc16.add_function(
        "HalfAdder", 
        ["a", "b"], ["in[0]", "true"], 
        ["sum", "carry"], ["out[0]", "carry0"]
    )
    for i in range(1, 15):
        inc16.add_function(
            "HalfAdder", 
            ["a", "b"], [f"carry{i-1}", f"in[{i}]"], 
            ["sum", "carry"], [f"out[{i}]", f"carry{i}"]
        )

    inc16.add_function(
        "HalfAdder", 
        ["a", "b"], [f"carry14", f"in[15]"], 
        ["sum", "carry"], [f"out[15]", "OF"]
    )


    inc16.dump(f"{directory}/Inc16.thdl")