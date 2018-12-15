#/usr/bin/python
# coding: utf-8

# Chao-Chuan Lu 20181215

import math
from tkinter import *
from tkinter import ttk

def calculate():
	try:
		money = float(moneyInput.get())
		interest = float(interestInput.get())
		times = float(timesInput.get())
		if isPeriodic.get():
			compoundResult = (money * (1 + interest) * (pow((1 + interest), times) - 1)) / ((1 + interest) - 1)
			simpleResult = money * times + money * interest * (1 + times) * times / 2 
		else:
			compoundResult = pow(1 + interest, times) * money
			simpleResult = interest * times * money + money

		compoundValue.set(compoundResult)
		simpleValue.set(simpleResult)
		differenceValue.set(compoundResult - simpleResult)
		
	except:
		compoundValue.set('Error')
		simpleValue.set('Error')
		differenceValue.set('Error')
		clear()
		
def clear():
	moneyInput.delete(0, END)
	interestInput.delete(0, END)
	timesInput.delete(0, END)

def main():
	# main window
	mainWindow = Tk()
	mainWindow.title('Compound Interest')

	global moneyInput
	global interestInput
	global timesInput

	global compoundValue
	global simpleValue
	global differenceValue
	compoundValue = DoubleVar()
	simpleValue = DoubleVar()
	differenceValue = DoubleVar()

	global isPeriodic
	isPeriodic = BooleanVar()

	Label(mainWindow, text = 'Money: ').grid(row = 0, column = 0)
	moneyInput = Entry(mainWindow, bg = '#d0d0d0', bd = 3, relief = SUNKEN)
	moneyInput.insert(0, 0)
	moneyInput.grid(row = 0, column = 1)

	Label(mainWindow, text = 'Interest: ').grid(row = 0, column = 2)
	interestInput = Entry(mainWindow, bg = '#d0d0d0', bd = 3, relief = SUNKEN)
	interestInput.insert(0, 0)
	interestInput.grid(row = 0, column = 3)

	Label(mainWindow, text = 'Times: ').grid(row = 0, column = 4)
	timesInput = Entry(mainWindow, bg = '#d0d0d0', bd = 3, relief = SUNKEN)
	timesInput.insert(0, 0)
	timesInput.grid(row = 0, column = 5)

	Label(mainWindow, text = 'Compound Interest: ').grid(row = 1, column = 0)
	compoundInterest = Label(mainWindow, bg = 'gold', bd = 3, relief = SUNKEN, width = 20)
	compoundInterest['textvariable'] = compoundValue
	compoundInterest.grid(row = 1, column = 1)
	Label(mainWindow, text = 'NTD').grid(row = 1, column = 2)

	Label(mainWindow, text = 'Simple Interest: ').grid(row = 2, column = 0)
	simpleInterest = Label(mainWindow, bg = 'gold', bd = 3, relief = SUNKEN, width = 20)
	simpleInterest['textvariable'] = simpleValue
	simpleInterest.grid(row = 2, column = 1)
	Label(mainWindow, text = 'NTD').grid(row = 2, column = 2)


	Label(mainWindow, text = 'Difference: ').grid(row = 2, column = 4)
	difference = Label(mainWindow, relief = SUNKEN, borderwidth = 2, width = 20)
	difference.config(bg = 'red')
	difference['textvariable'] = differenceValue
	difference.grid(row = 2, column = 5)
	Button(mainWindow, text = 'RUN', width = 10, relief = RAISED, bg = '#00BFFF', command = lambda: calculate()).grid(row = 1, column = 5)

	Checkbutton(mainWindow, text = 'Periodic', variable = isPeriodic).grid(row = 1, column = 4)

	mainWindow.mainloop()

if __name__ == '__main__':
	main()
