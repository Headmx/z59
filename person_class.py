class Person:
    'This is class Person'
    def __init__(self, first_name, last_name, age, country, auto = 'none', sex = 'male', work = 'none', passport = 'none'):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        self.work = work
        self.country = country
        self.auto = auto
        self.passport = passport
    # метод (принт объекта)

    def print_person(self):
        if self.age >= 18:
            return print (f'''
            1 {self.first_name}
            2 {self.last_name}
            3 age {self.age}
            4 country {self.country}
            5 auto {self.auto}
            6 passport {p1.passport_print}
            7 sex {self.sex}
            8 work {self.work}
            ''')
        elif  14 <= self.age < 18:
            return print (f"""
            1 {self.first_name} 
            2 {self.last_name} 
            3 age {self.age} 
            4 country {self.country} 
            5 auto none
            6 passport {self.passport} 
            7 sex {self.sex} 
            """)
        elif self.age < 14:
            return print(f"""
                1 {self.first_name} 
                2 {self.last_name} 
                3 age {self.age} 
                4 country {self.country} 
                5 auto none
                6 passport none 
                7 sex {self.sex} 
                """)
    # объект
pers1 = Person('vasia', 'Ivanov', 14, 'USA', 'BMW', 'male', 'Epam')

class Passport:
    # ввод переменные
    def __init__(self,number,date_give,who_give):
        self.number = number
        self.date_give = date_give
        self.who_give = who_give
    # метод (возврат данных паспорт для принта)
    def passport_print (self):
        return self.number, self.date_give, self.who_give
    # объект:
p1 = Passport(1158899,'12.12.2021', 'Minsk_GOVD')


print(pers1.print_person())
print (p1.passport_print())