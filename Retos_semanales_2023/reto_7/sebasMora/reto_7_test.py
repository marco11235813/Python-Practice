import unittest
import reto_7


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_valor_indefinido(self):
        combinacion = [(1, 2)]
        resultado = reto_7.ganador(combinacion)
        self.assertEqual(resultado, "Entrada incorrecta")

    def test_ganador_2(self):
        combinacion = [("🗿", "✂️"), ("✂️", "🗿"), ("📄", "✂️")]
        resultado = reto_7.ganador(combinacion)
        self.assertEqual(resultado, "Player 2")


if __name__ == "__main__":
    unittest.main()
