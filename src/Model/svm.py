from sklearn import svm
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    for c in [0.5, 1.0, 2.0, 3.0]:
        clf = svm.SVC(C=c, kernel="linear", tol=1e-4)
        print clf.fit(temp[0], temp[1])
        Pre.Predict(clf, temp1)

    # for c in [0.5, 1.0, 2.0, 3.0]:
    #     clf = svm.LinearSVC(C=c)
    #     print clf.fit(temp[0], temp[1])
    #     Pre.Predict(clf, temp1)
