# Declare 2 variables set and assign random values from game_data dict
from game_data import data
from random import randint

randInt = []
for i in range(0,2):
    generate_randint = randint(0, len(data))
    randInt.append(generate_randint)

a_MetaData = data[randInt[0]]
b_MetaData = 


a_Initial = "Compare A: " + a_MetaData['name'] + ", a " + a_MetaData['description'] + ", from " + a_MetaData['country'] + "."

print(a_Initial)
# ask user to input there guess
# Compare between two variables
# correct answer will lead to increase in score point by 1
# assign the correct choosen value to the first one and take random second value for next comparison
# wrong ans will end the game