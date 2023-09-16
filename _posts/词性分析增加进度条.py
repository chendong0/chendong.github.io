import thulac
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import time

WIDTH = 400
HEIGHT = 450

def analyze_text(input_file_path, output_file_path, tag_types, progress_var):
    start_time = time.time()
    thu1 = thulac.thulac()

    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:
        text = input_file.read()

        segmented_words = thu1.cut(text, text=True)
        total_words = len(segmented_words)
        marked_words = []

        for i, word in enumerate(segmented_words):
            if word.endswith(tag_types):
                marked_words.append(word.split('_')[0] + '/%s' % tag_types)
            else:
                marked_words.append(word.split('_')[0])

            progress_var.set((i+1) * 100 // total_words)
            root.update_idletasks()

        marked_text = ''.join(marked_words)
        output_file.write(marked_text)

    end_time = time.time()
    print("Runtime:", end_time - start_time, "seconds")


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

    if noun_var.get():
        tag_types += ('n',)
    if adjective_var.get():
        tag_types += ('a',)
    if verb_var.get():
        tag_types += ('v',)
    if adverb_var.get():
        tag_types += ('d',)

    progress_var.set(0)
    progress_bar.start()
    analyze_text(input_file_path, output_file_path, tag_types, progress_var)
    progress_bar.stop()


# Create the GUI window
root = tk.Tk()
root.title("Text Analyzer")

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
