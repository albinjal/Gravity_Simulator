import imageio
from typing import List
from Newton import SpaceImage, Body
import sys


def create_gif(name: str, images: List[str]):
    with imageio.get_writer(name, mode='I') as writer:
        for filename in images:
            image = imageio.imread(filename)
            writer.append_data(image)
    return name


def simulate(space: SpaceImage, time_for_frame: int, frames: int, gif_name: str, axises):
    images = []
    for frame in range(frames):
        images.append(space.save('frames/sim_frame_%d.png' % frame, axises, frame * time_for_frame))
        sys.stdout.write("\r%d%%" % int(frame * 100 / frames))
        sys.stdout.flush()
        for i in range(time_for_frame):
            space.next_image(1)
    create_gif('gifs/%s.gif' % gif_name, images)
    sys.stdout.write("\r100%")


def save_indata(name, bodies: List[Body], frames, seconds_frame):
    f = open('indata/%s.txt' % name, 'w+')
    f.write('Name: %s, Frames: %i, Seconds/Frame: %i' % (name, frames, seconds_frame))
    for body in bodies:
        f.write(body.disp())
    f.close()
    print('Input-data saved to indata/%s.txt' % name)


if __name__ == "__main__":
    # Example data
    # mars = Body('Mars', [0, -3700000], 10 ** 23, [3000, 0], 8474200, [0, 0], [0, 0])
    earth = Body('Earth', [0.0, 0.0], 6 * 10 ** 24, [0, 0], 12742000, [0, 0], [0, 0])
    moon = Body('Moon', [0, 369671 * 1000], 7.3 * 10 ** 22, [1082, 0], 3474200, [0, 0], [0, 0])
    init_image = SpaceImage([earth, moon])
    axises = [-420000000, 420000000.0, -420000000.0, 420000000.0]
    seconds_frame = 60 * 60
    frames = 685
    gif_name = input('simulation name: ')
    save_indata(gif_name, [earth, moon], frames, seconds_frame)
    simulate(init_image, seconds_frame, frames, gif_name, axises)
    print('\nSimulation saved to gifs/%s.gif' % gif_name)
