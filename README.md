# Department App

Department App is a simple web application for managing departments and employees. 
It uses RESTful web service to perform CRUD operations.
The user is allowed to:

1. Register and log in
   

2. Check the lists of departments with department name, description, employee count, average salary and average age columns. 
   
    Employee count, average salary and average age are calculated automatically based on employees data
   

3. Check the lists of employees with employee name which consists of the first and last name, department in which the employee is, salary and birthday columns


4. Perform operations with departments such as adding, editing, deleting
   

5. Perform operations with employees such as adding, assigning, editing, deleting
***
### Start using the application

Python3 and PostgreSQL must already be installed
***
### Installing and using PostgreSQL

In case if you have some difficulties to set up the PostgreSQL database there is presented such a small tutorial (for Ubuntu 18.04 or 20.04):

1. Download PostgreSQL:

   * `sudo apt update`
     
   * `sudo apt install postgresql postgresql-contrib`
   
2. Connect to base account (postgres is a default account): 
   
    * `sudo su - postgres`
   
3. Create department_db database:
   
    * `createdb department_db`
    
4. Connect to the database:
   
    * `psql -d department_db`

##### P.S. 
If something went wrong, or you do not want to use default postgres account you can read this tutorial:
<https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-20-04-quickstart>
***
### Deployment

1. Clone the repo: 
   
   * `git clone https://github.com/yegorks/epam-winter-2021-final-project`
    
2. Create the virtual environment in project:

   * `cd epam-winter-2021-final-project`

   * `python3 -m venv venv`
   
   * `source venv/bin/activate`
   
3. Install project requirements:

   * `pip install -r requirements.txt`

4. Run the migration scripts to create database schema:
       
   * `flask db init` - further use is optional, in case of intentional reinstallation
   
   * `flask db migrate`
     
   * `flask db update`
***
##### After these steps you should see the home page of the application

![alt text](documentation/mockups/home_for_unauthenticated_user.png)
***
### API operations

* ###### /api/departments

    * GET - get all departments in json format
    * POST - create a new department:
    
    `{'name': 'new department', 'description': 'department description' }`

* ###### /api/departments/id

    * GET - get the department with a given id in json format
    * PUT - ***completely*** update the department with a given id (every field required)
      
      `{'name': 'updated new department', 'description': 'new department description' }`
      
    * PATCH - ***partially*** update the department with a given id
      
      `{'name': 'Commercial Department ' }` or
      
      `{'description': 'Deals with the production tasks' }`
      
    * DELETE - delete the department with a given id

* ###### /api/employees

    * GET - get all employees in json format
    * POST - create a new employee:
      
      `{'username': 'new_employee',
      'email': 'new_testusr@gmail.com',
      'first_name': 'new',
      'last_name': 'employee',
      'password': 'new1111',
      'department_id': 1,
      'salary': '1000',
      'birthday': '11/11/1991'}`

* ###### /api/employees/id

    * GET - get the employee with a given id in json format
    * PUT - ***completely*** update the employee with a given id (every field required)
      
      `{'username': 'updated_employee',
      'email': 'updated_testusr@gmail.com',
      'first_name': 'updated',
      'last_name': 'employee',
      'password': 'updated1111',
      'department_id': 1,
      'salary': '1000',
      'birthday': '10/10/1990'}`
      
    * PATCH - ***partially*** update the employee with a given id
      
      `{'salary': '2000'}`
      
    * DELETE - delete the employee with a given id

* ###### /api/employees?date='date'

    * GET - get all employees who were born on the specified date in json format

* ###### /api/employees?start_date='start_date'&end_date='end_date'

    * GET - get all employees who were born between two dates in json format
    