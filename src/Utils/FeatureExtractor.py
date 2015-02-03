__author__ = 'Administrator'


def ExtractFeatureFile(inputFile, isFloat=True, labelHead=True):
    """
    extract features and labels for model
    :param inputFile:
    :param isFloat:
    :return: [features, labels]
    """
    items = open(inputFile, "r").read().split("\n")
    features = []
    labels = []
    for item in items:
        tokens = item.split(" ")
        if labelHead:
            labels.append(int(tokens[0]))
            if isFloat:
                features.append([float(i) for i in tokens[1:]])
            else:
                features.append([int(i) for i in tokens[1:]])
        else:
            labels.append(int(tokens[-1]))
            if isFloat:
                features.append([float(i) for i in tokens[:-1]])
            else:
                features.append([int(i) for i in tokens[:-1]])
    return [features, labels]


def ExtractFeatureFilForRegression(inputFile, splitStr=" "):
    """
    extract features and labels for model
    :param inputFile:
    :param isFloat:
    :return: [features, labels]
    """
    items = open(inputFile, "r").read().split("\n")
    features = []
    labels = []
    sId = []
    for item in items:
        if item == "":
            continue
        tokens = item.split(splitStr)
        sId.append(tokens[-1])
        labels.append(float(tokens[-2]))
        features.append([float(i) for i in tokens[:-2]])
    return [features, labels, sId]