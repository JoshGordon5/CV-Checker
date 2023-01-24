import tkinter as tk
import re
import os
from spellchecker import SpellChecker
from tkinter import filedialog
from PIL import Image
import customtkinter

spell = SpellChecker()

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("800x800")
app.title("Amber Labs CV Checker")


def choose_file():
    global text_files
    global text
    # Open the chosen file
    filename = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("Text files", "*.txt"), ("all files", "*.*")))
    with open(filename, "r") as f:
        text = f.read()
        #text_widget = tk.Text(frame_1, height=20, width=50)
        #text_widget.insert(tk.END, text)
        #text_widget.pack()

def search_keyword():
    global keyword
    global text
    global match
    keyword = entry.get()
    matches = re.findall(keyword, text)
    text_keyword.delete(0, tk.END)
    if matches:
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, text)
        text_widget.tag_config("highlight", background="yellow")
        start_index = "1.0"
        while True:
            start_index = text_widget.search(keyword, start_index, stopindex=tk.END)
            if not start_index:
                break
            end_index = f"{start_index}+{len(keyword)}c"
            text_widget.tag_add("highlight", start_index, end_index)
            start_index = end_index
        text_keyword.insert(0, f'Keyword found {len(matches)} times.')
    else:
        text_keyword.insert(0, "Keyword not found.")




def check_spelling():
    global words
    words = text.split()
    for word in words:
        if spell.correction(word) != word:
            text_1.insert(tk.END, f"Incorrect spelling: {word}. Did you mean {spell.correction(word)}?\n")


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_result = tk.Label(frame_1)
label_result.pack()

button_file = tk.Button(frame_1, text="Choose File", command=choose_file)
button_file.pack()

entry = tk.Entry(frame_1)
entry.pack()

button_keyword = customtkinter.CTkButton(master=frame_1, command=search_keyword, text="Search For Keyword")
button_keyword.pack(pady=10, padx=10)

text_keyword = customtkinter.CTkEntry(master=frame_1, width=200, height=35)
text_keyword.pack(pady=10, padx=10)

spelling = customtkinter.CTkButton(master=frame_1, command=check_spelling, text="Check for Spelling Errors")
spelling.pack(pady=10, padx=10)

#text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
#text_1.pack(pady=10, padx=10)

text_widget = customtkinter.CTkTextbox(frame_1, height=200, width=500)
text_widget.insert(tk.END, app)
text_widget.pack()


app.mainloop()
