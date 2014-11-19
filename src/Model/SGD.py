from sklearn.linear_model import SGDClassifier
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset2.feature")
    clf = SGDClassifier(loss="hinge", penalty="l2")
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)

