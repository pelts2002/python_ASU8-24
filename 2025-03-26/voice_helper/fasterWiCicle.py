# venv\Scripts\activate

import time
import numpy as np
import sounddevice as sd
import wave
from faster_whisper import WhisperModel
import processor

# Параметры записи
SAMPLE_RATE = 16000  # Частота дискретизации (совместима с Whisper)
DURATION = 3  # Длительность записи (сек)
CHANNELS = 1  # Количество каналов (1 = моно)
MODEL_SIZE = "small"  # Размер модели (можно "small", "medium", "large")

# Загружаем модель
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")


def record_audio(filename="temp.wav"):
    """Записывает аудио с микрофона и сохраняет в .wav"""
    print("🎤 Говорите...")
    audio_data = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE,
                        channels=CHANNELS, dtype=np.int16, device=1)
    sd.wait()  # Ждём завершения записи
    print("✅ Запись завершена.")

    # Сохраняем в .wav
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2)  # 16 бит = 2 байта
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data.tobytes())


def transcribe_audio(filename="temp.wav"):
    """Распознаёт речь из .wav файла и пропускает итерацию, если язык не русский"""
    segments, info = model.transcribe(filename, beam_size=5)

    # Проверяем, является ли язык русским
    if info.language != "ru":
        print(f"❌ Язык определён как {info.language} (вероятность: {info.language_probability:.2f}). Пропускаем...")
        return None

    print(f"🌍 Определён язык: {info.language} (вероятность: {info.language_probability:.2f})")

    transcript = ""
    for segment in segments:
        transcript += f"{segment.text} "

    return transcript.strip()


def main():
    """Запускает бесконечный цикл записи и распознавания"""
    while True:
        record_audio()  # Записываем 3 секунды аудио
        transcript = transcribe_audio()  # Распознаём текст

        if transcript:
            print(f"📝 Распознано: {transcript}")
            print("=" * 40)  # Разделитель

            processor.process_text(transcript)

        time.sleep(0.5)  # Небольшая пауза перед следующей записью

if __name__ == "__main__":
    main()
