from classes import Light, Pedestrian
import random
import numpy as np


def forward(time: int, distance: int, light: Light, pedestrian: Pedestrian) -> None:
    for i in range(time):
        light.step_time()
        pedestrian.step_time(distance, 1)


def cross_first_sim(ns_light_time, ew_light_time, ns_cross_time, ew_cross_time, min_go_time, ns_block_time) -> tuple[float, float]:
    # Cross First
    cross_first_results = []
    for i in range(500):
        light = Light(ns_light_time, ew_light_time, random.randint(0, ns_light_time + ew_light_time))
        pedestrian = Pedestrian()

        # Cross EW
        forward(ew_cross_time, 1, light, pedestrian)

        # Walk up block
        forward(ns_block_time, 1, light, pedestrian)

        if light.ns_on and light.ns_time_left >= min_go_time:
            forward(ns_cross_time, 1, light, pedestrian)
        else:
            while not light.ns_on:
                forward(1, 0, light, pedestrian)
            forward(ns_cross_time, 1, light, pedestrian)
        cross_first_results.append(pedestrian.elapsed_time)

        # plt.plot(pedestrian.time_list, pedestrian.distance_list, 'r-', alpha=0.1)
    return float(np.median(cross_first_results)), float(np.average(cross_first_results))


def cross_second_sim(ns_light_time, ew_light_time, ns_cross_time, ew_cross_time, min_go_time, ns_block_time) -> tuple[float, float]:
    # Cross Second
    cross_second_results = []
    for i in range(500):
        light = Light(ns_light_time, ew_light_time, random.randint(0, ns_light_time + ew_light_time))
        pedestrian = Pedestrian()

        # Walk up block
        forward(ns_block_time, 1, light, pedestrian)

        if light.ns_on and light.ns_time_left >= min_go_time:  # NS on and time left
            forward(ns_cross_time, 1, light, pedestrian)
            if light.ew_on and light.ew_time_left >= min_go_time:  # EW on and time left
                forward(ew_cross_time, 1, light, pedestrian)
            else:  # Wait for EW
                while not light.ew_on:
                    forward(1, 0, light, pedestrian)
                forward(ew_cross_time, 1, light, pedestrian)
        else:
            if light.ew_on and light.ew_time_left >= min_go_time:  # EW on and time left
                forward(ew_cross_time, 1, light, pedestrian)
                if light.ns_on and light.ns_time_left >= min_go_time:  # NS on and time left
                    forward(ns_cross_time, 1, light, pedestrian)
                else:  # Wait for NS
                    while not light.ew_on:
                        forward(1, 0, light, pedestrian)
                    forward(ns_cross_time, 1, light, pedestrian)
            else:  # Wait for EW
                while not light.ew_on:
                    forward(1, 0, light, pedestrian)
                forward(ew_cross_time, 1, light, pedestrian)
                if light.ns_on and light.ns_time_left >= min_go_time:  # NS on and time left
                    forward(ns_cross_time, 1, light, pedestrian)
                else:  # Wait for NS
                    while not light.ew_on:
                        forward(1, 0, light, pedestrian)
                    forward(ns_cross_time, 1, light, pedestrian)

        cross_second_results.append(pedestrian.elapsed_time)

    return float(np.median(cross_second_results)), float(np.average(cross_second_results))

