import random


def generate_question():
    # Generate a random question from the questions dictionary.
    question_name = random.choice(list(questions.keys()))
    question_info = questions[question_name]
    options = question_info["options"]
    # Shuffle options including the correct answer
    random.shuffle(options)
    return question_name, options, question_info["answer"]


def ask_question(question, options, correct_answer):
    # Ask the user a multiple-choice question and evaluate their answer.
    print("\n" + question)

    # Shuffle options for presentation
    shuffled_options = options.copy()
    random.shuffle(shuffled_options)

    for index, option in enumerate(shuffled_options):
        print(f"{index + 1}. {option}")

    correct_answer_index = shuffled_options.index(correct_answer)  # Index of correct answer

    while True:
        user_input = input("Enter the number of your answer: ")
        if user_input.isdigit():
            user_answer = int(user_input) - 1
            if 0 <= user_answer < len(options):
                break
            else:
                print("Please enter a valid option number.")
        else:
            print("Please enter a valid option number.")

    if user_answer == correct_answer_index:
        print("Correct!")
        return 1  # Add 1 point for correct answer
    else:
        print(f"Incorrect. The correct answer is: {correct_answer}")
        return 0  # No points for incorrect answer


def yes_no(prompt):
    # Prompt user for a yes or no response.
    while True:
        response = input(prompt).strip().lower()
        if response in ("yes", "no", "y", "n"):
            return response
        else:
            print("Please enter 'yes' or 'no'.")


def int_check(prompt, low=None, high=None):
    # Prompt user for an integer within a given range.
    while True:
        try:
            value = int(input(prompt))
            if (low is None or value >= low) and (high is None or value <= high):
                return value
            else:
                if low is not None and high is not None:
                    print(f"Please enter an integer between {low} and {high}.")
                elif low is not None:
                    print(f"Please enter an integer greater than or equal to {low}.")
                elif high is not None:
                    print(f"Please enter an integer less than or equal to {high}.")
        except ValueError:
            print("Please enter an integer.")


def string_checker(prompt):
    # Prompt user for a string response.
    while True:
        response = input(prompt).strip().lower()
        if response in ("yes", "no", "y", "n"):
            return response
        else:
            print("Please enter 'yes' or 'no'.")


# Define questions separately for readability
questions = {
    "capital_of_australia": {
        "question": "What is the capital of Australia?",
        "options": ["Sydney", "Canberra", "Darwin"],
        "answer": "Canberra"
    },
    "largest_planet": {
        "question": "What is the largest planet in our solar system?",
        "options": ["Jupiter", "Saturn", "Mars"],
        "answer": "Jupiter"
    },
    "romeo_and_juliet_author": {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Jane Austen", "Charles Dickens"],
        "answer": "William Shakespeare"
    },
    "resigning_us_president": {
        "question": "Who is currently the only President of The U.S.A to resign?",
        "options": ["Bill Clinton", "James Madison", "Richard Nixon"],
        "answer": "Richard Nixon"
    },
    "largest_human_organ": {
        "question": "What is the largest organ in the human body?",
        "options": ["Skin", "Liver", "Heart"],
        "answer": "Skin"
    },
    "smallest_country_by_land_area": {
        "question": "Which country is the smallest in the world by land area?",
        "options": ["Monaco", "Vatican City", "San Marino"],
        "answer": "Vatican City"
    },
    "longest_river": {
        "question": "What is the longest river in the world?",
        "options": ["Amazon River", "Nile River", "Yangtze River"],
        "answer": "Nile River"
    },
    "great_gatsby_author": {
        "question": "Who wrote 'The Great Gatsby'?",
        "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "William Faulkner"],
        "answer": "F. Scott Fitzgerald"
    },
    "smallest_bone_in_human_body": {
        "question": "What is the smallest bone in the human body?",
        "options": ["Femur", "Cochlea", "Patella"],
        "answer": "Cochlea"
    },
    "unelected_us_president": {
        "question": "Who is the only person in United States history, to have been president without being elected President or vice president?",
        "options": ["William Taft", "George H.W Bush", "Gerald Ford"],
        "answer": "Gerald Ford"
    },
    "capital_of_liechtenstein": {
        "question": "What is the capital of Liechtenstein?",
        "options": ["Vaduz", "Bern", "Luxembourg City"],
        "answer": "Vaduz"
    },
    "year_of_magna_carta": {
        "question": "In which year was the Magna Carta signed?",
        "options": ["1215", "1066", "1348"],
        "answer": "1215"
    },
    "discoverer_of_penicillin": {
        "question": "Who discovered penicillin?",
        "options": ["Alexander Fleming", "Louis Pasteur", "Joseph Lister"],
        "answer": "Alexander Fleming"
    },
    "sistine_chapel_ceiling_painter": {
        "question": "Who painted the ceiling of the Sistine Chapel?",
        "options": ["Michelangelo", "Leonardo da Vinci", "Raphael"],
        "answer": "Michelangelo"
    },
    "former_name_of_ethiopia": {
        "question": "Which African country was formerly known as Abyssinia?",
        "options": ["Ethiopia", "Egypt", "Eritrea"],
        "answer": "Ethiopia"
    },
    "library_material_classification_system": {
        "question": "Which system is used for classifying library materials based on subject categories, with numbers ranging from 000 to 999?",
        "options": ["Library of Congress Classification", "Dewey Decimal System", "Harvard Classification System"],
        "answer": "Dewey Decimal System"
    },
    "year_of_norman_invasion": {
        "question": "In what year did the Norman invasion of England occur?",
        "options": ["1066", "1200", "1400"],
        "answer": "1066"
    }
}

while True:  # Start of the main loop for restarting the quiz
    # Initialize game variables
    points = 0
    highest_score = float('-inf')
    lowest_score = float('inf')
    game_history = []
    questions_answered = 0
    questions_correct = 0

    print()
    print("🎭🎭🎭 Welcome to the General Knowledge Quiz! 🎭🎭🎭")
    print()

    # Game parameter customization
    total_rounds = int_check("Enter the total number of rounds (default is 1): ", 1)
    num_questions_per_round = int_check("Enter the number of questions per round (default is 3): ", 1)

    # Display instructions
    want_instructions = yes_no("Do you want to read the instructions? ")
    if want_instructions == "yes" or want_instructions == "y":
        print('''
        ⭐⭐⭐⭐ Instructions ⭐⭐⭐⭐

        In this quiz, you will be asked a series of questions,
        each with three options. Enter the number corresponding to your answer.

        You will earn 1 point for each correct answer.

        Let's begin! ''')

    elif want_instructions == "no" or want_instructions == "n":
        print()
    else:
        print("Please enter yes / no")

    # Game loop starts here
    for round_count in range(1, total_rounds + 1):
        print(f"\n💿💿💿 Round {round_count} 💿💿💿")
        round_points = 0  # Store points earned in each round
        round_questions_answered = 0  # Track the number of questions answered in this round
        round_questions_correct = 0  # Track the number of questions answered correctly in this round
        for _ in range(num_questions_per_round):
            if not questions:  # Check if all questions have been asked
                break
            # Generate a question
            question_name, options, answer = generate_question()

            # Ask the user the question
            points = ask_question(questions[question_name]["question"], options, answer)

            # Update statistics for this round
            round_points += points
            round_questions_answered += 1
            if points == 1:
                round_questions_correct += 1

            # Remove the asked question from the dictionary
            del questions[question_name]

        # Update overall statistics
        points += round_points
        questions_answered += round_questions_answered
        questions_correct += round_questions_correct

        # Update highest and lowest scores
        lowest_score = min(lowest_score, round_points)
        highest_score = max(highest_score, round_points)

        # If there are no more questions left
        if not questions:
            print("😲😲😲 Oh no! There are no more questions! 😲😲😲")

    # Calculate statistics
    questions_incorrect = questions_answered - questions_correct
    percent_correct = questions_correct / questions_answered * 100 if questions_answered > 0 else 0
    percent_incorrect = questions_incorrect / questions_answered * 100 if questions_answered > 0 else 0

    # Output game statistics
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"👍 Questions Correct: {questions_correct}/{questions_answered} ({percent_correct:.2f}%) \t"
          f"😥 Questions Incorrect: {questions_incorrect}/{questions_answered} ({percent_incorrect:.2f}%)")
    print(f"Highest Score For A Round: {highest_score}\t"
          f"Lowest Score For A Round: {lowest_score}\t")

    # Ask if the user wants to restart
    restart = yes_no("\nDo you want to restart the quiz? ")
    if restart == "no" or restart == "n":
        print("💕💕💕 Thank you for playing! Goodbye! 💕💕💕")
        break  # End the main loop and exit the program
