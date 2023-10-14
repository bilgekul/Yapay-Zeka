class Space_Game():
    _alien_color : str
    def __init__(self,alien_color) -> str:
        self._alien_color = alien_color
    @property
    def color(self):
        if self._alien_color == "green":
            return ("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
        else:
            return ("Tebrikler, yeşil olmayan uzaylıya ateş ettiğiniz için 10 puan kazandınız")


ch = input("Please choose any color: ")
game = Space_Game(ch)
print(game.color)

class New_Space_Game():
    _alien_color : str
    def __init__(self,alien_color) -> str:
        self._alien_color = alien_color
    @property
    def color(self):
        if self._alien_color == "green":
            return ("Tebrikler, yeşil uzaylıya ateş ettiğiniz için 5 puan kazandınız")
        elif self._alien_color == "red":
            return ("Tebrikler, kırmızı uzaylıya ateş ettiğiniz için 15 puan kazandınız")
        elif self._alien_color == "yellow":
            return ("Tebrikler, sarı uzaylıya ateş ettiğiniz için 10 puan kazandınız")

ch2 = input("Please choose any color: ")
game = New_Space_Game(ch2)
print(game.color)      
