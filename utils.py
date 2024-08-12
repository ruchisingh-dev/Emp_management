import csv
import os

def read_emp_data(file_path):
    try:
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []
    

def add_employee(file_path, data, append=True, headers=None):
    
    existing_emp = read_emp_data(file_path)
    unique_ids = {employee['id'] for employee in existing_emp}


    # filter duplicate values
    new_employee = []
    for employee in data:
        # if employee['id'] in unique_ids:
        #     print(f"Skipping duplicate employee with ID {employee['id']} name: {employee['name']}")
        #     continue
        unique_ids.add(employee['id'])
        new_employee.append(employee)

    if not new_employee:
            print("No new employee to add")

    mode = 'a' if append and os.path.isfile(file_path) else 'w'

    with open(file_path, mode, newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers if headers else data[0].keys())
        
        # Write headers if the file is being created or overwritten
        if mode == 'w':
            writer.writeheader()
        
        # Write the new employees
        writer.writerows(new_employee)

    print(f"Added {len(new_employee)} new employees.")
     
