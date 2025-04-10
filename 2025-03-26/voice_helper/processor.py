# venv\Scripts\activate

import os
import wave
import pyaudio
import sys
import webbrowser
import nltk
from nltk.tokenize import word_tokenize
import pymorphy3
from sympy.strategies.core import switch

nltk.download('punkt')  # Правильная загрузка токенизатора
morph = pymorphy3.MorphAnalyzer()

RESPONSES = {
    "привет": "audioFiles/hello.wav",
    "как дела": "audioFiles/aboutme.wav",
    "пока": "audioFiles/goodbye.wav"
}


def play_audio(filename):
    """Воспроизводит аудиофайл"""
    if not os.path.exists(filename):
        print(f"⚠️ Файл {filename} не найден!")
        return

    chunk = 1024
    wf = wave.open(filename, "rb")
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pa.get_format_from_width(wf.getsampwidth()),
                     channels=wf.getnchannels(),
                     rate=wf.getframerate(),
                     output=True)

    data = wf.readframes(chunk)
    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    pa.terminate()
    wf.close()

    print(f"🔊 Воспроизведён файл: {filename}")


def check_patterns(text):
    """Проверяет, содержит ли текст ключевые слова и запускает соответствующий аудиофайл"""
    for pattern, audio_file in RESPONSES.items():
        if pattern in text.lower():  # Игнорируем регистр
            print(f"🔍 Найдено ключевое слово: '{pattern}'")
            play_audio(audio_file)

def open_weather(text):
    """Открывает браузер с поиском 'Погода в <город>'"""
    words = text.lower().split()
    
    if len(words) >= 3 and words[0] == "погода" and words[1] == "в":
        city = " ".join(words[2:])  # Берём всё после "погода в"
        print(f"🌤 Ищу погоду для: {city}")
        url = f"https://www.google.com/search?q=Погода+в+{city}"
        webbrowser.open(url)
        return True  # Команда найдена
    
    return False  # Команда не найдена

def process_text(text):
    print(f"📌 Обрабатываем текст: {text}")

    # Токенизация
    tokens = word_tokenize(text)
    print(f"🔹 Токены: {tokens}")

    # Лемматизация
    lemmas = [morph.parse(word)[0].normal_form for word in tokens]
    lemmatized_text = " ".join(lemmas)
    print(f"🔹 Лемматизированный текст: {lemmatized_text}")

    # Проверяем, нужно ли открыть погоду
    if open_weather(lemmatized_text):  
        return  # Если нашли команду для погоды, дальше не идём

    # Проверяем аудиокоманды
    check_patterns(lemmatized_text)  

    # Сохраняем обработанный текст
    with open("recognized_text.txt", "a", encoding="utf-8") as file:
        file.write(lemmatized_text + "\n")

    print("✅ Текст сохранён в recognized_text.txt")