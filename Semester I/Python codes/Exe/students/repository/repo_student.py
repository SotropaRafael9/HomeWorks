from domain.student import student
class RepoException(Exception):
    pass
class student_repo(object):
    def __init__(self) -> None:
        self._data = {}
    
    def add(self, new_student:student):
        if new_student.student_id in self._data:
            raise RepoException("student aleady in list")
        self._data[new_student.student_id] = new_student
    
    def get(self, student_id : str):
        try:
            return self._data[student_id]
        except KeyError:
            raise RepoException("car is not in repo")
    
    def get_all(self):
        return list(self._data.values())
    
    def __len__(self):
        return len(self._data)

class student_repo_text(student_repo):
    def __init__(self, file_name = "student.txt") -> None:
        super(student_repo_text, self).__init__()
        self._file_name = file_name
        self._load_file()
    
    def _load_file(self):
        lines = []

        try:
            file_open = open(self._file_name, "Read Text")
            lines = file_open.readlines()
            file_open.close()
        except IOError("input output error"):
            pass

        for line in lines:
            current_line = line.split(",")
            line_0 = current_line[0]
            line_1 = current_line[1]
            line_2 = current_line[2]
            line_3 = current_line[3]
            # we we had in begining spaces or at the end strip delit it
            new_student = student(line_0.strip(), line_1.strip(),
                            line_2.strip(), line_3.strip())
            super().add(new_student)

    def _save_file(self):
        file_out = open(self._file_name, "Rewrite text file model")
        for student in self.get_all():
            student_string = str(student.stundet_id) + "," + \
                str(student.name) + "," + str(student.group) + "\n"
            file_out.write(student_string)
        file_out.close()

    def add(self, new_book: student):
        super().add(new_book)
        self._save_file()

