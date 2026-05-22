#!/usr/bin/python
# -*- coding: utf-8 -*-


class GameClass:
    def __init__(self):
        self.sequence = (1, 2, 3, 2, 1, 3, 1, 3, 2, 3, 2, 1, 3, 2, 1, 2)
        self.sequence_index = 0
        self.sequence_length = len(self.sequence)

    def get_item(self):
        return self.sequence[self.sequence_index]

    def get_item_index(self):
        return self.sequence_index

    def get_next_item(self):
        if self.sequence_index+1 == self.sequence_length:
            self.sequence_index = 0
            return None
        self.sequence_index += 1
        return self.get_item()

    def get_items_count(self):
        return self.sequence_length

    def reset(self):
        self.sequence_index = 0

