import unittest 
from script import cumprimentar, email, senha

class TestCumprimentar(unittest.TestCase):

    def test_cumprimentar(self):
        self.assertEqual(cumprimentar("Zimmermann"), "Olá Zimmermann")
        self.assertEqual(cumprimentar("Miguel"), "Olá Miguel")
        self.assertEqual(cumprimentar("Martins"), "Olá Martins")

    def test_email(self):
        self.assertEqual(email("migmig.zimmer@gmail.com"), "Seu e-mail é migmig.zimmer@gmail.com")
        self.assertEqual(email("newtetcc2025@gmail.com"), "Seu e-mail é newtetcc2025@gmail.com")
        self.assertEqual(email("miguel.silva190@etec.sp.gov.br"), "Seu e-mail é miguel.silva190@etec.sp.gov.br")

    def test_senha(self):
        self.assertEqual(senha("123456"), "Sua senha é 123456")
        self.assertEqual(senha("654321"), "Sua senha é 654321")
    
    if __name__ == "__main__":
        unittest.main()