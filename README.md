# Employee Management API

A simple REST API built with FastAPI for managing employee records. This project provides basic CRUD operations for employee data including create, read, update, and delete operations.

## Features

- **GET** `/employees` - Retrieve all employees
- **GET** `/employees/{employee_id}` - Retrieve a specific employee by ID
- **POST** `/employees` - Create a new employee
- **PUT** `/update_employees/{employee_id}` - Update an existing employee
- **DELETE** `/employees/{employee_id}` - Delete an employee
- **GET** `/` - Home endpoint with welcome message

## Employee Model

Each employee has the following attributes:

- `id` (int): Unique identifier for the employee
- `name` (str): Employee's full name
- `department` (str): Department the employee works in
- `age` (int): Employee's age

## Prerequisites

- Python 3.7+
- FastAPI
- Pydantic

## Installation

1. Clone the repository:

```bash
git clone <your-repository-url>
cd fastapi
```

2. Install the required dependencies:

```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

1. Start the FastAPI server:

```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

## API Usage Examples

### Create an Employee

```bash
curl -X POST "http://localhost:8000/employees" \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "John Doe", "department": "Engineering", "age": 30}'
```

### Get All Employees

```bash
curl "http://localhost:8000/employees"
```

### Get Employee by ID

```bash
curl "http://localhost:8000/employees/1"
```

### Update Employee

```bash
curl -X PUT "http://localhost:8000/update_employees/1" \
     -H "Content-Type: application/json" \
     -d '{"id": 1, "name": "John Smith", "department": "Engineering", "age": 31}'
```

### Delete Employee

```bash
curl -X DELETE "http://localhost:8000/employees/1"
```

## Project Structure

```
fastapi/
├── main.py          # Main FastAPI application with all endpoints
├── models.py        # Pydantic models for data validation
└── README.md        # This file
```

## Data Storage

Currently, the application uses in-memory storage (a Python list) for employee data. This means:

- Data is lost when the server restarts
- The application is suitable for development and testing
- For production use, consider implementing a proper database

## Error Handling

The API includes proper error handling:

- **404 Not Found**: When trying to access, update, or delete a non-existent employee
- **400 Bad Request**: When trying to create an employee with an ID that already exists

## Development

This is a basic implementation that can be extended with:

- Database integration (SQLite, PostgreSQL, etc.)
- Authentication and authorization
- Input validation and sanitization
- Logging and monitoring
- Unit tests
- Docker containerization

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
