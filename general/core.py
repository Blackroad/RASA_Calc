class Component:

    @staticmethod
    def get_width_variable(width, signed):
        variable_max = 2 ** (width - 1) - 1
        if signed is True:
            variable_min = -2 ** (width - 1)
            return {'x_max': variable_max, 'x_mid': 0, 'x_min': variable_min}
        elif signed is False:
            variable_middle = int(variable_max / 2)
            return {'x_max': variable_max, 'x_mid': variable_middle, 'x_min': 0}
