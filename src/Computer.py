from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))

    computer = Chip(name="Computer")
    computer.chip_io(["reset"], [])

    computer.add_comment("コンピュータ")
    computer.add_function(
        "ROM32K", 
        ["address"],
        ["pc"], 
        ["out"], 
        ["instruction"],
    )
    computer.add_function(
        "CPU", 
        [
            "inM", 
            "instruction", 
            "reset"
        ],
        [
            "inM", 
            "instruction",
            "reset"
        ], 
        [
            "outM",
            "writeM",
            "addressM",
            "pc"
        ],
        [
            "outM",
            "writeM",
            "addressM",
            "pc"
        ],
    )

    computer.add_function(
        "Memory", 
        ["in", "load", "address"], 
        ["outM", "writeM", "addressM"],
        ["out"], 
        ["inM"],
    )

    computer.dump(f"{directory}/Computer.thdl")