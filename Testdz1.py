import unittest
from unittest.mock import patch
import tkinter as tk
import sys
import io

# Импортируем основной класс приложения
from konfig1 import CommandLineApp  # Замените your_script_name на имя файла, где хранится ваш код


class TestCommandLineApp(unittest.TestCase):
    def setUp(self):
        # Создаем корневое окно Tkinter
        self.root = tk.Tk()
        self.app = CommandLineApp(self.root, path = 'example.zip')

    def tearDown(self):
        self.root.destroy()

    @patch('sys.exit')  # Мокируем sys.exit для предотвращения реального выхода
    def test_exit_command(self, mock_exit):
        # Симулируем ввод команды "exit"
        self.app.text_area.insert(tk.END, "exit\n")
        self.app.process_command(None)

        # Проверяем, что sys.exit был вызван
        mock_exit.assert_called_once()


if __name__ == "__main__":
    unittest.main()


