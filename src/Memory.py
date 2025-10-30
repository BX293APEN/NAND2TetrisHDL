from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    memory = Chip(name="Memory")
    memory.chip_io(["in[16]", "load", "address[15]"], ["out[16]"])

    memory.add_comment("アクセスするレジスタを決定する")

    memory.add_function(
        "DMux",
        ["in", "sel"],
        ["true", "address[14]"],
        ["a", "b"],
        ["rl", "ml"]
    )

    memory.add_function(
        "DMux",
        ["in", "sel"],
        ["ml", "address[13]"],
        ["a", "b"],
        ["sl", "kl"]
    )

    memory.add_function(
        "And",
        ["a", "b"],
        ["rl", "load"],
        ["out"],
        ["rLoad"]
    )


    memory.add_function(
        "RAM16K", 
        [
            "in", "load", 
            "address[13]", "address[12]",
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "rLoad", 
            "address[13]", "address[12]",
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["rOut"], 
    )

    memory.add_function(
        "And",
        ["a", "b"],
        ["sl", "load"],
        ["out"],
        ["scLoad"]
    )

    memory.add_function(
        "Screen", 
        [
            "in", "load", 
            "address[12]",
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ], 
        [
            "in", "scLoad", 
            "address[12]",
            "address[11]", "address[10]", "address[9]",
            "address[8]", "address[7]", "address[6]",
            "address[5]", "address[4]", "address[3]",
            "address[2]", "address[1]", "address[0]",
        ],
        ["out"], 
        ["scOut"], 
    )

    memory.add_function(
        "Keyboard", 
        [], 
        [],
        ["out"], 
        ["keyOut"], 
    )

    memory.add_function(
        "Mux4Way16", 
        [
            "a", "b", "c", "d",
            "sel[1]", "sel[0]"
        ], 
        [
            "rOut", "rOut", "scOut", "keyOut", 
            "address[14]", "address[13]",
        ], 
        ["out"], 
        ["out"]
    )

    memory.dump(f"{directory}/Memory.thdl")