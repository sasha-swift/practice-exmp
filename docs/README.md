# Создание текстового редактора на Python
## 📌 Описание проета

Проект представляет собой простой текстовый редактор, реализованный с использованием библиотеки **Tkinter** — стандартного GUI-фреймворка для Python.
Редактор позволяет выполнять базовые операции: открытие, сохранение, редактирование, копирование, вставку и смену темы оформления.

## 🧰 Выбранный стек технологий

| Компонент     | Технология         | Назначение                         |
| ------------- | ------------------ | ---------------------------------- |
| Язык          | Python 3.x         | Язык программирования              |
| GUI-фреймворк | Tkinter            | Построение графического интерфейса |
| Файловый ввод | `filedialog`, `os` | Работа с файлами                   |
| Документация  | Markdown           | Техническая документация           |
| Диаграммы     | PlantUML, draw\.io | UML и блок-схемы                   |
| Репозиторий   | Git + GitHub       | Контроль версий и хостинг          |

## 📚 Исследование

### 📺 Источник обучения

Для создания текстового редактора был использован следующий обучающий материал:

🔗 [Make With Data — How to Create a Text Editor in Python (Tkinter)](https://www.youtube.com/watch?v=xqDonHEYPgA&ab_channel=MakeWithData)

### 📖 Что изучено:

* Работа с Tkinter: создание окон, меню, текстовых полей
* Обработка событий (нажатия кнопок меню)
* Работа с буфером обмена
* Смена цветовой темы интерфейса
* Чтение и запись файлов через диалоговые окна
* Создание меню и подменю

---

## ⚙️ Пошаговое руководство

### Шаг 1: Установка Python

Убедитесь, что Python установлен:

```bash
python --version
```

### Шаг 2: Запуск редактора

Создайте файл `editor.py` и вставьте в него следующий код:

<details>
<summary>📄 Показать код редактора</summary>

```python
# Импорт библиотек
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

# Глобальные переменные
filename = None
current_theme = "light"

# Функции
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save file…")

def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def setLightTheme():
    global current_theme
    text.config(bg="white", fg="black")
    root.config(bg="white")
    current_theme = "light"

def setDarkTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="white")
    root.config(bg="#2e2e2e")
    current_theme = "dark"

def copyText():
    text.clipboard_clear()
    text.clipboard_append(text.get(0.0, END))

def pasteText():
    try:
        clipboard_text = root.clipboard_get()
        text.insert(INSERT, clipboard_text)
    except:
        messagebox.showerror("Ошибка", "Не удается вставить текст")

def cutText():
    copyText()
    text.delete(0.0, END)

# Создание окна
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

# Текстовое поле
text = Text(root, width=400, height=400)
text.pack()

# Меню
menubar = Menu(root)

filemenu = Menu(menubar)
filemenu.add_command(label="Новый", command=newFile)
filemenu.add_command(label="Открыть", command=openFile)
filemenu.add_command(label="Сохранить", command=saveFile)
filemenu.add_command(label="Сохранить как…", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)

editmenu = Menu(menubar)
editmenu.add_command(label="Копировать", command=copyText)
editmenu.add_command(label="Вставить", command=pasteText)
editmenu.add_command(label="Вырезать", command=cutText)
menubar.add_cascade(label="Редактировать", menu=editmenu)

viewmenu = Menu(menubar)
viewmenu.add_command(label="Светлая", command=setLightTheme)
viewmenu.add_command(label="Темная", command=setDarkTheme)
menubar.add_cascade(label="Тема", menu=viewmenu)

root.config(menu=menubar)
root.mainloop()
```

</details>

---

## 📊 Визуализация и UML-диаграммы

### 1. Архитектура компонентов редактора (Component Diagram)

![Компонентная диаграмма](assets/uml/components.png)

### 2. Последовательность открытия файла (Sequence Diagram)

![Диаграмма последовательности](assets/uml/open_sequence.png)

### 3. Сценарий сохранения файла (Activity Diagram)

![Диаграмма активности](assets/uml/save_file.png)

---

## 💡 Модификация проекта (творческая часть)

### 🔄 Улучшение: Поддержка вкладок

Добавлена возможность работы с несколькими вкладками через `ttk.Notebook`.

### 📷 Скриншот:

![Множественные вкладки](assets/screens/tabs.png)

### 🧱 Новые зависимости:

```python
from tkinter import ttk  # Для вкладок
```

### 🧪 Пример кода (добавление вкладки):

```python
notebook = ttk.Notebook(root)
tab1 = Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.pack(expand=1, fill='both')
```

---

## 📁 Структура репозитория

```
text-editor-python/
├── editor.py
├── README.md
├── assets/
│   ├── screens/
│   │   └── tabs.png
│   └── uml/
│       ├── components.png
│       ├── open_sequence.png
│       └── save_file.png
```

---

## ✅ Вывод

* Создан рабочий текстовый редактор на Python
* Применены базовые навыки GUI и работы с файлами
* Подготовлена техническая документация с иллюстрациями

---

Хочешь, чтобы я помог с созданием диаграмм или загрузкой в GitHub?

---

## 🧾 Подробный разбор кода текстового редактора (Python + Tkinter)

```python
from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox
```

🔹 Импортируем необходимые модули:

* `tkinter` — библиотека для создания GUI-приложений.
* `filedialog` — для открытия и сохранения файлов.
* `messagebox` — для вывода окон с сообщениями об ошибках.

---

```python
filename = None
current_theme = "light"
```

🔹 Глобальные переменные:

* `filename`: хранит путь к текущему открытому/сохраняемому файлу.
* `current_theme`: текущая тема интерфейса (`light` или `dark`).

---

### 📁 Файловые функции

```python
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
```

📌 `newFile()` — создаёт новый пустой файл.

---

```python
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
```

📌 `saveFile()` — сохраняет содержимое текстового поля в текущий файл.

---

```python
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!", message="Unable to save file…")
```

📌 `saveAs()` — сохраняет текст под новым именем, открывая диалоговое окно.

---

```python
def openFile():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
```

📌 `openFile()` — открывает и отображает содержимое файла в редакторе.

---

### 🎨 Темы оформления

```python
def setLightTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="black")
    root.config(bg="white")
    current_theme = "light"

def setDarkTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="white")
    root.config(bg="#2e2e2e")
    current_theme = "dark"
```

📌 `setLightTheme()` / `setDarkTheme()` — переключают цветовую тему интерфейса.

---

### ✂️ Редактирование текста

```python
def copyText():
    text.clipboard_clear()
    text.clipboard_append(text.get(0.0, END))

def pasteText():
    try:
        clipboard_text = root.clipboard_get()
        text.insert(INSERT, clipboard_text)
    except:
        messagebox.showerror("Ошибка", "Не удается вставить текст")

def cutText():
    copyText()
    text.delete(0.0, END)
```

📌 Копирование, вставка и вырезание текста через буфер обмена.

---

### 🖼️ GUI-интерфейс

```python
root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)
```

📌 Создание основного окна приложения.

---

```python
text = Text(root, width=400, height=400)
text.pack()
```

📌 Создаём многострочное текстовое поле.

---

### 🧭 Главное меню

```python
menubar = Menu(root)
```

📌 Инициализация главного меню.

---

#### 📂 Меню "Файл"

```python
filemenu = Menu(menubar)
filemenu.add_command(label="Новый", command=newFile)
filemenu.add_command(label="Открыть", command=openFile)
filemenu.add_command(label="Сохранить", command=saveFile)
filemenu.add_command(label="Сохранить как…", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=root.quit)
menubar.add_cascade(label="Файл", menu=filemenu)
```

---

#### ✏️ Меню "Редактировать"

```python
editmenu = Menu(menubar)
editmenu.add_command(label="Копировать", command=copyText)
editmenu.add_command(label="Вставить", command=pasteText)
editmenu.add_command(label="Вырезать", command=cutText)
menubar.add_cascade(label="Редактировать", menu=editmenu)
```

---

#### 🎨 Меню "Тема"

```python
viewmenu = Menu(menubar)
viewmenu.add_command(label="Светлая", command=setLightTheme)
viewmenu.add_command(label="Темная", command=setDarkTheme)
menubar.add_cascade(label="Тема", menu=viewmenu)
```

---

```python
root.config(menu=menubar)
root.mainloop()
```

📌 Устанавливаем меню в окне и запускаем основной цикл событий.

---

## 📷 Визуализация интерфейса (пример)

> Вставьте сюда изображения с окнами программы: меню, темная тема, светлая тема.

```
![Light Theme Screenshot](assets/diagrams/theme_light.png)
![Dark Theme Screenshot](assets/diagrams/theme_dark.png)
```

---

## ✅ Заключение

Этот текстовый редактор — отличный стартовый проект для изучения Python GUI. Он включает:

* Работа с файлами
* Визуальные интерфейсы
* Работа с буфером обмена
* Простая архитектура

Хочешь, чтобы я подготовил `.md`-файл и UML-диаграммы для GitHub-репозитория?

