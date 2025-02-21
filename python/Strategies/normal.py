import sys
sys.path.append('Interfaces')

from Interfaces import UpdateStrategyInterface

class NormalItemUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality -= 1 if item.quality > 0 else 0
        item.quality -= 1 if item.sell_in < 0 and item.quality > 0 else 0