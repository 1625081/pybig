from stu import *
class Database:
	def __init__(self,data):
		self.data=data
		self.former=[]
		self.former.append(self.data[:])
		self.btnlist=[]
		self.labelist=[]
		self.varlist=[]
	def add(self,uid,name,sex,height):
		for Stu in self.data:
			if str(uid)==str(Stu.uid):return "Uid already exists!"
		
		#validations
		newStu=Student(uid,name,sex,height)
		if newStu.validate()!="Data is alright.":
			return newStu.validate()
		else:
			self.former.append(self.data[:])
			self.data.append(newStu)
			return "Successed."
			#self.save()'''

	def edit(self,uid,name,sex,height):#here we confirm that uid can't be changed
		#try:
			Stu=self.accurate_search("uid",str(uid))
			newStu=self.accurate_search("uid",str(uid)).edit(name,sex,height)
			if type(newStu)==str:
				return newStu
			else:
				self.data[self.data.index(Stu)]=newStu
				return newStu #return a list of result
		#except:return "Unknown Error!"

	def search(self,keyword):
		result=[]
		dicts=["uid","name","sex","height"]
		for Stu in self.data: #keyword must be a string as no "int" before "input()"
			for key in dicts:
				if eval("len(str(Stu."+key+").split(keyword))>=2"):
						if not Stu in result:result.append(Stu)
		#if len(result)==1:return result[0]
		return result #maybe返回空列表

	def accurate_search(self,mode,keyword):
		for Stu in self.data:
			if eval("str(Stu."+mode+")==keyword"):
				return Stu 

	def condition_search(self,*conditions):
		category=conditions[0]
		upper=conditions[1]
		lower=conditions[2]
		result=[]
		if category=="uid":
			for Stu in self.data:
				try:
					if int(Stu.uid) <= int(upper) and int(Stu.uid) >= int(lower):
						result.append(Stu)
				except:return "Search Error!Please Check your inputs!"
		elif category=="height":
			for Stu in self.data:
				try:
					if int(Stu.height) <= int(upper) and int(Stu.height) >= int(lower):
						result.append(Stu)
				except:return "Search Error!Please Check your inputs!"
		else: return "Search Error!Please Check your inputs!"
		return result

	def delete(self,deletelist):
		self.former.append(self.data[:])
		for Stu in deletelist:
			self.data.remove(Stu)
	def rollback(self):
		if len(self.former)>1: 
			tmp=self.former.pop()
			self.data=tmp[:]

