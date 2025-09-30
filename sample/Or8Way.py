class Chip:
    def __init__(self, name, bit=1, debug = False):
        self.name       = name
        if bit >1:
            self.bit    = f"{bit}"
        else:
            self.bit    = ""
        self.inputs     = []
        self.outputs    = []
        self.parts      = []

        self.debug      = debug

    def chip_io(self, wireInput=[], wireOutput=[]):
        self.inputs     = wireInput
        self.outputs    = wireOutput

    def add_comment(self, message):
        self.parts.append(f"// {message}")

    def add_function(
        self, 
        chipName, 
        inputChip       = [], inputWire     = [], 
        outChip         = [], outWire       = [],
        lsb             = 0, msb            = 0,
        internal        = [],
        directPin       = []
    ):
        if (msb - lsb) == 0:
            args        = []
            for inputPair in zip(inputChip, inputWire):
                args.append(f"{inputPair[0]}={inputPair[1]}")
            
            for outPair in zip(outChip, outWire):
                args.append(f"{outPair[0]}={outPair[1]}")

            self.parts.append(f"{chipName}({", ".join(args)});")
            if self.debug:
                print(f"{chipName}({", ".join(args)});")
        
        else:
            for b in range(lsb, msb, 1):
                args    = []
                for inputPair in zip(inputChip, inputWire):
                    if inputPair[1] in internal:
                        args.append(f"{inputPair[0]}={inputPair[1]}{b}")
                    elif inputPair[1] in directPin:
                        args.append(f"{inputPair[0]}={inputPair[1]}")
                    else:
                        args.append(f"{inputPair[0]}={inputPair[1]}[{b}]")
                
                for outPair in zip(outChip, outWire):
                    if outPair[1] in internal:
                        args.append(f"{outPair[0]}={outPair[1]}{b}")
                    elif outPair[1] in directPin:
                        args.append(f"{outPair[0]}={outPair[1]}")
                    else:
                        args.append(f"{outPair[0]}={outPair[1]}[{b}]")

                self.parts.append(f"{chipName}({", ".join(args)});")

    def dump(self, path):
        hdlData = f"""// {self.name} CHIP
CHIP {self.name}{self.bit} {{
    IN {', '.join(self.inputs)};
    OUT {', '.join(self.outputs)};
    PARTS:
        {"\n        ".join(self.parts)}
}}"""
        
        with open(path, "w", encoding="UTF-8") as f:
            f.write(hdlData)

if __name__ == "__main__":
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

    andChip.dump("Or8Way.thdl")