employee={"name":["kesava","srikanth","venky","hari","ram"],"age":[22,23,24,25,26],"salary":[100000,80000,60000,40000,200000]}
sal=employee["salary"]
print("total salary is",sum(sal))
print("minimum salary is",min(sal))
print("maximum salary is",max(sal))
# Find the index of the employee with the highest salary
max_age_index = employee["salary"].index(max(employee["salary"]))

# Get the details of the employee with the highest salary
employee_name = employee["name"][max_age_index]
#employee_age = emp["Age"][max_age_index]
#employee_salary = emp["Salary"][max_age_index]
print("Employee name with highest salary is:",employee_name)
# List to store names of employees with salary greater than 25000
high_salary_employees = []

# Iterate through the salaries and check if they are greater than 25000
for i in range(len(employee["salary"])):
    if employee["salary"][i] > 25000:
        high_salary_employees.append(employee["name"][i])

print("Employees with salary greater than ₹25,000:", high_salary_employees)
#kesava
#Kesavalover