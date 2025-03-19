from abc import ABC, abstractmethod
from . lesson import Lesson
from . professor import Professor
from reportlab.pdfgen import canvas
import io

# Abstract Classes
class AbstractCourse(ABC):
    @abstractmethod
    def retrieve_list_of_lessons(self) -> list:
        pass
        
    @abstractmethod
    def retrieve_list_of_results(self) -> dict:
        pass
    
    @abstractmethod
    def retrieve_results(self, student:User) -> float | str:
        pass
    
    @abstractmethod
    def generate_certificate(self):
        pass
        
    @abstractmethod
    def add_lesson():
        pass
    
    @abstractmethod
    def remove_lesson():
        pass
    
    @abstractmethod
    def add_student(self):
        pass
    
    @abstractmethod
    def remove_student(self):
        pass

# Interfaces


# Classes
class Course(AbstractCourse):
    def __init__(self, name:str, description:str, suscription_required:bool, professor:Professor):
        self.__name = name
        self.__description = description
        self.__suscription_required = suscription_required
        self.__proffessor = professor
        self.__lessons = []
        self.__students = []
        self.__results = []
        
    # Properties
    @property
    def lessons(self) -> list:
        return self.__lessons
    
    @property
    def students(self) -> list:
        return self.__students
        
    @property
    def results(self) -> list:
        return self.__results
    
    
    # Lessons
    def retrieve_list_of_lessons(self) -> list:
        return self.lessons
    
    def add_lesson(lesson:Lesson):
        try:
            self.lessons.append(lesson)
        except Exception as e:
            raise Exception(f'Error: {e}')
            
    def remove_lesson(lesson:Lesson):
        try:
            self.lessons.remove(lesson)
        except Exception as e:
            raise Exception(f'Error: {e}')
        
    # Students
    def add_student(student:User):
        try:
            self.students.append(student)
            self.results.append(0)
        except Exception as e:
            raise Exception(f'Error: {e}')
            
    def remove_student(student:User):
        try:
            self.students.remove(student)
        except Exception as e:
            raise Exception(f'Error: {e}')
    
    # Results
    def retrieve_list_of_results(self) -> dict:
        result = {'students':self.students, 'results':self.results}
        return result
    
    def retrieve_results(self, student:User) -> float | str:
        if student in self.students:
            result = [item for item in self.results if self.results.index(item) == self.students.index(student)]
        else:
            result = 'The requested student is no..........................................000t suscribed to this course.'
        return result
        
    def generate_certificate(self, user:User) -> bytes:
        # Validate if the student had completed all the lessons for this course.
        # Obtain the student note for this course.
        note = [item for item in self.__results if self.results.index(item) == self.students.index(user)]
        # Generate the certification as PDF file.
        c = canvas.Canvas(f'{user.username}_{self.__name}_certificate.pdf')
        c.drawString(100, 500, f'Congratulations for your dedication on this course!')
        c.drawString(100, 700, f'{user.username} is cetificated on this area with a note of:')
        c.drawString(100, 800, f'{note}')
        c.save()
        # Obtain the generated file.
        with open(f'{user.username}_{self.__name}_certificate.pdf', 'rb') as pdf_file:
            file = io.BytesIO(pdf_file.read())
        return file
        
    