import cv2  # Імпорт бібліотеки OpenCV для обробки відео

# Відкриття відеофайлу для читання за допомогою методу VideoCapture з вказанням шляху до файлу
cap = cv2.VideoCapture("C:\\Users\\Alex\\Desktop\\course-work\\videos\\Video Test 2K Samsung.mp4")

# Безкінечний цикл для читання кадрів з відеофайлу
while True:
    # Читання кадру з відеофайлу, ret - змінна, що показує, чи вдалося прочитати кадр
    ret, frame = cap.read()
    
    # Перевірка, чи вдалося прочитати кадр; якщо ні, вихід із циклу
    if not ret:
        break
    
    # Відображення обробленого кадру у вікні з назвою "Processed Frame"
    cv2.imshow("Processed Frame", frame)
    
    # Очікування натискання клавіші 'q' для виходу з циклу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Звільнення ресурсів, пов'язаних із відеофайлом
cap.release()

# Закриття всіх вікон OpenCV
cv2.destroyAllWindows()
