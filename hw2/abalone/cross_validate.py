import os
import sys
k_limit = 14
d_limit = 4


def train(trainingdata, n_fold, outputfile):
    command = './svm-train -s 0 -t 1 -q -c {} -d {} -v {} {}'
    with open(outputfile, 'w+') as f:
        f.write('c,d,avg,std\n')
        for k in range(-k_limit, k_limit+1):
            for d in range(1, d_limit+1):
                c = f'{2**k:.20f}'
                print('Running with c={}, d={}'.format(c, d))
                initial_string = '{},{},'.format(c, d)
                f.write(initial_string)
                execute_command = command.format(c, d, n_fold, trainingdata)
                stream = os.popen(execute_command)
                result = stream.read()
                f.write(result)


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 4:
        print("Usage: input file, fold num, outputfile\n")
        sys.exit(-1)
    train(args[1], args[2], args[3])
