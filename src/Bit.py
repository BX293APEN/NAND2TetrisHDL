from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))

    bit = Chip(name="Bit")
    bit.chip_io(["in", "load"], ["out"])
    bit.add_function("Mux", ["a", "b", "sel"], ["in1", "in", "load"], ["out"], ["outVal"])
    bit.add_function("DFF", ["in"], ["outVal"], ["out"], ["in1"])
    bit.add_function("And", ["a", "b"], ["in1", "in1"], ["out"], ["out"])
    bit.dump(f"{directory}/Bit.thdl")