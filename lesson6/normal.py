# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


import uuid
from enum import Enum


class Subject(Enum):
    NONE = 'NO SUBJECT'
    MATH = 'MATH'
    PHYSICS = 'PHYSICS'


subject_name = {
    Subject.NONE: 'нет дисциплин',
    Subject.MATH: 'математика',
    Subject.PHYSICS: 'физика'
}


def short_guid():
    return str(uuid.uuid4())[:8]


class Human:
    def __init__(self, name: str, lastname: str, patronymic: str):
        self._id = short_guid()
        self.name = name
        self.lastname = lastname
        self.patronymic = patronymic

    def __str__(self):
        return f'{self.lastname} {self.name[0]}.{self.patronymic[0]}.'

    @property
    def id(self):
        return self._id


class Grade:
    def __init__(self, level: int, letter: str):
        self.level = level
        self.letter = letter

    def __str__(self):
        return f'{self.level}{self.letter}'.upper()

    @property
    def code(self):
        return str(self)


class Student(Human):
    def __init__(self, name: str, lastname: str, patronymic: str):
        Human.__init__(self, name, lastname, patronymic)
        self._father = None
        self._mother = None

    @property
    def father(self) -> Human:
        return self._father

    @father.setter
    def father(self, value: Human):
        self._father = value

    @property
    def mother(self) -> Human:
        return self._mother

    @mother.setter
    def mother(self, value: Human):
        self._mother = value


class Teacher(Human):
    def __init__(self, name: str, lastname: str, patronymic: str):
        Human.__init__(self, name, lastname, patronymic)
        self._subject = Subject.NONE

    @property
    def subject(self) -> Subject:
        return self._subject

    @subject.setter
    def subject(self, value: Subject):
        self._subject = value


class School:
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name
        self._students = set()
        self._teachers = set()
        self._classes = set()
        self._students_class_table = dict()  # key is student.id, value is class.code
        self._class_subjects_table = set()  # set of tuples (class.code, subject)

    @property
    def students(self) -> set:
        return self._students

    @property
    def classes(self) -> set:
        return self._classes

    @property
    def teachers(self) -> set:
        return self._teachers

    def add_student(self, student: Human):
        self.students.add(student)

    def add_teacher(self, student: Human):
        self.teachers.add(student)

    def add_class(self, class_: Grade):
        self.classes.add(class_)

    def add_student_to_class(self, student: Student, class_: Grade):
        self._students_class_table[student.id] = class_.code

    def remove_student_from_class(self, student: Student):
        del self._students_class_table[student.id]

    def assign_subject_to_class(self, subject: Subject, class_: Grade):
        self._class_subjects_table.add((str(class_), subject))

    def remove_subject_fro_class(self, subject: Subject, class_: Grade):
        self._class_subjects_table.remove((str(class_), subject))

    def students_in_class(self, class_code: str):
        student_ids = []
        for k in self._students_class_table.keys():
            if self._students_class_table[k] == class_code:
                student_ids.append(k)
        return map(lambda st_id: next(x for x in self.students if x.id == st_id), student_ids)

    def student_subjects(self, student_id: str):
        student_class = self._students_class_table[student_id]
        return map(lambda x: x[1], [x for x in self._class_subjects_table if x[0] == student_class])

    def teachers_for_class(self, class_code):
        subjects = list(map(lambda x: x[1], [x for x in self._class_subjects_table if x[0] == class_code]))
        return [x for x in self.teachers if x.subject in subjects]


p1 = Student('Иван', 'Иванов', 'Иванович')
p2 = Student('Алексей', 'Алексеев', 'Алексеевич')
p3 = Student('Петр', 'Петров', 'Петрович')

t1 = Teacher('Иван', 'ИвановУчитель', 'Иванович')
t2 = Teacher('Петр', 'ПетровУчитель', 'Петрович')
t1.subject = Subject.MATH
t2.subject = Subject.PHYSICS

c1 = Grade(7, 'А')
c2 = Grade(9, 'Е')

school = School(19, 'Гимназия #1')
school.add_student(p1)
school.add_student(p2)
school.add_student(p3)
school.add_teacher(t1)
school.add_teacher(t2)
school.add_class(c1)
school.add_class(c2)
school.add_student_to_class(p1, c1)
school.add_student_to_class(p2, c1)
school.add_student_to_class(p3, c2)
school.assign_subject_to_class(Subject.MATH, c1)
school.assign_subject_to_class(Subject.PHYSICS, c1)
school.assign_subject_to_class(Subject.MATH, c2)

print(f'{school.name}:')
print('Классы в школе:', ', '.join(map(str, school.classes)))
print('Ученики 7А:', ', '.join(map(str, school.students_in_class('7А'))))
print(f'{p1} изучает:', ', '.join(map(subject_name.get, school.student_subjects(p1.id))))
print('В 7А преподают: ', ', '.join(map(str, school.teachers_for_class('7А'))))
