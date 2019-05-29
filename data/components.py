# Each class - is component
# Calculation function returns massive of x-values like [x-min, x-mid, x-max]
# Calculation formula specified in (   ) inside list comprehension [    ]
# Do not change statement in list comprehension! *for x in values.values()


class Ra_J5_JFS:
    @staticmethod
    def calculations(values, dot):
        # sensor calibration values
        seb_output = 2.00662
        capacity = 200
        el_gain = 132.83
        offset = 35.433
        # sensor calibration values
        gain = float(capacity/(seb_output/1000*el_gain))
        y = [float(gain*(x/2 ** dot) - offset) for x in values.values()]
        return sorted(y)


class RA_L1_PINCHSENSOR:
    @staticmethod
    def calculations(values, dot):
        y = [float(x/2**dot * 2) for x in values.values()]
        return sorted(y)


class RA_L2_PINCHSENSOR:
    @staticmethod
    def calculations(values, dot):
        y = [float(x/2**dot * 2) for x in values.values()]
        return sorted(y)


class SA_J1_BVS:
    @staticmethod
    def calculations(values, dot):
        gain = 78.1
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)
