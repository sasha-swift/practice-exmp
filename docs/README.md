# Создание текстового редактора на Python
## Введение

### Цель: 
Разработать функциональный текстовый редактор с графическим интерфейсом на языке программирования Python с использованием библиотеки Tkinter, обеспечивающий базовые возможности работы с текстовыми файлами.

### Задачи:
1. Изучить возможности библиотеки Tkinter для создания графического интерфейса.
2. Реализовать основные функции редактора:
    - создание нового файла
    - открытие и сохранение файлов
    - сохранение с новым именем
3. Реализовать дополнительные функции редакторы (модифицировать проект):
    - переключение темы оформления
    - функции "Копировать", "Вставить и "Вырезать"
4. Обеспечить удобный и понятный пользовательский интерфейс.

---

### Cтек технологий

| **Инструмент / Технология** | **Назначение** |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| **Python 3.x**              | Язык программирования, на котором построена логика текстового редактора                      |
| **Tkinter**                 | Встроенная в Python библиотека для создания графического пользовательского интерфейса (GUI)  |
| **Visual Studio Code**      | Основная среда разработки (IDE), используемая для написания, редактирования и отладки кода   |
| **Markdown**                | Формат для написания технической документации и описания проекта                             |
| **Git**                     | Система контроля версий для отслеживания изменений в коде                                    |
| **GitHub**                  | Платформа для размещения репозитория                                                         |



## Библиотека Tkinter
**Tkinter** — это стандартная библиотека Python для создания графического интерфейса пользователя (GUI), предоставляющая простой и эффективный способ разработки кроссплатформенных настольных приложений. Она входит в стандартную поставку Python и не требует дополнительной установки, что делает её удобным инструментом для быстрого создания GUI-приложений.

Tkinter является обёрткой над библиотекой **Tk**, реализованной на языке C и предназначенной для создания и управления графическими элементами интерфейса. Каждый объект Tk содержит собственный экземпляр интерпретатора Tcl с загруженным Tk, что обеспечивает высокую настраиваемость виджетов, хотя и с устаревшим внешним видом. Tk использует очередь событий Tcl для генерации и обработки событий GUI.

### Основные возможности
- **Создание окон и виджетов**: Tkinter предоставляет разнообразные виджеты, такие как кнопки, метки, текстовые поля, меню и другие, позволяя создавать интерактивные пользовательские интерфейсы. ([GeeksforGeeks][2])
- **Управление размещением элементов**: Существует три способа размещения виджетов: `pack()` — для последовательного размещения, `grid()` — для табличной компоновки и `place()` — для точного позиционирования по координатам.
- **Обработка событий**: Tkinter использует событийно-ориентированную модель, позволяя реагировать на действия пользователя, такие как нажатия кнопок, перемещения мыши и ввод текста.
- **Графика и рисование**: С помощью виджета `Canvas` можно рисовать линии, фигуры, текст и изображения, что полезно для создания визуализаций и простых игр.
- **Меню и диалоговые окна**: Поддерживается создание выпадающих и контекстных меню, а также стандартных диалогов для открытия/сохранения файлов, выбора цвета и отображения сообщений.
- **Поддержка стилей и тем**: Модуль `ttk` предоставляет стилизованные версии стандартных виджетов, приближая внешний вид интерфейса к нативному для операционной системы.
- **Кроссплатформенность**: Приложения, созданные с использованием Tkinter, работают на Windows, macOS и Linux без необходимости изменения кода.

## Возможности Tkinter

* Создание графического окна
* Виджет `Label` (отображение текста и изображений)
* Виджет `Button` (создание кнопок)
* Виджет `Entry` (однострочные текстовые поля)
* Виджет `Text` (многострочные текстовые поля)
* Виджет `Checkbutton` (флажки)
* Виджет `Radiobutton` (переключатели)
* Виджет `Listbox` (список с возможностью выбора)
* Виджет `Canvas` (рисование, графика)
* Виджет `Scale` (ползунок)
* Виджет `Spinbox` (числовой выбор)
* Виджет `Menu` (создание многоуровневых меню)
* Диалоговые окна:

  * Открытие и сохранение файлов
  * Выбор цвета
  * Ввод данных
  * Сообщения об ошибках и подтверждения
* Менеджеры размещения элементов: `pack()`, `grid()`, `place()`
* Обработка событий (нажатия клавиш, мыши и прочего ввода)
* Использование переменных: `StringVar`, `IntVar`, `BooleanVar`
* Поддержка тем и кастомизации стиля
* Работа с буфером обмена
* Поддержка таймеров (`after`)
* Возможность создания всплывающих окон (топ-окон)
* Интеграция с изображениями (`PhotoImage`)
* Возможность создания вложенных фреймов (`Frame`, `LabelFrame`)
* Организация вкладок через `ttk.Notebook`
* Использование библиотеки `ttk` для улучшенного внешнего вида виджетов

---

## 📌 Где применяется Tkinter

Tkinter идеально подходит для:

* Образовательных целей (обучение GUI)
* Быстрого создания прототипов интерфейсов
* Небольших настольных приложений
* Программ с простым пользовательским вводом и взаимодействием

---

## 🔗 Источники

* [SkillFactory: Глоссарий по Tkinter](https://blog.skillfactory.ru/glossary/tkinter/)
* [Selectel: Учебник по Tkinter](https://selectel.ru/blog/tutorials/tkinter-library-in-python/)
* [IT-Black: Tkinter в Python](https://www.it-black.ru/tpost/vb3g6ek5t1-biblioteka-tkinter-v-python)
* [RealPython: Tkinter GUI Tutorial](https://realpython.com/python-gui-tkinter/)
* [GeeksForGeeks: Tkinter Overview](https://www.geeksforgeeks.org/python-gui-tkinter/)
* [Официальная документация](https://docs.python.org/3/library/tkinter.html)

---

Нужно ли добавить схемы или иллюстрации для визуализации структуры виджетов?


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

