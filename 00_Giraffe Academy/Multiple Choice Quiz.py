from Question import Question

question_prompt = [
    "Which wheel brand are consider Real Wheels?\n(a) ESR's\n(b) Rota's\n(c) Rays\n\n",
    "Which car drivetrain is RWD?\n(a) 2002 Honda Civic\n(b) 2010 Lancer Evo\n(c) 2015 Subaru BRZ\n\n",
    "Which car is faster?\n(a) BMW Z4\n(b) Toyota MR Spyder\n(c) Subaru BRZ\n\n"
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "a"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)