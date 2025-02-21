import sys
sys.path.append('Interfaces')

from Interfaces import UpdateStrategyInterface

class BackstagePassesUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality += 1 if item.quality < 50 else 0
        item.quality += 1 if item.sell_in < 11 and item.quality < 50 else 0
        item.quality += 1 if item.sell_in < 6 and item.quality < 50 else 0
        item.quality = 0 if item.sell_in < 0 else item.quality