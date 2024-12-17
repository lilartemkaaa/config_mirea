import unittest
import subprocess

class TestParser(unittest.TestCase):

    def test_config_transformation(self):
        # Ожидаемый результат, который мы хотим получить в YAML
        expected_output = '''name: Bakery
products:
  - Bread
  - Croissants
  - Buns
bread_price: 100
croissant_price: 50
discount: 50
player: Player 1
levels:
  - Forest
  - Cave
  - Castle
weapons:
  - Sword
  - Bow
  - Shield
health: 100
attack: 50
total_power: 150
'''
        # Запускаем программу с файлом конфигурации
        result = subprocess.run(['python', 'dz3.py', 'config_3.txt'], capture_output=True, text=True)

        # Сравниваем результат работы программы с ожидаемым выводом
        self.assertEqual(result.stdout.strip(), expected_output.strip())

if __name__ == '__main__':
    unittest.main()
