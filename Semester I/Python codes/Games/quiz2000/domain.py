class Question:
    def __init__(self, id, text, answers, correct_answer, difficutly):
        self._id = id
        self._text = text
        self._answers = answers
        self._correct_answer = correct_answer
        self._difficulty = difficutly

    @property
    def id(self):
        return self._id
    
    @property
    def text(self):
        return self._text
    
    @property
    def answers(self):
        return self._answers
    
    @property
    def correct_answer(self):
        return self._correct_answer
    
    @property
    def difficulty(self):
        return self._difficulty

    def __str__(self):
        return self._id + " " + self._text + " " + str(self._answers)+ " " + self._correct_answer+ " " + self._difficulty
    
