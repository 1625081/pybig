class Student:
	def __init__(self,uid,name,sex,height):
		#if self.validate(uid,name,sex,height)!="Data is alright.":
		#	print (self.validate(uid,name,sex,height))
		self.uid=uid
		self.name=name
		self.sex=sex
		self.height=height
	def show(self):
		print(self.uid,"\t",end="")
		print(self.name,"\t",end="")
		print(self.sex,"\t",end="")
		print(self.height)
	
	def edit(self,name,sex,height):
		uid=self.uid
		temp=Student(uid,name,sex,height)
		if temp.validate()!="Data is alright.":
			return temp.validate()
		else:
			self=temp
			return self
	
	def validate(self):
		if self.sex!="boy" and self.sex!="girl":return "Sex is not correct!"
		try:
			test0=int(self.uid)
			test1=int(self.height)
		except ValueError:
			return "uid or height should be integer!"
		if int(self.uid)<0 or int(self.height)<0 or int(self.height)>300:return "Please check the data you input!"
		return "Data is alright."
