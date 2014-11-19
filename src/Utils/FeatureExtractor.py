__author__ = 'Administrator'


def ExtractFeatureFile(inputFile, isFloat=True):
    items = open(inputFile, "r").read().split("\n")
    features = []
    labels = []
    for item in items:
        tokens = item.split(" ")
        labels.append(int(tokens[0]))
        if isFloat:
            features.append([float(i) for i in tokens[1:]])
        else:
            features.append([int(i) for i in tokens[1:]])
    return [features, labels]
