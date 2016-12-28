def callback():
	for var in my.varlist:
		if var.get()==1:
			my.btnlist[my.varlist.index(var)].config(bg="Yellow")
			my.labelist[my.varlist.index(var)].config(bg="Yellow")
		else:
			my.btnlist[my.varlist.index(var)].config(bg="White")
			my.labelist[my.varlist.index(var)].config(bg="White")

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
	for var in my.varlist:
		showbox.window_create(END,window=my.btnlist[my.varlist.index(var)])
		showbox.window_create(END,window=my.labelist[my.varlist.index(var)])
		showbox.insert(END,"\\n")

def dataall():
	global showlist,my
	showlist=my.data[:]
	my.varlist,my.btnlist,my.labelist=datas()
	datashow()

def dataedit():
	global my
	showbox.delete(1.0,END)
	showbox.insert(END,'Please enter new data in the following format:\\n')
	showbox.insert(END,"Enter \'TAB\' to devide each column\\n")
	showbox.insert(END,'uid:\\tname:\\tsex:\\theight(cm):\\n')
	for var in my.varlist:
		if var.get()==1:
			Stu=showlist[my.varlist.index(var)]
			showbox.insert(END,"%d\\t%s\\t%s\\t%d\\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
	editbutton.config(text="确认",command=editdataconfirm)
	for btn in generalbuttons:
		if btn!=editbutton:
			btn.config(state=DISABLED)

def editdataconfirm():
	global my
	global showlist
	raw=showbox.get(4.0,END)
	rawdata=raw.split('\\n')
	#print(rawdata)
	rawdata.pop()
	uids=[]
	qsave=my.data[:]
	for var in my.varlist:
		if var.get()==1:
			tmpdata=rawdata.pop(0).split('\\t')
			formeruid=str(showlist[my.varlist.index(var)].uid)
			if formeruid!=tmpdata[0]:
				messagebox.showerror("Error","Uid must remain unchanged!")
				#reset
				showbox.delete(4.0,END)
				for var in my.varlist:
					if var.get()==1:
						Stu=showlist[my.varlist.index(var)]
						showbox.insert(END,"%d\\t%s\\t%s\\t%d\\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
				break

			#Judge the situation of edit
			if type(my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))==str:
				messagebox.showerror("Error",my.edit(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
				#reset
				showbox.delete(4.0,END)
				for var in my.varlist:
					if var.get()==1:
						Stu=showlist[my.varlist.index(var)]
						showbox.insert(END,"%d\\t%s\\t%s\\t%d\\n"%(int(Stu.uid),Stu.name,Stu.sex,int(Stu.height)))
				break
	else:
		my.former.append(qsave[:])
		showbox.delete(1.0,END)
		showbox.insert(END,'uid:\\t'+'      '+'name:\\t\\tsex:\\theight(cm):\\n')
		editbutton.config(text="修改",command=dataedit)
		for btn in generalbuttons:
			if btn!=editbutton:
				btn.config(state=NORMAL)
		showlist=my.data[:]
		my.varlist,my.btnlist,my.labelist=datas()
		messagebox.showinfo("Successed","Your new data is updated!")
		datashow()

def newdataconfirm():
	global my
	global showlist
	#global varlist,btnlist,labelist
	raw=showbox.get(4.0,END)
	#print(raw)
	rawdata=raw.split('\\n')
	#print(rawdata)
	rawdata.pop()
	#print(rawdata)
	for newdata in rawdata:
		if newdata=="":continue
		tmpdata=newdata.split('\\t')
		#print(tmpdata)
		if my.add(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3])!="Successed.":
			messagebox.showerror("Error",my.add(tmpdata[0],tmpdata[1],tmpdata[2],tmpdata[3]))
			showbox.delete(4.0,END)
			break
	else:
		showbox.delete(1.0,END)
		showbox.insert(END,'uid:\\t'+'      '+'name:\\t\\tsex:\\theight(cm):\\n')
		createbutton.config(text="新增",command=datanew)
		for btn in generalbuttons:
			if btn!=createbutton:
				btn.config(state=NORMAL)
		messagebox.showinfo("Successed","Your new data is updated!")
		showlist=my.data[:]
		my.varlist,my.btnlist,my.labelist=datas()
		datashow()


def datanew():
	showbox.delete(1.0,END)
	showbox.insert(END,'Please enter new data in the following format:\\n')
	showbox.insert(END,"Enter \'TAB\' to devide each column\\n")
	showbox.insert(END,'uid:\tname:\tsex:\theight(cm):\\n')
	createbutton.config(text="确认",command=newdataconfirm)
	for btn in generalbuttons:
		if btn!=createbutton:
			btn.config(state=DISABLED)

def datasearch():
	key=searchbox.get(1.0,END)
	k=key.split('\\n')
	global showlist
	#global varlist,btnlist,labelist	
	if len(k[0].split("!"))!=1:
		showlist=[]
		keys=k[0].split("!")
		showlist.append(my.accurate_search(keys[0],keys[1]))
		my.varlist,my.btnlist,my.labelist=datas()
		datashow()
	elif len(k[0].split(":"))==1:
		showlist=my.search(k[0])[:]
		my.varlist,my.btnlist,my.labelist=datas()
		datashow()
	elif len(k[0].split(":"))==3:
		keys=k[0].split(":")
		try:
			showlist=my.condition_search(keys[0],keys[1],keys[2])[:]
			my.varlist,my.btnlist,my.labelist=datas()
			datashow()
		except:
			messagebox.showerror("Error",my.condition_search(keys[0],keys[1],keys[2]))
			return

def datadel():
	global showlist
	global my
	rlist=my.varlist[:]
	rlist.reverse()
	deletelist=[]
	for var in rlist:
		if var.get()==1:
			showbox.delete(my.labelist[my.varlist.index(var)])
			deletelist.append(showlist.pop(my.varlist.index(var)))
			showbox.delete(my.btnlist[my.varlist.index(var)])
	my.delete(deletelist)
	showlist=my.data[:]
	my.varlist,my.btnlist,my.labelist=datas()
	datashow()

def dataopen():
	global my
	global showlist
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
				my.varlist,my.btnlist,my.labelist=datas()
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

def datarollback():
	global my,showlist
	my.rollback()
	showlist=my.data[:]
	my.varlist,my.btnlist,my.labelist=datas()
	datashow()