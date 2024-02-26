from art import vs, logo
from game_data import data
from random import choice

class InvalidChoiceException(Exception):
    '''Raised when the user inputs anything other than a or b'''


print(logo)
testdata = data
guesses = 0

def get_choice(testdata):
    '''A function that takes the current state of the data and returns a random user from the current data'''

    return choice(testdata)

def remove_option(current_data, choice):
    '''A function that takes in the current list of users and a user to remove, removes the user from the list and returns the modified list'''

    current_data.remove(choice)
    return current_data

def get_winner(choicea, choiceb):
    '''takes in 2 people and returns the person with the highest 
    follower count'''
    counta = get_follower_count(choicea)
    countb = get_follower_count(choiceb)

    if counta > countb:
        return choicea
    elif countb > counta:
        return choiceb
    
def format_choice(choice):
    '''Takes in a user and formats the output string'''

    name = choice['name']
    followers = choice['follower_count']
    description = choice['description']
    country = choice['country']
    output = f"{name}, a {description}, from {country}"
    return output

def get_follower_count(user):
    '''A function that takes in a user and returns the follower 
       count as an integer'''
    
    return user['follower_count']

winner = get_choice(data)
play = True
while play:
    if guesses == 0:
        choice_a = get_choice(testdata)
        testdata = remove_option(testdata, choice_a)
    else:
        choice_a = winner
    choice_b = get_choice(testdata)
    testdata = remove_option(testdata, choice_b)

    first = f"Compare A: {format_choice(choice_a)}"
    second = f"Against B: {format_choice(choice_b)}"

    winner = get_winner(choice_a, choice_b)
    print(first)

    print(vs)

    print(second)

    while True:
        try:
            guess = input("Who has more followers? A or B: ").upper()
            if guess not in ['A', 'B']:
                raise InvalidChoiceException
            break
        except InvalidChoiceException:
            print(f"{guess} is an invalid entry please enter either A or B")
    if guess == "A" and winner['name'] == choice_a['name']:
        guesses += 1
    elif guess == "B" and winner['name'] == choice_b['name']:
        guesses += 1
    else:
        play = False
        print(f"you've lost with {guesses} number of correct guesses")
