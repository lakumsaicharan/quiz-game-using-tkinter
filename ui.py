from tkinter import PhotoImage
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
import tkinter as tk
class Interface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Quiz")
        self.window.config(pady=20,padx=20,bg= THEME_COLOR)
        self.score_board = tk.Label(text="Score: 0", bg= THEME_COLOR, fg="white", font=("Arial", 20), highlightthickness=0)
        self.score_board.grid(row=0, column=1, pady=10)
        self.canvas = tk.Canvas(width=300,height=250,bg="white")
        self.question = self.canvas.create_text(150,125,width=280,text="Questions go here!",font=("Arial",20))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        false = PhotoImage(file="images/false.png")
        self.false_button = tk.Button(image=false,highlightthickness=0,command=self.false)
        self.false_button.grid(row=2,column=1)
        true = PhotoImage(file="images/true.png")
        self.true_button = tk.Button(image=true,highlightthickness=0,command= self.true)
        self.true_button.grid(row=2,column=0)

        self.get_next_question()



        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score: {self.quiz.score}")
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text="You are done with the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true(self):
        is_right= self.quiz.check_answer("True")
        self.feedback(is_right)


    def false(self):
        is_right = self.quiz.check_answer("False")
        self.feedback(is_right)


    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)