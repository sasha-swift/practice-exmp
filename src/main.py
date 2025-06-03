from tkinter import * 
from tkinter.filedialog import * 
from tkinter import messagebox

# Глобальные переменные
filename = None
current_theme = "light"

# Создание нового файла
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

# Сохранение текущего файла
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close() 

# Сохранить как...
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Ошибка", message="Не удалось сохранить файл")

# Открытие файла
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

# Светлая тема оформления
def setLightTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="black")
    root.config(bg="white")
    current_theme = "light"

# Тёмная тема оформления
def setDarkTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="white")
    root.config(bg="#2e2e2e")
    current_theme = "dark"

# Копирование текста
def copyText():
    text.clipboard_clear()
    text.clipboard_append(text.get(0.0, END))

# Вставка текста
def pasteText():
    try:
        clipboard_text = root.clipboard_get()
        text.insert(INSERT, clipboard_text)
    except:
        messagebox.showerror("Ошибка", "Не удается вставить текст")

# Вырезание текста
def cutText():
    copyText()
    text.delete(0.0, END)

# Инициализация главного окна
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

# Текстовое поле
text = Text(root, width=400, height=400)
text.pack()

# Меню
menubar = Menu(root)

# Подменю "Файл"
filemenu = Menu(menubar)
filemenu.add_command(label="Новый", command=newFile)
filemenu.add_command(label="Открыть", command=openFile)
filemenu.add_command(label="Сохранить", command=saveFile) 
filemenu.add_command(label="Сохранить как…", command=saveAs) 
filemenu.add_separator() 
filemenu.add_command(label="Выход", command=root.quit) 
menubar.add_cascade(label="Файл", menu=filemenu)

# Подменю "Редактировать"
editmenu = Menu(menubar)
editmenu.add_command(label="Копировать", command=copyText) 
editmenu.add_command(label="Вставить", command=pasteText)
editmenu.add_command(label="Вырезать", command=cutText)
menubar.add_cascade(label="Редактировать", menu=editmenu)

# Подменю "Тема"
viewmenu = Menu(menubar)
viewmenu.add_command(label="Светлая", command=setLightTheme)
viewmenu.add_command(label="Темная", command=setDarkTheme)
menubar.add_cascade(label="Тема", menu=viewmenu)

# Применение меню
root.config(menu=menubar)
root.mainloop()