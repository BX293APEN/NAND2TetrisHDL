from NAND2Tetris import Chip
import os
if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    
    dmux4way = Chip(name="DMux4Way")
    dmux4way.chip_io(["in", "sel[2]"], ["a", "b", "c", "d"])
    dmux4way.add_function("Not", ["in"], ["sel[0]"], ["out"], ["notsel0"])
    dmux4way.add_function("Not", ["in"], ["sel[1]"], ["out"], ["notsel1"])
    
    dmux4way.add_comment("MSB : sel[1] LSB : sel[0] の順番")
    dmux4way.add_function("And", ["a", "b"], ["notsel1", "notsel0"], ["out"], ["selA"])
    dmux4way.add_function("And", ["a", "b"], ["notsel1", "sel[0]"], ["out"], ["selB"])
    dmux4way.add_function("And", ["a", "b"], ["sel[1]", "notsel0"], ["out"], ["selC"])
    dmux4way.add_function("And", ["a", "b"], ["sel[1]", "sel[0]"], ["out"], ["selD"])

    dmux4way.add_comment("出力をセレクトする")
    dmux4way.add_function("And", ["a", "b"], ["in", "selA"], ["out"], ["a"])
    dmux4way.add_function("And", ["a", "b"], ["in", "selB"], ["out"], ["b"])
    dmux4way.add_function("And", ["a", "b"], ["in", "selC"], ["out"], ["c"])
    dmux4way.add_function("And", ["a", "b"], ["in", "selD"], ["out"], ["d"])

    dmux4way.dump(f"{directory}/DMux4Way.thdl")