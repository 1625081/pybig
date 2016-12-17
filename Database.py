from stu import *
class Database:
	def __init__(self,data):
		self.data=data
		self.index=len(data)

	def add(self,uid,name,sex,height):
		for Stu in self.data:
			if uid==Stu.uid:return "Uid already exists!"
		
		#validations
		newStu=Student(uid,name,sex,height)
		if newStu.validate()!="Data is alright.":
			return newStu.validate()
		else:
			self.data.append(newStu)
			return "Successed."
			#self.save()'''

	def show(self):
		for Stu in self.data:
			Stu.show()

	def edit(self,name,sex,height,*uids):#here we confirm that uid can't be changed
		try:
			result=[]
			for uid in uids:
				Stu=self.search(str(uid))
				newStu=self.search(str(uid)).edit(name,sex,height)
				if type(newStu)==str:
					return newStu
				else:
					self.data[self.data.index(Stu)]=newStu
					result.append(newStu)
			return result #return a list of result
		except:return "Unknown Error!"

	def search(self,keyword):
		result=[]
		for Stu in self.data: #keyword must be a string as no "int" before "input()"
			if str(Stu.uid)==keyword or str(Stu.name)==keyword or str(Stu.sex)==keyword or str(Stu.height)==keyword:
					result.append(Stu)
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
					if Stu.uid <= int(upper) and Stu.uid >= int(lower):
						result.append(Stu)
				except:return "Search Error!Please Check your inputs!"
		elif category=="height":
			for Stu in self.data:
				try:
					if Stu.height <= int(upper) and Stu.height >= int(lower):
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
		datatmp=[]
		for Stu in self.data:
			if Stu.uid in deletelist:
				continue
			else:
				datatmp.append(Stu)
		self.data=datatmp[:]
		#for Stu in self.data:
		#	Stu.show()

	def open(self):	
		pass
	def save(self):
		pass