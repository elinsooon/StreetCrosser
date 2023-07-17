import random
from utility import cross_first_sim, cross_second_sim
import matplotlib.pyplot as plt

NS_CROSS_TIME = 10
EW_CROSS_TIME = 10
NS_BLOCK_TIME = 50  # this value has no implications on the final result, it is constant between both scenarios

NS_LIGHT_TIME = 0
EW_LIGHT_TIME = 0

MIN_GO_TIME = 5


if __name__ == "__main__":
    #random.seed(42)

    val_list = list(range(1, 100))

    cross_first_medians = []
    cross_first_averages = []
    cross_second_medians = []
    cross_second_averages = []
    for i in val_list:
        NS_LIGHT_TIME = i
        EW_LIGHT_TIME = 100 - i
        cfr = cross_first_sim(NS_LIGHT_TIME, EW_LIGHT_TIME, NS_CROSS_TIME, EW_CROSS_TIME, MIN_GO_TIME, NS_BLOCK_TIME)
        csr = cross_second_sim(NS_LIGHT_TIME, EW_LIGHT_TIME, NS_CROSS_TIME, EW_CROSS_TIME, MIN_GO_TIME, NS_BLOCK_TIME)

        cross_first_medians.append(cfr[0])
        cross_first_averages.append(cfr[1])
        cross_second_medians.append(csr[0])
        cross_second_averages.append(csr[1])

    plt.plot(val_list, cross_first_averages, 'r-', label='Cross First Average')
    plt.plot(val_list, cross_first_medians, 'r-.', alpha=0.3, label='Cross First Median')
    plt.plot(val_list, cross_second_averages, 'b-', label='Cross Second Average')
    plt.plot(val_list, cross_second_medians, 'b-.', alpha=0.3, label='Cross Second Median')
    plt.legend(loc='upper center')
    plt.xlabel('NS Light Time as % of Total Light Cycle')
    plt.ylabel('Time (seconds)')

    plt.show()
