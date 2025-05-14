import tkinter as tk
from tkinter import messagebox
import random

# Word bank categorized by difficulty
word_bank = {
    "Easy": ["apple", "house", "table", "chair", "water"],
    "Medium": ["python", "jumble", "planet", "rocket", "guitar"],
    "Hard": ["encyclopedia", "architecture", "complication", "microbiology", "transformation"]
}

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("500x600")

        self.word = ""
        self.guesses_left = 0
        self.display_word = []
        self.guessed_letters = set()

        self.setup_ui()

    def setup_ui(self):
        self.label_title = tk.Label(self.root, text="Hangman Game", font=("Helvetica", 16))
        self.label_title.pack(pady=10)

        self.frame_settings = tk.Frame(self.root)
        self.frame_settings.pack(pady=10)

        tk.Label(self.frame_settings, text="Select Difficulty:").grid(row=0, column=0)
        self.difficulty = tk.StringVar(value="Easy")
        tk.OptionMenu(self.frame_settings, self.difficulty, "Easy", "Medium", "Hard").grid(row=0, column=1)

        tk.Label(self.frame_settings, text="Guesses Allowed:").grid(row=1, column=0)
        self.entry_guesses = tk.Entry(self.frame_settings, width=5)
        self.entry_guesses.insert(0, "6")
        self.entry_guesses.grid(row=1, column=1)

        self.btn_start = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.btn_start.pack(pady=10)

        self.label_word = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.label_word.pack(pady=20)

        self.label_info = tk.Label(self.root, text="", font=("Helvetica", 12))
        self.label_info.pack(pady=5)

        self.frame_letters = tk.Frame(self.root)
        self.frame_letters.pack(pady=10)

    def start_game(self):
        try:
            self.guesses_left = int(self.entry_guesses.get())
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number of guesses.")
            return

        difficulty = self.difficulty.get()
        self.word = random.choice(word_bank[difficulty]).lower()
        self.display_word = ["_" for _ in self.word]
        self.guessed_letters = set()

        self.label_word.config(text=" ".join(self.display_word))
        self.label_info.config(text=f"Guesses Left: {self.guesses_left}")

        for widget in self.frame_letters.winfo_children():
            widget.destroy()

        for letter in "abcdefghijklmnopqrstuvwxyz":
            btn = tk.Button(self.frame_letters, text=letter, width=3, command=lambda l=letter: self.guess_letter(l))
            btn.pack(side=tk.LEFT, padx=2, pady=2)

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return
        self.guessed_letters.add(letter)

        if letter in self.word:
            for i, l in enumerate(self.word):
                if l == letter:
                    self.display_word[i] = letter
        else:
            self.guesses_left -= 1

        self.label_word.config(text=" ".join(self.display_word))
        self.label_info.config(text=f"Guesses Left: {self.guesses_left}")

        if "_" not in self.display_word:
            messagebox.showinfo("Game Over", f"You Win! The word was '{self.word}'.")
            self.disable_buttons()
        elif self.guesses_left <= 0:
            messagebox.showinfo("Game Over", f"You Lose! The word was '{self.word}'.")
            self.disable_buttons()

    def disable_buttons(self):
        for widget in self.frame_letters.winfo_children():
            widget.config(state=tk.DISABLED)

if __name__ == '__main__':
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()