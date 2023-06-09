import tkinter as tk
import subprocess

# Функции, которые будут выполняться при нажатии кнопок

def run_module1():
    subprocess.run(["python", "object_detection.py"])

def run_module2():
    subprocess.run(["python", "motion_detection.py"])

def run_module3():
    subprocess.run(["python", "loitering_detection.py"])

def run_module4():
    subprocess.run(["python", "abandoned_object_detection.py"])

# Создание главного окна
window = tk.Tk()
window.title("Выбор функции обнаружения")

# Задание размеров и положения окна
window_width = 500
window_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Добавление фонового изображения
bg_image = tk.PhotoImage(file="resources/1.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создание контейнера для кнопок с промежутками
button_container = tk.Frame(window)
button_container.pack(pady=20)  # Отступ между контейнером и другими виджетами

# Создание стиля для кнопок
button_style = {
    "bg": "#fbfcfe",  # Цвет фона кнопок
    "fg": "black",   # Цвет шрифта кнопок
    "font": ("Times New Roman", 14),  # Шрифт кнопок
    "relief": "flat",  # Тип границы кнопок
    "pady": 10  # Отступ по вертикали
}

# Создание кнопок в контейнере
button1 = tk.Button(button_container, text="Распознавание базовых объектов", command=run_module1, width=45, **button_style)
button1.pack(pady=10)  # Отступ между кнопками

button2 = tk.Button(button_container, text="Детектирование движения (драки)", command=run_module2, width=45, **button_style)
button2.pack(pady=10)  # Отступ между кнопками

button3 = tk.Button(button_container, text="Распознавание бесцельного поведения", command=run_module3, width=45, **button_style)
button3.pack(pady=10)  # Отступ между кнопками

button4 = tk.Button(button_container, text="Обнаружение подозрительных вещей (оставленных)", command=run_module4, width=45, **button_style)
button4.pack(pady=10)  # Отступ между кнопками

# Запуск главного цикла окна
window.mainloop()
