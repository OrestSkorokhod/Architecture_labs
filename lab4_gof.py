# from __future__ import annotations
from typing import Optional
from abc import ABC, abstractmethod

#SINGLETON


class SingletonMeta(type):


    _instance = None

    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


# if __name__ == "__main__":
#
#     s1 = Singleton()
#     s2 = Singleton()
#     print('Singleton: ')
#     if id(s1) == id(s2):
#         print(True)
#     else:
#         print(False)


#COMMAND


class Receiver:


    def do_something(self, a: str) -> None:
        print(f"\nReceiver:  ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver:  ({b}.)", end="")

class Command(ABC):


    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):


    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: "
              f"({self._payload})")


class ComplexCommand(Command):


    def __init__(self, receiver: Receiver, a: str, b: str) -> None:


        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:

        print("ComplexCommand: ", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)





class Invoker:

    _on_start = None
    _on_finish = None



    def set_on_start(self, command: Command):
        self._on_start = command

    def set_on_finish(self, command: Command):
        self._on_finish = command

    def do_something_important(self) -> None:


        print("Invoker - start")
        if isinstance(self._on_start, Command):
            self._on_start.execute()

        print("Invoker - middle ")

        print("Invoker - finish ")
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()


# if __name__ == "__main__":
#
#     invoker = Invoker()
#     invoker.set_on_start(SimpleCommand("Hello world!"))
#     receiver = Receiver()
#     invoker.set_on_finish(ComplexCommand(
#         receiver, "Send email", "Save report"))
#
#     invoker.do_something_important()
#     print('\n')


#CHAINS


from typing import Any, Optional


class Handler(ABC):
    """
    Интерфейс Обработчика объявляет метод построения цепочки обработчиков. Он
    также объявляет метод для выполнения запроса.
    """

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):


    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None



class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:


    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")

#
# if __name__ == "__main__":
#     monkey = MonkeyHandler()
#     squirrel = SquirrelHandler()
#     dog = DogHandler()
#
#     monkey.set_next(squirrel).set_next(dog)
#
#     # Клиент должен иметь возможность отправлять запрос любому обработчику, а не
#     # только первому в цепочке.
#     print("Chain: Monkey > Squirrel > Dog")
#     client_code(monkey)
#     print("\n")
#
#     print("Subchain: Squirrel > Dog")
#     client_code(squirrel)
#     print('\n')




#DECORATOR



class Component():
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):

    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):


    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> str:

        return self._component

    def operation(self) -> str:
        self._component.operation()


class ConcreteDecoratorA(Decorator):

    def operation(self) -> str:

        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):

    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def client_code(component: Component) -> None:

    print(f"RESULT: {component.operation()}", end="")


#
# if __name__ == "__main__":
#
#     simple = ConcreteComponent()
#     print("Client: I've got a simple component:")
#     client_code(simple)
#     print("\n")
#
#     decorator1 = ConcreteDecoratorA(simple)
#     decorator2 = ConcreteDecoratorB(decorator1)
#     print("Client: Now I've got a decorated component:")
#     client_code(decorator2)
#
#     print("\n")



#PROXY


class Subject(ABC):
    """
    Интерфейс Субъекта объявляет общие операции как для Реального Субъекта, так
    и для Заместителя. Пока клиент работает с Реальным Субъектом, используя этот
    интерфейс, вы сможете передать ему заместителя вместо реального субъекта.
    """

    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):

    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):


    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:

        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:


    subject.request()



if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)

    print("")
