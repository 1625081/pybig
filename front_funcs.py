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
from tkinter import filedialog
root=Tk()
root.title="My Database"

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
		exec("button"+str(Stu.uid)+"=Checkbutton(root,text=str(Stu.uid),onvalue=1,variable="+tmpvar+",offvalue=0,bg='White',command=callback,height=2,width=8,anchor=W)")
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
	showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\n')
	for var in varlist:
		if var.get()==1:
			Stu=showlist[varlist.index(var)]
			showbox.insert(END,"%d\t%s\t%s\t%d\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
	editbutton.config(text="确认",command=editdataconfirm)
	for btn in generalbuttons:
		if btn!=editbutton:
			btn.config(state=DISABLED)

def editdataconfirm():
	global my
	global showlist
	global varlist,btnlist,labelist
	raw=showbox.get(4.0,END)
	rawdata=raw.split('\n')
	print(rawdata)
	rawdata.pop()
	uids=[]
	for var in varlist:
		if var.get()==1:
			print(rawdata)
			tmpdata=rawdata.pop(0).split('\t')
			print(tmpdata)
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
						showbox.insert(END,"%d\t%s\t%s\t%d\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
				break
			#Judge the situation of edit
			if type(my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))==str:
				messagebox.showerror("Error",my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
				#reset
				showbox.delete(4.0,END)
				for var in varlist:
					if var.get()==1:
						Stu=showlist[varlist.index(var)]
						showbox.insert(END,"%d\t%s\t%s\t%d\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
				break
	else:
		showbox.delete(1.0,END)
		showbox.insert(END,'uid:\t'+'      '+'name:\t\tsex:\theight(cm):\n')
		editbutton.config(text="修改",command=dataedit)
		for btn in generalbuttons:
			if btn!=editbutton:
				btn.config(state=NORMAL)
		showlist=my.data[:]
		varlist,btnlist,labelist=datas()
		messagebox.showinfo("Successed","Your new data is updated!")
		datashow()

def newdataconfirm():
	global my
	global showlist
	global varlist,btnlist,labelist
	raw=showbox.get(4.0,END)
	print(raw)
	rawdata=raw.split('\n')
	print(rawdata)
	rawdata.pop()
	print(rawdata)
	for newdata in rawdata:
		if newdata=="":continue
		tmpdata=newdata.split('\t')
		print(tmpdata)
		if my.add(int(tmpdata[0]),tmpdata[1],tmpdata[2],int(tmpdata[3]))!="Successed.":
			messagebox.showerror("Error",my.add(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
			showbox.delete(4.0,END)
			break
	else:
		showbox.delete(1.0,END)
		showbox.insert(END,'uid:\t'+'      '+'name:\t\tsex:\theight(cm):\n')
		createbutton.config(text="新增",command=datanew)
		for btn in generalbuttons:
			if btn!=createbutton:
				btn.config(state=NORMAL)
		messagebox.showinfo("Successed","Your new data is updated!")
		showlist=my.data[:]
		varlist,btnlist,labelist=datas()
		datashow()


def datanew():
	showbox.delete(1.0,END)
	showbox.insert(END,'Please enter new data in the following format:\n')
	showbox.insert(END,"Enter \'TAB\' to devide each column\n")
	showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\n')
	createbutton.config(text="确认",command=newdataconfirm)
	for btn in generalbuttons:
		if btn!=createbutton:
			btn.config(state=DISABLED)

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

def dataopen():
	global my
	global showlist,btnlist,varlist,labelist
	qsave=my.data[:]
	my.data=[]
	name=filedialog.askopenfilename()
	if name !="":
		with open(name,'r+') as f:
			reader=csv.reader(f)
			for row in reader:
				if len(row)!=4:
					messagebox.showerror("Error","Please Check Your FILE format!")
					my.data=qsave[:]
					break
				if my.add(row[0],row[1],row[2],row[3])!="Successed.":
					messagebox.showerror("Error",my.add(row[0],row[1],row[2],row[3]))
					my.data=qsave[:]
					break
			else:
				messagebox.showinfo("Successed.","Your file have been read successfully.")
				showlist=my.data[:]
				varlist,btnlist,labelist=datas()
				datashow()
	else:messagebox.showinfo("Attention","File can't be NULL.")

def datasave():
	global my
	name=filedialog.asksaveasfilename()
	with open(name, 'w+') as csvfile:
		try:
			spamwriter = csv.writer(csvfile,dialect='excel')
			for Stu in my.data:
				tmplist=[Stu.uid,Stu.name,Stu.sex,Stu.height]
				spamwriter.writerow(tmplist)
		except:
			messagebox.showerror("Error","Unknown Error!")
		else:
			messagebox.showinfo("Successed.","File saved as CSV successfully.")
showlist=my.data[:]
root.geometry('400x400')
showbox=Text(root,width=47)

#button label全局化
varlist,btnlist,labelist=datas()
