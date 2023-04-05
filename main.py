import random
import jokes

def print_random_joke():
    joke = random.choice(jokes.jokes)
    print(joke)

print_random_joke()
