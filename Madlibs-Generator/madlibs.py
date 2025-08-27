import os

script_dir = os.path.dirname(os.path.abspath(__file__))  
file_path = os.path.join(script_dir, "story.txt")

with open(file_path, "r") as f:
    story = f.read()

words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_end and start_of_word != -1:
        word = story[start_of_word:i + 1]
        words.add(word)
        start_of_word = -1

answers = {}
placeholders = {
    "<adjective>": "a describing word (e.g., happy, scary, tiny, enormous)",
    "<animal>": "any animal (e.g., dog, cat, dragon, penguin)",
    "<object>": "a random object (e.g., ball, sword, phone, sandwich)",
    "<container>": "something that holds things (e.g., bag, backpack, box, pocket)",
    "<place>": "a location (e.g., park, castle, space, beach)",
    "<person>": "a type of person (e.g., wizard, teacher, pirate, astronaut)",
    "<food>": "something edible (e.g., pizza, apple, spaghetti, taco)",
    "<verb>": "an action word (e.g., run, jump, dance, sing)",
    "<monster>": "a creature (e.g., zombie, dragon, troll, alien)",
    "<exclamation>": "something you’d shout (e.g., Wow!, Oh no!, Yikes!)",
    "<funny object>": "something silly (e.g., rubber duck, banana, clown nose)",
    "<song>": "any song title (e.g., Happy Birthday, Baby Shark, Thriller)"
}

for placeholder, explanation in placeholders.items():
    answer = input(f"Please give me {explanation}: ")
    answers[placeholder] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)