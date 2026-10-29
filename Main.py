# Scott Mason
# Premise: A basic general knowledge quiz

"""This is a basic General Knowledge Quiz."""
__author__ = "Scott Mason"

def welcome_player(name):
    # A string + operator takes 2 strings and joins them in one print statement:
    print("Hello", name + ", welcome to the quiz and good luck!!")

def main():
    total_questions = 3
    correct_answers = 0
    total_points = 0
    streak = 0

    # A string * operator takes the string "=" and repeats it 30 times:
    print("="*30)
    print("GENERAL KNOWLEDGE QUIZ!")
    print("="*30)

    name = input("What is your name? ")
    welcome_player(name)
    print("="*30)

    for x in range(3, 0, -1):
        print(x)
    print("GO!")
    print("="*30)

    # Quiz starts here:

    print("Question 1: Who painted the Mona Lisa?")
    print("-"*30)
    print("A: Leonardo Da Vinci")
    print("B: Vincent Van Gogh")
    print("C: Pablo Picasso")
    print("D: Michaelangelo")
    print("-"*30)
    
    answering_question = True

    while answering_question == True: 
        answer = input("Which do you choose? ")

        if answer.lower() in ("a", "b", "c", "d"):
            answering_question = False
        else:
            print("Invalid answer. Try again.")
    print("-"*30)

    if answer == "A" or answer == "a":
        print("CORRECT!")
        # Adding points to the players score, using the numeric operator "+":
        total_points += 25
        streak += 1
        correct_answers += 1
    else:
        print("INCORRECT! The answer was A!")

    print("="*30)

    print("Question 2: What is the largest planet in our Solar System?")
    print("-"*30)
    print("A: Saturn")
    print("B: Neptune")
    print("C: Jupiter")
    print("D: Mars")
    print("-"*30)

    answering_question = True

    while answering_question == True: 
        answer = input("Which do you choose? ")

        if answer.lower() in ("a", "b", "c", "d"):
            answering_question = False
        else:
            print("Invalid answer. Try again.")
    print("-"*30)

    if answer == "C" or answer == "c":
        print("CORRECT!")
        total_points += 25
        streak += 1
        correct_answers += 1
    else:
        print("INCORRECT! The answer was C!")
        streak = 0
        # Checks if score > 10, removes 10 points using the numeric operator "-":
        if total_points > 10:
            total_points -= 10

    print("="*30)

    print("Question 3: What gas do humans need to survive?")
    print("-"*30)
    print("A: CO^2")
    print("B: Oxygen")
    print("C: Helium")
    print("D: Nitrogen")
    print("-"*30)

    answering_question = True

    while answering_question == True: 
        answer = input("Which do you choose? ")

        if answer.lower() in ("a", "b", "c", "d"):
            answering_question = False
        else:
            print("Invalid answer. Try again.")
    print("-"*30)

    if answer == "B" or answer == "b":
        print("CORRECT!")
        total_points += 25
        streak += 1
        correct_answers += 1
    else:
        print("INCORRECT! The answer was B!")
        streak = 0
        # Checks if score > 10, removes 10 points using the numeric operator "-":
        if total_points > 10:
            total_points -= 10

    print("="*30)

    # End of quiz:

    print("Statistics:")

    # Using the numeric operator "/", we can calculate the % the player scored:
    percentage = (correct_answers/total_questions)*100
    if percentage >= 80:
        print("You got:", str(percentage) + "%", "on this quiz! Great job!")
    elif percentage >= 60:
        print("You got:", str(percentage) + "%", "on this quiz! You did alright!")
    else:
        print("You got:", str(percentage) + "%", "on this quiz! You failed.")

    if not correct_answers > 0:
        print("You didn't get any questions right!")

    # Using the numeric operator "**", we can give a streak bonus to total points!:
    streak_bonus = streak**2

    if streak > 0 and total_points >=25:  
        print("Since your streak was", str(streak) + ", you got an extra", streak_bonus, "points!")

    # Using the numeric operator "//", we can make a new int "stars"
    # Stars will go up by 1 for every 50 points:
    stars = (total_points + streak_bonus) // 50
    print("You got", stars, "star(s) on this quiz.")

    # Using "%", we can tell the player how many points towards their next star:
    next_star = (total_points + streak_bonus) % 50
    print("You have", str(next_star) + "/50", "points towards gaining another star!")

    # Using "*", we can tell the player the maximum points they could've scored
    # The maximum points includes the maximum streak bonus the player can get:
    max_number_of_points = (total_questions * 25) + total_questions**2
    if total_points + streak_bonus != max_number_of_points:
        print("The maximum points you could've scored was", max_number_of_points)

    # Using end= joins 2 lines of code on one line rather than going to a new one:
    print("Your final score is:", end=" ")
    # Using sep= separates the multiple values in the print statement with a space:
    print(total_points + streak_bonus, "points!", sep=" ")

if __name__ == "__main__":
    main()
