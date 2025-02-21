# -*- coding: utf-8 -*-
from strategy_context import StrategyContext

class GildedRose(object):

    def __init__(self, items, strategy_context=None) -> None:
        self.items = items
        self.strategy_context = strategy_context or StrategyContext()

    def update_quality(self) -> None:
        
        for item in self.items:
            strategy = self.strategy_context.get_strategy(item)
            strategy.update(item)

class Item:
    def __init__(self, name, sell_in, quality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

