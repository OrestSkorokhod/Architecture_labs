import unittest
import requests
from mockito import when, mock, unstub

from  lab1_reflection import Triangle, Quadrilateral

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
        pass
        # do(self.sa, self.sb, self.sc)

    def get_data(self):
        self.sa = int(input('input a: '))
        self.sb = int(input('input b: '))
        self.sc = int(input('input c: '))

        # Tria = Triangle(a=3, b=4, c=5)
        Tria = Triangle(a=self.sa, b=self.sb, c=self.sc)

        # if self.sa < 0 or self.sb < 0 or self.sc < 0:
            # answer_2 = mock({'value': 'NO!'})

        when(Tria).get_perimetr(-5, -5, -5).thenReturn('no!!!')
        when(Tria).get_perimetr(0, 0, 0).thenReturn('zero')
        when(Tria).get_perimetr(5, 5, 5).thenReturn(15)
        obj = Tria.get_perimetr(self.sa, self.sb, self.sc)
        return obj
        # print(obj.__dict__)
        # print(obj)
        # else:
        #     sides = self.sa, self.sb, self.sc
        #     print(Tria.get_perimetr(*sides))

class View(object):

    def show_data(self, data):
        print(data)




controller = Controller()
data = controller.get_data()
View().show_data(data)

class Controller:
    def __init__(self):
        

# response = mock({'status_code': 800, 'text': 'All is ok'}, spec=requests.Response, strict=True)
# when(requests, strict=False).get('http://google.com/').thenReturn(response)
# obj = requests.get('http://google.com/')
# print(obj.__dict__)


unstub()
