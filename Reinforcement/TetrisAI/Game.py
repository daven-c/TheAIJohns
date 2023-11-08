import pygame as pyg
import numpy as np
from random import choice
from typing import List, Dict


class Block:

    NUM_BLOCKS = 7
    # I, O, T, S, Z, J, and L
    types: Dict = {
        "I": np.array([1, 1, 1, 1]),
        "O": np.array([[1, 1],
                       [1, 1]]),
        "T": np.array([[0, 1, 0],
                       [1, 1, 1]]),
        "S": np.array([[0, 1, 1]
                       [1, 1, 0]]),
        "Z": np.array([[1, 1, 0]
                       [0, 1, 1]]),
        "J": np.array([[0, 0, 1]
                       [1, 1, 1]]),
        "L": np.array([[1, 0, 0],
                       [1, 1, 1]]),
    }

    @staticmethod
    def get_random_type() -> str:
        return choice(Block.types.keys())

    def __init__(self, type: str):
        self.type = type
        self.array = Block.types.get(type)

    def rotate(self):
        self.array = np.rot90(self.array, -1)


class Tetris:

    WIDTH: int = 10  # number of block as the width
    HEIGHT: int = 20  # number of blocks as the height
    GAME_PX_WIDTH: int = 400  # In pixels
    STAT_PX_WIDTH: int = 200  # In pixels
    WINDOW_HEIGHT: int = 800  # In pixels

    def __init__(self, *, name: str = "No Name"):
        # General
        self.name = name

        # Graphics
        self.tile_width = Tetris.GAME_PX_WIDTH // Tetris.WIDTH
        self.tile_height = Tetris.WINDOW_HEIGHT // Tetris.HEIGHT

        # Game Variables
        self.game_array = np.zeros(shape=(Tetris.HEIGHT, Tetris.WIDTH))
        self.points = 0
        self.current_block: Block = None

        self.__initDisplay

    def __initDisplay(self):
        if pyg.display.get_init() is False:
            pyg.init()
            self.game_window = pyg.display.set_mode(
                (Tetris.GAME_PX_WIDTH + Tetris.STAT_PX_WIDTH, Tetris.WINDOW_HEIGHT))
            pyg.display.set_caption(
                f"Tetris {pyg.display.get_window_size()}, {self.width}x{self.width}")
            self.fps = pyg.time.Clock()

    def step(self):
        if self.block_exists is None:
            # Create a new block
            type = Block.get_random_type()
            self.current_block = Block(type)
            self._insert_block(self.current_block)
        else:
            ...
            # Logic for locking in place

            # Check rows for completion

    def _spawn_block(self, block: Block):
        spawn_width = (Tetris.GAME_PX_WIDTH) // 2 - 2 * self.tile_width
        spawn_height = 0

        for i in range(block.array.shape[0]):
            for j in range(block.array.shape[1]):
                self.game_array[i + spawn_width, j +
                                spawn_height] = block.array[i, j]
