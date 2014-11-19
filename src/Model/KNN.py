__author__ = 'Administrator'
from sklearn.neighbors import RadiusNeighborsClassifier
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset2.feature")
    clf = RadiusNeighborsClassifier(radius=1.0)
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)
