import unittest
from unittest.mock import MagicMock, patch
import tkinter as tk
import sys

class TestCommandLineApp(unittest.TestCase):
    @patch.object(tk.Tk, 'quit')
    def test_exit_command(self, mock_quit):
        # Создание фальшивого объекта Tk
        root = tk.Tk()

        # Инициализация приложения
        app = CommandLineApp(root)

        # Эмулируем ввод команды "exit" в поле
        app.text_area.insert(tk.END, "exit")

        # Вызываем обработчик команды
        app.process_command(None)

        # Проверяем, что метод quit() был вызван для завершения работы
        mock_quit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
