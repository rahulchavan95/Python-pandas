import os
import fnmatch
from sys import *
import xlsxwriter


def ExcelCreate(name):
	workbook=xlsxwriter.Workbook(name)
	worksheet=workbook.add_worksheet()

	worksheet.write('A1','Name')
	worksheet.write('B1','College')
	worksheet.write('C1','Mail Id')
	worksheet.write('D1','Mobile')

	workbook.close()


def main():
	if(len(argv)!=2):
		print("invalid number of arguments")

	try:
		ExcelCreate(argv[1])
	
	except Exception:
		print("invalid input")


if __name__=="__main__":	
	main()
