import thulac
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import time
import PyPDF2
from docx import Document
from ebooklib import epub

WIDTH = 400
HEIGHT = 450

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def analyze_text(input_file_path, output_file_path, tag_types, progress_var):
    start_time = time.time()
    thu1 = thulac.thulac()

    if input_file_path.endswith('.txt'):
        text = read_txt(input_file_path)
    elif input_file_path.endswith('.docx'):
        text = read_docx(input_file_path)
    elif input_file_path.endswith('.pdf'):
        text = read_pdf(input_file_path)
    elif input_file_path.endswith('.mobi') or input_file_path.endswith('.epub'):
        text = read_ebook(input_file_path)
    else:
        raise Exception("Unsupported file format: %s" % input_file_path)

        segmented_words = thu1.cut(text, text=True)
        total_words = len(segmented_words)
        marked_words = []

        for i, word in enumerate(segmented_words):
            if word.endswith(tag_types):
                marked_words.append(word.split('_')[0] + '/%s' % tag_types)
            else:
                marked_words.append(word.split('_')[0])

            progress_var.set((i + 1) * 100 // total_words)
            root.update_idletasks()

        marked_text = ''.join(marked_words)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(marked_text)

    end_time = time.time()
    print("Runtime:", end_time - start_time, "seconds")


def read_docx(file_path):
    doc = Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
        return text


def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_ebook(file_path):
    book = epub.read_epub(file_path)
    text = ''
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            text += item.get_content().decode('utf-8') + '\n'
        return text


def browse_input_file():
    file_path = filedialog.askopenfilename()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)


def browse_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)


def analyze_button_click():
    input_file_path = input_entry.get()
    output_file_path = output_entry.get()
    tag_types = ()
    # 根据用户选择的磁性分析按钮来设置tag_types
    if noun_var.get():
        tag_types += ('n',)
    if adjective_var.get():
        tag_types += ('a',)
    if verb_var.get():
        tag_types += ('v',)
    if adverb_var.get():
        tag_types += ('d',)

    # No tag_types selected, do nothing
    # 如果用户没有选择任何词性分析按钮,则不启动代码
    if not tag_types:
        return

    progress_var.set(0)
    progress_bar.start()
    analyze_text(input_file_path, output_file_path, tag_types, progress_var)
    progress_bar.stop()


# Create the GUI window
root = tk.Tk()
root.title("词性分析")

# 设置窗口大小
root.geometry(f"{WIDTH}x{HEIGHT}")

# Create and place GUI elements
input_label = tk.Label(root, text="Input Text File:")
input_label.pack()

input_entry = tk.Entry(root)
input_entry.pack()

browse_input_button = tk.Button(root, text="Browse", command=browse_input_file)
browse_input_button.pack()

output_label = tk.Label(root, text="Output Text File:")
output_label.pack()

output_entry = tk.Entry(root)
output_entry.pack()

browse_output_button = tk.Button(root, text="Browse", command=browse_output_file)
browse_output_button.pack()

noun_var = tk.BooleanVar()
noun_checkbutton = tk.Checkbutton(root, text="Mark Nouns", variable=noun_var)
noun_checkbutton.pack()

adverb_var = tk.BooleanVar()
adverb_checkbutton = tk.Checkbutton(root, text="Mark Adverbs", variable=adverb_var)
adverb_checkbutton.pack()

adjective_var = tk.BooleanVar()
adverb_checkbutton = tk.Checkbutton(root, text="Mark adjective", variable=adjective_var)
adverb_checkbutton.pack()

verb_var = tk.BooleanVar()
verb_checkbutton = tk.Checkbutton(root, text="Mark verb", variable=verb_var)
verb_checkbutton.pack()

analyze_button = tk.Button(root, text="Analyze Text", command=analyze_button_click)
analyze_button.pack()

progress_var = tk.IntVar()
progress_bar = ttk.Progressbar(root, mode='determinate', variable=progress_var)
progress_bar.pack()

root.mainloop()
