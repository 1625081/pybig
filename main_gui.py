from tkinter import *
root=Tk()
root.title="My Database"
showlist=[]
root.geometry('400x400')
showbox=Text(root)
button=Button(root,text="展示",command=show)
button.pack(side=RIGHT,anchor=N,pady=20)
showbox.pack(side=RIGHT,fill='both')
showbox.insert(END,'someyhing\n')
showbox.insert(END,'someyhing')

def show():
	for Stu in showlist:
		content=str(Stu.uid)+"\t"+str(Stu.name)+"\t"+str(Stu.sex)+"\t"+(Stu.height)+"\n"
		showbox.insert(END,content)
mainloop()