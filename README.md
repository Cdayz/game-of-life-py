# game-of-life-py
Conway Game of Life with Image processing backends

# Example usage
```py
from gol.logics import next_state


state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

state_new = next_state(state)

```

The ```state_new``` variable will be a

```py
state_new = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
```

# Usage of image backends

```py
from gol.img_backend.pillow_backend import ImgBackend

def create_image(state):
    bc = ImgBackend('test.png', (len(state), len(state[0])), (1, 1),
                    line_width=1)
    img = bc.to_image(state)

    img.save(bc.img_path.as_posix())

state = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

create_image(state)

```
Now in ```test.png``` file will be image wich represents that state