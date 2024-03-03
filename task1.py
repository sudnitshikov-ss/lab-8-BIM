from math import sin, radians


class Parallelepiped:
    """Базовый класс для все параллелепипедов"""
    amount = 0  # колличество созданных экземпляров класса

    def __init__(self, a: float, b: float, alpha=90.0) -> None:
        """
        Создание и подготовка к работе объекта 'Параллелепипед'
        :param a: Длина 1 стороны параллелепипеда
        :param b: Длина 2 (смежной) стороны параллелепипеда
        :param alpha: Угол между 1 и 2 стороной параллелепипеда в градусах
        Примеры:
        par1 = Parallelepiped(1.1, 2.2, 60)  # инициализация экземпляра класса
        """
        self.side1, self.side2, = None, None

        if not isinstance(a, float):
            raise TypeError("Длина - вещественное число")
        if a <= 0:
            raise ValueError("Длина стороны должны быть положительным числом")
        self.side1 = a

        if not isinstance(a, float):
            raise TypeError("Длина - вещественное число")
        if a <= 0:
            raise ValueError("Длина стороны должны быть положительным числом")
        self.side2 = b

        if not isinstance(alpha, float):
            raise TypeError("Угол должыен быть вещественным числом")
        if alpha <= 0:
            raise ValueError("Угол должен быть положительным числом")
        self.angle = alpha

        self.__class__.amount += 1

    def __str__(self) -> str:
        return f"Параллелепипед со сторонами {self.side1}, {self.side2} и углом между ними {self.angle}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a = {self.side1}, b = {self.side2}, alpha = {self.angle})"

    @property
    def area(self):
        """Свойство возвращает значение площади параллелепипеда"""
        return self.side1 * self.side2 * sin(radians(self.angle))

    def is_equal(self, other_object):
        """Функция проверяет 2 параллелепипеда на равенство, даже если они принадлежат разным дочерним классам"""
        if not isinstance(other_object, self.__class__):
            raise ValueError('Экземпляры принадлежат разным классам')
        if self.side1 == other_object.side1 and self.side2 == other_object.side2 and self.angle == other_object.angle:
            return True
        else:
            return False

    @classmethod
    def get_amount(cls) -> str:
        return f'Создано {cls.amount} экземпляров(-a) параллелепипедов'


class Rectangle(Parallelepiped):
    """Дочерний класс для параллелепипедов - прямоугольники"""
    amount = 0  # колличество созданных экземпляров класса

    def __init__(self, a: float, b: float) -> None:
        """
                Создание и подготовка к работе объекта 'Прямоугольник'
                :param a: Длина 1 стороны прямоугольника
                :param b: Длина 2 (смежной) стороны прямоугольника
                Примеры:
                 rec1 = Rectangle(5.0, 10.2) # инициализация экземпляра класса
                """
        super().__init__(a, b)

    def __str__(self) -> str:
        return f'Прямоугольник со сторонами {self.side1}, {self.side2}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a = {self.side1}, b = {self.side2})"

    @classmethod
    def get_amount(cls) -> str:  # в дочернем классе изменен метод, т.к. требуется вывод строки с другим именем фигуры
        return f"Создано {cls.amount}  экземпляров(-a) прямоугольников"


class Rombus(Parallelepiped):
    """Дочерний класс  для параллелепипедов - ромбы"""
    amount = 0  # колличество созданных экземпляров класса

    def __init__(self, a: float, alpha: float) -> None:
        """
                Создание и подготовка к работе объекта 'Ромб'
                :param a: Длина  стороны ромба
                :param alpha: Угол между сторонами ромба
                Примеры:
                 romb1 = Rombus(5.0, 60.0) # инициализация экземпляра класса
                """
        super().__init__(a, a, alpha)

    def __str__(self) -> str:
        return f'Ромб со сторонами {self.side1}, и углом: {self.angle}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a = {self.side1}, alpha = {self.angle})"

    @classmethod
    def get_amount(cls) -> str:  # в дочернем классе изменен метод, т.к. требуется вывод строки с другим именем фигуры
        return f"Создано {cls.amount}  экземпляров(-a) ромбов"


if __name__ == "__main__":
    par1 = Parallelepiped(5.0, 15.0, 22.5)
    print(par1)
    print(repr(par1))
    print(par1.area)
    rec1 = Rectangle(15.0, 20.0)
    print(rec1)
    print(repr(rec1))
    print(rec1.area)
    romb1 = Rombus(5.0, 52.0)
    print(romb1)
    print(repr(romb1))
    print(romb1.area)
    romb2 = Rombus(5.0, 52.0)
    par2 = Parallelepiped(5.0, 5.0, 52.0)
    print(par2.is_equal(romb1))
    # print(romb1.is_equal('romb2')) - пример сравнения экземпляров разных классов
    print(Parallelepiped.get_amount())
    print(Rombus.get_amount())