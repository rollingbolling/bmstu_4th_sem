class Point:
    def __init__(self, x, y, derivative):
        self._x = x
        self._y = y
        self._derivative = derivative

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def derivative(self):
        return self._derivative

    @x.setter
    def x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError('Координата x должна быть типа int или float')
        else:
            self._x = x

    @y.setter
    def y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError('Координата y должна быть типа int или float')
        else:
            self._y = y

    @derivative.setter
    def derivative(self, derivative):
        if not isinstance(derivative, (float, int)):
            raise ValueError('Производная может быть типа int или float')
        else:
            self._derivative = derivative
    
    def __repr__(self):
        return "Point({}, {})".format(self._x, self._y)
    
    
    def __str__(self):
        return self.__str__()