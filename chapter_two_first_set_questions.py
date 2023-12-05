"""
3-1. Greeting Variable:

Task: Create a variable named greeting and assign it a welcoming message. Print this message.

Unit Test: Check if the printed message matches the assigned value in the greeting variable.

"""

def greeting_message():
    x = "Welcome to Python!"
    return x

"""
3-2. Updating Status:

Task: Assign a status message to a variable named status. Print the message. 
Then, update the status variable to a different message and print the new message.

Unit Test: Verify that the two printed messages are different and match their respective assignments.

"""

def update_status():
    status = "Python is hard"
    print(status)
    update_status = "Python is fun!"
    print(update_status)
    return status, update_status

"""

3-3. Compliment Generator:

Task: Use a variable to represent a person's name and print a personalized compliment for them, 
like "Great job, Alex, on your Python progress!"

Unit Test: Ensure the printed message includes the person's name and a compliment.

"""
#        self.assertEqual(compliment_generator("Alex"), "Great job, Alex, on your Python progress!")
def compliment_generator(name):
    return (f"Great job, {name}, on your Python progress!")
"""

3-4. Name Variations:

Task: Store a person's name in a variable and print the name in reversed order, 
in all caps, and with each letter as a separate line.

Unit Test: Check if each printed format of the name is correct.

unit test: 
        reversed_name, upper_name, letter_lines = name_variations("Alex")
        self.assertEqual(reversed_name, "xelA")
        self.assertEqual(upper_name, "ALEX")
        self.assertEqual(letter_lines, "A\nl\ne\nx")
""" 
def name_variations(name: str):
    reversed_name = ''.join(reversed(name));
    upper_case = name.upper();
    separated_lines = '\n'.join(list(name))
    print(separated_lines)
    
    return reversed_name, upper_case, separated_lines
"""

3-5. Historical Quote:

Task: Find a historical quote and print it along with the author's name in a format similar to: 
"Thomas Edison once said, 'Genius is one percent inspiration, ninety-nine percent perspiration.'"

Unit Test: Verify the correct formatting of the printed quote and author.

    def test_historical_quote(self):
        self.assertEqual(historical_quote(), "Thomas Edison once said, 
        'Genius is one percent inspiration, ninety-nine percent perspiration.'")

"""
def historical_quote():
    author = 'Thomas Edison'
    quote = 'Genius is one percent inspiration, ninety-nine percent perspiration.'
    return (f"{author} once said, '{quote}'")
"""

3-6. Quote Representation:

Task: Repeat 3-5, but use two variables: historical_figure for the name and quote for the quote. 
Print them together.

Unit Test: Check if the printed message correctly combines both variables.

    def test_quote_representation(self):
        self.assertEqual(quote_representation("Albert Einstein", "Life is like riding a bicycle. To keep your balance, you must keep moving."), "Albert Einstein once said, 'Life is like riding a bicycle. To keep your balance, you must keep moving.'")

"""


def quote_representation(historical_figure, quote):
    return (f"{historical_figure} once said, '{quote}'")

"""

3-7. Name Clean-Up:

Task: Assign a name with leading and trailing whitespace and newlines to a variable. Print it with whitespace, and then use strip(), lstrip(), and rstrip() to clean it up.

Unit Test: Confirm that each method removes the correct whitespace.

3-8. File Renaming:

Task: Use the removeprefix() method on a filename variable (e.g., 'backup_python_notes.txt') to display the filename without a specific prefix like 'backup_'.

Unit Test: Ensure the output is correctly stripped of the prefix.

3-9. Lucky Number Seven:

Task: Perform addition, subtraction, multiplication, and division to get the number 7. Print each operation.

Unit Test: Verify that each operation correctly results in the number 7.

3-10. Birth Year:

Task: Store your birth year in a variable and print a message like "I was born in 1990."

Unit Test: Check if the message correctly displays the birth year.

3-11. Code Annotation:

Task: Add a comment explaining the purpose of one of your previous exercises. Include your name and the date.

Unit Test: Review the comment to ensure it explains the program's purpose.

3-12. Pythonic Principles:

Task: Execute import antigravity in a Python session and briefly describe the comic it shows.

Unit Test: Summarize the theme or main idea of the comic.
"""