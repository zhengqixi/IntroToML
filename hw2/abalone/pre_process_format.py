import sys
sexToInt = {
    'M': '0',
    'F': '1',
    'I': '2'
}

positiveClass = set(range(1, 10))
negativeClass = set(range(10, 30))


def preprocess(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        outputList = []
        for line in lines:
            outputLine = []
            data = line.split(',')
            outputClass = 1
            if int(data.pop()) in negativeClass:
                outputClass = -1
            sexClass = sexToInt[data[0]]
            # first point is sex, last point is class
            outputLine.append(str(outputClass))
            outputLine.append("1:" + sexClass)
            for i in range(1, len(data)):
                outputLine.append(str(i+1) + ':' + data[i])
            outputList.append(' '.join(outputLine))
        return outputList


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Please provide input file name")
        sys.exit(-1)
    output = preprocess(args[1])
    for i in output:
        print(i)
