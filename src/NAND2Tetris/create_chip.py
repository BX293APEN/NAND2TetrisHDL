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

    def dump(self, path, mode = "w"):
        hdlData = f"""// {self.name} CHIP
CHIP {self.name}{self.bit} {{
    IN {', '.join(self.inputs)};
    OUT {', '.join(self.outputs)};
    PARTS:
        {"\n        ".join(self.parts)}
}}"""
        
        with open(path, mode, encoding="UTF-8") as f:
            f.write(hdlData)


if __name__ == "__main__":
    andChip = Chip(name="Mux4Way16")
    andChip.chip_io(["a[16]", "b[16]", "c[16]", "d[16]", "sel[2]"], ["out[16]"])
    andChip.add_function("Not", ["in"], ["sel[0]"], ["out"], ["notsel0"])
    andChip.add_function("Not", ["in"], ["sel[1]"], ["out"], ["notsel1"])
    andChip.add_comment("MSB : sel[1] LSB : sel[0] の順番")
    andChip.add_function("And", ["a", "b"], ["notsel1", "notsel0"], ["out"], ["selA"])
    andChip.add_function("And", ["a", "b"], ["notsel1", "sel[0]"], ["out"], ["selB"])
    andChip.add_function("And", ["a", "b"], ["sel[1]", "notsel0"], ["out"], ["selC"])
    andChip.add_function("And", ["a", "b"], ["sel[1]", "sel[0]"], ["out"], ["selD"])

    andChip.add_comment("チップをセレクトする")
    andChip.add_function("And", ["a", "b"], ["a", "selA"], ["out"], ["aVal"], lsb=0, msb=16, directPin=["selA"], internal=["aVal"])
    andChip.add_function("And", ["a", "b"], ["b", "selB"], ["out"], ["bVal"], lsb=0, msb=16, directPin=["selB"], internal=["bVal"])
    andChip.add_function("And", ["a", "b"], ["c", "selC"], ["out"], ["cVal"], lsb=0, msb=16, directPin=["selC"], internal=["cVal"])
    andChip.add_function("And", ["a", "b"], ["d", "selD"], ["out"], ["dVal"], lsb=0, msb=16, directPin=["selD"], internal=["dVal"])
    
    andChip.add_comment("結果の合成")
    andChip.add_function("Or", ["a", "b"], ["aVal", "bVal"], ["out"], ["abVal"], lsb=0, msb=16, internal=["aVal", "bVal", "abVal"])
    andChip.add_function("Or", ["a", "b"], ["cVal", "dVal"], ["out"], ["cdVal"], lsb=0, msb=16, internal=["cVal", "dVal", "cdVal"])
    andChip.add_function("Or", ["a", "b"], ["abVal", "cdVal"], ["out"], ["out"], lsb=0, msb=16, internal=["abVal", "cdVal"])
    andChip.dump("Mux4Way16.thdl")
