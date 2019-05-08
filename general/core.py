class Component:
    def __init__(self, dot: int, width: int, signed: bool):
        self.dot = dot
        self.width = width
        self.signed = signed

    def get_width_variable(self):
        variable_max = 2 ** (self.width - 1) - 1
        variable_middle = None
        variable_min = None
        if self.signed  is True:
            variable_middle = 0
            variable_min = -2 ** (self.width - 1)
        elif self.signed is False:
            variable_middle = int(variable_max / 2)
            variable_min = 0
        return variable_max, variable_middle, variable_min
