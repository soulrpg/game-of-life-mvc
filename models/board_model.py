from .abstract_model import AbstractModel


class BoardModel(AbstractModel):
    def __init__(self):
        super().__init__()
        self.__cells = []
        self.__simulation_running = False
        
    def change_simulation_state(self):
        self.__simulation_running = not self.__simulation_running


    def modify(self, *args, **kwargs):
        self.notify()


    def notify(self):
        for obs in self._obs_list.values():
            obs.update(self)


    def add_cell(self, cell):
        self.__cells.append(cell)


    @property
    def cells(self):
        return self.__cells
        
        
    @property
    def simulation_running(self):
        return self.__simulation_running
