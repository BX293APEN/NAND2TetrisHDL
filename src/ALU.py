from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    alu = Chip(name="ALU")
    alu.chip_io(
        [
            "x[16]", "y[16]", 
            "zx", "nx", "zy", "ny", "f",  
            "no"
        ], 
        ["out[16]", "zr", "ng"]
    )

    alu.add_comment("zx : 1 → xを0にする")
    #alu.add_function(
    #    "Mux", 
    #    ["a", "b", "sel"], ["x", "false", "zx"], 
    #    ["out"], ["xzx"],
    #    lsb = 0, msb=16,
    #    internal=["xzx"],
    #    directPin=["false", "zx"]
    #)
    alu.add_function(
        "Not",
        ["in"], ["zx"], 
        ["out"], ["nzx"]
    )

    alu.add_function(
        "And", 
        ["a", "b"], ["x", "nzx"], 
        ["out"], ["xzx"],
        lsb = 0, msb=16,
        internal=["xzx"],
        directPin=["nzx"]
    )

    alu.add_comment("nx : 1 → xを反転する")
    alu.add_function(
        "Xor", 
        ["a", "b"], ["xzx", "nx"], 
        ["out"], ["xVal"],
        lsb = 0, msb=16,
        internal=["xzx", "xVal"],
        directPin=["nx"]
    )

    alu.add_comment("zy : 1 → yを0にする")
    #alu.add_function(
    #    "Mux", 
    #    ["a", "b", "sel"], ["y", "false", "zy"], 
    #    ["out"], ["yzy"],
    #    lsb = 0, msb=16,
    #    internal=["yzy"],
    #    directPin=["false", "zy"]
    #)
    alu.add_function(
        "Not",
        ["in"], ["zy"], 
        ["out"], ["nzy"]
    )

    alu.add_function(
        "And", 
        ["a", "b"], ["y", "nzy"], 
        ["out"], ["yzy"],
        lsb = 0, msb=16,
        internal=["yzy"],
        directPin=["nzy"]
    )

    alu.add_comment("nx : 1 → xを反転する")
    alu.add_function(
        "Xor", 
        ["a", "b"], ["yzy", "ny"], 
        ["out"], ["yVal"],
        lsb = 0, msb=16,
        internal=["yzy", "yVal"],
        directPin=["ny"]
    )

    alu.add_comment("半加算回路で全ビット計算")
    alu.add_function(
        "HalfAdder", 
        ["a", "b"], ["xVal", "yVal"], 
        ["sum", "carry"], ["bitSumXY", "bitCarryXY"],
        lsb = 0, msb=16,
        internal=["xVal", "yVal", "bitSumXY", "bitCarryXY"]
    )

    alu.add_function(
        "And", 
        ["a", "b"], ["bitSumXY0", "bitSumXY0"], 
        ["out"], ["sum0"],
    )

    alu.add_function(
        "And", 
        ["a", "b"], ["bitCarryXY0", "bitCarryXY0"], 
        ["out"], ["carry0"],
    )


    for i in range(1, 16):
        alu.add_function(
            "HalfAdder", 
            ["a", "b"], [f"bitSumXY{i}", f"carry{i-1}"], 
            ["sum", "carry"], [f"sum{i}", f"carryXYC{i}"]
        )

        alu.add_function(
            "Or", ["a", "b"], 
            [f"bitCarryXY{i}", f"carryXYC{i}"], 
            ["out"], [f"carry{i}"]
        )
    
    alu.add_comment("f : 1 → sumN  0 : → bitCarryXYN")
    
    alu.add_function(
        "Mux", 
        ["a", "b", "sel"], ["bitCarryXY", "sum", "f"], 
        ["out"], ["calcVal"],
        lsb = 0, msb=16,
        internal=["bitCarryXY", "sum", "calcVal"],
        directPin=["f"]
    )

    alu.add_comment("no : 1 → calcValを反転する")
    alu.add_function(
        "Xor", 
        ["a", "b"], ["calcVal", "no"], 
        ["out"], ["outVal"],
        lsb = 0, msb=16,
        internal=["calcVal", "outVal"],
        directPin=["no"]
    )

    alu.add_comment("ngフラグ生成")

    alu.add_function(
        "And", 
        ["a", "b"], ["outVal15", "outVal15"], 
        ["out"], ["ng"]
    )


    alu.add_comment("zrフラグ生成")

    maxBit = 16
    b = 0
    flag = 0
    state = 0
    lastB = maxBit
    while True:
        abit = b + state
        bbit = lastB  - b - 1 + state
        if abit < bbit:
            if flag == 0:
                alu.add_function("Or", ["a", "b"], [f"outVal{abit}", f"outVal{bbit}"], ["out"], [f"zrVal{abit}"])
            else:
                alu.add_function("Or", ["a", "b"], [f"zrVal{abit}", f"zrVal{bbit}"], ["out"], [f"zrVal{abit + lastB}"])
            b += 1
        else:
            if flag == 0:
                flag = 1
            else:
                state += b*2
            lastB = b
            if lastB == 0:
                alu.add_function("Not", ["in"], [f"zrVal{state}"], ["out"], ["zr"])
                break
            b = 0
    
    alu.add_comment("出力生成")

    alu.add_function(
        "Not", 
        ["in"], ["outVal"], 
        ["out"], ["notOutVal"],
        lsb = 0, msb=16,
        internal=["outVal", "notOutVal"],
    )

    alu.add_function(
        "Not", 
        ["in"], ["notOutVal"], 
        ["out"], ["out"],
        lsb = 0, msb=16,
        internal=["notOutVal"],
    )

    alu.dump(f"{directory}/ALU.thdl")