'''
Напишите для задачи 1 тесты unittest. Проверьте следующие варианты:
возврат строки без изменений
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)
'''

import unittest
from task01 import del_symbol

text_original = 'my string'
text_upper = 'My String'
text_punctuation = 'my, string!'
text_foreign = 'my stringмоястрока'
text_all = 'My String_моя_строка!'


class TestDelSymbol(unittest.TestCase):

    def test_original(self):
        self.assertEqual(del_symbol(text_original), text_original)

    def test_upper(self):
        self.assertEqual(del_symbol(text_upper), text_original)

    def test_punctuation(self):
        self.assertEqual(del_symbol(text_punctuation), text_original)

    def test_foreign(self):
        self.assertEqual(del_symbol(text_foreign), text_original)

    def test_all(self):
        self.assertEqual(del_symbol(text_all), text_original)


if __name__ == '__main__':
    unittest.main(verbosity=0)
