# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.

class Employee:  
    def __init__(self, name, id_number, department, job_title):  
        self.name = name  
        self.id_number = id_number  
        self.department = department  
        self.job_title = job_title  

def main():  
    # Create Employee
    employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")  
    employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")  
    employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")  

    # Display data  
    print(f"Name: {employee1.name}, ID Number: {employee1.id_number}, Department: {employee1.department}, Job Title: {employee1.job_title}")  
    print(f"Name: {employee2.name}, ID Number: {employee2.id_number}, Department: {employee2.department}, Job Title: {employee2.job_title}")  
    print(f"Name: {employee3.name}, ID Number: {employee3.id_number}, Department: {employee3.department}, Job Title: {employee3.job_title}")  

# Run main program  
if __name__ == "__main__":  
    main()
  
#Jadon Anderstrom, 11/5/2024
