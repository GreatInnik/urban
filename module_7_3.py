class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line_words = line.lower().split()
                    cleaned_words = [word.strip("'.,=!?:;-") for word in line_words]
                    words.extend(cleaned_words)
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word.lower() in words:
                result[file_name] = words.index(word.lower())
        return result

    def count(self, word):
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            count = words.count(word.lower())
            if count > 0:
                result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

