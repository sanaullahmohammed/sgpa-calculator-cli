from prettytable import PrettyTable
from  os import system

class Semester5:

    credPoints = {'18CS51':3, '18CS52':4, '18CS53':4, '18CS54':3, '18CS55':3, '18CS56':3, '18CSL57': 2, '18CSL58':2, '18CIV59':1}
    credSum = 25

    def __init__(self):
        self.subjects = { '18CS51':0, '18CS52':0, '18CS53':0, '18CS54':0, '18CS55':0, '18CS56':0, '18CSL57': 0, '18CSL58':0, '18CIV59':0 }
        self.credXgrade = { '18CS51':0, '18CS52':0, '18CS53':0, '18CS54':0, '18CS55':0, '18CS56':0, '18CSL57': 0, '18CSL58':0, '18CIV59':0 }
        self.gradePoints = { '18CS51':0, '18CS52':0, '18CS53':0, '18CS54':0, '18CS55':0, '18CS56':0, '18CSL57': 0, '18CSL58':0, '18CIV59':0 }
        self.sgpa = 0
        self.percentage = 0
        self.Total = 0
        self.gradeTotal = 0
        self.credXgradeSum = 0


    
def initialize(self):
    print("Enter the required details below: ")
        
    for key in self.subjects:
        self.subjects[key] = int(input("Enter the marks of "+key+": "))    

def calculate(self):
    for key in self.subjects:
        if self.subjects[key] >= 90:
            self.gradePoints[key] = 10
        elif self.subjects[key] >= 80 and self.subjects[key] < 90:
            self.gradePoints[key] = 9
        elif self.subjects[key] >= 70 and self.subjects[key] < 80:
            self.gradePoints[key] = 8
        elif self.subjects[key] >= 60 and self.subjects[key] < 70:
            self.gradePoints[key] = 7
        elif self.subjects[key] >= 50 and self.subjects[key] < 60:
            self.gradePoints[key] = 6
        elif self.subjects[key] >= 45 and self.subjects[key] < 50:
            self.gradePoints[key] = 5
        elif self.subjects[key] >= 40 and self.subjects[key] < 45:
            self.gradePoints[key] = 4
        else:
            self.gradePoints[key] = 0
        
    for key in self.credXgrade:
        self.credXgrade[key] = self.gradePoints[key] * self.credPoints[key]

    for key in self.subjects:
        self.Total += self.subjects[key]
        self.gradeTotal += self.gradePoints[key]
        self.credXgradeSum += self.credXgrade[key]
        
    self.sgpa = self.credXgradeSum / self.credSum
    self.percentage = (self.Total/900)*100
        
def display(self):
    myTable = PrettyTable(["Subject", "Total Marks", "Grade Points", "Credits * Grade"])
    
    for key in self.subjects:
        myTable.add_row(["18"+str(key), (self.subjects[key]), (self.gradePoints[key]), (self.credXgrade[key])])
    print("\n\n")
    print(myTable)
    print("\n\nThe SGPA is: %f" %self.sgpa)
    print("The percentage is: %f" %self.percentage)


print("\n─────────────────────────────────────────────────────────────")
print("─██████████████─██████████████─██████████████─██████████████─")
print("─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─")
print("─██░░██████████─██░░██████████─██░░██████░░██─██░░██████░░██─")
print("─██░░██─────────██░░██─────────██░░██──██░░██─██░░██──██░░██─")
print("─██░░██████████─██░░██─────────██░░██████░░██─██░░██████░░██─")
print("─██░░░░░░░░░░██─██░░██──██████─██░░░░░░░░░░██─██░░░░░░░░░░██─")
print("─██████████░░██─██░░██──██░░██─██░░██████████─██░░██████░░██─")
print("─────────██░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─")
print("─██████████░░██─██░░██████░░██─██░░██─────────██░░██──██░░██─")
print("─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░██──██░░██─")
print("─██████████████─██████████████─██████─────────██████──██████─")
print("─────────────────────────────────────────────────────────────")
print("─────────────────────────────────────────────────────────────")
print("░█▀▀█ ─█▀▀█ ░█─── ░█▀▀█ ░█─░█ ░█─── ─█▀▀█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ ")
print("░█─── ░█▄▄█ ░█─── ░█─── ░█─░█ ░█─── ░█▄▄█ ─░█── ░█──░█ ░█▄▄▀ ")
print("░█▄▄█ ░█─░█ ░█▄▄█ ░█▄▄█ ─▀▄▄▀ ░█▄▄█ ░█─░█ ─░█── ░█▄▄▄█ ░█─░█ ")
print("─────────────────────────────────────────────────────────────")

print("This Version is limited to 5th semester CSE 2018 scheme")
print("Created by Sanaullah\n\n\n")

obj1 = Semester5()
initialize(obj1)
calculate(obj1)
display(obj1)

print("\n\n")
system("pause")