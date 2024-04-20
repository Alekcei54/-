import cv2  # Імпорт бібліотеки OpenCV для обробки відео

# функція виділення меж canny
def canny_edge_detection(frame, t_lower=250, t_upper=250):
    # Перетворення зображення у відтінки сірого
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Використання алгоритму Canny для знаходження країв у зображенні
    frame_edges = cv2.Canny(gray_image, t_lower, t_upper)
    return frame_edges

# Відкриття відеофайлу для читання за допомогою методу VideoCapture з вказанням шляху до файлу
cap = cv2.VideoCapture("C:\\Users\\Alex\\Desktop\\course-work\\videos\\TEST VIDEO.mp4")

# Безкінечний цикл для читання кадрів з відеофайлу
while True:
    # Читання кадру з відеофайлу, ret - змінна, що показує, чи вдалося прочитати кадр
    ret, frame = cap.read()
    
    # Перевірка, чи вдалося прочитати кадр; якщо ні, вихід із циклу
    if not ret:
        break
    
    # Виділення меж методом Canny
    frame = canny_edge_detection(frame)

    # Відображення обробленого кадру у вікні з назвою "Processed Frame"
    cv2.imshow("Processed Frame", frame)
    
    # Очікування натискання клавіші 'q' для виходу з циклу
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Звільнення ресурсів, пов'язаних із відеофайлом
cap.release()

# Закриття всіх вікон OpenCV
cv2.destroyAllWindows()
