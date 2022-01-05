from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Interface:
    def __init__(self, quiz:QuizBrain):
        self.quiz=quiz
        self.ventana=Tk()
        self.ventana.title="Quizzler"
        self.ventana.config(padx=20,pady=10,bg=THEME_COLOR)
        self.puntuacion=Label(text="Puntuación: 0",fg="white",bg=THEME_COLOR)
        self.puntuacion.grid(row=0,column=1)
        self.canva=Canvas(width=300,height=250,bg="#f2f2f2")
        self.pregunta=self.canva.create_text(150,125,text="Las preguntas aquí",fill=THEME_COLOR,
        font=("Arial",20,"italic"),width=280)
        self.canva.grid(column=0,row=1,columnspan=2,padx=20,pady=20)
        img_ver=PhotoImage(file="day 34/images/true.png")
        self.verdadero=Button(image=img_ver,highlightthickness=0,command=self.presiono_true)
        self.verdadero.grid(column=0,row=2)
        img_fal=PhotoImage(file="day 34/images/false.png")
        self.falso=Button(image=img_fal,highlightthickness=0,command=self.presiono_false)
        self.falso.grid(column=1,row=2)
        self.pregunta_sig()
        self.ventana.mainloop()
    
    def pregunta_sig(self):
        self.canva.config(bg="white")
        self.canva.itemconfig(self.pregunta,fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            self.puntuacion.config(text=f"Puntuación: {self.quiz.score}/{self.quiz.question_number}")
            texto_pregunta=self.quiz.next_question()
            self.canva.itemconfig(self.pregunta,text=texto_pregunta)
        else:
            self.canva.itemconfig(self.pregunta,text="Haz terminado el quizz")
            self.puntuacion.config(text=f"Puntuación: {self.quiz.score}/{self.quiz.question_number}")
            self.verdadero.config(state="disable")
            self.falso.config(state="disable")

    def presiono_true(self):
        self.comparacion(self.quiz.check_answer("True"))
    def presiono_false(self):
        self.comparacion(self.quiz.check_answer("False"))
    
    def comparacion(self,respuesta):
        if respuesta:
            self.canva.config(bg="green")
            self.canva.itemconfig(self.pregunta,fill="white")
        else:
            self.canva.config(bg="red")
            self.canva.itemconfig(self.pregunta,fill="white")
        self.ventana.after(1000,self.pregunta_sig)
