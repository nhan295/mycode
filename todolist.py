from tkinter import* 
from tkinter import messagebox 
import pickle

def newTask():
    task=my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,"end")
    else: 
        messagebox.showwarning("Enter task!")

def deleteTask():
    lb.delete(ANCHOR)

def cross_off_item():
    lb.itemconfig(
        lb.curselection(),
        fg="#dedede")

def save_task():
   task=lb.get(0, lb.size())
   pickle.dump(task,open("task.dat","wb"))


ws = Tk()
 #size of window
ws.geometry('500x400+500+400')
ws.title('MyToDoList')
ws.config(bg='#446eb3')
ws.resizable(width=False, height=False) 

frame = Frame(ws)
frame.pack(pady=10)

lb=Listbox(
frame,
width=25,
height=8,
font=('Times',18),
bd=0,
fg='#692323',
highlightthickness=0,
selectbackground='#a6a6a6',
activestyle="none",
)
lb.pack(side=LEFT,fill=BOTH)
#fake data
task_list=[
    
]
for item in task_list:
    lb.insert(END, item)
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
#link with scrollbar
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview) 
#input box
my_entry=Entry(
    ws,
    font=('Times',24),
)
my_entry.pack(pady=20)

button_frame=Frame(ws)
button_frame.pack(pady=20)

addTask_btn=Button(
    button_frame,
    text='Add Task',
    font=('Times',12),
    bg='#a8a8a8',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete',
    font=('Times',12),
    bg='#a8a8a8',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH,side=LEFT)

crossTask_btn = Button(
    button_frame,
    text="Completed",
    font=('Times',12),
    bg="#a8a8a8",
    padx=20,
    pady=10,
    command=cross_off_item

)
crossTask_btn.pack(fill=BOTH,side=LEFT)

saveTask_btn = Button(
    button_frame,
    text="Save",
    font=('Times',12),
    bg="#a8a8a8",
    padx=20,
    pady=10,
    command=save_task
)
saveTask_btn.pack(fill=BOTH, side=LEFT)

ws.mainloop()
