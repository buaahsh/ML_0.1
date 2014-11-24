from sklearn.ensemble import RandomForestClassifier
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.v1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset1.v1.feature")
    for c in xrange(5, 20):
        clf = RandomForestClassifier(n_estimators=c)
        print clf.fit(temp[0], temp[1])
        Pre.Predict(clf, temp1)

