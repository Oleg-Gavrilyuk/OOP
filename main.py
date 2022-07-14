class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def get_arg(self):
        sum1 = 0
        for i in self.grades.values():
            sum1 += i
            estimation = round(sum1 / len(self.grades), 1)
        return estimation


    def __lt__(self,stud):
        if not isinstance(stud, Student):
            print("Not a student")
            return
        return self.get_arg()<stud.get_arg()




    def __str__(self):
        courses = ','.join(self.courses_in_progress)
        finish = ','.join(self.finished_courses)
        print(f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашнее задание: {self.get_arg()}')
        print(f'Курсы в процессе изучения: {courses}')
        print(f'Завершенные курсы: {finish}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Student) and course in self.courses_attached and course in Student.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def get_arg(self):
        sum = 0
        for i in self.grades.values():
            sum += i
        return print(round(sum / len(self.grades), 1))
    def __lt__(self,lect):
        if not isinstance(lect, Student):
            print("Not a lecturer")
            return
        return self.get_arg()<lect.get_arg()
    def __str__(self):
        return print(f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.get_arg()}')


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return print(f'Имя: {self.name} \nФамилия: {self.surname}')





# some_reviewer = Reviewer('Some', 'Buddy')
# some_reviewer.__str__()
#
# some_lecturer = Lecturer('Some', 'Buddy')
# some_lecturer.grades = {1: 10, 2: 9, 3: 9}
# some_lecturer.__str__()

some_student = Student('Ruoy', 'Eman', 'man')
some_student.grades = {1: 10, 2: 9, 3: 9}
some_student.__str__()


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.grades = {1: 10, 2: 10, 3: 10}
best_student.__str__()
# print(some_student.__lt__(best_student))
#
# cool_mentor = Reviewer('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
# #
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)

