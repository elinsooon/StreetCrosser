import copy

INTER_LIGHT_TIME = 6


class Pedestrian:
    elapsed_time: int
    distance_covered: int
    time_list: list[int]
    distance_list: list[int]

    def __init__(self):
        self.elapsed_time = 0
        self.distance_covered = 0
        self.time_list = [0]
        self.distance_list = [0]

    def step_time(self, distance_step: int, time_step: int = 1) -> None:
        self.elapsed_time += time_step
        self.distance_covered += distance_step
        for i in range(time_step):
            self.time_list.append(self.time_list[len(self.time_list) - 1] + 1)
            self.distance_list.append(self.distance_list[len(self.distance_list) - 1] + distance_step)


class Light:
    ns_time: int
    ns_time_left: int
    ns_on: bool
    ew_time: int
    ew_time_left: int
    ew_on: bool
    cycle_length: int
    cycle_start: int
    green_gap: int

    def __init__(self, ns_time: int, ew_time: int, cycle_start: int):
        self.ns_time = ns_time
        self.ew_time = ew_time
        self.cycle_length = self.ns_time + self.ew_time
        self.cycle_start = cycle_start
        self.green_gap = copy.copy(INTER_LIGHT_TIME)

        if self.cycle_start <= self.ns_time:
            self.ns_on = True
            self.ns_time_left = self.ns_time - self.cycle_start

            self.ew_on = False
            self.ew_time_left = 0
        else:
            self.ns_on = False
            self.ns_time_left = 0

            self.ew_on = True
            self.ew_time_left = self.cycle_length - self.cycle_start

    def step_time(self) -> None:
        if self.ns_on:
            if self.ns_time_left == 0 and self.green_gap != 0:
                self.green_gap -= 1
            elif self.ns_time_left == 0:
                self.ns_on = False
                self.ew_time_left = self.ew_time
                self.ew_on = True
                self.green_gap = copy.copy(INTER_LIGHT_TIME)

            else:
                self.ns_time_left -= 1
        else:
            if self.ew_time_left == 0 and self.green_gap != 0:
                self.green_gap -= 1
            elif self.ew_time_left == 0:
                self.ew_on = False
                self.ns_time_left = self.ns_time
                self.ns_on = True
                self.green_gap = copy.copy(INTER_LIGHT_TIME)

            else:
                self.ew_time_left -= 1
