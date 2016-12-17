from Database import *

data=[]
a=Student(1,"jack","boy",180)
b=Student(2,"jac","boy",184)
c=Student(3,"ja","boy",170)
d=Student(4,"j","boy",155)
data=[a,b,c,d]
my=Database(data)
my.add(5,"mary","girl",160)


from tkinter import *

def callback():
	print(varlist)
	for var in varlist:
		if var.get()==1:
			btnlist[varlist.index(var)].config(bg="Yellow")
			labelist[varlist.index(var)].config(bg="Yellow")
			#exec("button"+str(Stu.uid)+".config(bg='Yellow')")
			#exec("label"+str(Stu.uid)+".config(bg='Yellow')")
		else:
			print(var.get())
			btnlist[varlist.index(var)].config(bg="White")
			labelist[varlist.index(var)].config(bg="White")

def datas():
	varlist=[]
	btnlist=[]
	labelist=[]
	for Stu in showlist:
		tmpvar="var"+str(Stu.uid)	
		locals()[tmpvar]=IntVar()
		locals()[tmpvar].set(0)
		content=str(Stu.name)+"\t"+str(Stu.sex)+"\t"+str(Stu.height)+"\t"
		exec("button"+str(Stu.uid)+"=Checkbutton(root,text=str(Stu.uid),onvalue=1,variable="+tmpvar+",offvalue=0,bg='White',command=callback,width=2,height=2)")
		locals()["label"+str(Stu.uid)]=Label(root,text=content,padx=15,pady=10,bg="White",relief=FLAT)
		varlist.append(locals()[tmpvar])
		btnlist.append(locals()["button"+str(Stu.uid)])
		labelist.append(locals()["label"+str(Stu.uid)])
	return varlist,btnlist,labelist

def datashow():
	showbox.delete(2.0,END)
	#varlist,btnlist,labelist=datas()
	for var in varlist:
		showbox.window_create(END,window=btnlist[varlist.index(var)])
		showbox.window_create(END,window=labelist[varlist.index(var)])
		showbox.insert(END,'\n')




'''def datashow():
	#this func show all data
	varlist=[]
	btnlist=[]
	labelist=[]
	showbox.delete(2.0,END)
	for Stu in showlist:
		tmpvar="var"+str(Stu.uid)	
		locals()[tmpvar]=IntVar()
		locals()[tmpvar].set(0)
		content=str(Stu.name)+"\t"+str(Stu.sex)+"\t"+str(Stu.height)+"\t"
		exec("button"+str(Stu.uid)+"=Checkbutton(root,text=str(Stu.uid),onvalue=1,variable="+tmpvar+",offvalue=0,bg='White',command=callback,width=2,height=2)")
		locals()["label"+str(Stu.uid)]=Label(root,text=content,padx=15,pady=10,bg="White",relief=FLAT)
		exec("showbox.window_create(END,window="+"button"+str(Stu.uid)+")")
		exec("showbox.window_create(END,window="+"label"+str(Stu.uid)+")")
		varlist.append(locals()[tmpvar])
		btnlist.append(locals()["button"+str(Stu.uid)])
		labelist.append(locals()["label"+str(Stu.uid)])
		showbox.insert(END,'\n')
	return varlist,btnlist,labelist'''

def dataedit():
	pass

def datadel():
	global showlist
	for Stu in showlist:
		if eval("var"+str(Stu.uid)+".get()==1"):
			showlist.remove(Stu)



def datanew():
	pass

def datasearch():
	key=searchbox.get(1.0,END)
	k=key.split('\n')
	showlist=my.search(key)[:]
	datashow()

root=Tk()
root.title="My Database"
showlist=data[:]
root.geometry('400x400')
showbox=Text(root,width=47)

#button label全局化

varlist,btnlist,labelist=datas()

showbutton=Button(root,text="展示",command=datashow)
editbutton=Button(root,text="修改",command=dataedit)
deletebutton=Button(root,text="删除",command=datadel)
createbutton=Button(root,text="新增",command=datanew)
searchlabel=Label(root,text="Search:")
searchbox=Text(root,height=1,width=10)
searchbtn=Button(root,text="Go!",command=datasearch)

chooselist=[]

#showbox.grid(row=0,column=0,rowspan=3,columnspan=5,sticky=W,)
showbutton.grid(row=0,column=16,sticky=NE,padx=6,pady=9)
createbutton.grid(row=1,column=16,sticky=NE,padx=6,pady=6)
editbutton.grid(row=2,column=16,sticky=NE,padx=6,pady=6)
deletebutton.grid(row=3,column=16,sticky=NE,padx=6,pady=6)

searchlabel.grid(row=0,column=0,sticky=W)
searchbox.grid(row=0,column=1,sticky=W)
searchbtn.grid(row=0,column=2,sticky=W)
showbox.grid(row=1,column=0,rowspan=17,columnspan=15,sticky=E)
#createbutton.pack(anchor=NE,pady=0)
#showbox.pack(anchor=N,fill=BOTH)
showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\n')



mainloop()

#edit example
'''for afteredit in my.edit("mike","boy",165,(5)):
	afteredit.show()'''
#search example
'''for answer in my.condition_search("height","180","100","boy"):
	answer.show()
my.accurate_search(0,"1")'''