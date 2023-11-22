from repository.file_repo import File_repo
import random
import copy

class Services:
    def __init__(self, repo : File_repo) -> None:
        self.__repo = repo
        self.__sentence = []
        self.__score = 0
        self.__scramble_sentece = []
    
    def make_swap(self, word_1, letter_1, word_2, letter_2):

        if word_1 < 0 or word_1 >= len(self.__sentence):
            raise ValueError("First word index is not appropriate !")

        if word_2 < 0 or word_2 >= len(self.__sentence):
            raise ValueError("Secound word index is not appropriate ! ")

        if letter_1 < 1 or letter_1 >= len(self.__scramble_sentece[word_1]) - 1:
            raise ValueError("First letter index is not appropriate !")

        if letter_2 < 1 or letter_2 >= len(self.__scramble_sentece[word_2]) - 1:
            raise ValueError("Secound letter index is not appropiate !")

        self.__scramble_sentece[word_1][letter_1] , self.__scramble_sentece[word_2][letter_1] = self.__scramble_sentece[word_1][letter_2], self.__scramble_sentece[word_2][letter_2]
        self.__score -= 1


    def is_over(self):
        if self.get_sentece() == self.get_scramble_sentence():
            return 1

        if self.get_score() == 0:
            return -1
        return 0


    def get_all(self):
        return self.__repo.get_all()

    def select_sentence(self):

        sentences = self.get_all()
        sentences = random.choice(sentences)

        for word in sentences.split():
            letters = []
            for ch in word:
                letters.append(ch)
                self.__score += 1

            self.__sentence.append(letters)


    def select_words(self):
        word_1 = random.randint(0, len(self.__sentence) -1)
        word_2 = random.randint(0, len(self.__sentence) -1)

        while len(self.__scramble_sentece[word_1]) <= 2 or len(self.__scramble_sentece[word_2]) <= 2:
            word_1 = random.randint(0, len(self.__sentence) -1)
            word_2 = random.randint(0, len(self.__sentence) -1)
        return word_1,word_2


    def scramble_sentence(self):
        self.__scramble_sentece = copy.deepcopy(self.__sentence)

        for i in range(20):

            word1, word2 = self.select_words()
            letter_1 = random.randint(0, len(self.__scramble_sentece) -2)
            letter_2 = random.randint(0, len(self.__scramble_sentece) -2)

            self.__scramble_sentece[word1][letter_1], self.__scramble_sentece[word2][letter_2] = self.__scramble_sentece[word1][letter_2], self.__scramble_sentece[word2][letter_1]


    def get_sentece(self):
        sentence = ""

        for word in self.__sentence:
            for ch in word:
                sentence += ch

            sentence +=" "

        return sentence


    def get_scramble_sentence(self):
        scramble_sentence = ""

        for word in self.__scramble_sentece:
            for ch in word:
                scramble_sentence += ch
            scramble_sentence += " "

        return scramble_sentence
    
    def get_score(self):
        return self.__score

    


