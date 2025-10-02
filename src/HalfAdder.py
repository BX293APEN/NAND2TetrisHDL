from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    halfAdder = Chip(name="HalfAdder")
    halfAdder.chip_io(["a", "b"], ["sum", "carry"])
    halfAdder.add_function("Xor", ["a", "b"], ["a", "b"], ["out"], ["sum"])
    halfAdder.add_function("And", ["a", "b"], ["a", "b"], ["out"], ["carry"])

    halfAdder.dump(f"{directory}/HalfAdder.thdl")