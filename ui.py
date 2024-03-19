THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Jeff the Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score = Label(self.window,text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",10, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"placeholder",
            fill=THEME_COLOR,
            font=("Arial",20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        correct_image = PhotoImage(file="./images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0, borderwidth=0, command=self.true_command)
        self.correct.grid(row=2, column=0)


        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=self.false_command)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've made it to the end!")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_command(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_command(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, answer):
        if answer:
            self.canvas.config(bg="green")
            #change it to green

        else:
            self.canvas.config(bg="red")
            #change it to red
        self.window.after(1000, self.get_next_question)


    def starting_screen(self):
        





























