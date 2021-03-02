from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row=2, column=1, columnspan=2, pady=40)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Welcome to the Quizzler\nLets test your IQ",
                                                     font=("Arial", 15, "italic"),
                                                     fill="black")
        self.score = 0

        true_image = PhotoImage(file="images/true.png")
        self.button = Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.button.grid(row=3, column=2)

        false_image = PhotoImage(file="images/false.png")
        self.button2 = Button(image=false_image, highlightthickness=0, command=self.false_answer)
        self.button2.grid(row=3, column=1)

        self.label = Label(text=f"Score : {self.score}", bg=THEME_COLOR, fg="black")
        self.label.grid(row=1, column=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:

            self.canvas.itemconfig(self.question_text, text="Game Over")
            self.button.config(state="disabled")
            self.button2.config(state="disabled")

    def true_answer(self):
        right = self.quiz.check_answer("true")
        self.give_feedback(right)

    def false_answer(self):
        right = self.quiz.check_answer("false")
        self.give_feedback(right)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            self.score += 1
            self.label.config(text=f"Score : {self.score}")

        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.next_question)
