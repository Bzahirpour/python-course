import random 

for i in range(3):
    print(random.random())



for i in range(3):
    print(random.randint(20, 30))



members = ['john', 'mary', 'bob']
leader = random.choice(members)
print(leader)



class Dice:
    def __init__(self, sides):
        self.sides  = (sides)

    def roll(self):
        results = []
        for i in range(2):
            results.append(random.randint(1, self.sides))
        final_result = tuple(results)
        return final_result

num_of_sides = input('how many sides does your dice have: ')
dice = Dice(int(num_of_sides))
print(dice.roll())