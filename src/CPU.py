from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    cpu = Chip(name="CPU")
    cpu.chip_io(
        [
            "inM[16]", 
            "instruction[16]", 
            "reset"
        ], 
        [
            "outM[16]",
            "writeM",
            "addressM[15]",
            "pc[15]"
        ]
    )

    cpu.add_comment("CPUを作る")

    cpu.add_function(
        "Mux16",
        ["a", "b", "sel"], 
        ["instruction", "aluOut", "instruction[15]"]
        ["out"]
        ["instOut"]
    )

    cpu.add_function( # Aレジスタ
        "Register",
        ["in", "load"], 
        ["instOut", ""]
        ["out"]
        ["aROut"]
    )

    cpu.add_function(
        "Mux16",
        ["a", "b", "sel"], 
        ["aROut", "inM", ""]
        ["out"]
        ["amOut"]
    )

    cpu.add_function(
        "ALU",
        ["x", "y", "zx", "nx", "zy", "ny", "f", "no"], 
        ["dOut", "amOut", ""]
        ["out"]
        ["aluOut"]
    )

    cpu.add_function(
        "PC",
        ["in", "load", "inc", "reset"], 
        ["", "", "", "reset"]
        ["out"]
        ["pc"]
    )

    cpu.dump(f"{directory}/CPU.thdl")