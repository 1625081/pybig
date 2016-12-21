import csv
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root=Tk()
name=filedialog.asksaveasfilename()
with open(name, 'w+') as csvfile:
	spamwriter = csv.writer(csvfile,dialect='excel')
	spamwriter.writerow(['a', '1', '1', '2', '2'])
	spamwriter.writerow(['b', '3', '3', '6', '4'])
	spamwriter.writerow(['c', '7', '7', '10', '4'])
	spamwriter.writerow(['d', '11','11','11', '1'])
	spamwriter.writerow(['e', '12','12','14', '3'])