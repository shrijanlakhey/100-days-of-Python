from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    # 'quizbrain:QuizBrain' specifying that the 'quizbrain' object must be of the data type QuizBrain
    def __init__(self, quizbrain:QuizBrain):
        self.quiz = quizbrain
        self.window = Tk()
        self.window.title = "Quiz Game"    
        self.window.config(background=THEME_COLOR, padx=20, pady=20)

        # Score label
        self.score_label = Label(text="Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(width=300, height=250)
        # the 'width' property is given to wrap the text
        self.question_text = self.canvas.create_text(150, 125, text="", font=("Arial", 15, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # Buttons
        # since these images are not going to be used anywhere else other then the buttons, so it is not turned into a property by not adding 'self.'  
        true_img = PhotoImage(file="034/quiz_game/images/true.png")
        false_img = PhotoImage(file="034/quiz_game/images/false.png")

        self.true_button = Button(image=true_img, bd=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        self.false_button = Button(image=false_img, bd=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz")
            # disabling buttons
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def answer_false(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.get_next_question)
        