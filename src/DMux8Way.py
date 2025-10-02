from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    dmux8way = Chip(name="DMux8Way")
    dmux8way.chip_io(["in", "sel[3]"], ["a", "b", "c", "d", "e", "f", "g", "h"])
    dmux8way.add_function("Not", ["in"], ["sel[0]"], ["out"], ["notsel0"])
    dmux8way.add_function("Not", ["in"], ["sel[1]"], ["out"], ["notsel1"])
    dmux8way.add_function("Not", ["in"], ["sel[2]"], ["out"], ["notsel2"])
    
    dmux8way.add_comment("MSB : sel[2] LSB : sel[0] の順番")

    dmux8way.add_function("And", ["a", "b"], ["notsel1", "notsel0"], ["out"], ["sel00"])
    dmux8way.add_function("And", ["a", "b"], ["notsel1", "sel[0]"], ["out"], ["sel01"])
    dmux8way.add_function("And", ["a", "b"], ["sel[1]", "notsel0"], ["out"], ["sel10"])
    dmux8way.add_function("And", ["a", "b"], ["sel[1]", "sel[0]"], ["out"], ["sel11"])

    dmux8way.add_function("And", ["a", "b"], ["notsel2", "sel00"], ["out"], ["selA"])
    dmux8way.add_function("And", ["a", "b"], ["notsel2", "sel01"], ["out"], ["selB"])
    dmux8way.add_function("And", ["a", "b"], ["notsel2", "sel10"], ["out"], ["selC"])
    dmux8way.add_function("And", ["a", "b"], ["notsel2", "sel11"], ["out"], ["selD"])
    dmux8way.add_function("And", ["a", "b"], ["sel[2]", "sel00"], ["out"], ["selE"])
    dmux8way.add_function("And", ["a", "b"], ["sel[2]", "sel01"], ["out"], ["selF"])
    dmux8way.add_function("And", ["a", "b"], ["sel[2]", "sel10"], ["out"], ["selG"])
    dmux8way.add_function("And", ["a", "b"], ["sel[2]", "sel11"], ["out"], ["selH"])

    dmux8way.add_comment("出力をセレクトする")
    dmux8way.add_function("And", ["a", "b"], ["in", "selA"], ["out"], ["a"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selB"], ["out"], ["b"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selC"], ["out"], ["c"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selD"], ["out"], ["d"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selE"], ["out"], ["e"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selF"], ["out"], ["f"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selG"], ["out"], ["g"])
    dmux8way.add_function("And", ["a", "b"], ["in", "selH"], ["out"], ["h"])

    dmux8way.dump(f"{directory}/DMux8Way.thdl")