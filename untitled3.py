from tkinter import * 
root = Tk()
root.title("heart_Report")
root.geometry("600x600")

question1_radioButton=StringVar(value="0")

Question1=Label(root, text ="Do you experience shortness of breath during routine activites")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()

question2_radioButton=StringVar(value="0")
Question2=Label(root, text ="Do you experience shortness of breath while at rest/lying down?")
Question2.pack()
question2_r1=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question2_r1.pack()
question2_r2=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question2_r2.pack()

question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="Do you feel short of breath while lying flat and feel the need to stack multiple pillows to sleep well?")
Question3.pack()
question3_r1=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question3_r1.pack()
question3_r2=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question3_r2.pack()


question4_radioButton=StringVar(value="0")
Question4=Label(root, text ="Do you experience persistent wheezing / coughing that produces white or pink blood tinged mucus?")
Question4.pack()
question4_r1=Radiobutton(root, text = "yes", variable=question4_radioButton, value="yes")
question4_r1.pack()
question4_r2=Radiobutton(root, text = "no", variable=question4_radioButton, value="no")
question4_r2.pack()


question5_radioButton=StringVar(value="0")
Question5=Label(root, text ="Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?")
Question5.pack()
question5_r1=Radiobutton(root, text = "yes", variable=question5_radioButton, value="yes")
question5_r1.pack()
question5_r2=Radiobutton(root, text = "no", variable=question5_radioButton, value="no")
question5_r2.pack()


question6_radioButton=StringVar(value="0")
Question6=Label(root, text ="Do you feel tired while doing routine activities such as shopping, climbing stairs, carrying groceries or walking?")
Question6.pack()
question6_r1=Radiobutton(root, text = "yes", variable=question6_radioButton, value="yes")
question6_r1.pack()
question6_r2=Radiobutton(root, text = "no", variable=question6_radioButton, value="no")
question6_r2.pack()


question7_radioButton=StringVar(value="0")
Question7=Label(root, text ="Have you experienced loss of appetite (frequent feeling of being full) or nausea recently")
Question7.pack()
question7_r1=Radiobutton(root, text = "yes", variable=question7_radioButton, value="yes")
question7_r1.pack()
question7_r2=Radiobutton(root, text = "no", variable=question7_radioButton, value="no")
question7_r2.pack()


question8_radioButton=StringVar(value="0")
Question8=Label(root, text ="Do you feel any of these symptoms - confusion, disorientation or loss of memory?")
Question8.pack()
question8_r1=Radiobutton(root, text = "yes", variable=question8_radioButton, value="yes")
question8_r1.pack()
question8_r2=Radiobutton(root, text = "no", variable=question8_radioButton, value="no")
question8_r2.pack()


question9_radioButton=StringVar(value="0")
Question9=Label(root, text ="Do you often feel that you are having a racing heartbeat and experience palpitations?")
Question9.pack()
question9_r1=Radiobutton(root, text = "yes", variable=question9_radioButton, value="yes")
question9_r1.pack()
question9_r2=Radiobutton(root, text = "no", variable=question9_radioButton, value="no")
question9_r2.pack()



def fever_score():
    score = 0 
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question5_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question6_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question7_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question8_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question9_radioButton.get()=="yes":
        score = score+20
        print(score)
        
    if score <= 20:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif  score > 20 and score <= 40:
        messagebox.showinfo("Report","You might perhaps have to vist a doctor")
    else :
        messagebox.showinfo("Report", "I strongly advise you to vist a doctor")
btn = Button(root, text= "click me", command= fever_score)
btn.pack()
root.mainloop()
