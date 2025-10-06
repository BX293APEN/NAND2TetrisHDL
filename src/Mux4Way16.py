from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))

    mux4way16 = Chip(name="Mux4Way16")
    mux4way16.chip_io(["a[16]", "b[16]", "c[16]", "d[16]", "sel[2]"], ["out[16]"])
    mux4way16.add_function("Mux16", ["a", "b", "sel"], ["a", "b", "sel[0]"], ["out"], ["ab"])
    mux4way16.add_function("Mux16", ["a", "b", "sel"], ["c", "d", "sel[0]"], ["out"], ["cd"])
    mux4way16.add_function("Mux16", ["a", "b", "sel"], ["ab", "cd", "sel[1]"], ["out"], ["out"])
    mux4way16.dump(f"{directory}/Mux4Way16.thdl")