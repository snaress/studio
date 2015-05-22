import math, random


def getDistance(p1, p2):
    """ Get distance between two 3d points
        :param p1: First point coord
        :type p1: tuple
        :param p2: Second point coord
        :type p2: tuple
        :return: Distance between p1 and p2
        :rtype: float """
    dist = math.sqrt(math.pow((p1[0]-p2[0]), 2) +
                     math.pow((p1[1]-p2[1]), 2) +
                     math.pow((p1[2]-p2[2]), 2))
    return dist

def coordOp(p1, p2, operation):
    """ Coord operations
        :param p1: First point coord
        :type p1: tuple
        :param p2: Second point coord
        :type p2: tuple
        :param operation: 'plus', 'minus', 'mult', 'divide' or 'average'
        :type operation: str
        :return: New coords
        :rtype: tuple """
    operations = ('plus', 'minus', 'mult', 'divide', 'average')
    if not operation in operations:
        raise NotImplementedError("The operation must be in %s" % ", ".join(operations))
    newCoord = []
    if operation == 'plus':
        for x, y in zip(p1, p2):
            newCoord.append(x + y)
    elif operation == 'minus':
        for x, y in zip(p1, p2):
            newCoord.append(x - y)
    elif operation == 'mult':
        for x, y in zip(p1, p2):
            newCoord.append(x * y)
    elif operation == 'divide':
        for x, y in zip(p1, p2):
            newCoord.append(x / y)
    elif operation == 'average':
        for x, y in zip(p1, p2):
            newCoord.append((x + y) / 2)
    result = (newCoord[0], newCoord[1], newCoord[2])
    return result

def linear(minVal, maxVal, newMin, newMax, value):
    """ Linear step from range (minVal, maxVal) to new range (newMin, newMax)
        :param minVal: Range min value
        :type minVal: float
        :param maxVal: Range max value
        :type maxVal: float
        :param newMin: New range min value
        :type newMin: float
        :param newMax: New range max value
        :type newMax: float
        :param value: Range value to convert
        :type value: float
        :return: Linear value
        :rtype: float """
    coef = ((float(value) - float(minVal)) * 100) / (float(maxVal) - float(minVal))
    newVal = float(newMin) + ((coef * (float(newMax) - float(newMin))) / 100)
    return newVal


class RandomSequence(object):
    """ Create random sequence from given params
        Usage: r = RandomSequence('sinusoidal', -5, 5, 10, 2, bias=True, biasMin=-3, biasMax=3)
               r.printRandParams()
               rand = r.generate()
        :param randType: 'uniform' or 'sinusoidal'
        :type randType: str
        :param ampMin: Amplitude Minimum
        :type ampMin: float
        :param ampMax: Amplitude Maximum
        :type ampMax: float
        :param octaves: Number of random value to create
        :type octaves: int
        :param frequence: Octaves repetition
        :type frequence: int
        :param bias: Amplitude Bias on or off
        :type bias: bool
        :param biasMin: Bias Minimum
        :type biasMin: float
        :param biasMax: Bias Maximum
        :type biasMax: float """

    def __init__(self, randType, ampMin, ampMax, octaves, frequence, bias=False, biasMin=0, biasMax=0):
        self.randType = randType
        self.ampMin = ampMin
        self.ampMax = ampMax
        self.octaves = octaves
        self.frequence = frequence
        self.bias = bias
        self.biasMin = biasMin
        self.biasMax = biasMax

    def generate(self):
        """ Generate random sequence
            :return: Random sequence
            :rtype: list """
        if self.randType == 'uniform':
            return self.getUniformRand
        elif self.randType == 'sinusoidal':
            return self.getSinusoidalRand

    @property
    def getUniformRand(self):
        """ Create uniform random sequence from params
            :return: Uniform random sequence
            :rtype: list """
        #-- Create Random Sequence --#
        randSeq = []
        for n in range(self.octaves):
            rand = random.uniform(self.ampMin, self.ampMax)
            if self.bias:
                if not rand > self.biasMax and not rand < self.biasMin:
                    if rand > (self.ampMin + self.ampMax)/2:
                        rand = random.uniform(self.biasMax, self.ampMax)
                    else:
                        rand = random.uniform(self.biasMin, self.ampMin)
            randSeq.append(rand)
        #-- Create Random Frequence --#
        rOctaves = randSeq
        for m in range(self.frequence-1):
            randSeq.extend(rOctaves)
        return randSeq

    @property
    def getSinusoidalRand(self):
        """ Create sinusoidal random sequence from params
            :return: Sinusoidal random sequence
            :rtype: list """
        #-- Create Sinusoidal Random Sequence --#
        randSeq = []
        rand = 0
        sign = ''
        for n in range(self.octaves):
            #-- Random Init --#
            if sign == '':
                rand = random.uniform(self.ampMin, self.ampMax)
                if rand > (self.ampMin + self.ampMax)/2:
                    if self.bias:
                        rand = self.getSinBiasValue(rand, '-')
                    sign = '+'
                else:
                    if self.bias:
                        rand = self.getSinBiasValue(rand, '+')
                    sign = '-'
            #-- Random Lo --#
            elif sign == '+':
                rand = random.uniform(self.ampMin, (self.ampMin + self.ampMax)/2)
                if self.bias:
                    rand = self.getSinBiasValue(rand, sign)
                sign = '-'
            #-- Random Hi --#
            elif sign == '-':
                rand = random.uniform((self.ampMin + self.ampMax)/2, self.ampMax)
                if self.bias:
                    rand = self.getSinBiasValue(rand, sign)
                sign = '+'
            randSeq.append(rand)
        #-- Create Random Frequence --#
        rOctaves = randSeq
        for m in range(self.frequence-1):
            randSeq.extend(rOctaves)
        return randSeq

    def getSinBiasValue(self, rand, sign):
        """ Get bias value from given params
            :param rand: Random value
            :type rand: float
            :param sign: '-' or '+'
            :type sign: str
            :return: Bias value
            :rtype: float """
        if not rand > self.biasMax and not rand < self.biasMin:
            if sign == '+':
                rand = random.uniform(self.ampMin, self.biasMin)
            else:
                rand = random.uniform(self.biasMax, self.ampMax)
        return rand

    def printRandParams(self):
        """ Print noise params """
        print "\n", "#" * 60
        print "#-- Random Params --#"
        for k, v in self.__dict__.iteritems():
            print k, ' = ', v
        print "#" * 60


class Vec3(object):
    """ A three dimensional vector """

    def __init__(self, v_x=0, v_y=0, v_z=0):
        self.x = v_x
        self.y = v_y
        self.z = v_z

    def __str__(self):
        return '<%s>' % ','.join([str(val) for val in (self.x, self.y, self.z)])

    def __repr__(self):
        return '%s instance at 0x%s' % (str(self), str(hex(id(self))[2:].upper()))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("index out of range for Vec3")

    def __mul__(self, other):
        """ Multiplication, supports types Vec3 and other types that supports the '*' operator """
        if isinstance(other, Vec3):
            return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vec3(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        """ Division, supports types Vec3 and other types that supports the '/' operator """
        if isinstance(other, Vec3):
            return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            return Vec3(self.x / other, self.y / other, self.z / other)

    def __add__(self, other):
        """ Addition, supports types Vec3 and other types that supports the '+' operator """
        if isinstance(other, Vec3):
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vec3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        """ Subtraction, supports types Vec3 and other types that supports the - operator """
        if isinstance(other, Vec3):
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return Vec3(self.x - other, self.y - other, self.z - other)

    def __abs__(self):
        """ Absolute value: the abs() method """
        return Vec3(abs(self.x), abs(self.y), abs(self.z))

    def __neg__(self):
        """ Negate this vector """
        return Vec3(-self.x, -self.y, -self.z)

    def length(self):
        """ This vectors length """
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def length_squared(self):
        """ Returns this vectors length squared (saves a sqrt call, usefull for vector comparisons) """
        return self.x**2 + self.y**2 + self.z**2

    def cross(self, other):
        """ Return the cross product of this and another Vec3 """
        return Vec3((self.y * other.z) - (other.y * self.z),
                    (self.z * other.x) - (other.z * self.x),
                    (self.x * other.y) - (self.y * other.x))

    def dot(self, other):
        """ Return the dot product of this and another Vec3 """
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def normalize(self):
        """ Return this vector normalized """
        return self / self.length()
