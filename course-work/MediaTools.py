import cv2
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

class MediaTools:
    def open(self):
        self.__loadGui()

    # Константи (можливі варіанти обробки відео)
    VERTICAL_SHIFT = 1
    EDGE_DETECTION_CANNY = 2
    COLOR_SPACE_XYZ = 3
    SHIFT_EFFECT_FILTER = 4

    # Метод вертикального зсуву зображення
    def __vertical_shift(self, frame, top=200):
        # Отримання розмірів кадру (висоти та ширини)
        num_rows, num_cols = frame.shape[:2]
        # Створення матриці зсуву зображення за допомогою зміщення у вертикальному напрямку
        translation_matrix = np.float32([[1, 0, 0], [0, 1, top]])
        # Застосування зсуву до зображення за допомогою афінного перетворення
        shifted_frame = cv2.warpAffine(frame, translation_matrix, (num_cols, num_rows))
        return shifted_frame
    
    # Метод виділення меж canny
    def __canny_edge_detection(self, frame, t_lower=250, t_upper=250):
        # Перетворення зображення у відтінки сірого
        gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Використання алгоритму Canny для знаходження країв у зображенні
        frame_edges = cv2.Canny(gray_image, t_lower, t_upper)
        return frame_edges
    
    # Метод зміни кольорового простору на XYZ
    def __to_xyz_colorspace(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    
    # Метод фільтрації з ефектом зсуву
    def __motion_blur(self, frame, kernel_size=5):
        # Створення пустого ядра для фільтра зсуву
        kernel_motion_blur = np.zeros((kernel_size, kernel_size))
        # Встановлення одиниць у рядках ядра для створення зсуву
        kernel_motion_blur[int((kernel_size - 1) / 2), :] = np.ones(kernel_size)
        # Нормалізація ядра для отримання середнього значення
        kernel_motion_blur = kernel_motion_blur / kernel_size
        return cv2.filter2D(frame, -1, kernel_motion_blur)

    # Метод завантаження графічного інтерфейсу
    def __loadGui(self):
        self.root = tk.Tk()
        self.root.title("Media Tools")

        # Обирання варіацій обробки відео
        self.tool_selection_frame = tk.Frame(self.root)
        self.tool_selection_frame.pack(pady=10)
        self.tools_var = tk.IntVar()
        self.video_file_path = ""
        
        tk.Checkbutton(self.tool_selection_frame, text="Video Shift", variable=self.tools_var, onvalue=self.VERTICAL_SHIFT).grid(row=0, sticky="w")
        tk.Checkbutton(self.tool_selection_frame, text="Edge Detection (Canny)", variable=self.tools_var, onvalue=self.EDGE_DETECTION_CANNY).grid(row=1, sticky="w")
        tk.Checkbutton(self.tool_selection_frame, text="Color Space (XYZ)", variable=self.tools_var, onvalue=self.COLOR_SPACE_XYZ).grid(row=2, sticky="w")
        tk.Checkbutton(self.tool_selection_frame, text="Shift Effect Filter", variable=self.tools_var, onvalue=self.SHIFT_EFFECT_FILTER).grid(row=3, sticky="w")

        # Обирання джерела відео
        self.video_source_frame = tk.Frame(self.root)
        self.video_source_frame.pack(pady=10)
        self.video_source_var = tk.StringVar()
        self.video_source_var.set("File")

        tk.Radiobutton(self.video_source_frame, text="Webcam", variable=self.video_source_var, value="Webcam").grid(row=0, sticky="w")
        tk.Radiobutton(self.video_source_frame, text="File", variable=self.video_source_var, value="File").grid(row=1, sticky="w")

        # Обирання шляху відео
        tk.Button(self.root, text="Select Video File", command=self.__set_video_file_path).pack(pady=10)

        # Запуск відео
        tk.Button(self.root, text="Start Processing", command=self.__start_processing).pack(pady=10)

        self.root.mainloop()

    # Метод встановлення шляху до відеу за допомогою діалогового вікна обирання файлу
    def __set_video_file_path(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi")])
        if file_path:
            self.video_file_path = file_path

    # Метод обробки та показу відео
    def __start_processing(self):
        selected_tool = self.tools_var.get()
        video_source = self.video_source_var.get()

        if video_source == "File":
            if not self.video_file_path:
                messagebox.showerror("Error", "Please select a video file.")
                return
            cap = cv2.VideoCapture(self.video_file_path)
        elif video_source == "Webcam":
            cap = cv2.VideoCapture(0)
        else:
            messagebox.showerror("Error", "Invalid video source.")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Застосування обраного інструменту обробки відео
            if selected_tool == self.VERTICAL_SHIFT:
                frame = self.__vertical_shift(frame)
                pass
            elif selected_tool == self.EDGE_DETECTION_CANNY:
                frame = self.__canny_edge_detection(frame)
                pass
            elif selected_tool == self.COLOR_SPACE_XYZ:
                frame = self.__to_xyz_colorspace(frame)
                pass
            elif selected_tool == self.SHIFT_EFFECT_FILTER:
                frame = self.__motion_blur(frame)
                pass

            cv2.imshow("Processed Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

media_tools = MediaTools()
media_tools.open()
