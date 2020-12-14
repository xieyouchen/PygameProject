import pygame

from Settings import *

from pygame.math import Vector2
from pygame.rect import Rect
from pygame.sprite import AbstractGroup
from typing import Union


class BaseBlock():
    def __init__(self, id: str, text: bool, passable: bool, moveable: bool, controllable: bool, location: Vector2, texture: str):
        """
        :param id: 每个关卡方块的唯一编号
        :param text: 方块是否是语法方块
        :param passable: 方块是否能被穿过
        :param moveable: 方块是否可以移动
        :param controllable: 方块是否可以被控制
        :param location: 方块的初始位置
        :param texture: 方块的贴图
        """

        self._id = id
        self._text = text
        self._passable = passable
        self._moveable = moveable
        self._controllable = controllable
        self.location = location
        self.texture = pygame.image.load(texture)
        # self.rect = self.texture.get_rect()
        # self.rect.top, self.rect.bottom = self.location.x, self.location.y
        # self.location = Vector2(int(self.rect.centerx), int(self.rect.centery))
        self.rect = Rect(self.location.x, self.location.y, CELL_SIZE_X, CELL_SIZE_Y)

    def is_pass(self) -> bool:
        """
        :return: 返回方块是否可以被穿过
        """

        return self._passable

    def is_move(self) -> bool:
        """
        :return: 返回方块是否可以移动
        """

        return self._moveable

    def is_control(self) -> bool:
        """
        :return: 返回方块是否可以被控制
        """

        return self._controllable
