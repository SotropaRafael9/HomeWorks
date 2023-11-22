import random
from domain import Question
from repository.repository import Repo_Question
class Services:
    def __init__(self) -> None:
        self._repo = Repo_Question()
        self._repo.add(Question("1", "What is the capital of Romania?", ["Bucharest","Canada", "Russia"], "Bucharest", "easy"))
        self._repo.add(Question("2", "What is the capital of Canada?", ["Bucharest","Canada", "Russia"], "Canada", "hard"))
        self._repo.add(Question("3", "What is the capital of Russia?", ["Bucharest","Canada", "Russia"], "Russia","medium"))
        self._repo.add(Question("4", "What is the capital of zimbabue?", ["Bucharest","Singapore", "zen"], "zen", "easy"))
    
    def add(self, new_question):
        self._repo.add(new_question)
    
    def get_all(self):
        return self._repo.get_all()
    
    def create_quiz(self, number_of_questions, difficulty, file):
        list_of_questions_selected = []
        list_of_questions_other = []
        for question in self._repo.get_all():
            if question.difficulty == difficulty:
                list_of_questions_selected.append(question)
            else:
                list_of_questions_other.append(question)
        if len(list_of_questions_selected) <= number_of_questions//2:
            raise Services_exception("Not enough question ")
        if len(list_of_questions_other) < number_of_questions//2:
            raise Services_exception("Not enough question . ")
        final_list =[]

        for i in range(number_of_questions//2+1):
            final_list.append(random.choice(list_of_questions_selected))
            list_of_questions_selected.remove(final_list[-1])
        for j in range(number_of_questions-((number_of_questions//2)+1)):
            final_list.append(random.choice(list_of_questions_other))
            list_of_questions_other.remove(final_list[-1])

        # final_list+=random.choices(list_of_questions_selected, k = (number_of_questions//2)+1)
        # final_list += random.choices(list_of_questions_other, k = number_of_questions-((number_of_questions//2)+1))
        
        f = open(file, "wt")
        for line in final_list:
            f.write(str(line)+"\n")
        f.close()


class Services_exception(Exception):
    pass


