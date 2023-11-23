import tkinter as tk
from tkinter import ttk, messagebox
import winsound
from PIL import ImageTk, Image
import time

def update_progressbar():  
    c = progress_bar['value']
    nv = c + 1
    if nv <= 100:
        # Изменяем цвет полоски в зависимости от значения
        if nv >= 95:
            progress_bar['style'] = 'red.Horizontal.TProgressbar'
        elif nv > 80 and nv < 95:
            progress_bar['style'] = 'orange.Horizontal.TProgressbar'
        else:
            progress_bar['style'] = 'green.Horizontal.TProgressbar'
            
        progress_bar['value'] = nv
        if nv < 100:
            root.after(270, update_progressbar)
        else:
            show_message()

def show_message():
    
    winsound.PlaySound("C:\\8989.wav", winsound.SND_FILENAME)
    top = tk.Toplevel(root)
    img = ImageTk.PhotoImage(Image.open('C:\\8989.png'))
    msg = tk.Label(top, text='апарапрпр', image=img)
    msg.image = img
    msg.pack()
    top.after(1000, top.destroy)  # Закрытие окна через 1 секунду (1000 миллисекунд)
    root.after(1000, show_message)  # Запуск функции show_message через 1 секунду
        
##        top.after(3000, top.destroy)  # Закрытие окна через 1 секунду (1000 миллисекунд)
    

def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def moving(event):
    x = (event.x_root - root.x - x_pos)
    y = (event.y_root - root.y - y_pos)
    root.geometry(f"+{x}+{y}")

root = tk.Tk()
root.attributes('-topmost', 1)  # Делаем окно всегда видимым поверх других
x_pos = 120
y_pos = 20
width = 500
height = 30
root.geometry(f"{width}x{height}+{x_pos}+{y_pos}")
# Создаем стили для полоски индикатора
style = ttk.Style()
style.configure('red.Horizontal.TProgressbar', background='red')
style.configure('orange.Horizontal.TProgressbar', background='orange')
style.configure('green.Horizontal.TProgressbar', background='green')

progress_bar = ttk.Progressbar(root, orient='horizontal', mode='determinate', length=1000, style='orange.Horizontal.TProgressbar')
progress_bar.pack(pady=10)

root.bind("<Button-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", moving)

root.resizable(False, False) 

update_progressbar()
root.overrideredirect(True)  # Убираем рамки окна






# Дальше идёт остальной ваш код.
