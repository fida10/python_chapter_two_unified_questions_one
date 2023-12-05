import chapter_two_first_set_questions as answers

import unittest


class TestGreetingMessage(unittest.TestCase):
    def test_greeting_message(self):
        self.assertEqual(
            answers.greeting_message(), "Welcome to Python!")

class TestUpdateStatus(unittest.TestCase):
    def test_update_status(self):
        status, updated_status = answers.update_status()
        self.assertNotEqual(status, updated_status)
        self.assertEqual(updated_status, "Python is fun!")

class TestComplimentGenerator(unittest.TestCase):
    def test_compliment_generator(self):
        self.assertEqual(answers.compliment_generator("Alex"), "Great job, Alex, on your Python progress!")

class TestNameVariations(unittest.TestCase):
    def test_name_variations(self):
        reversed_name, upper_name, letter_lines = answers.name_variations("Alex")
        self.assertEqual(reversed_name, "xelA")
        self.assertEqual(upper_name, "ALEX")
        self.assertEqual(letter_lines, "A\nl\ne\nx")

class TestHistoricalQuote(unittest.TestCase):
    def test_historical_quote(self):
        self.assertEqual(answers.historical_quote(), "Thomas Edison once said, 'Genius is one percent inspiration, ninety-nine percent perspiration.'")

class TestQuoteRepresentation(unittest.TestCase):
    def test_quote_representation(self):
        self.assertEqual(answers.quote_representation("Albert Einstein", "Life is like riding a bicycle. To keep your balance, you must keep moving."), "Albert Einstein once said, 'Life is like riding a bicycle. To keep your balance, you must keep moving.'")

class TestCleanName(unittest.TestCase):
    def test_clean_name(self):
        name = "\t\n Alex \n\t"
        stripped, lstripped, rstripped = answers.clean_name(name)
        self.assertEqual(stripped, "Alex")
        self.assertEqual(lstripped, "Alex \n\t")
        self.assertEqual(rstripped, "\t\n Alex")

class TestRemovePrefix(unittest.TestCase):
    def test_remove_prefix(self):
        self.assertEqual(answers.remove_prefix(
            "backup_python_notes.txt", "backup_"), "python_notes.txt")

class TestLuckySevenOperations(unittest.TestCase):
    def test_lucky_seven_operations(self):
        self.assertEqual(answers.lucky_seven_operations(), (7, 7, 7, 7))

class TestBirthYearMessage(unittest.TestCase):
    def test_birth_year_message(self):
        self.assertEqual(answers.birth_year_message(
            1990), "I was born in 1990.")

