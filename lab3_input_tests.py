import unittest
import requests
from mockito import when, mock, unstub

from  lab1_reflection import Triangle, Quadrilateral

# class Number:
#     value = 255
#     __name__ = 'kek'
#
#     def __repr__(self):
#         return value

def do(a, b, c):

    # response = mock({'status_code': 800, 'text': 'Ok'})
    # when(requests).get('http://google.com/').thenReturn(response)
    obj = requests.get('http://google.com/')
    print(obj.__dict__)


    # answer = mock({'value': 'yes'})
    a = Triangle(a=3, b=4, c=5)
    # when(a).is_true().thenReturn(answer)
    print(a.is_true().__dict__)




    # answer_2 = mock({'value': 255})
    a = Triangle(a=3, b=4, c=5)
    # when(a).get_perimetr(2, 3, 4).thenReturn(answer)
    obj = a.get_perimetr(2, 3, 4)
    print(c.__dict__)

    c = a.get_perimetr(5, 3, 4)
    print(c.__dict__)

class Controller(object):

    def __init__(self):
        self.sa = int(input('input a: '))
        self.sb = int(input('input b: '))
        self.sc = int(input('input c: '))

        Tria = Triangle(a=3, b=4, c=5)

        if self.sa < 0 or self.sb < 0 or self.sc < 0:
            answer_2 = mock({'value': 'NO!'})

            when(Tria).get_perimetr(2, 3, 4).thenReturn(answer_2)
            obj = Tria.get_perimetr(2, 3, 4)
            print(obj.__dict__)
        else:
            sides = self.sa, self.sb, self.sc
            print(Tria.get_perimetr(*sides))
        # do(self.sa, self.sb, self.sc)


Controller()


response = mock({'status_code': 800, 'text': 'All is ok'}, spec=requests.Response, strict=True)
when(requests, strict=False).get('http://google.com/').thenReturn(response)
obj = requests.get('http://google.com/')
print(obj.__dict__)


unstub()
