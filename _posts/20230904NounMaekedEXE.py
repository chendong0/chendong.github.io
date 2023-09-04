import thulac
import tkinter as tk
from tkinter import filedialog
import time


def analyze_text(input_file_path, output_file_path):
    start_time = time.time()
    thu1 = thulac.thulac()

    with open(input_file_path, 'r', encoding='utf-8') as input_file, \
            open(output_file_path, 'w', encoding='utf-8') as output_file:
        text = input_file.read()

        segmented_text = thu1.cut(text, text=True)

        segmented_words = segmented_text.split()

        marked_words = []

        for word in segmented_words:
            if word.endswith('_n'):
                marked_words.append(word.split('_')[0] + '/n')
            else:
                marked_words.append(word.split('_')[0])

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
    analyze_text(input_file_path, output_file_path)


# Create the GUI window
root = tk.Tk()
root.title("Text Analyzer")

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

analyze_button = tk.Button(root, text="Analyze", command=analyze_button_click)
analyze_button.pack()

root.mainloop()
