# -*- coding:utf-8 -*-


class FeatureExtractor:

    def __init__(self):
        self.__trainNum = 538

    def ExtractGrade(self, inputFile, num):
        """
        :param inputFile:
        :param num:
        :return: dict {id : [1_g, 2_g, 3_g]}
        """
        items = open(inputFile, "r").read().split("\n")
        d = {}
        for item in items[1:]:
            tokens = map(lambda x: int(x), item.strip().split("\t"))
            if tokens[1] not in d:
                d[tokens[1]] = [0, 0, 0]
            d[tokens[1]][tokens[0]-1] = 1.0 * tokens[2] / num
        return d

    def ExtractLib(self, inputFile):
        items = open(inputFile, "r").read().split("\n")
        # items = map(lambda x:"\t".join(x.split("\t")[:-1]), items[1:])
        # items = set(items)
        d = {}
        for item in items[1:]:
            tokens = map(lambda x: int(x), item.strip().split("\t"))
            if tokens[1] not in d:
                d[tokens[1]] = [0, 0, 0]
            d[tokens[1]][tokens[0]-1] += 1
        return d

    def ExtractFile(self, gradeFile, libFile, outputFile):
        g_feature = self.ExtractGrade(gradeFile, self.__trainNum)
        l_feature = self.ExtractLib(libFile)
        wr = open(outputFile, "w")
        for item in g_feature:
            print item
            g = "\t".join(map(lambda x: str(x), g_feature[item]))
            if item not in l_feature:
                l = "\t".join(["0", "0", "0"])
            else:
                l = "\t".join(map(lambda x: str(x), l_feature[item]))
            wr.write(l+"\t"+g+"\t"+str(item)+"\n")

        wr.close()

if __name__ == "__main__":
    fe = FeatureExtractor()
    gradeFile = "data/test_grade.txt"
    libFile = "data/test_lib.txt"
    outputFile = "data/test_out_2.f"
    train_gradeFile = "data/train/grade.txt"
    train_libFile = "data/train/lib.txt"
    train_outputFile = "data/train/train_out_2.f"
    # fe.ExtractFile(train_gradeFile, train_libFile, train_outputFile)
    fe.ExtractFile(gradeFile, libFile, outputFile)

