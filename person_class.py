class Person:
    'This is class Person'
    def __init__(self, first_name, last_name, age, country,sex, *args):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.country = country
    # гетер ( я так понимаю вывод атрибута, в смысле его значения)
    def get_age(self):
        return self._age
    # сетеры (я так понимаю задают условия входа,меняют входные даные(проверяют) в атрибуты.
    # только как его применить к методу print_person ?)
    def set_age(self,age):
        if age in range(1,100):
            self._age = age
        else:
            print (' Erorr, there are not so many people living in Belarus')
    # геттер
    def get_sex(self):
        return self.__sex
    # сеттер
    def set_sex(self,sex):
        if sex in ('man','men','woman','girl', 'male', 'female'):
            self.__sex = sex
        else:
            print ("No gender!")
    # метод (принт объекта)
    def print_person(self):
        return print (f'''Hello, I am {self.first_name} {self.last_name}  {self.age} years old, i am from {self.country}''')
        # объект
pers1 = Person('vasia', 'Pupkin', 13, 'USA', 'lll')

class Passport (Person):
    # ввод переменныx
    def __init__(self,number,date_give,who_give):
        self.number = number
        self.date_give = date_give
        self.who_give = who_give
    def get_passport(self):
        return self._age
    def set_passport(self):
        if age >= 14:
            self.passport_print()
        else:
            print(' Erorr, he is really little')
    # метод (возврат данных паспорт)
    def passport_print (self):
        return print (self.number, self.date_give, self.who_give)
    # объект:
p1 = Passport(1158899,'12.12.2021', 'Minsk_GOVD')

class Work (Person):
    def __init__(self,company, special,*args):
        self.company = company
        self.special = special
    def print_work(self):
        return print(f"I work in {self.company} {self.special}")
job = Work('MMM','god')

# примеры
pers1.print_person()
p1.passport_print()
job.print_work()
