import sys
sys.path.append('Interfaces')

from handlers import UpdateStrategyInterface

class AgedBrieUpdateStrategy(UpdateStrategyInterface):
    def update(self, item) -> None:
        item.sell_in -= 1
        if item.quality < 50: item.quality += 1 
