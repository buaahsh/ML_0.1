__author__ = 'Administrator'


def Predict(model, testDataset):
    result = model.predict(testDataset[0])
    m = 0
    for i,j in zip(result, testDataset[1]):
        if i == j:
            m += 1
    print "Acc:", m*1.0/len(testDataset[1])
