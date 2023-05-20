import csv

def read_operations_from_csv(filename):
    operations = []
    with open(filename, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            operation = (int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]))
            operations.append(operation)
    return operations

def read_departments_from_csv(filename):
    departments = {}
    with open(filename, 'r', encoding='utf8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            department_id = int(row[0])
            department_name = row[3]
            department_start_year = int(row[1])
            department_end_year = int(row[2])
            departments[department_id] = (department_name, department_start_year, department_end_year)
    return departments

def is_valid_operation(year, month, day, department_id, departments):
    if month > 12 or day > 31:
        return False
    if department_id not in departments:
        return False
    department_start_year, department_end_year = departments[department_id][1], departments[department_id][2]
    if department_start_year >= department_end_year:
        return False
    if year < department_start_year or year > department_end_year:
        return False
    return True

def print_income(income_by_month):
    print("Год, Месяц, Название подразделения, Суммарная прибыль")
    for key, income in income_by_month.items():
        year, month, department = key
        print(f"{year}, {month}, {department}, {income}")

def calculate_income():
    operations = read_operations_from_csv('operations.csv')
    departments = read_departments_from_csv('departments.csv')

    income_by_month = {}
    for operation in operations:
        year, month, day, department_id, income = operation
        if is_valid_operation(year, month, day, department_id, departments):
            key = (year, month, departments[department_id][0])
            if key not in income_by_month:
                income_by_month[key] = 0
            income_by_month[key] += income

    print_income(income_by_month)

calculate_income()