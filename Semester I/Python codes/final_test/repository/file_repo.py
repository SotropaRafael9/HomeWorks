class File_repo:
    def __init__(self, file_name = "./repository/text.txt"):
        self._data = []
        self.__file_name = file_name
        
        self.load_files()
        print(self.get_all())
    
    def load_files(self):
        try:
            file = open(self.__file_name, "r")
        except IOError:
            return
        
        for line in file.readlines():
            sentence = line.strip()

            if sentence == '':
                continue
            self._data.append(sentence)
            
        file.close()

    def find_sentence(self, sentence):
        for item in self._data:
            if sentence == item:
                return item

        return None

    def add_sentence(self, sentence):
        if self.find_sentence(sentence) is not None:
            raise ValueError("Sentence already in repo !")
        self._data.append(sentence)
    
    def get_all(self):
        return self._data
  