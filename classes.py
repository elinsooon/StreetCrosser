

class Light:
    ns_time: int
    ns_time_left: int
    ns_on: bool
    ew_time: int
    ew_time_left: int
    ew_on: bool
    cycle_length: int
    cycle_start: int

    def __init__(self, ns_time: int, ew_time: int, cycle_start: int):
        self.ns_time = ns_time
        self.ew_time = ew_time
        self.cycle_length = self.ns_time + self.ew_time
        self.cycle_start = cycle_start

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
            if self.ns_time_left == 0:
                self.ns_on = False
                self.ew_on = True
                self.ew_time_left = self.ew_time
            else:
                self.ns_time_left -= 1
        else:
            if self.ew_time_left == 0:
                self.ew_on = False
                self.ns_on = True
                self.ns_time_left = self.ns_time
            else:
                self.ew_time_left -= 1


class Pedestrian:
    elapsed_time: int

    def __init__(self):
        self.elapsed_time = 0
