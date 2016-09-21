#!/usr/bin/python
# -*- coding: utf-8 -*-


class GameClass:
    def __init__(self):
        self.sequence = (1, 1, 1, 2, 3, 2, 1, 3, 2, 1, 2, 2, 3)
        self.sequence_index = 0
        self.sequence_length = len(self.sequence)

    def get_item(self):
        return self.sequence[self.sequence_index]

    def get_next_item(self):
        self.sequence_index += 1
        if self.sequence_index == self.sequence_length + 1:
            return None
        return self.get_item()
