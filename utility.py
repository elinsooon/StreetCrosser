from classes import Light, Pedestrian, Environment


def forward(time: int, distance: int, light: Light, pedestrian: Pedestrian) -> None:
    for i in range(time):
        #env.step_time(distance)
        light.step_time()
        pedestrian.step_time(distance, 1)
