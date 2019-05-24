from general.core import Component


class Ra_J5_JFS:
    seb_output = 2.00662
    capacity = 200
    el_gain = 132.83
    offset = 35.433

    def calculations(self, values, dot):
        gain = float(self.capacity/(self.seb_output/1000*self.el_gain))
        y = [float(gain*(x/2 ** dot) - self.offset) for x in values.values()]
        return sorted(y)

class RA_L1_PINCHSENSOR:

    def calculations(self, values, dot):
        y = [float(x/2**dot * 2) for x in values.values()]
        return sorted(y)


def get_all_components():
    import sys, inspect
    class_list = [obj.__name__ for name, obj in inspect.getmembers(sys.modules[__name__])[1:] if inspect.isclass(obj)]
    class_list.append('Not selected')
    return sorted(class_list)


