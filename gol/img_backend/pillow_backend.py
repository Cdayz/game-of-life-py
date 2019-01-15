"""
Module wich represent backend for saving states into images using PIL
"""

from typing import Tuple, List

from PIL import Image

State = List[List[int]]
StateSize = Tuple[int, int]
Point = Tuple[int, int]
CellSize = Tuple[int, int]


class ImgBackend:
    """
    Class wich represents low-level image operations as backend to GoL
    """

    __slots__ = ('width', 'height', 'img_path', 'cell_w', 'cell_h',
                 'img_w', 'img_h', 'line_width')

    def __init__(self, size: StateSize,
                 cell_size: CellSize, line_width: int = 1):
        """
        Initialize class and calculate needed values

        :param str img_path: path to image (may be relative)
        :param size: size of state
        :type size: Tuple[int, int]
        :param cell_size: Size of cell on image
        :type cell_size: Tuple[int, int]
        :param int line_width: width of line in pixels
        """
        self.width, self.height = size
        self.cell_w, self.cell_h = cell_size
        self.img_w = (self.cell_w + line_width) * self.width + line_width
        self.img_h = (self.cell_h + line_width) * self.height + line_width
        self.line_width = line_width

    def make_default_structure(self) -> Image:
        """
        Make default structure of image

        :return: Image with cells
        :rtype: `~.Image`
        """
        img_size = (self.img_w, self.img_h)
        image = Image.new('L', img_size, color=255)

        x_step = self.cell_w
        y_step = self.cell_h

        for x_index in range(0, self.img_w, x_step):
            for y_index in range(0, self.img_h, y_step):
                image.putpixel((x_index, y_index), 180)

        for x_index in range(0, self.img_h, x_step):
            for y_index in range(0, self.img_w, y_step):
                image.putpixel((x_index, y_index), 180)

        return image

    def to_image(self, state: State):
        """
        Saves state into image

        :param state: State of the game
        :type state: List[List[int]]

        :return: Image with state represents
        :rtype: `~.Image`
        """
        img = self.make_default_structure()
        if len(state) != self.width or len(state[0]) != self.height:
            raise Exception('State size differ from initial!')

        for x_index in range(self.width):
            for y_index in range(self.height):
                img = self.put_value(img, (x_index, y_index), state)

        return img

    def put_value(self, img: Image, point: Point, state: State) -> Image:
        """
        Insert value into image by state point

        :param img: image object
        :type img: `~.Image`
        :param point: point to state
        :type point: Tuple[int, int]
        :param state: State
        :type state: List[List[int]]

        :return: Image with pixels set
        :rtype: `~.Image`
        """
        x_point, y_point = point
        value = 0 if state[x_point][y_point] else 255

        x_start = (self.cell_h + self.line_width) * x_point + self.line_width
        y_start = (self.cell_w + self.line_width) * y_point + self.line_width


        for x_index in range(x_start, x_start + self.cell_h):
            for y_index in range(y_start, y_start + self.cell_w):
                img.putpixel((y_index, x_index), value)

        return img
