from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    fullAdder = Chip(name="FullAdder")
    fullAdder.chip_io(["a", "b", "c"], ["sum", "carry"])

    fullAdder.add_function(
        "HalfAdder", 
        ["a", "b"], ["a", "b"], 
        ["sum", "carry"], ["sumAB", "carryAB"]
    )

    fullAdder.add_function(
        "HalfAdder", 
        ["a", "b"], ["sumAB", "c"], 
        ["sum", "carry"], 
        ["sum", "carryABC"]
    )

    fullAdder.add_function("Or", ["a", "b"], ["carryAB", "carryABC"], ["out"], ["carry"])

    fullAdder.dump(f"{directory}/FullAdder.thdl")