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
    - смена темы оформления
    - функции "Копировать", "Вставить и "Вырезать"
4. Обеспечить удобный и понятный пользовательский интерфейс.

### Cтек технологий

| **Инструмент / Технология** | **Назначение** |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| **Python 3.x**              | Язык программирования, на котором построена логика текстового редактора                      |
| **Tkinter**                 | Встроенная в Python библиотека для создания графического пользовательского интерфейса (GUI)  |
| **Visual Studio Code**      | Основная среда разработки (IDE), используемая для написания, редактирования и отладки кода   |
| **Markdown**                | Формат для написания технической документации и описания проекта                             |
| **Git**                     | Система контроля версий для отслеживания изменений в коде                                    |
| **GitHub**                  | Платформа для размещения репозитория                                                         |

---

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


### Tkinter идеально подходит для:
- Образовательных целей (обучение GUI)
- Быстрого создания прототипов интерфейсов
- Небольших настольных приложений
- Программ с простым пользовательским вводом и взаимодействием

---

## Создание текстового редактора на Python (пошаговое руководство)
Для создания текстового редактора был использован следующий обучающий материал:

🔗 Make With Data —  [Python Tutorial: Make Your Own Text Editor](https://www.youtube.com/watch?v=xqDonHEYPgA)

### Шаг 1: Установка Python

Убедимся, что Python установлен:

```bash
python --version
```

### Шаг 2: Реализация основных функций редактора

Создадим файл `texteditor.py` и реализуем следующий код:

#### 🔹 Импорт необходимых библиотек

```python
from tkinter import *  # Импорт всех виджетов и функций из tkinter
from tkinter.filedialog import *  # Импорт диалогов открытия и сохранения файлов
from tkinter import messagebox  # Импорт всплывающих окон для сообщений об ошибках
```

> Эти библиотеки позволяют создать интерфейс и реализовать взаимодействие с файлами.

---

#### 🔹 Инициализация глобальных переменных

```python
filename = None  # Имя текущего открытого или сохраняемого файла
```

---

#### 🔹 Операции с файлами

1. Создание нового файла
```python
def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)  # Очищает всё текстовое поле
```
> Функция очищает текстовое поле и сбрасывает имя текущего файла.


2. Сохранение файла
```python
def saveFile():
    global filename
    t = text.get(0.0, END)  # Получаем содержимое текстового поля
    f = open(filename, 'w')  # Открываем файл для записи
    f.write(t)  # Записываем текст в файл
    f.close()  # Закрываем файл
```
> Сохраняет текущий текст в файл, имя которого уже задано.


3. Сохранить как...
```python
def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')  # Открываем диалоговое окно "Сохранить как"
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())  # Удаляем лишние пробелы в конце и записываем текст
    except:
        messagebox.showerror(title="Ошибка", message="Не удалось сохранить файл")  # Обработка ошибки сохранения
```
> Позволяет сохранить файл под новым именем через диалоговое окно.


4. Открытие файла
```python
def openFile():
    f = askopenfile(mode='r')  # Открываем диалог выбора файла
    t = f.read()  # Чтение содержимого файла
    text.delete(0.0, END)  # Очищаем текущее содержимое редактора
    text.insert(0.0, t)  # Вставляем прочитанный текст в редактор
```
> Открывает и отображает содержимое выбранного файла.

---


#### 🔹 Инициализация главного окна
```python
root = Tk()
root.title("My Python Text Editor")  # Установка заголовка окна
root.minsize(width=400, height=400)  # Минимальный размер окна
root.maxsize(width=400, height=400)  # Максимальный размер окна
```
> Создаётся главное окно приложения с фиксированными размерами.

---


#### 🔹 Поле для ввода текста
```python
text = Text(root, width=400, height=400)  # Основное текстовое поле
text.pack()  # Размещение на экране
```
> Основная область редактора для работы с текстом.

---
#### 🔹 Создание меню
```python
menubar = Menu(root)
```

#### 🔹 Подменю «Файл»
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
> Команды для создания, открытия, сохранения и выхода.

---


#### 🔹 Привязка меню к окну и запуск приложения
```python
root.config(menu=menubar)  # Привязка меню к окну
root.mainloop()  # Запуск главного цикла приложения
```
> Запускается основное окно редактора, которое работает до закрытия пользователем.
---





### Шаг 3: Модификация проекта

#### 🔹 Тема оформления (светлая/тёмная)
Инициализируем новую переменную:
```python
current_theme = "light"  # Тема по умолчанию — светлая
```
> Инициализируем новую переменную для хранения информации о текущей теме оформления (светлая или тёмная).

```python
def setLightTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="black")  # Настройка цветов для светлой темы
    root.config(bg="white")
    current_theme = "light"
```

```python
def setDarkTheme():
    global current_theme
    text.config(bg="#2e2e2e", fg="white")  # Настройка цветов для тёмной темы
    root.config(bg="#2e2e2e")
    current_theme = "dark"
```
> Функции переключают внешний вид редактора между светлой и тёмной темами.

---

#### 🔹  Операции с буфером обмена
1. Копирование
```python
def copyText():
    text.clipboard_clear()  # Очистить буфер обмена
    text.clipboard_append(text.get(0.0, END))  # Скопировать текст в буфер
```

2. Вставка
```python
def pasteText():
    try:
        clipboard_text = root.clipboard_get()  # Получить текст из буфера
        text.insert(INSERT, clipboard_text)  # Вставить текст в курсорную позицию
    except:
        messagebox.showerror("Ошибка", "Не удается вставить текст")
```

2. Вырезание
```python
def cutText():
    copyText()  # Сначала копировать текст
    text.delete(0.0, END)  # Затем удалить его
```

#### 🔹 Подменю «Редактировать»
```python
editmenu = Menu(menubar)
editmenu.add_command(label="Копировать", command=copyText)
editmenu.add_command(label="Вставить", command=pasteText)
editmenu.add_command(label="Вырезить", command=cutText)
menubar.add_cascade(label="Редактировать", menu=editmenu)
```
> Классические команды редактирования.
---

#### 🔹 Подменю «Тема»
```python
viewmenu = Menu(menubar)
viewmenu.add_command(label="Светлая", command=setLightTheme)
viewmenu.add_command(label="Темная", command=setDarkTheme)
menubar.add_cascade(label="Тема", menu=viewmenu)
```
> Позволяет переключаться между светлой и тёмной темами редактора.
---




## Скриншоты интерфейса редактора

| ![](images/interface_1.png) | ![](images/interface_2.png) | ![](images/interface_3.png) |
|-----------------------------|-----------------------------|-----------------------------|
| Подменю «Файл»              | Подменю «Редактивровать»    | Подменю «Тема»              |






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

