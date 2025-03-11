"""Для моего проекта по алгоритму фонтанного преобразования (распознавание цифр и чисел)
на изображениях, я использовал технологию оптического распознавания символов (OCR) с
библиотекой Tesseract. Это такой инструмент, который помогает вытащить текст, включая цифры,
из картинок. Он использует разные штуки, типа обработки изображений, пороговой обработки и размытия.
Я настроил Tesseract так, чтобы он работал только с цифрами, и это помогло мне получить более
точные результаты для моей задачи."""

import pytesseract
from PIL import Image
import cv2
import numpy as np
import os

# Путь к папке с изображениями
input_directory = 'images'  # Папка images должна находиться в той же директории, что и скрипт

# Получаем список всех файлов в папке images
image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

# Проходим по каждому файлу в папке
for image_file in image_files:
    # Формируем полный путь к файлу
    image_path = os.path.join(input_directory, image_file)

    # Открываем изображение
    image = Image.open(image_path)

    # Преобразуем изображение в массив NumPy для обработки через OpenCV
    opencv_image = np.array(image)

    # Преобразуем изображение в черно-белое (оттенки серого)
    gray_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2GRAY)

    # Применяем размытие для устранения шума
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Применяем пороговую обработку (бинаризация)
    _, threshold_image = cv2.threshold(blurred_image, 150, 255, cv2.THRESH_BINARY)

    # Используем tesseract для извлечения только цифр
    custom_config = r'--oem 3 --psm 6 tessedit_char_whitelist=0123456789'
    text = pytesseract.image_to_string(threshold_image, config=custom_config)

    # Получаем имя файла без расширения
    file_name_without_extension = os.path.splitext(image_file)[0]

    # Путь для сохранения файла
    output_file_path = os.path.join(input_directory, f'{file_name_without_extension}_detective.txt')

    # Записываем распознанный текст в файл
    with open(output_file_path, 'w') as f:
        f.write(text)

    print(f"Распознанный текст для {image_file} сохранен в файл: {output_file_path}")



"""Короче, хоть я и пытался использовать Tesseract для распознавания цифр в алгоритме фонтанного преобразования,
оказалось, что это не такая уж и простая задача. Когда картинки не очень четкие, или цифры написаны как-то криво,
или там много шума, алгоритм начинает жутко тупить. Он то цифру неправильно распознает, то вообще ничего не видит.
Получается, что для более-менее нормальных результатов нужно, чтобы картинки были прям идеальными, а это в реальной
жизни почти нереально. Так что, для сложных задач, типа распознавания цифр в грязных или сложных условиях, этот алгоритм, 
мягко говоря, не самый лучший вариант."""