import sys
sys.path.append('Interfaces')

from Interfaces import UpdateStrategyInterface

class AgedBrieUpdateStrategy(UpdateStrategyInterface):
    def update(self, item):
        item.sell_in -= 1
        item.quality += 1 if item.quality < 50 else 0
