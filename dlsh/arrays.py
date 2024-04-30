# import numpy as np
import random
from collections import deque
import matplotlib.pyplot as plt



# Python = good for AI/ML and web dev
#        = dynamically-typed, types are inferred (to check the type of a variable: type(var))
#           dictionary type = key:value pairing type

if __name__ == "__main__":      # not necessary but use it for the code flow
    print("Hello World")

i = True
name = "Adam"

# CONDITIONAL STATEMENT

if i == True and name == "Adam":
    print("yey!")


# LOOPS

health = 100
while health > 0:
    print(health)
    health -= 25

favSongs = ["Set Fire to the Rain", "Don't Look Back in Anger", "Friend"]
for song in favSongs:
    print(song)

# (2d array)

treasure_map = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', 'X']
]

for row in treasure_map:
    for pixel in row:
        if pixel == 'X':
            print("I found the treasure!")
            break

# FUNCTIONS
            
def greet(n):
    return "Hello, " + name + "!"

print(greet(name))

# Lists

# Unlike in Java, lists in Python can store elements of different types
# Lists are dynamic (size can be changed)

winningNumbers = [7, 2, 13]
winningNumbers.append(6)
print("Last Element:", winningNumbers[-1])

winningLoto = []

while len(winningLoto) < 6:
    x = random.randint(1, 100)  # both included (== randrage(1, 101))
    if  x not in winningLoto:
        winningLoto.append(x)

print(winningLoto)

winningLoto[0] = 1
print(winningLoto)

# STACKS - uses: Web browser nav system, undo mechanisms in software, Syntax checking in IDEs, reversing text, Pathfinding algorithms (DFS)
# (A stack of plates)

# = LIFO Structure
# There is no built-in class in the standad library, but lists can implement them effectively
# append (add/push), pop (remove last item), to peek: [-1], len



def reverse_string(s):
    stack = []

    for char in s:
        stack.append(char)

    reversed_string = ""
    while stack:    # while stack is not empty
        reversed_string += stack.pop()

    return reversed_string

print(reverse_string("Axoloton"))


# QUEUES - uses: Job schedulling system (manage processes in operating systems), customer services (concert ticket sales system), searching algorithms (BFS)
# (Queue at a shop)

# = FIFO Structure
# Although lists in Python can function as a Queue, the Deque type is preffered
# Deque = Double ended queue
# Deque has a faster insertion/deletion at the beginning of list than regular list

# append/pop or enqueue/dequeue
# from collections import deque


fans = deque(["Josh", "Owen", "Emmett", "Lisa", "Oria", "Sheila"])
i = 0
while i < 5:
    print(fans.popleft(), "GOT A TICKET!")    # FIFO (first pops JOSH)
    i += 1

# DICTIONARY - use: hash a name to a bank account balance
    
# it is a type of hash map (maps a key to a value)
    
def count_word_fq(sentence):
    sentence = sentence.lower()
    sentence = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in sentence)
    words = sentence.split()
    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

sentence = """well HELLO!! I am so glad to see ye
            I've been waiting for ye ye know"""

frequencies = count_word_fq(sentence)
print (frequencies)

for term in frequencies:
    print("Word: ", term, "- Frequencies: ", frequencies[term])

# PYPLOT IN PYTHON
    
# Python is often used for data-centric purposes (data science, machine learning,...)
# Pyplot makes graphs
    
# Data

module = ["CS4221", "CS4182", "CS4043", "ET4162", "MA4402"]
grade = [96, 85, 87, 89, 93]

plt.bar(module, grade, color="green", alpha = 0.5)

plt.title("My Second Semester")
plt.xlabel("Module")
plt.ylabel("Grade")

plt.show()