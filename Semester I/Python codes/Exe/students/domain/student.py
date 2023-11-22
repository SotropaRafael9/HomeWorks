from typing import Self
from validator import ValidatorException


class student:
    def __init__(self, student_id, name, group) -> None:
        self._student_id = student_id
        self._name = name
        self._group = group
    
    @property
    def student_id(self):
        return self._student_id
    
    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    @student_id.setter
    def student_id(self, new_student_id):
        self._student_id = new_student_id

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @group.setter
    def group(self, new_group):
        self._name = new_group
    
    
    def __str__(self) -> str:
        return "Student -> "+self._student_id + " " + self._name + " " + self._group
    
    def __repr__(self) -> str:
        return str(self)
    
    def __eq__(self, other_student):
        if not isinstance(other_student, student):
            return False
        return self._student_id == other_student._student_id

class student_validator:
    def validate(self, Student):
        if isinstance(Student, student) == False:
            raise TypeError("We can validate only stundet type object ! ")
        
        _list_of_errors = []
        if len(student.name) < 2:
            _list_of_errors.append("Student name is incomplet !")
        if len(student.group) < 3:
            _list_of_errors.append("Group name is too short !")

        if len(_list_of_errors) > 0:
            raise ValidatorException(_list_of_errors)
        return True
