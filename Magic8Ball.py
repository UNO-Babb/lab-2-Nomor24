# Magic8Ball.py
# Name:
# Date:
# Assignment:

import random

def main():
    # Create a list of possible responses.
    answers = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",  
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes - definitely.",  
        "You may rely on it."
    ]
    
    # Display the title of the program.
    print("Magic 8 Ball")
    
    # Prompt the user for their question.
    question = input("Ask a yes/no question: ")
    
    # Answer the question randomly using random.choice().
    response = random.choice(answers)
    
    # Display the random response.
    print("\nMagic 8 Ball says: " + response)

if __name__ == '__main__':
    main()
