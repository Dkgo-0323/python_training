from random import randint
class Die():
    """模拟骰子"""
    
    def __init__(self,sides=6):
        """定义骰子的属性"""
        self.sides = sides

    def roll_dice(self):
        """模拟摇骰子"""
        x = randint(1,6)
        print(x)

my_dice = Die()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()
my_dice.roll_dice()