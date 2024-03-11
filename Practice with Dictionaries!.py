# Evan Wallace
# Practice in Class 8: Use Collections
# IT 111

# Improvements made by using collections:

# I made use of dictionaries to store questions and their corresponding options in, and
# did the same with the answers.

# The functions askQuestion and answerQuestion have been modified to utilize these dictionaries for improved efficiency and readability.
# Input is normalized to uppercase to handle variations in user input.

def askQuestion():
    questions = {
        1: {
            'question': "Which of the following video games was published by Nintendo?",
            'options': {
                1: "Assassin's Creed II",
                2: "Sonic the Hedgehog",
                3: "Pokemon Black 2 Version"
            }
        },
        2: {
            'question': "Which cable is used to connect a graphics card to a power supply within a computer?",
            'options': {
                1: "SATA cable",
                2: "VGA cable",
                3: "PCIe"
            }
        },
        3: {
            'question': "Which film won best picture at the Oscars in 1978?",
            'options': {
                1: "The Goodbye Girl",
                2: "Star Wars",
                3: "Annie Hall"
            }
        }
    }
    
    choice = input("Do you want to see a question? (Y/N)").upper()
    
    if choice == 'Y':
        whichQuestion = int(input('Which question?: Enter 1, 2, or 3: '))
        if whichQuestion in questions:
            questionInfo = questions[whichQuestion]
            print(questionInfo['question'])
            for optionNum, option in questionInfo['options'].items():
                print(f"{optionNum}. {option}")
        else:
            print("Invalid question number!")
        return whichQuestion
    else:
        print("See ya!")
        return None

def answerQuestions(questionNum, answer):
    answers = {
        1: {1: "Incorrect! The Assassin's Creed series was developed by Ubisoft.",
            2: "Close! While the Sonic franchise was developed by Sega, there have been multiple crossovers with Nintendo characters.",
            3: "Correct! The Pokemon games are owned by Nintendo, however they are developed by a studio called Game Freak."},
        2: {1: "Incorrect! The SATA cable is used to connect SSD drives to power.",
            2: "Nope! VGA cables are used to connect older monitors to the back of an I/O panel on older motherboards.",
            3: "Correct!"},
        3: {1: "Incorrect!",
            2: "Incorrect!",
            3: "Correct!"}
    }
    
    if questionNum in answers:
        if answer in answers[questionNum]:
            print(answers[questionNum][answer])
        else:
            print("Invalid answer choice!")
    else:
        print("Invalid question number!")

whichQuestion = askQuestion()
if whichQuestion is not None:
    answer = int(input("Enter your answer 1, 2, or 3: "))
    answerQuestions(whichQuestion, answer)
