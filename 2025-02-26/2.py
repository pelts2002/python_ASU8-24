from ultralytics import YOLO

# Загрузка модели
model_path = r"C:\Users\user\Desktop\python_ASU8-24\2025-02-26\My-First-Project-1\runs\detect\train6\weights\best.pt"
model = YOLO(model_path)

# Путь к изображению
image_path = r"C:\Users\user\Desktop\python_ASU8-24\2025-02-26\sdvs2.jpg"

# Выполнение инференса
results = model(image_path, conf=0.99)

# Отображение результатов для первого изображения в списке
results[0].show()