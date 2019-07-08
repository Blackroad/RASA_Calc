class SA_J1_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 78.1
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 78.1
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("SA_J1_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))




class SA_J1_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.672
        x = x/2**12
        y = gain * x
        return y


class SA_J2_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.672
        x = x/2**12
        y = gain * x
        return y

class SA_J2_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 78.1
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 78.1
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("SA_J2_BVS\n "
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


class SA_J3_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.672
        x = x/2**12
        y = gain * x
        return y


class SA_J3_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 78.1
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 78.1
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("SA_J3_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


class SA_J4_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.114
        x = x/2**12
        y = gain * x
        return y

class SA_J4_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 50.05
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 50.05
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("SA_J4_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


class RA_J1_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.114
        x = x/2**12
        y = gain * x
        return y

class RA_J1_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 50.05
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 50.05
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("RA_J1_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


class RA_J2_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.114
        x = x/2**12
        y = gain * x
        return y

class RA_J2_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 50.05
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 50.05
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("RA_J2_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


class RA_J5_BCS:
    @staticmethod
    def calculations(x):
        gain = 1.114
        x = x/2**12
        y = gain * x
        return y

class RA_J5_BVS:
    @staticmethod
    def calculations_Y(x):
        gain = 50.05
        x = x / 2 ** 12
        y = gain * x
        return y

    @staticmethod
    def calculation_X(y, resistance):
        gain = 50.05
        x1 = round(y * resistance) - 1
        x2 = round(y * resistance) + 1
        x_converted1 = round(x1 * 4095/gain)
        x_converted2 = round(x2 * 4095/gain)
        print("RA_J5_BVS\n"
              "Ubrake(min)  = {0},  Ubrake(min converted) = {2}\n"
              "Ubrake (max) = {1},  Ubrake(max converted) = {3}\n ".format(x1, x2, x_converted1, x_converted2))


SA_J1_BVS().calculation_X(1.672, 34.6)
SA_J1_BVS().calculation_X(1.672, 20.6)

SA_J2_BVS().calculation_X(1.672, 31.5)
SA_J2_BVS().calculation_X(1.672, 18.7)

SA_J3_BVS().calculation_X(1.672, 40.8)
SA_J3_BVS().calculation_X(1.672, 24.2)

print(SA_J4_BCS().calculations(1700))
SA_J4_BVS().calculation_X(0.5, 87)
SA_J4_BVS().calculation_X(0.5, 51.7)

print(RA_J1_BCS().calculations(800))
RA_J1_BVS().calculation_X(0.2, 147.2)
RA_J1_BVS().calculation_X(0.2, 87.6)
#
RA_J2_BVS().calculation_X(0.2, 147.2)
RA_J2_BVS().calculation_X(0.2, 87.6)
#
print(RA_J5_BCS().calculations(500))
RA_J5_BVS().calculation_X(0.1, 325.6 )
RA_J5_BVS().calculation_X(0.1, 193)