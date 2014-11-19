from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import MultinomialNB
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre

if __name__ == "__main__":
    temp = FE.ExtractFeatureFile("../../ins/data/dataset1.feature")
    temp1 = FE.ExtractFeatureFile("../../ins/data/dataset2.feature")
    clf = GaussianNB()
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)

    clf = BernoulliNB()
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)

    clf = MultinomialNB()
    print clf.fit(temp[0], temp[1])
    Pre.Predict(clf, temp1)