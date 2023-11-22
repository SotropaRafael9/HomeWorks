class player:
    def __init__(self, player_id, name, stregth) -> None:
        self.__player_id = player_id
        self.__name = name
        self.__strength = stregth
    
    @property
    def player_id(self):
        return self.__player_id
    
    @player_id.setter
    def player_id(self, new_value):
        self.__name = new_value

    @property
    def name(self):
        return self.__name
    
    @property
    def strength(self):
        return self.__strength
    
    def __str__(self) -> str:
        return self.__player_id + " -> " + self.__name + " " + self.__strength

        