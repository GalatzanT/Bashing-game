import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


def caesar_cipher(word, shift):
    encrypted_word = ""
    for char in word:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_word += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_word += chr(shifted)
        else:
            encrypted_word += char
    return encrypted_word


# Lista de cuvinte în limba română și relevante pentru Cluj
word_list = ["cluj", "napoca", "somes", "matei", "corvin", "muzeu", "universitate", "student", "bastion", "botanic"]


class WordGuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Joc de Ghicire a Cuvintelor - Societatea Hermes")
        self.geometry("500x400")

        # Afișare siglă
        self.logo = Image.open("hermes_logo.png")
        self.logo = self.logo.resize((100, 100), Image.LANCZOS)
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self, image=self.logo)
        self.logo_label.pack(anchor="ne")

        self.chosen_word = random.choice(word_list)
        self.shift = 1  # Deplasare fixă pentru cifrul lui Caesar
        self.encrypted_word = caesar_cipher(self.chosen_word, self.shift)

        self.create_widgets()

    def create_widgets(self):
        # Setări pentru font și padding
        label_font = ("Helvetica", 14)
        button_font = ("Helvetica", 14)
        padding = {'padx': 10, 'pady': 10}

        self.label = tk.Label(self, text="Ghiceste cuvântul decriptat:", font=label_font)
        self.label.pack(pady=10)

        self.encrypted_label = tk.Label(self, text=f"Cuvântul criptat: {self.encrypted_word}", font=label_font)
        self.encrypted_label.pack(pady=10)

        self.entry = tk.Entry(self, font=label_font)
        self.entry.pack(pady=10)

        self.guess_button = tk.Button(self, text="Ghiceste", font=button_font, command=self.check_guess)
        self.guess_button.pack(pady=10)

        self.result_label = tk.Label(self, text="", font=label_font)
        self.result_label.pack(pady=10)

    def check_guess(self):
        user_guess = self.entry.get().lower()
        if user_guess == self.chosen_word:
            self.result_label.config(text="Felicitări! Ai ghicit corect!")
            messagebox.showinfo("Rezultat", "Felicitări! Ai ghicit corect!")
        else:
            self.result_label.config(text="Îmi pare rău, încearcă din nou.")
            messagebox.showinfo("Rezultat", "Îmi pare rău, încearcă din nou.")


if __name__ == "__main__":
    app = WordGuessingGame()
    app.mainloop()
