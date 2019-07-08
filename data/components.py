# Each class - is component
# Calculation function returns massive of x-values like [x-min, x-mid, x-max]
# Calculation formula specified in (   ) inside list comprehension [    ]
# Do not change statement in list comprehension! *for x in values.values()
import numpy as np


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


class SA_J1_BCS:
    @staticmethod
    def calculations(values, dot):
        gain = 1.672
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J2_BVS:
    @staticmethod
    def calculations(values, dot):
        gain = 78.1
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J2_BCS:
    @staticmethod
    def calculations(values, dot):
        gain = 1.672
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J3_BVS:
    @staticmethod
    def calculations(values, dot):
        gain = 78.1
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J3_BCS:
    @staticmethod
    def calculations(values, dot):
        gain = 1.672
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J4_BVS:
    @staticmethod
    def calculations(values, dot):
        gain = 50.05
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class SA_J4_BCS:
    @staticmethod
    def calculations(values, dot):
        gain = 1.114
        y = [float(gain*x/2**dot) for x in values.values()]
        return sorted(y)


class RA_J5_MPS_SECONDARY:
    # y = gear_ratio * x * pi/3 [rad] / numer of pole pairs
    # gear_ratio: (1/(4.125*4.4)) * 0.01528 / 2 [m/rad]
    @staticmethod
    def calculations(values, dot):
        gear_ratio = (1/(4.125*4.4)) * 0.01528 / 2
        pole_pairs = 2
        y = [float(gear_ratio*x*np.pi/3/pole_pairs) for x in values.values()]
        return sorted(y)


class RA_J6_MPS_SECONDARY:
    # y = gear_ratio * x * pi/3 [rad] / numer of pole pairs
    # gear_ratio: (1/29.16)*(-1/4.25) [rad/rad]
    @staticmethod
    def calculations(values, dot):
        gear_ratio = (1/29.16)*(-1/4.25)
        pole_pairs = 1
        y = [float(gear_ratio*x*np.pi/3/pole_pairs) for x in values.values()]
        return sorted(y)


class IDU_A0_MCS:
    # q=(x / 0.0077) * (1.0 / 29.16)
    @staticmethod
    def calculations(values, dot):
        y = [float(((x/2**dot)*6.0363/1.647) * 29.16*0.0077) for x in values.values()]
        return sorted(y)