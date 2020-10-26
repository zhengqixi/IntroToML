import matplotlib
import matplotlib.pyplot as plt
import pandas


def selection(input_file, save_file=None, show=False):
    data = pandas.read_csv(input_file)
    c_value = data['c'].drop_duplicates()
    min_d = min(data['d'])
    max_d = max(data['d'])
    split_by_d_avg = [data[data['d'] == x][['avg']]
                      for x in range(min_d, max_d+1)]
    split_by_d_std = [data[data['d'] == x]['std']
                      for x in range(min_d, max_d + 1)]
    fig, axs = plt.subplots(2, sharex=True)
    fig.suptitle('Cross Validation Error')
    # Plot the avg
    for d, avg in enumerate(split_by_d_avg, start=min_d):
        axs[0].plot(c_value, avg, label=d)
    # plot the std
    for d, std in enumerate(split_by_d_std, start=min_d):
        axs[1].plot(c_value, std, label=d)
    plt.xlabel('c')
    axs[0].set(title='Avg')
    axs[0].set_xscale('log', base=2)
    axs[1].set(title='Std')
    axs[0].legend(loc='best', ncol=2, shadow=True, title='d =')
    axs[1].legend(loc='best', ncol=2, shadow=True, title='d =')
    if save_file is not None:
        plt.savefig(save_file)
    if show:
        plt.show()
    plt.close()


def best_pair_plot(input_file, save_file=None, show=False):
    data = pandas.read_csv(input_file)
    c = data['c'][0]
    fig, axs = plt.subplots(2, sharex=True)
    plt.xlabel('d')
    fig.suptitle('SVM Results for C={}'.format(c))
    axs[0].plot(data['d'], data['test-error'], label='Test Error')
    axs[0].plot(data['d'], data['validation-error'],
                label='Cross Validation Error')
    axs[0].legend(loc='best', ncol=2, shadow=True)
    axs[0].set(title='Errors')
    axs[1].plot(data['d'], data['svs'])
    axs[1].set(title='# Support Vectors')
    if save_file is not None:
        plt.savefig(save_file)
    if show:
        plt.show()
    plt.close()


selection('crossValidate.csv', 'crossValidate', True)
best_pair_plot('./models/result.csv', './models/results', True)
