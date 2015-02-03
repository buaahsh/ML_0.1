__author__ = 'Administrator'


def Predict(model, testDataset):
    result = model.predict(testDataset[0])
    m = 0
    for i,j in zip(result, testDataset[1]):
        if i == j:
            m += 1
    print "Acc:", m*1.0/len(testDataset[1])


def PredictFile(model, testDataSet, outputFile):
    result = model.predict(testDataSet[0])
    temp = zip(testDataSet[2], result)
    temp = sorted(temp, key=lambda pair: pair[1], reverse=False)
    wr = open(outputFile, "w")
    for index, item in enumerate(temp):
        wr.write(item[0] + "," + str(index+1) + "\n")
    wr.close()


