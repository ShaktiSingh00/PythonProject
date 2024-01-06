from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

root = Tk()
root.title('Comedy.com - Translator')
root.geometry("880x300")

def translate_it():
    original = original_text.get("1.0", "end-1c")
    if original:
        try:
            from_language_code = get_language_code(original_combo.get())
            to_language_code = get_language_code(translated_combo.get())

            translator = Translator()
            translation = translator.translate(original, src=from_language_code, dest=to_language_code)
            translated_text.delete(1.0, END)
            translated_text.insert(END, translation.text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Warning", "Please enter text to translate.")

def clear():
    original_text.delete(1.0, END)
    translated_text.delete(1.0, END)

def get_language_code(language_name):
    for code, name in LANGUAGES.items():
        if name == language_name:
            return code
    return None

language_list = list(LANGUAGES.values())

original_text = Text(root, height=10, width=40)
original_text.grid(row=0, column=0, pady=20, padx=10)

translate_button = Button(root, text="Translate!", font=("Helvetica", 24), command=translate_it)
translate_button.grid(row=0, column=1, padx=10)

translated_text = Text(root, height=10, width=40)
translated_text.grid(row=0, column=2, pady=20, padx=10)

original_combo = ttk.Combobox(root, width=50, values=language_list)
original_combo.current(0)
original_combo.grid(row=1, column=0)

translated_combo = ttk.Combobox(root, width=50, values=language_list)
translated_combo.current(0)
translated_combo.grid(row=1, column=2)  # Corrected column position for translated_combo

clear_button = Button(root, text="Clear", command=clear)
clear_button.grid(row=2, column=1)

root.mainloop()
