from sklearn.linear_model import LogisticRegression
import src.Utils.FeatureExtractor as FE
import src.Utils.Predict as Pre


if __name__ == "__main__":
    featureFile = "data/train/train_out_2.f"
    outputFile = "data/train/test_out_2.cvs"
    lr = LogisticRegression()
    temp = FE.ExtractFeatureFilForRegression(featureFile, "\t")
    temp1 = FE.ExtractFeatureFilForRegression("data/test_out_2.f", "\t")
    print lr.fit(temp[0], temp[1])
    Pre.PredictFile(lr, temp1, outputFile)