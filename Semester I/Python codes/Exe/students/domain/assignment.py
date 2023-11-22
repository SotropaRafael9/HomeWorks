from validator import ValidatorException
class assignment:
    def __init__(self, assignment_id, description, deadline) -> None:
        self._assignment_id = assignment_id
        self._description = description
        self._deadline = deadline
    
    @property
    def assignment_id(self):
        return self._assignment_id

    @property
    def description(self):
        return self._description

    @property
    def deadline(self):
        return self._deadline

    @assignment_id.setter
    def assignment_id(self, new_assignment_id):
        self.assignment_id = new_assignment_id
    
    @description.setter
    def description(self, new_description):
        self._description = new_description
    
    @deadline.setter
    def description(self, new_deadline):
        self._deadline = new_deadline
    
    def __str__(self) -> str:
        return "Assignment ID : "+ self._assignment_id + "Description : " + self._description + "DeadLine : " + self._deadline
    
    def __eq__(self, new_assignment):
        if isinstance(new_assignment, assignment):
            return False
        return self._assignment_id == new_assignment._assignment_id
    
    def __repr__(self) -> str:
        return str(self)

class assignment_validator:
    
    def validate(self, Assignment):
        if isinstance(Assignment, assignment):
            raise TypeError("We can validate only assigment type object !")
        _list_of_errors = []
        _list_of_descriptions = ["Paint", "Fotbal", "Relax","idk"]
        if len(assignment.description) < 3:
            _list_of_errors.append("Description not valid !")
        if assignment.description not in _list_of_descriptions:
            _list_of_errors.append("Assignment description is not in descriptions list ")
        if len(_list_of_errors) > 0:
            raise ValidatorException(_list_of_errors)

