# -*- coding: utf-8 -*-
# author: LJIN
# start date: 2020-03-11
# python-version: conda 3.7.1
#


class Course:
    def __init__(self,title):
        self.title = title
    
    def create_rubric(self,rubric=None):
        if rubric:
            self.rubric = rubric
            self.create_grades()
            self.get_total_points_possible()
            return self.rubric
        self.rubric = {}
        create_rubric_message_start = str(input("Please enter the name of the category (ex: midterm).\nTo exit, please press enter.\n"))
        while create_rubric_message_start != "":
            create_rubric_message_percentage = float(input("What percentage of the final grade is this category?: \n"))
            self.rubric[create_rubric_message_start] = create_rubric_message_percentage
            create_rubric_message_start = str(input("Please enter the name of the category (ex: midterm).\nTo exit, please press enter.\n"))
        self.create_grades()
        self.get_total_points_possible()
        print(self.rubric)
        
    def get_rubric(self):
        return self.rubric
    
    def get_total_points_possible(self):
        self.total_points_possible = 0
        for points in list(self.rubric.values()):
            self.total_points_possible += points
        return self.total_points_possible

    def create_grades(self):
        self.categories = list(self.rubric.keys())
        self.grades = {}
        for category in self.categories:
            self.grades[category] = ""
        
    def get_grades(self):
        return self.grades
    
    def input_grades(self):
        print("Which grade would you like to update?\n")
        for i in range(len(self.categories)):
            print(f'{i+1}: {self.categories[i]}')
        user_update_input = int(input("Type the NUMBER ofthe category that you want to update.\n"))
        user_update_grade_value = float(input(f"What is the new grade for {self.categories[user_update_input-1]}?\n"))
        self.grades[self.categories[user_update_input-1]] = user_update_grade_value
        print(self.grades)
        
    def calculate_best(self):
        """
        Calculates the final grade assuming that you get 100% on all 
        of the remaining categories.
        
        returns: final_best (float value)
        """
        final_best_value = 0
        for category, grade in self.grades.items():
            if self.grades[category] == "":
                self.grades[category] = self.rubric[category]
            final_best_value += self.grades[category]
        
        return (final_best_value/self.total_points_possible)*100
 
    def calculate_worst(self):
        """
        Calculates the final grade assuming that you get 0% on all 
        of the remaining categories.
        
        returns: final_worst (float value)
        """
        final_worst_value = 0
        for category, grade in self.grades.items():
            if self.grades[category] == "":
                self.grades[category] = 0
            final_worst_value += self.grades[category]
        
        return (final_worst_value/self.total_points_possible)*100
   
class Semester:
    def __init__(self,courses=[]):
        
    
        
if __name__ == "__main__":
    #for stat
#    rubric_stat = {"midterm1":100.0,"midterm2":100.0,"final":200.0,"homework1":10.0,"homework2":10.0,"homework3":10.0,"homework4":10.0,"homework5":10.0,"homework6":10.0,"homework7":10.0,"homework8":10.0,"homework9":10.0,"homework10":10.0}
#    stat = Course("Stat")
#    stat.create_rubric(rubric_stat)
#    stat.get_rubric()
#    print(stat.get_grades())
#    stat.input_grades() 
    
    #astr
#    rubric_astr = {'participation':50.0,'hw1':50.0,'hw2':50.0,'hw3':50.0,'hw4':50.0,'hw5':50.0,'hw6':50.0,'hw7':50.0,'hw8':50.0,'hw9':50.0,'hw10':50.0,'midterm1':100.0,'midterm2':100.0,'observation':50.0,'final':200.0}
#    astr = Course('Astr210')
#    astr.create_rubric(rubric_astr)
#    astr.input_grades()
    
    
    