'''Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.'''

from seminar_08.task_02.task02 import json_load
import pickle


def pickle_writer(file_name, pickle_data):
    with open(file_name, 'wb') as f:
        pickle.dump(pickle_data, f)


def pickle_read(file_name):
    with open(file_name, 'rb') as f:
        return pickle.load(f)


if __name__ == '__main__':
    pickle_writer('pickle_test.pkl', json_load('../task_04/s8_t04.json'))
    print(pickle_read('pickle_test.pkl'))
