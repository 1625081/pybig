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
from tkinter import messagebox
def callback():
	for var in varlist:
		if var.get()==1:
			btnlist[varlist.index(var)].config(bg="Yellow")
			labelist[varlist.index(var)].config(bg="Yellow")
		else:
			btnlist[varlist.index(var)].config(bg="White")
			labelist[varlist.index(var)].config(bg="White")

def datas():
	showbox.delete(2.0,END)
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
	#showbox.delete(2.0,END)
	#varlist,btnlist,labelist=datas()
	for var in varlist:
		showbox.window_create(END,window=btnlist[varlist.index(var)])
		showbox.window_create(END,window=labelist[varlist.index(var)])
		showbox.insert(END,'\n')

def dataall():
	global showlist
	showlist=my.data[:]
	global varlist,btnlist,labelist
	varlist,btnlist,labelist=datas()
	datashow()

def dataedit():
	global varlist
	showbox.delete(1.0,END)
	showbox.insert(END,'Please enter new data in the following format:\n')
	showbox.insert(END,"Enter \'TAB\' to devide each column\n")
	showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\t')
	showbox.insert(END,'\n')
	for var in varlist:
		if var.get()==1:
			Stu=showlist[varlist.index(var)]
			showbox.insert(END,"%d\t%s\t%s\t%d\n"%(Stu.uid,Stu.name,Stu.sex,Stu.height))
	editbutton.config(text="确认",command=editdataconfirm)
	showbutton.config(state=DISABLED)
	deletebutton.config(state=DISABLED)
	searchbtn.config(state=DISABLED)
	createbutton.config(state=DISABLED)

def editdataconfirm():
	global my
	global showlist
	global varlist,btnlist,labelist
	raw=showbox.get(4.0,END)
	rawdata=raw.split('\n')
	rawdata.pop()
	uids=[]
	for var in varlist:
		if var.get()==1:
			tmpdata=rawdata.pop(0).split('\t')
			#Judge whether uid already existed
			if not tmpdata[0] in uids:
				uids.append(tmpdata[0])
			else:
				messagebox.showerror("Error","Uid already existed!")
				#reset
				showbox.delete(4.0,END)
				for var in varlist:
					if var.get()==1:
						Stu=showlist[varlist.index(var)]
						showbox.insert(END,"%d\t%s\t%s\t%d\n"%(Stu.uid,Stu.name,Stu.sex,Stu.height))
				break
			#Judge the situation of edit
			if type(my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))==str:
				messagebox.showerror("Error",my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
				#reset
				showbox.delete(4.0,END)
				for var in varlist:
					if var.get()==1:
						Stu=showlist[varlist.index(var)]
						showbox.insert(END,"%d\t%s\t%s\t%d\n"%(Stu.uid,Stu.name,Stu.sex,Stu.height))
				break
	else:
		showbox.delete(1.0,3.0)
		editbutton.config(text="修改",command=dataedit)
		showbutton.config(state=NORMAL)
		deletebutton.config(state=NORMAL)
		searchbtn.config(state=NORMAL)
		createbutton.config(state=NORMAL)
		showlist=my.data[:]
		varlist,btnlist,labelist=datas()
		messagebox.showinfo("Successed","Your new data is updated!")
		datashow()

def newdataconfirm():
	global my
	global showlist
	global varlist,btnlist,labelist
	raw=showbox.get(4.0,END)
	rawdata=raw.split('\n')
	rawdata.pop()
	for newdata in rawdata:
		tmpdata=newdata.split('\t')
		if my.add(int(tmpdata[0]),tmpdata[1],tmpdata[2],int(tmpdata[3]))!="Successed.":
			messagebox.showerror("Error",my.add(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
			showbox.delete(4.0,END)
			break
	else:
		showbox.delete(1.0,3.0)
		createbutton.config(text="新增",command=datanew)
		showbutton.config(state=NORMAL)
		deletebutton.config(state=NORMAL)
		searchbtn.config(state=NORMAL)
		editbutton.config(state=NORMAL)
		messagebox.showinfo("Successed","Your new data is updated!")
		showlist=my.data[:]
		varlist,btnlist,labelist=datas()
		datashow()


def datanew():
	showbox.delete(1.0,END)
	showbox.insert(END,'Please enter new data in the following format:\n')
	showbox.insert(END,"Enter \'TAB\' to devide each column\n")
	showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\t')
	showbox.insert(END,'\n')
	createbutton.config(text="确认",command=newdataconfirm)
	showbutton.config(state=DISABLED)
	deletebutton.config(state=DISABLED)
	searchbtn.config(state=DISABLED)
	editbutton.config(state=DISABLED)

def datasearch():
	key=searchbox.get(1.0,END)
	k=key.split('\n')
	global showlist
	global varlist,btnlist,labelist	
	if len(k[0].split(":"))==1:
		showlist=my.search(k[0])[:]
		varlist,btnlist,labelist=datas()
		datashow()
	elif len(k[0].split(":"))==3:
		keys=k[0].split(":")
		try:
			showlist=my.condition_search(keys[0],keys[1],keys[2])[:]
			varlist,btnlist,labelist=datas()
			datashow()
		except:
			messagebox.showerror("Error",my.condition_search(keys[0],keys[1],keys[2]))
			return

def datadel():
	global varlist,btnlist,labelist
	global my
	rlist=varlist[:]
	rlist.reverse()
	for var in rlist:
		if var.get()==1:
			showbox.delete(labelist[varlist.index(var)])
			my.data.remove(showlist.pop(varlist.index(var)))
			showbox.delete(btnlist[varlist.index(var)])
	varlist,btnlist,labelist=datas()
	datashow()


root=Tk()
root.title="My Database"
showlist=my.data[:]
root.geometry('400x400')
showbox=Text(root,width=47)

#button label全局化

varlist,btnlist,labelist=datas()

showbutton=Button(root,text="全部",command=dataall)
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