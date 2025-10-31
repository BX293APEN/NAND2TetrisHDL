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
    cpu.add_function(
        "Not",
        ["in"],
        ["instruction[15]"],
        ["out"],
        ["instA"]
    )

    cpu.add_function(
        "Not",
        ["in"],
        ["instA"],
        ["out"],
        ["instC"]
    )

    cpu.add_function(
        "Mux16",
        ["a", "b", "sel"], 
        ["instruction", "aluOut", "instC"],
        ["out"],
        ["instOut"]
    )

    cpu.add_function(
        "Or",
        ["a", "b"],
        ["instA", "instruction[5]"],
        ["out"],
        ["aLoad"]
    )

    cpu.add_function( # Aレジスタ
        "ARegister",
        ["in", "load"], 
        ["instOut", "aLoad"],
        ["out", "out[0..14]"],
        ["aROut", "addressM[0..14]"]
    )

    cpu.add_function(
        "And",
        ["a", "b"],
        ["instC", "instruction[4]"],
        ["out"],
        ["dLoad"]
    )

    cpu.add_function( # Dレジスタ
        "DRegister",
        ["in", "load"], 
        ["aluOut", "dLoad"],
        ["out"],
        ["dOut"]
    )

    cpu.add_function(
        "Mux16",
        ["a", "b", "sel"], 
        ["aROut", "inM", "instruction[12]"],
        ["out"],
        ["amOut"]
    )

    cpu.add_function(
        "ALU",
        [
            "x", "y", 
            "zx", "nx", "zy", 
            "ny", "f", "no"
        ], 
        [
            "dOut", "amOut", 
            "instruction[11]", "instruction[10]", "instruction[9]", 
            "instruction[8]", "instruction[7]", "instruction[6]"
        ],
        ["out", "out", "zr", "ng"],
        ["aluOut", "outM", "zr", "ng"]
    )

    cpu.add_function(
        "And",
        ["a", "b"], 
        ["instruction[3]", "instC"],
        ["out"],
        ["writeM"]
    )


    cpu.add_comment("プログラムカウンタ処理")

    cpu.add_function( # ng処理
        "And",
        ["a", "b"],
        ["ng", "instruction[2]"],
        ["out"],
        ["ngJmp"]
    )

    cpu.add_function( # zr処理
        "And",
        ["a", "b"],
        ["zr", "instruction[1]"],
        ["out"],
        ["zrJmp"]
    )

    cpu.add_function(
        "Or",
        ["a", "b"],
        ["ng", "zr"],
        ["out"],
        ["lezero"]
    )

    cpu.add_function(
        "Not",
        ["in"],
        ["lezero"],
        ["out"],
        ["gtzero"]
    )

    cpu.add_function( # 0より大きい処理
        "And",
        ["a", "b"],
        ["gtzero", "instruction[0]"],
        ["out"],
        ["gtJmp"]
    )

    cpu.add_function(
        "Or",
        ["a", "b"],
        ["ngJmp", "zrJmp"],
        ["out"],
        ["ngzrJmp"]
    )

    cpu.add_function(
        "Or",
        ["a", "b"],
        ["ngzrJmp", "gtJmp"],
        ["out"],
        ["jmp"]
    )

    cpu.add_function(
        "And",
        ["a", "b"],
        ["jmp", "instC"],
        ["out"],
        ["pcLoad"]
    )

    cpu.add_function(
        "Not",
        ["in"],
        ["pcLoad"],
        ["out"],
        ["pcInc"]
    )

    cpu.add_function(
        "PC",
        ["in", "load", "inc", "reset"], 
        ["aROut", "pcLoad", "pcInc", "reset"],
        ["out[0..14]", "out[15]"],
        ["pc[0..14]", "pcsp"]
    )

    cpu.dump(f"{directory}/CPU.thdl")