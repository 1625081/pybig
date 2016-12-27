from Database import *
import csv

a=Student(1,"jack","boy",180)
b=Student(2,"jac","boy",184)
c=Student(3,"ja","boy",170)
d=Student(4,"j","boy",155)
e=Student(5,"mary","girl",160)
data=[a,b,c,d,e]
my=Database(data)

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from front_funcs import *

exec(funcs_string)

def helpme(event):
	helpwindow=Tk()
	helpwindow.geometry('300x300')
	helptext=Text(helpwindow,width=200)
	helptext.pack()
	helptext.insert(END,"【搜索相关事项】\n目前直接搜索展现出的结果是模糊搜索的结果，条件搜索和精确搜索方法如下：\n【条件搜索】要搜索的项目名:上界:下界\n可选择的项目名只有uid和height\n[例子]uid:10:1\n则1<=uid<=10的数据会被输出\n【精确搜索】搜索项+!+具体值\n[例子]uid!1\n则uid为1的用户会被输出\n更多说明请访问\nhttps://github.com/1625081/pybig")
root=Tk()
root.title="My Database"
showlist=my.data[:]
root.geometry('420x400')
showbox=Text(root,width=47)
ybar=Scrollbar(root,orient=VERTICAL)
ybar.config(command=showbox.yview)
showbox.config(yscrollcommand=ybar.set)
#button label全局化

#varlist,btnlist,labelist=datas()

showbutton=Button(root,text="全部",command=dataall)
editbutton=Button(root,text="修改",command=dataedit)
deletebutton=Button(root,text="删除",command=datadel)
createbutton=Button(root,text="新增",command=datanew)
openbutton=Button(root,text="打开",command=dataopen)
savebutton=Button(root,text="保存",command=datasave)
rollbutton=Button(root,text="回卷",command=datarollback)
searchlabel=Label(root,text="Search:")
searchbox=Text(root,height=1,width=15)
searchbtn=Button(root,text="Go!",command=datasearch)
photo=PhotoImage(file="info-small.png",width=30,height=30)
helpimg=Label(root,image=photo)
helpimg.bind("<Button-1>",helpme)
generalbuttons=[showbutton,editbutton,deletebutton,createbutton,openbutton,savebutton,searchbtn,rollbutton]

showbutton.grid(row=0,column=16,sticky=NE,padx=6,pady=9)
createbutton.grid(row=1,column=16,sticky=NE,padx=6,pady=6)
editbutton.grid(row=2,column=16,sticky=NE,padx=6,pady=6)
deletebutton.grid(row=3,column=16,sticky=NE,padx=6,pady=6)
openbutton.grid(row=4,column=16,sticky=NE,padx=6,pady=6)
savebutton.grid(row=5,column=16,sticky=NE,padx=6,pady=6)
rollbutton.grid(row=6,column=16,sticky=NE,padx=6,pady=6)

searchlabel.grid(row=0,column=0,sticky=W)
searchbox.grid(row=0,column=1,sticky=W)
searchbtn.grid(row=0,column=3,sticky=W)
helpimg.grid(row=0,column=4,sticky=W)
showbox.grid(row=1,column=0,rowspan=17,columnspan=14,sticky=E)
ybar.grid(row=1,column=15,rowspan=17,sticky=NS)
showbox.insert(END,'uid:\t'+'      '+'name:\t\tsex:\theight(cm):\n')

mainloop()