# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self) -> None:
        
        for item in self.items:
            strategy = StrategyContext.get_strategy(item)
            strategy.update(item)

class Item:
    def __init__(self, name, sell_in, quality) -> None:
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

class UpdateStrategyInterface:
    def update(self, item):
        pass

class NormalItemUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality -= 1 if item.quality > 0 else 0
        item.quality -= 1 if item.sell_in < 0 and item.quality > 0 else 0

class AgedBrieUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality += 1 if item.quality < 50 else 0

class SulfurasUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        pass
    
class BackstagePassUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality += 1 if item.quality < 50 else 0
        item.quality += 1 if item.sell_in < 11 and item.quality < 50 else 0
        item.quality += 1 if item.sell_in < 6 and item.quality < 50 else 0
        item.quality = 0 if item.sell_in < 0 else item.quality

class ConjuredUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality -= 2 if item.quality > 0 else 0
        item.quality -= 2 if item.sell_in < 0 and item.quality > 0 else 0
        
class StrategyContext:
    def get_strategy(item):
        if "aged brie" in item.name.lower():
            return AgedBrieUpdateStrategy()
        elif "sulfuras" in item.name.lower():
            return SulfurasUpdateStrategy()
        elif "backstage pass" in item.name.lower():
            return BackstagePassUpdateStrategy()
        elif "conjured" in item.name.lower():
            return ConjuredUpdateStrategy()
        else:
            return NormalItemUpdateStrategy()