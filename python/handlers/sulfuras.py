import sys
sys.path.append('Interfaces')

from handlers import UpdateStrategyInterface

class SulfurasUpdateStrategy(UpdateStrategyInterface):
    def update(self, item) -> None:
        pass
