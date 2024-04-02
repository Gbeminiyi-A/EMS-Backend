---

## Django API Documentation

This Django application provides RESTful API endpoints for managing employees, projects, and benefits. It includes authentication and authorization mechanisms to ensure secure access to the resources.

### Endpoints:

#### 1. User Authentication:

- **Endpoint:** `/login/`
  - **Method:** POST
  - **Description:** Allows users to log in to the system.
  - **Parameters:**
    - `name`: Username
    - `email`: User email
    - `password`: User password
  - **Response:**
    - Success: `{ "Success": "Login Successful" }`
    - Error: `{ "Error": "Try checking your login details or creating an account first" }`

#### 2. Employee Management:

- **Endpoint:** `/employees/`
  - **Method:** GET, POST
  - **Description:** Retrieve a list of employees or create a new employee.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "employees": [...] }`
    - POST Success: `{ "employees": [...] }`
    - Error: `{ "error": "Employee does not exist" }`

- **Endpoint:** `/employees/<employee_id>/`
  - **Method:** GET, PUT, DELETE
  - **Description:** Retrieve, update, or delete a specific employee.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "employee": [...] }`
    - PUT Success: `{ "Employee": [...] }`
    - DELETE Success: `{ "Success": "The employee detail has been deleted" }`
    - Error: `{ "error": "Employee does not exist" }`

#### 3. Project Management:

- **Endpoint:** `/projects/`
  - **Method:** GET, POST
  - **Description:** Retrieve a list of projects or create a new project.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "projects": [...] }`
    - POST Success: `{ "project": [...] }`
    - Error: `{ "Error": "You do not have access to add a project" }`

- **Endpoint:** `/projects/<project_id>/`
  - **Method:** GET, PUT, DELETE
  - **Description:** Retrieve, update, or delete a specific project.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "project": [...] }`
    - PUT Success: `{ "project": [...] }`
    - DELETE Success: `{ "Success": "Project Not found" }`
    - Error: `{ "Error": "Project Not Found" }`

#### 4. Benefits Management:

- **Endpoint:** `/benefits/`
  - **Method:** GET, POST
  - **Description:** Retrieve a list of benefits or create a new benefit.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "benefits": [...] }`
    - POST Success: `{ "benefits": [...] }`
    - Error: `{ "Error": "Check your details and try changing your username" }`

- **Endpoint:** `/benefits/<benefit_id>/`
  - **Method:** GET, PUT, DELETE
  - **Description:** Retrieve, update, or delete a specific benefit.
  - **Authentication Required:** Yes
  - **Response:**
    - GET Success: `{ "Benefit": [...] }`
    - PUT Success: `{ "Benefit": [...] }`
    - DELETE Success: `{ "Success": "Benefit has been deleted" }`
    - Error: `{ "Error": "No User or Benefits with that ID" }`

#### 5. User Registration:

- **Endpoint:** `/createUser/`
  - **Method:** POST
  - **Description:** Create a new user account.
  - **Parameters:**
    - `name`: Username
    - `email`: User email
    - `password`: User password
  - **Response:**
    - Success: `{ "Success": "User created successfully!" }`
    - Error: `{ "Error": "Email already exists" }`

---
