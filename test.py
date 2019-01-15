from gol.logics import next_state
from gol.img_backend.pillow_backend import ImgBackend

def create_image(state):
    bc = ImgBackend((len(state), len(state[0])), (1, 1),
                    line_width=1)
    img = bc.to_image(state)

    img.save('test.png')


def create_gif(initial_state, path, frames=10, fps=3):
    state_size = (len(initial_state), len(initial_state[0]))
    cell_size = (1, 1)
    bc = ImgBackend(state_size, cell_size, line_width=1)
    all_states = [initial_state, ]
    state = initial_state
    for _ in range(frames):
        state = next_state(state)
        all_states.append(state)

    images = [bc.to_image(state) for state in all_states]

    images[0].save(path,
                   save_all=True,
                   append_images=images[1:],
                   duration=len(images) / fps,
                   loop=0)


state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

create_gif(state, 'test.gif', fps=50)