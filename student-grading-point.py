# A Calculator Application Code
# BY :
        # 吴 敏
        # 伊衣
        # 远航
        # 乐成


# Importing Python module responsible for building the Calculator interfaces
from tkinter import *

# Importing messagebox from python module tkinter for showing messages to users in a box
import tkinter.messagebox

# class for starting the application
# contains the layout of the entry boxes
class App:
    def __init__(self, parent):

        self.parent = parent
        self.frame_1 = Frame(parent)
        self.frame_1.pack()

        self.lbl_1 = Label(self.frame_1, text="Current CGPA :")
        self.lbl_1.grid(row=0, column=0)
        self.entry_1 = Entry(self.frame_1)
        self.entry_1.grid(row=0, column=1)

        self.lbl_2 = Label(self.frame_1, text="Units Completed :")
        self.lbl_2.grid(row=1, column=0)
        self.entry_2 = Entry(self.frame_1)
        self.entry_2.grid(row=1, column=1)

        self.lbl_0 = Label(self.frame_1, text="Enter Matric Number:")
        self.lbl_0.grid(row=2, column=0)
        self.entry_0 = Entry(self.frame_1)
        self.entry_0.grid(row=2, column=1)

        self.lbl_3 = Label(self.frame_1, text="Number of Courses to add :")
        self.lbl_3.grid(row=3, column=0)
        self.entry_3 = Entry(self.frame_1)
        self.entry_3.grid(row=3, column=1)

        self.btn_1 = Button(parent, text="Add Courses !", command=self.add_courses)
        self.btn_1.pack(pady=8)

        self.frame_2 = Frame(parent)
        self.frame_2.pack()

# Function handling number of courses to be added depending on the users input
    def add_courses(self):
        if ((self.entry_3.get() != '') & (self.entry_3.get().isdigit())):
            self.num_courses = int(self.entry_3.get())
            self.grades_list = []
            self.units_list = []
            self.course_name_list = []
            self.lbl_course_name = Label(self.frame_2, text="Course Name/Code :")
            self.lbl_course_name.grid(row=0, column=0)
            self.lbl_units = Label(self.frame_2, text="Units :")
            self.lbl_units.grid(row=0, column=1)
            self.lbl_grades = Label(self.frame_2, text="Grades :")
            self.lbl_grades.grid(row=0, column=3)

            for i in range(0, self.num_courses):
                self.course_name_list.append(Spinbox(self.frame_2, value=""))
                self.course_name_list[i].grid(row=i + 1, column=0, padx=10, pady=10)

                self.units_list.append(Spinbox(self.frame_2, values=(1, 2, 3, 4, 5, 20)))
                self.units_list[i].grid(row=i + 1, column=1, padx=10, pady=10)

                self.grades_list.append(Spinbox(self.frame_2, values=("A", "A-", "B", "B-", "C", "C-", "D", "E")))
                self.grades_list[i].grid(row=i + 1, column=3, padx=10, pady=10)
            self.btn_calcCG = Button(self.parent, text="Calculate CGPA", command=self.calc_CG)
            self.btn_calcCG.pack(pady=8)
            self.btn_1.config(state=DISABLED)
        else:
            tkinter.messagebox.showinfo("Hey ! ", "Enter a Valid Value")

# function that calculates the cgpa using the provided information
    def calc_CG(self):
        print("Calculating !!!")
        credits_this_sem = 0
        units_this_sem = 0
        for j in range(0, self.num_courses):
            credits_this_sem = credits_this_sem + int(self.units_list[j].get()) * (
                self.grade(self.grades_list[j].get()))
            units_this_sem = units_this_sem + int(self.units_list[j].get())
            final_courses = str(self.course_name_list[j].get())
        final_courses = final_courses
        final_cgpa = (credits_this_sem + float(self.entry_1.get()) * int(self.entry_2.get())) / (
                units_this_sem + int(self.entry_2.get()))
        final_cgpa = str(final_cgpa)
        student_matric_number = str(self.entry_0.get())
        save_record = open("Student_grade_database.txt", "a")
        print("Matric Number: " + student_matric_number +
              "CGPA : " + final_cgpa
              )
        a = ("\n\n Matric Number: " + student_matric_number +
             "\n\n CGPA : " + final_cgpa
             )
        save_record.write(a)
        tkinter.messagebox.showinfo("Done!!!", "Record saved successfully!!!"
                                    + "\n The CGPA for: " + str(student_matric_number) + " is " + str(final_cgpa)
                                    + "\n"
                                    + "\n"
                                    )
        tkinter.messagebox.showinfo("Alert", "Restart the Application to make a new Entry")
        print("Starting New Session!!! \n "
              "Done....")

# grade letter equivalence to grade points
    # users will be allowed to set values to their grade letters in the future updates
    def grade(self, grd):
        dict_ = {'A': 10, 'A-': 9, 'B': 8, 'B-': 7, 'C': 6, 'C-': 5, 'D': 4, 'E': 2}
        return dict_[grd]

# program start
# GUI build point

root = Tk()
app = App(root)
root.title("Student Grading System")
root.mainloop()
