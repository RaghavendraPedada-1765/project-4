import tkinter as tk
from tkinter import messagebox
import json

# Sample questions; to load from file, see bottom of file
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "London", "Paris", "Madrid"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "2"],
        "answer": 1
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "answer": 1
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("500x350")
        self.qn = 0
        self.correct = 0
        self.selected = tk.IntVar(value=-1)
        self.answers = [-1] * len(questions)
        self.create_widgets()
        self.display_question()

    def create_widgets(self):
        self.lbl_question = tk.Label(self.root, text="", font=("Arial", 16), wraplength=400, justify="left")
        self.lbl_question.pack(pady=20)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.root, text="", variable=self.selected, value=i, font=("Arial", 14))
            rb.pack(anchor="w", padx=30)
            self.radio_buttons.append(rb)

        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=20, fill="x")

        self.btn_prev = tk.Button(nav_frame, text="Previous", command=self.prev_question, width=10)
        self.btn_prev.pack(side="left", padx=40)

        self.btn_next = tk.Button(nav_frame, text="Next", command=self.next_question, width=10)
        self.btn_next.pack(side="right", padx=40)

    def display_question(self):
        self.selected.set(self.answers[self.qn] if self.answers[self.qn] != -1 else -1)
        q = questions[self.qn]
        self.lbl_question.config(text=f"Q{self.qn+1}: {q['question']}")
        for idx, option in enumerate(q["options"]):
            self.radio_buttons[idx].config(text=option)
        self.update_buttons()

    def save_answer(self):
        self.answers[self.qn] = self.selected.get()

    def next_question(self):
        self.save_answer()
        if self.selected.get() == -1:
            messagebox.showwarning("No Selection", "Please select an option before proceeding.")
            return
        if self.qn < len(questions) - 1:
            self.qn += 1
            self.display_question()
        else:
            self.finish_quiz()

    def prev_question(self):
        self.save_answer()
        if self.qn > 0:
            self.qn -= 1
            self.display_question()

    def finish_quiz(self):
        self.save_answer()
        self.correct = 0
        for i, q in enumerate(questions):
            if self.answers[i] == q["answer"]:
                self.correct += 1
        score_msg = f"Your Score: {self.correct} / {len(questions)}"
        messagebox.showinfo("Quiz Completed", score_msg)
        self.root.destroy()

    def update_buttons(self):
        self.btn_prev.config(state="disabled" if self.qn == 0 else "normal")
        self.btn_next.config(text="Finish" if self.qn == len(questions) - 1 else "Next")

def load_questions_from_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

if __name__ == "__main__":
    # To load questions from a JSON file, uncomment these lines:
    # global questions
    # questions = load_questions_from_json("questions.json")
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
