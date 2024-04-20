import cv2  # Імпорт бібліотеки OpenCV для обробки відео
import numpy as np # Імпорт бібліотеки numpy для роботи з матрицями

# Відкриття відеофайлу для читання за допомогою методу VideoCapture з вказанням шляху до файлу
cap = cv2.VideoCapture("C:\\Users\\Alex\\Desktop\\course-work\\videos\\TEST VIDEO.mp4")

# Функція вертикального зсуву зображення
def vertical_shift(frame, top=200):
    # Отримання розмірів кадру (висоти та ширини)
    num_rows, num_cols = frame.shape[:2]
    # Створення матриці зсуву зображення за допомогою зміщення у вертикальному напрямку
    translation_matrix = np.float32([[1, 0, 0], [0, 1, top]])
    # Застосування зсуву до зображення за допомогою афінного перетворення
    shifted_frame = cv2.warpAffine(frame, translation_matrix, (num_cols, num_rows))
    return shifted_frame

# Безкінечний цикл для читання кадрів з відеофайлу
while True:
    # Читання кадру з відеофайлу, ret - змінна, що показує, чи вдалося прочитати кадр
    ret, frame = cap.read()
    
    # Перевірка, чи вдалося прочитати кадр; якщо ні, вихід із циклу
    if not ret:
        break

    # Вертикальний зсув кадру
    frame = vertical_shift(frame)
    
    # Відображення обробленого кадру
    cv2.imshow("Processed Frame", frame)
    
    # Очікування натискання клавіші 'q' для виходу з циклу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Звільнення ресурсів, пов'язаних із відеофайлом
cap.release()

# Закриття всіх вікон OpenCV
cv2.destroyAllWindows()
