from stu import *
class Database:
	def __init__(self,data):
		self.data=data
		self.index=len(data)
		self.former=data
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
			self.former=self.data[:]
			self.data.append(newStu)
			return "Successed."
			#self.save()'''

	def show(self):
		for Stu in self.data:
			Stu.show()

	def edit(self,uid,name,sex,height):#here we confirm that uid can't be changed
		try:
			Stu=self.search(str(uid))[0]
			newStu=self.search(str(uid))[0].edit(name,sex,height)
			if type(newStu)==str:
				return newStu
			else:
				self.data[self.data.index(Stu)]=newStu
				return newStu #return a list of result
		except:return "Unknown Error!"

	def search(self,keyword):
		result=[]
		dicts=["uid","name","sex","height"]
		for Stu in self.data: #keyword must be a string as no "int" before "input()"
			for key in dicts:
				if eval("len(str(Stu."+key+").split(keyword))>=2"):
						if not Stu in result:result.append(Stu)
		#if len(result)==1:return result[0]
		return result #maybe返回空列表


	def condition_search(self,*conditions):
		category=conditions[0]
		upper=conditions[1]
		lower=conditions[2]
		#keyword=conditions[3]
		result=[]
		#if category=="sex" or category=="name":return self.search(keyword)
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

	def accurate_search(self,mode,keyword):
		#accurate search return only one result,so it's not recommended to search for sex or height 
		#eval()is a great way to run raw code
		dicts={0:"uid",1:"name",2:"sex",3:"height"}
		for Stu in self.data:
			if eval("str(Stu."+eval("dicts[mode]")+")==keyword"):
				return Stu
		else: print("No Found.")

	def delete(self,deletelist):
		self.former=self.data[:]
		for Stu in deletelist:
			self.data.remove(Stu)

	def open(self):	
		pass
	def save(self):
		pass