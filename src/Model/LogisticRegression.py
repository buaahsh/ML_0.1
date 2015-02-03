from sklearn.linear_model import LogisticRegression
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre


if __name__ == "__main__":
    lr = LogisticRegression()
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset2.feature")
    clf = GaussianNB()
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)
    lr.fit()