__author__ = 'Administrator'
from sklearn import tree
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset2.feature")
    clf = tree.DecisionTreeClassifier()
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)
