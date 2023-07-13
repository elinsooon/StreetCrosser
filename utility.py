from classes import Light, Pedestrian


def forward(amount: int, light: Light, pedestrian: Pedestrian) -> None:
    for i in range(amount):
        pedestrian.elapsed_time += 1
        light.step_time()
