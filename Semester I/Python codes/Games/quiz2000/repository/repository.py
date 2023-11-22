class Repo_Question:
    def __init__(self):
        self._questions = []
    
    def add(self, question):
        if self.get_by_id(question.id):
            raise repo_exception("Question already exists")
        self._questions.append(question)
    
    def get_all(self):
        return self._questions
    
    def get_by_id(self, id):
        for question in self._questions:
            if question.id == id:
                return True
        return False
        
class repo_exception(Exception):
    pass