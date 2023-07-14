import random
from utility import forward, cross_first_sim, cross_second_sim
from collections import Counter
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

    cross_first_results = []
    cross_second_results = []
    for i in val_list:
        NS_LIGHT_TIME = i
        EW_LIGHT_TIME = 100 - i
        cross_first_results.append(cross_first_sim(NS_LIGHT_TIME, EW_LIGHT_TIME, NS_CROSS_TIME, EW_CROSS_TIME, MIN_GO_TIME, NS_BLOCK_TIME))
        cross_second_results.append(cross_second_sim(NS_LIGHT_TIME, EW_LIGHT_TIME, NS_CROSS_TIME, EW_CROSS_TIME, MIN_GO_TIME, NS_BLOCK_TIME))

    plt.plot(val_list, cross_first_results, 'r-')
    plt.plot(val_list, cross_second_results, 'b-')

    plt.show()
