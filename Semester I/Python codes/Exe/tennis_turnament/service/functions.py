from domain.player_class import player
class Service:
    
    def __init__(self, repository) -> None:
        self.__repository = repository

    def add_service(self, player_id, author, title):
        self.save_to_history()
        new_book = player(player_id, author, title)
        self.__repository.add(new_book)

    def get_rep_service(self):
        l = sorted(self.__repository.get_all(), key = lambda X : X.strength)
        return l
    
    # the function remove_by_firs_word 
    def remove_by_first_word(self, word):
        self.save_to_history()
        for player in self.__repository.get_all():
            if player.title[:len(word)] == word:
                self.__repository.remove(player.book_id)
    def remove_by_strength(self):
        for player in self.__repository.get_all():
            if 
    def power_of_2(self):

        n = 1
        z= len (self.__repository.get_all())
        while n <= z:
            n=n*2
        n/=2
        return n

    def pair_players(self):
        if self.__repository == '5':
            remove_by_strength