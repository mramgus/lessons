import pprint

word = 'TEXT'  # искомое слово



class WordsFinder:
    res = {}  # для вывода результатов

    def __init__(self, *file_names):
        self.file_names = list(file_names)  # атрибут file_names в виде списка

    def get_all_words(self):
        all_words = {}  # 1 Создайте пустой словарь all_words
        punctuation = ',.=!?;:'  # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
        for filename in self.file_names:  # 2 Переберите названия файлов и открывайте каждый из них, используя with.
            words = []
            clear_line = ''  # обнуляем строки
            with open(filename, "r", encoding='utf-8') as file:
                for line in file:
                    line = line.lower()  # Для каждого файла считывайте единые строки, переводя их в нижний регистр
                    while line.find(' — ') != -1:  # 4 Избавьтесь от пунктуации [' — '] в строке.
                        line = line.replace(' — ', " ")  # (тире обособлено пробелами, это не дефис в слове)
                        continue
                    for char in line:  # 4 Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':'] в строке.
                        if not char in punctuation:
                            clear_line += char
                words = clear_line.split()  # Разбейте эту строку на элементы списка методом split().
            all_words[filename] = words  # В словарь all_words запишите полученные данные,
            #   ключ - название файла, значение - список из слов этого файла.
            self.res.clear()
        return all_words

    def find(self, word):  # - метод, где word - искомое слово.
        # f_dict = {}
        for names, words in self.get_all_words().items():
            place = 0
            if word.lower() in words:
                place = words.index(word.lower()) + 1
                self.res[names] = place
        return self.res

    def count(self, word):  # count(self, word) - метод, где word - искомое слово.
        for names, words in self.get_all_words().items():
            counter = 0
            if word.lower() in words:
                counter = words.count(word.lower())
                self.res[names] = counter
        return self.res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find(word), f' # Позиция первого искомого слова "{word}" в списке:', *finder2.res.values())
print(finder2.count(word), f' # Количество повторений найденного слова "{word}": ', *finder2.res.values(), '\n')

