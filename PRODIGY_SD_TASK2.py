import random
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Guess the Number")
root.geometry("300x200")
root.configure(bg="#f5bd02")

target_number = random.randint(1, 1000)
attempts = 0

def guess_number():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1

        if guess < target_number:
            if target_number - guess > 100:
                label_result.config(text="Too low! Try a much higher number.")
            else:
                label_result.config(text="Low!")
        elif guess > target_number:
            if guess - target_number > 100:
                label_result.config(text="Too high! Try a much lower number.")
            else:
                label_result.config(text="High!")
        else:
            messagebox.showinfo("Congratulations!", f"You've guessed the number in {attempts} attempts!")
            reset_game()

    except ValueError:
        messagebox.showerror("Input error", "Please enter a valid number.")

def reset_game():
    global target_number, attempts
    target_number = random.randint(1, 1000)
    attempts = 0
    label_result.config(text="")
    entry_guess.delete(0, tk.END)


tk.Label(root, text="Guess a number between 1 and 1000:").pack(pady=10)

entry_guess = tk.Entry(root)
entry_guess.pack(pady=5)

btn_guess = tk.Button(root, text="Submit Guess", command=guess_number)
btn_guess.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=10)

root.mainloop()
