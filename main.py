# Katelyn Curtiss 
# January 29 2025
# Dictionary Quiz Game

score = 0 
questions = [
    {
        'question': "What year did World War I ___ start?",
        'answer': "1914"
    },
      {
        'question': "What year did World War II ___ start?",
        'answer': "1939"
    },
      
      {
        'question': "How many years did World War II  ___ last?",
        'answer': "6"
    },
    
    {
        'question': "In World War II Germany invaded ___ ,which started the war?",
        'answer': "Poland"
    },
    
    {
        'question': "What was the deadliest war ___ ?",
        'answer': "World War II"
    }
]

for question in questions:
    question_text = question.get("question")
    print(question_text)

    user_answer = input("Enter answer: ")
    correct_answer = question.get("answer")
    
    if user_answer == correct_answer:
       score = score + 10

print("Your score is = ", score)