THEME_COLOR = "#375362"
from tkinter import *
class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Jeff the Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        self.score = Label(self.window,text=f"Score: 0", bg=THEME_COLOR, fg="white", font=("Arial",10, "bold"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text=f"placeholder", fill=THEME_COLOR, font=("Arial",20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)


        correct_image = PhotoImage(file="./images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0, borderwidth=0)
        self.correct.grid(row=2, column=0)


        wrong_image = PhotoImage(file="./images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0, borderwidth=0)
        self.wrong.grid(row=2, column=1)





























        self.window.mainloop()

