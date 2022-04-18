from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -1")
def shutdown():
    os.system("shutdown /s /t 1")


st=Tk()
st.title("shutdown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button=Button(st,text="Restart", font=("Time New Roman", 20, "bold"), relief=RAISED,cursor="plus")
r_button.place(x=150, y=60, height=50, width=200, command=restart())

r_button=Button(st,text="Restart Time",font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus")
r_button.place(x=150, y=170, height=50, width=200, command=restart_time())


r_button=Button(st,text="Log Out", font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus")
r_button.place(x=150, y=270, height=50, width=200, command=logout())


r_button=Button(st,text="Shut Down",font=("Time New Roman", 20, "bold"), relief=RAISED, cursor="plus")
r_button.place(x=150, y=370, height=50, width=200, command=shutdown())



st.mainloop()