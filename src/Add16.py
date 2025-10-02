from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    add16 = Chip(name="Add16")
    add16.chip_io(["a[16]", "b[16]"], ["out[16]"])

    add16.add_function(
        "HalfAdder", 
        ["a", "b"], ["a[0]", "b[0]"], 
        ["sum", "carry"], ["out[0]", "carry0"]
    )
    for i in range(1, 15):
        add16.add_function(
            "FullAdder", 
            ["a", "b", "c"], [f"carry{i-1}", f"a[{i}]", f"b[{i}]"], 
            ["sum", "carry"], [f"out[{i}]", f"carry{i}"]
        )

    add16.add_function(
        "FullAdder", 
        ["a", "b", "c"], [f"carry14", f"a[15]", f"b[15]"], 
        ["sum", "carry"], [f"out[15]", "OF"]
    )


    add16.dump(f"{directory}/Add16.thdl")