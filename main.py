import random
from classes import Light, Pedestrian, Environment
from utility import forward
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

NS_CROSS_TIME = 10
EW_CROSS_TIME = 10
NS_BLOCK_TIME = 60

NS_LIGHT_TIME = 35
EW_LIGHT_TIME = 25
LIGHT_TIME = NS_LIGHT_TIME + EW_LIGHT_TIME

MIN_GO_TIME = 5


if __name__ == "__main__":
    #random.seed(42)

    # Cross First
    cross_first_results = []
    for i in range(1000):
        light = Light(NS_LIGHT_TIME, EW_LIGHT_TIME, random.randint(0, LIGHT_TIME))
        pedestrian = Pedestrian()
        env = Environment(light, pedestrian)

        # Cross EW
        forward(EW_CROSS_TIME, 1, light, pedestrian)

        # Walk up block
        forward(NS_BLOCK_TIME, 1, light, pedestrian)

        if light.ns_on and light.ns_time_left >= MIN_GO_TIME:
            forward(NS_CROSS_TIME, 1, light, pedestrian)
        else:
            while not light.ns_on:
                forward(1, 0, light, pedestrian)
            forward(NS_CROSS_TIME, 1, light, pedestrian)
        cross_first_results.append(pedestrian.elapsed_time)

        plt.plot(pedestrian.time_list, pedestrian.distance_list, 'r-', alpha=0.1)
    #plt.show()

    # Cross Second
    cross_second_results = []
    for i in range(1000):
        light = Light(NS_LIGHT_TIME, EW_LIGHT_TIME, random.randint(0, LIGHT_TIME))
        pedestrian = Pedestrian()

        # Walk up block
        forward(NS_BLOCK_TIME, 1, light, pedestrian)

        if light.ns_on and light.ns_time_left >= MIN_GO_TIME:  # NS on and time left
            forward(NS_CROSS_TIME, 1, light, pedestrian)
            if light.ew_on and light.ew_time_left >= MIN_GO_TIME:  # EW on and time left
                forward(EW_CROSS_TIME, 1, light, pedestrian)
            else:  # Wait for EW
                while not light.ew_on:
                    forward(1, 0, light, pedestrian)
                forward(EW_CROSS_TIME, 1, light, pedestrian)
        else:
            if light.ew_on and light.ew_time_left >= MIN_GO_TIME:  # EW on and time left
                forward(EW_CROSS_TIME, 1, light, pedestrian)
                if light.ns_on and light.ns_time_left >= MIN_GO_TIME:  # NS on and time left
                    forward(NS_CROSS_TIME, 1, light, pedestrian)
                else:  # Wait for NS
                    while not light.ew_on:
                        forward(1, 0, light, pedestrian)
                    forward(NS_CROSS_TIME, 1, light, pedestrian)
            else:  # Wait for EW
                while not light.ew_on:
                    forward(1, 0, light, pedestrian)
                forward(EW_CROSS_TIME, 1, light, pedestrian)
                if light.ns_on and light.ns_time_left >= MIN_GO_TIME:  # NS on and time left
                    forward(NS_CROSS_TIME, 1, light, pedestrian)
                else:  # Wait for NS
                    while not light.ew_on:
                        forward(1, 0, light, pedestrian)
                    forward(NS_CROSS_TIME, 1, light, pedestrian)

        cross_second_results.append(pedestrian.elapsed_time)

        plt.plot(pedestrian.time_list, pedestrian.distance_list, 'b-', alpha=0.1)

    first_results = Counter(cross_first_results)
    print(first_results)
    print(np.average(cross_first_results))
    print(np.median(cross_first_results))
    second_results = Counter(cross_second_results)
    print(second_results)
    print(np.average(cross_second_results))
    print(np.median(cross_second_results))

    plt.show()




    # first_results = Counter(cross_first_results)
    # print(first_results)
    #
    # second_results = Counter(cross_second_results)
    # print(second_results)
    #
    # lists1 = sorted(first_results.items())
    # lists2 = sorted(second_results.items())
    #
    # x1, y1 = zip(*lists1)
    # x2, y2 = zip(*lists2)
    #
    # fig, axs = plt.subplots(1, 2)
    # axs[0].plot(x1, y1)
    # axs[1].plot(x2, y2)
    # plt.show()



