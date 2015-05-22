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


class Vector3D(object):
    """A 3D vector object. Intended to basically be an api wrapper 
       around a tuple of 3 float values. It would allow people to 
       reset different coordinates, and to treat the Vector like a 
       list or even a dictionary, but at heart it would be a tuple 
       of floats.
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        for arg in (x, y, z):
            if not isinstance(arg, numbers.Number):
                raise TypeError
        # coords is the essence of the data structure. It's immutable and
        # iterable
        self.coords = (x, y, z)
    # defining x, y, and z like this to allow for the coords to remain a
    # non-mutable iterable.
    @property
    def x(self):
        return self[0]
    @x.setter
    def x(self, number):
        self.coords = (number, self[1], self[2])
    @property
    def y(self):
        return self[1]
    @y.setter
    def y(self, number):
        self.coords = (self[0], number, self[2])
    @property
    def z(self):
        return self[2]
    @z.setter
    def z(self, number):
        self.coords = (self[0], self[1], number)

    @property
    def length(self):
        """get the vector length / amplitude
            >>> v = Vector3D(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
        """
        # iterate through the coordinates, square each, and return the root of
        # the sum
        return math.sqrt(sum(n**2 for n in self))

    @length.setter
    def length(self, number):
        """set the vector amplitude
            >>> v = Vector3D(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
            >>> v.length = -3.689
            >>> v
            Vector3D(-0.0, -3.2995419076, -1.6497709538)
        """
        # depends on normalized() and __mult__
        # create a vector as long as the number
        v = self.normalized() * number
        # copy it
        self.match(v)


    def normalize(self):
        """edits vector in place to amplitude 1.0 and then returns self
            >>> v
            Vector3D(-0.0, -3.2995419076, -1.6497709538)
            >>> v.normalize()
            Vector3D(-0.0, -0.894427191, -0.4472135955)
            >>> v
            Vector3D(-0.0, -0.894427191, -0.4472135955)
        """
        # depends on normalized and match
        self.match(self.normalized())
        return self

    def normalized(self):
        """just returns the normalized version of self without editing self in
        place.
            >>> v.normalized()
            Vector3D(0.0, 0.894427191, 0.4472135955)
            >>> v
            Vector3D(0.0, 3.2995419076, 1.6497709538)
        """
        # think how important float accuracy is here!
        if isRoughlyZero(sum(n**2 for n in self)):
            raise ZeroDivisionError
        else:
            return self * (1 / self.length)

    def match(self, other):
        """sets the vector to something, either another vector,
        a dictionary, or an iterable.
        If an iterable, it ignores everything
        beyond the first 3 items.
        If a dictionary, it only uses keys 'x','y', and 'z'
            >>> v
            Vector3D(0.0, 3.2995419076, 1.6497709538)
            >>> v.match({'x':2.0, 'y':1.0, 'z':2.2})
            >>> v
            Vector3D(2.0, 1.0, 2.2)
        """
        # this basically just makes a new vector and uses it's coordinates to
        # reset the coordinates of this one.
        if isinstance(other, Vector3D):
            self.coords = other.coords
        elif isinstance(other, dict):
            self.coords = (other['x'], other['y'], other['z'])
        else: # assume it is some other iterable
            self.coords = tuple(other[:3])

    def asList(self):
        """return vector as a list"""
        return [c for c in self]

    def asDict(self):
        """return dictionary representation of the vector"""
        return dict( zip( list('xyz'), self.coords ) )

    def __getitem__(self, key):
        """Treats the vector as a tuple or dict for indexes and slicing.
            >>> v
            Vector3D(2.0, 1.0, 2.2)
            >>> v[0]
            2.0
            >>> v[-1]
            2.2000000000000002
            >>> v[:2]
            (2.0, 1.0)
            >>> v['y']
            1.0
        """
        # key index
        if isinstance(key, int):
            return self.coords[key]
        # dictionary
        elif key in ('x','y','z'):
            return self.asDict()[key]
        # slicing
        elif isinstance(key, type(slice(1))):
            return self.coords.__getitem__(key)
        else:
            raise KeyError

    def __setitem__(self, key, value):
        """Treats the vector as a list or dictionary for setting values.
            >>> v
            Vector3D(0.0, 1.20747670785, 2.4149534157)
            >>> v[0] = 5
            >>> v
            Vector3D(5, 1.20747670785, 2.4149534157)
            >>> v['z'] = 60.0
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
        """
        if not isinstance(value, numbers.Number):
            raise ValueError
        if key in ('x','y','z'):
            d = self.asDict()
            d.__setitem__(key, value)
            self.match(d)
        elif key in (0,1,2):
            l = self.asList()
            l.__setitem__(key, value)
            self.match(l)
        else:
            raise KeyError

    def __iter__(self):
        """For iterating, the vectors coordinates are represented as a tuple."""
        return self.coords.__iter__()

    ## Time for some math

    def dot(self, other):
        """Gets the dot product of this vector and another.
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
            >>> v1
            Vector3D(0.0, 2.0, 1.0)
            >>> v1.dot(v)
            62.41495341569977
        """
        return sum((p[0] * p[1]) for p in zip(self, other))

    def cross(self, other):
        """Gets the cross product between two vectors
            >>> v
            Vector3D(5, 1.20747670785, 60.0)
            >>> v1
            Vector3D(0.0, 2.0, 1.0)
            >>> v1.cross(v)
            Vector3D(118.792523292, 5.0, -10.0)
        """
        # I hope I did this right
        x = (self[1] * other[2]) - (self[2] * other[1])
        y = (self[2] * other[0]) - (self[0] * other[2])
        z = (self[0] * other[1]) - (self[1] * other[0])
        return Vector3D(x, y, z)

    def __add__(self, other):
        """we want to add single numbers as a way of changing the length of the
        vector, while it would be nice to be able to do vector addition with
        other vectors.
            >>> from core import Vector3D
            >>> # test add
            ... v = Vector3D(0.0, 1.0, 2.0)
            >>> v1 = v + 1
            >>> v1
            Vector3D(0.0, 1.4472135955, 2.894427191)
            >>> v1.length - v.length
            0.99999999999999956
            >>> v1 + v
            Vector3D(0.0, 2.4472135955, 4.894427191)
        """
        if isinstance(other, numbers.Number):
            # then add to the length of the vector
            # multiply the number by the normalized self, and then
            # add the multiplied vector to self
            return self.normalized() * other + self

        elif isinstance(other, Vector3D):
            # add all the coordinates together
            # there are probably more efficient ways to do this
            return Vector3D(*(sum(p) for p in zip(self, other)))
        else:
            raise NotImplementedError

    def __sub__(self, other):
        """Subtract a vector or number
            >>> v2 = Vector3D(-4.0, 1.2, 3.5)
            >>> v1 = Vector3D(2.0, 1.1, 0.0)
            >>> v2 - v1
            Vector3D(-6.0, 0.1, 3.5)
        """
        return self.__add__(other * -1)

    def __mul__(self, other):
        """if with a number, then scalar multiplication of the vector,
            if with a Vector, then dot product, I guess for now, because
            the asterisk looks more like a dot than an X.
            >>> v2 = Vector3D(-4.0, 1.2, 3.5)
            >>> v1 = Vector3D(2.0, 1.1, 0.0)
            >>> v2 * 1.25
            Vector3D(-5.0, 1.5, 4.375)
            >>> v2 * v1 #dot product
            -6.6799999999999997
        """
        if isinstance(other, numbers.Number):
            # scalar multiplication for numbers
            return Vector3D( *((n * other) for n in self))

        elif isinstance(other, Vector3D):
            # dot product for other vectors
            return self.dot(other)

    def __hash__(self):
        """This method provides a hashing value that is the same hashing value
        returned by the vector's coordinate tuple. This allows for testing for
        equality between vectors and tuples, as well as between vectors.

        Two vector instances (a and b) with the same coordinates would return True
        when compared for equality: a == b, a behavior that I would love to
        have, and which would seem very intuitive.

        They would also return true when compared for equality with a tuple
        equivalent to their coordinates. My hope is that this will greatly aid
        in filtering duplicate points where necessary - something I presume
        many geometry algorithms will need to look out for.

        I'm not sure it is a bad idea, but I intend this class to basically be a
        tuple of floats wrapped with additional functionality.
        """
        return self.coords.__hash__()

    def __repr__(self):
        return 'Vector3D%s' % self.coords

