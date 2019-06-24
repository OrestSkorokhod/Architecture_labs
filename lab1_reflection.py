import math
import sys
import inspect
# from inspect import signature

def check_range(f):
    def decorated(*args, **kwargs):
        # for key in args:
        #     print(key)
        # for key, value in kwargs.items():
        #     print("{} = {}".format(key, value))
        for name, range in f.__annotations__.items():
            # print(name, range)
            min_value, max_value = range
            if not (min_value <= kwargs[name] <= max_value):
                msg = 'argument {} is out of range [{} - {}]'
                raise ValueError(msg.format(name, min_value, max_value))
        return f(*args, **kwargs)
    return decorated


class Triangle:
    side_1 = None
    side_2 = None
    side_3 = None

    # @check_range
    def __init__(self, a: ( 0, 50), b: (0, 50) , c: (0, 50)):
        # felf = Triangle[inspect.getframeinfo(inspect.currentframe()).function]
        # print("** myfunc inspect : %s"%felf.__name__)
        self.side_1 = a
        self.side_2 = b
        self.side_3 = c

    def get_area(self):
        p = float(self.side_1 + self.side_2 + self.side_3) / 2
        s = math.sqrt(p * ( p - self.side_1) * ( p - self.side_2) * ( p - self.side_3))
        return s
        # return 'Area of triangle with sides {}, {}, {} is {}'.format(self.side_1, self.side_2, self.side_3, s)

    def is_true(self):
        if max(self.side_1, self.side_2, self.side_3) > sum([self.side_1, self.side_2, self.side_3]) / 2:
            return False
        else:
            return True
    def get_perimetr(self, *args):
        # print(type(args))
        return sum(args)

    def __repr__(self):
        return 'Triangle with sides {}, {}, {} and area {}'.format(self.side_1, self.side_2, self.side_3, self.get_area())




class Quadrilateral(Triangle):
    side_4 = None
    diagonal = None


    # @check_range
    # def __init__(self, a: ( 0, 50), b: ( 0, 50), c: ( 0, 50), d: ( 0, 50), diagonal: ( 0, 50)):
    #     # print('hello')
    #     self.side_1 = a
    #     self.side_2 = b
    #     self.side_3 = c
    #     self.side_4 = d
    #     self.diagonal = diagonal
    def __init__(self, triangle, side_4):
        self.side_1 = triangle.side_1
        self.side_2 = triangle.side_2
        self.side_3 = triangle.side_3
        self.side_4 = side_4
    def get_area(self):

        s = Triangle(a=self.side_1, b=self.side_2, c=self.diagonal).get_area() + Triangle(a=self.side_3, b=self.side_4, c=self.diagonal).get_area()
        return s
        # return 'Area of Quadrilateral with sides {}, {}, {}, {} is {}'.format(self.side_1, self.side_2, self.side_3, self.side_4, s)
    def __repr__(self):
        return 'Quadrilateral with sides {}, {}, {}, {} and area {}'.format(self.side_1, self.side_2, self.side_3, self.side_4, self.get_area())

    def get_sides(self):
        return self.side_1, self.side_2,self.side_3,self.side_4
    # def hello(self):
    #     print('hello')
    def get_perimetr(self):
        return self.side_1 + self.side_2 + self.side_3 + self.side_4


if __name__ == '__main__':

    tr = Triangle(a=3, b=4, c=5)
    print('Area of Triangle:')
    print(tr.get_area())

    q = Quadrilateral(a=3, b=4, c=3, d=4, diagonal=5)
    print('Area of Quadrilateral:')
    print(q.get_area())

    print('toString methods:')
    print(q)
    print(tr)


    print('Name:')
    print(q.__class__.__name__)
    print('Attr and types:')

    for field, value in q.__dict__.items():
        print(field, type(value))

        # print(Quadrilateral(3, 4, 3, 4, 5).__doc__)
        # print(dir(q))
        # print(q.__doc__)
        # print(q.__dict__)
        print('Methods:')
        # print(inspect.getmembers(q, predicate=inspect.ismethod))

    for method in inspect.getmembers(q, predicate=inspect.ismethod):
        # print(type(method[1]))
        print(method[0])
        print()

        print('Invoke:')
        class_name = "Quadrilateral"
        method = "get_area"
        obj = globals()[class_name](a=3, b=4, c=3, d=4, diagonal=5)
        answer = getattr(obj, method)()
        print(answer)

        print('Superclass:')
        # print(super(q.__class__))
        print(inspect.getmro(Quadrilateral)[1])
        print('-----------------------------------------')


        #
        # def myfunc():
        #     felf = globals()[inspect.getframeinfo(inspect.currentframe()).function]
        #     print("** myfunc inspect : %s"%felf.__name__)
        #
        #     felf = globals()[sys._getframe().f_code.co_name]
        #     print("** myfunc globals : %s"%felf.__name__)
        #
        #     print( 'wrapper =' )
        #     print( myfunc )
        #
        #     print( 'done myfunc' )

        #
        # myfunc()
        #
        # print(globals())





# class Point:
    # x































print('---------------------------------------------')
