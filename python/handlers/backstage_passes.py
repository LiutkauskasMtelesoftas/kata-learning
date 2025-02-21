import sys
sys.path.append('Interfaces')

from handlers import UpdateStrategyInterface

class BackstagePassesUpdateStrategy(UpdateStrategyInterface):
    def update(self, item) -> None:
        item.sell_in -= 1
        if item.quality < 50: item.quality += 1 
        if item.sell_in < 11 and item.quality < 50: item.quality += 1
        if item.sell_in < 6 and item.quality < 50: item.quality += 1
        if item.sell_in < 0: item.quality = 0 
