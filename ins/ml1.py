__author__ = 'Administrator'


def ExtractFeature(inputFile, outputFile):
    items = open(inputFile, "r").read().split("\n")
    wr = open(outputFile, "w")
    for item in items:
        s = ConvertFeature(item)
        if s:
            wr.write(s + "\n")

def ConvertFeature(item):
    s = []
    tokens = item.split("\t")
    if len(tokens) != 3:
        return
    s.append(tokens[0])
    s.append(tokens[1])
    s.append(str(float(tokens[0])/float(tokens[1])))
    s.append(str(float(tokens[1])/float(tokens[0])))
    s.append(str(float(tokens[1])/(float(tokens[0])**2/10000)))
    s.append(str(float(tokens[1])*float(tokens[0])))
    ss = " ".join(s)
    if tokens[2].lower() == "f":
        return "1 " + ss
    else:
        return "0 " + ss


if __name__ == "__main__":
    ExtractFeature("./data/dataset2.txt","./data/dataset2.feature" )