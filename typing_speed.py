import tkinter as tk
from tkinter import messagebox

import time

import random



# -----------------------------

# Text Provider Logic

# -----------------------------

TEXTS = [

    "Python is a powerful and easy to learn programming language used widely in software development.",

    "Typing speed is an important skill for programmers data entry operators and content writers.",

    "Tkinter is Python's standard library for creating graphical user interface applications.",

    "Practice typing every day to improve speed accuracy and confidence while coding."

]



def get_random_text():

    return random.choice(TEXTS)





# -----------------------------

# Speed Calculation Logic

# -----------------------------

def calculate_wpm(typed_text, time_taken):

    words = len(typed_text.split())

    minutes = time_taken / 60

    if minutes == 0:

        return 0

    return round(words / minutes)



def calculate_accuracy(original_text, typed_text):

    original_words = original_text.split()

    typed_words = typed_text.split()



    correct = 0

    for o, t in zip(original_words, typed_words):

        if o == t:

            correct += 1



    if len(original_words) == 0:

        return 0



    accuracy = (correct / len(original_words)) * 100

    return round(accuracy, 2)





# -----------------------------

# Main UI Application

# -----------------------------

class TypingSpeedApp:

    def __init__(self):

        self.window = tk.Tk()

        self.window.title("Typewriter Speed Checker")

        self.window.geometry("800x550")

        self.window.resizable(False, False)



        self.start_time = None

        self.test_text = get_random_text()



        self.create_widgets()



    def create_widgets(self):

        tk.Label(

            self.window,

            text="Typing Speed Test",

            font=("Arial", 18, "bold")

        ).pack(pady=10)



        self.text_label = tk.Label(

            self.window,

            text=self.test_text,

            wraplength=760,

            font=("Arial", 12),

            justify="left"

        )

        self.text_label.pack(pady=10)



        self.text_entry = tk.Text(

            self.window,

            height=8,

            width=90,

            font=("Arial", 12)

        )

        self.text_entry.pack(pady=10)



        # Start timer on first key press

        self.text_entry.bind("<KeyPress>", self.start_timer)



        self.submit_btn = tk.Button(

            self.window,

            text="Submit",

            font=("Arial", 12),

            command=self.submit_test

        )

        self.submit_btn.pack(pady=10)



        tk.Label(

            self.window,

            text=(

                "Instructions:\n"

                "1. Timer starts when you type the first character\n"

                "2. Press Enter key to submit the test"

            ),

            font=("Arial", 10),

            justify="left"

        ).pack(pady=5)



        self.window.bind("<Return>", self.enter_key_submit)



    def start_timer(self, event):

        if self.start_time is None:

            self.start_time = time.time()



    def enter_key_submit(self, event):

        self.submit_test()



    def submit_test(self):

        if self.start_time is None:

            messagebox.showwarning("Warning", "Start typing first!")

            return



        end_time = time.time()

        typed_text = self.text_entry.get("1.0", tk.END).strip()



        time_taken = end_time - self.start_time

        wpm = calculate_wpm(typed_text, time_taken)

        accuracy = calculate_accuracy(self.test_text, typed_text)



        messagebox.showinfo(

            "Result",

            f"Time Taken: {round(time_taken, 2)} seconds\n"

            f"Speed: {wpm} WPM\n"

            f"Accuracy: {accuracy}%"

        )



        self.reset_test()



    def reset_test(self):

        self.start_time = None

        self.test_text = get_random_text()

        self.text_label.config(text=self.test_text)

        self.text_entry.delete("1.0", tk.END)



    def run(self):

        self.window.mainloop()





# -----------------------------

# Program Entry Point

# -----------------------------

if __name__ == "__main__":

    app = TypingSpeedApp()

    app.run()