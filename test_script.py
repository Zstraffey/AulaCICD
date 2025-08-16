import unittest 
from script import cumprimentar, conversar, despedir

class TestCumprimentar(unittest.TestCase):

    def test_cumprimentar(self):
        self.assertEqual(cumprimentar("Zimmermann"), "Olá Zimmermann")
        self.assertEqual(cumprimentar("Miguel"), "Olá Miguel")
        self.assertEqual(cumprimentar("Martins"), "Olá Martins")

    def test_conversar(self):
        self.assertEqual(conversar("Jujutsu Kaisen"), "Vamos falar de Jujutsu Kaisen")
        self.assertEqual(conversar("Sakamoto Days"), "Vamos falar de Sakamoto Days")

    def test_despedir(self):
        self.assertEqual(despedir("Amanhã"), "Adeus, nos vemos Amanhã")
        self.assertEqual(despedir("no Inferno"), "Adeus, nos vemos no Inferno")
    
    if __name__ == "__main__":
        unittest.main()