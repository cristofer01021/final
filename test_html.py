import unittest

class TestHTML(unittest.TestCase):
    def test_title(self):
        with open("index.html", "r") as file:
            content = file.read()
            self.assertIn("<title>Hola Mundo</title>", content)

if __name__ == '__main__':
    unittest.main()
