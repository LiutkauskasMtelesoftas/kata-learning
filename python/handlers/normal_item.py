import sys
sys.path.append('Interfaces')

from handlers import UpdateStrategyInterface

class NormalItemUpdateStrategy(UpdateStrategyInterface):
    def update(self, item) -> None:
        item.sell_in -= 1
        if item.quality > 0: item.quality -= 1
        if item.sell_in < 0 and item.quality > 0: item.quality -= 1 
