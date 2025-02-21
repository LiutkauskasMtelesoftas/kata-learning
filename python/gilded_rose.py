# -*- coding: utf-8 -*-
import sys
sys.path.append('Strategies')
from Strategies.context import StrategyContext

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        
        for item in self.items:
            strategy_context = StrategyContext()
            strategy = strategy_context.get_strategy(item)
            strategy.update(item)

class Item:
    def __init__(self, name, sell_in, quality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

