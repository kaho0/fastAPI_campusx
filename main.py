from fastapi import FastAPI,HTTPException
from models import Employee
employees_db: list[Employee] = []
app = FastAPI()

@app.get('/employees',response_model=list[Employee])
def get_employees():
    return employees_db
@app.get('/employees/{employee_id}', response_model=Employee)
def get_employee(employee_id: int):
    for index, employee in enumerate(employees_db) :
        if employee.id == employee_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")

@app.post('/employees')
def create(new_employee:Employee):
    for employee in employees_db:
        if employee.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees_db.append(new_employee)
    return new_employee

@app.put('/update_employees/{employee_id}')
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")
@app.delete('/employees/{employee_id}')
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            del employees_db[index]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")

@app.get("/")
def home():
    return {"message": "Hello, World!"}