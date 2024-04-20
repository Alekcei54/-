import cv2  # Імпорт бібліотеки OpenCV для обробки відео
import numpy as np # Імпорт бібліотеки numpy для роботи з матрицями

# Функція фільтрації з ефектом зсуву
def motion_blur(frame, kernel_size=5):
    # Створення пустого ядра для фільтра зсуву
    kernel_motion_blur = np.zeros((kernel_size, kernel_size))
    # Встановлення одиниць у рядках ядра для створення зсуву
    kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
    # Нормалізація ядра для отримання середнього значення
    kernel_motion_blur = kernel_motion_blur / kernel_size
    return cv2.filter2D(frame, -1, kernel_motion_blur)


# Відкриття відеофайлу для читання за допомогою методу VideoCapture з вказанням шляху до файлу
cap = cv2.VideoCapture("C:\\Users\\Alex\\Desktop\\course-work\\videos\\TEST VIDEO.mp4")

# Безкінечний цикл для читання кадрів з відеофайлу
while True:
    # Читання кадру з відеофайлу, ret - змінна, що показує, чи вдалося прочитати кадр
    ret, frame = cap.read()
    
    # Перевірка, чи вдалося прочитати кадр; якщо ні, вихід із циклу
    if not ret:
        break
    
    # Застосовування фільтру з ефектом зсуву
    frame = motion_blur(frame)

    # Відображення обробленого кадру у вікні з назвою "Processed Frame"
    cv2.imshow("Processed Frame", frame)
    
    # Очікування натискання клавіші 'q' для виходу з циклу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Звільнення ресурсів, пов'язаних із відеофайлом
cap.release()

# Закриття всіх вікон OpenCV
cv2.destroyAllWindows()