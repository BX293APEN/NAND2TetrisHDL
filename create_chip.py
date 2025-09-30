class Chip:
    def __init__(self, name, bit=1):
        self.name = name
        if bit >1:
            self.bit = f"{bit}"
        else:
            self.bit = ""
        self.inputs = []
        self.outputs = []
        self.parts = []

    def chip_io(self, wireInput=[], wireOutput=[]):
        self.inputs = wireInput
        self.outputs = wireOutput

    def add_function(
        self, 
        chipName, 
        inputChip = [], inputWire =[], 
        outChip = [], outWire = [],
        lsb = 0, msb = 0,
        internal = []
    ):
        if (msb - lsb) == 0:
            args = []
            for inputPair in zip(inputChip, inputWire):
                args.append(f"{inputPair[0]}={inputPair[1]}")
            
            for outPair in zip(outChip, outWire):
                args.append(f"{outPair[0]}={outPair[1]}")

            self.parts.append(f"{chipName}({", ".join(args)});")
        
        else:
            for b in range(lsb, msb, 1):
                args = []
                for inputPair in zip(inputChip, inputWire):
                    if inputPair[1] in internal:
                        args.append(f"{inputPair[0]}={inputPair[1]}{b}")
                    else:
                        args.append(f"{inputPair[0]}={inputPair[1]}[{b}]")
                
                for outPair in zip(outChip, outWire):
                    if outPair[1] in internal:
                        args.append(f"{outPair[0]}={outPair[1]}{b}")
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
    andChip = Chip(name="Or", bit=16)
    andChip.chip_io(["a[16]", "b[16]"], ["out[16]"])
    andChip.add_function("Or", ["a", "b"], ["a", "b"], ["out"], ["out"], 0, 16)
    andChip.dump("Or16.thdl")