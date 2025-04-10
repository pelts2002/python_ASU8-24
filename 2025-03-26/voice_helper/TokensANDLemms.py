import nltk
from nltk.tokenize import word_tokenize
import pymorphy3

nltk.download('punkt')  # Правильная загрузка токенизатора
morph = pymorphy3.MorphAnalyzer()

text = "Мальчики играли в футбол, а девочки рисовали на асфальте."
tokens = word_tokenize(text)

print("Токены:", tokens)

lemmas = [morph.parse(word)[0].normal_form for word in tokens]
print("Леммы:", lemmas)
