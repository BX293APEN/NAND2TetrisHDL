from NAND2Tetris import Chip
import os

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    andChip = Chip(name="Or8Way")
    andChip.chip_io(["in[8]"], ["out"])
    maxBit = 8
    b = 0
    flag = 0
    state = 0
    lastB = maxBit
    while True:
        abit = b + state
        bbit = lastB  - b - 1 + state
        if abit < bbit:
            if flag == 0:
                andChip.add_function("Or", ["a", "b"], [f"in[{abit}]", f"in[{bbit}]"], ["out"], [f"w{abit}"])
            else:
                andChip.add_function("Or", ["a", "b"], [f"w{abit}", f"w{bbit}"], ["out"], [f"w{abit + lastB}"])
            b += 1
        else:
            if flag == 0:
                flag = 1
            else:
                state += b*2
            lastB = b
            if lastB == 0:
                andChip.add_function("Or", ["a", "b"], [f"w{state}", f"w{state}"], ["out"], [f"out"])
                break
            b = 0

    andChip.dump(f"{directory}/Or8Way.thdl")