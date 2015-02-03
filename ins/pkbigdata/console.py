__author__ = 'Administrator'


def test(fileName):
    reader = open(fileName, "r")
    d = {}
    for line in reader:
        tokens = line.split("\t")
        if tokens[0] == "1":
            d[tokens[1]] = int(tokens[2])
        else:
            d[tokens[1]] += int(tokens[2])

    d = sorted(d.iteritems(), key=lambda d:d[1])
    wr = open("data/test_out.csv", "w")
    index = 1
    for item in d:
        print item[0], index

        wr.write(item[0]+","+str(index)+"\n")
        index += 1
    print d


if __name__ == "__main__":
    test("data/test_grade.txt")