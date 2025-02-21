import sys
sys.path.append('Interfaces')

from handlers import UpdateStrategyInterface

class ConjuredUpdateStrategy(UpdateStrategyInterface):
    def update(self, item) -> None:
        item.sell_in -= 1
        if item.quality >= 2 :item.quality -= 2
        elif item.quality == 1: item.quality -= 1
        if item.sell_in < 0 and item.quality >=2:  item.quality -=2 
        elif item.sell_in < 0 and item.quality == 1: item.quality -= 1
