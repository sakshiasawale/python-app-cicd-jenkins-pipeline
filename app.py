from flask import Flask, render_template
import re

app = Flask(__name__)

# Sum of digits of a number until it becomes one
def num2digit(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    if total > 9:
        return num2digit(total)
    return total

# Count the sum of alphabets in a word for "numerology"
def numerology(name): 
    total = 0
    for ch in name:
        if ch in ['a', 'r', 's']:
            total += 1
        elif ch in ['b', 'q', 't']:
            total += 2
        elif ch in ['c', 'p', 'u']:
            total += 3
        elif ch in ['d', 'o', 'v']:
            total += 4
        elif ch in ['e', 'n', 'w']:
            total += 5
        elif ch in ['f', 'm', 'x']:
            total += 6
        elif ch in ['g', 'l', 'y']:
            total += 7
        elif ch in ['h', 'k', 'z']:
            total += 8
        elif ch in ['i', 'j']:
            total += 9
        else:
            total = -9999  # unexpected character
            break

    if total > 0:
        total = num2digit(total)

    # Random messages based on the digit
    messages = {
        1: "You are a sad person",
        2: "You are an angry person",
        3: "An introvert",
        4: "You have a golly nature",
        5: "You like to party",
        6: "Your revenge is bitter",
        7: "A nerd",
        8: "too much attitude",
        9: "you are a shy person"
    }

    return messages.get(total, "I know who you are. THE ROBOT :P")


# Main page route
@app.route('/')
def hello():
    # FIXED message to match test expectation
    return render_template('index.html', message="hello brother, Lets have some fun!!", imgname="hello")


# Dynamic route for a username
@app.route('/<username>')
def hello_user(username):
    username = username.lower()
    result = numerology(username)
    return render_template('index.html', message=f"{username}: {result}", imgname="jenkins")


if __name__ == '__main__':
    # Use debug=True for development
    app.run(host='0.0.0.0', debug=True)
