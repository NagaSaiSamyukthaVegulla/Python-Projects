import json
import random

# Helper function to generate unique identifiers
def generate_id(prefix):
    """Generate a unique ID using a specified prefix followed by a 6-digit number."""
    number = random.randint(100000, 999999)
    return f"{prefix}_{number}"

class Address:
    def __init__(self, mail_id, phone_number, house_no, building_number, road_number, street_name, land_mark, city, state, zip_code):
        self.mail_id = mail_id
        self.phone_number = phone_number
        self.house_no = house_no
        self.building_number = building_number
        self.road_number = road_number
        self.street_name = street_name
        self.land_mark = land_mark
        self.city = city
        self.state = state
        self.zip_code = zip_code

    def __repr__(self):
        return (f"Address(mail_id={self.mail_id}, phone_number={self.phone_number}, house_no={self.house_no}, "
                f"building_number={self.building_number}, road_number={self.road_number}, street_name={self.street_name}, "
                f"land_mark={self.land_mark}, city={self.city}, state={self.state}, zip_code={self.zip_code})")

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def create_task(self, task_name, chargeable, rate_card):
        task_id = generate_id("TSK")
        self.tasks[task_id] = {
            "task_name": task_name,
            "chargeable": chargeable,
            "rate_card": rate_card
        }
        return task_id

    def update_task(self, task_id, task_name=None, chargeable=None, rate_card=None):
        task = self.tasks.get(task_id)
        if task:
            if task_name:
                task["task_name"] = task_name
            if chargeable is not None:
                task["chargeable"] = chargeable
            if rate_card is not None:
                task["rate_card"] = rate_card
            print("Task updated successfully.")
        else:
            print("Task not found!")

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print("Task deleted.")
        else:
            print("Task not found.")

    def search_task(self, task_id):
        return json.dumps(self.tasks.get(task_id, "Task not found"), indent=4)

    def display_tasks(self):
        return json.dumps(self.tasks, indent=4)

class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def create_employee(self, name, address,bill_rate):
        emp_id = generate_id("EMP")
        self.employees[emp_id] = {
            "name": name,
            "address": address,
            "bill_rate": bill_rate
        }
        return emp_id

    def update_employee(self, emp_id, name=None, address=None):
        employee = self.employees.get(emp_id)
        if employee:
            if name:
                employee["name"] = name
            if address:
                employee["address"] = address
            print("Employee updated successfully.")
        else:
            print("Employee not found.")

    def delete_employee(self, emp_id):
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def search_employee(self, emp_id):
        employee = self.employees.get(emp_id)
        if employee:
            return json.dumps({"name": employee["name"], "address": str(employee["address"])}, indent=4)
        else:
            return "Employee not found"

    def display_employees(self):
        return json.dumps({emp_id: {"name": emp["name"], "address": str(emp["address"])} for emp_id, emp in self.employees.items()}, indent=4)

class ClientManager:
    def __init__(self):
        self.clients = {}

    def create_client(self, name, address):
        client_id = generate_id("CLT")
        self.clients[client_id] = {
            "name": name,
            "address": address
        }
        return client_id

    def update_client(self, client_id, name=None, address=None):
        client = self.clients.get(client_id)
        if client:
            if name:
                client["name"] = name
            if address:
                client["address"] = address
            print("Client updated successfully.")
        else:
            print("Client not found.")

    def delete_client(self, client_id):
        if client_id in self.clients:
            del self.clients[client_id]
            print("Client deleted.")
        else:
            print("Client not found.")

    def search_client(self, client_id):
        client = self.clients.get(client_id)
        if client:
            return json.dumps({"name": client["name"], "address": str(client["address"])}, indent=4)
        else:
            return "Client not found"

    def display_clients(self):
        return json.dumps({client_id: {"name": cl["name"], "address": str(cl["address"])} for client_id, cl in self.clients.items()}, indent=4)

class TimeSheetManager:
    def __init__(self):
        self.timesheets = {}

    def create_timesheet(self, employee_id, client_id, task_id, date, hours):
        timesheet_id = generate_id("TMS")
        self.timesheets[timesheet_id] = {
            "employee_id": employee_id,
            "client_id": client_id,
            "task_id": task_id,
            "date": date,
            "hours": hours
        }
        return timesheet_id

    def update_timesheet(self, timesheet_id, employee_id=None, client_id=None, task_id=None, date=None, hours=None):
        timesheet = self.timesheets.get(timesheet_id)
        if timesheet:
            if employee_id:
                timesheet["employee_id"] = employee_id
            if client_id:
                timesheet["client_id"] = client_id
            if task_id:
                timesheet["task_id"] = task_id
            if date:
                timesheet["date"] = date
            if hours is not None:
                timesheet["hours"] = hours
            print("Timesheet updated successfully.")
        else:
            print("Timesheet not found.")

    def delete_timesheet(self, timesheet_id):
        if timesheet_id in self.timesheets:
            del self.timesheets[timesheet_id]
            print("Timesheet deleted.")
        else:
            print("Timesheet not found.")

    def search_timesheet(self, timesheet_id):
        return json.dumps(self.timesheets.get(timesheet_id, "Timesheet not found"), indent=4)

    def display_timesheets(self):
        return json.dumps(self.timesheets, indent=4)

class BillingManager:
    def __init__(self):
        self.bills = {}

    def generate_bill(self, timesheet_id, timesheet_manager):
        timesheet = timesheet_manager.timesheets.get(timesheet_id)
        if not timesheet:
            return "Timesheet not found"
        
        employee_id = timesheet["employee_id"]
        hours = timesheet["hours"]
        employee = emp_mgr.employees.get(employee_id)
        if not employee:
            return "Employee data missing"

        bill_amount = hours * employee.get("bill_rate", 0)  # Assume bill_rate is stored directly in employee dictionary
        bill_id = generate_id("BIL")
        self.bills[bill_id] = {
            "employee_id": employee_id,
            "bill_date": timesheet["date"],
            "hours": hours,
            "bill_amount": bill_amount
        }
        return json.dumps(self.bills[bill_id], indent=4)

    def display_bills(self):
        return json.dumps(self.bills, indent=4)

# Instantiate managers
task_mgr = TaskManager()
emp_mgr = EmployeeManager()
client_mgr = ClientManager()
timesheet_mgr = TimeSheetManager()
billing_mgr = BillingManager()

# Main Menu and Submenus
def main_menu():
    while True:
        print("\nANALYTIC AMERICAN ASSOCIATION")
        print("1. Task Management")
        print("2. Employee Management")
        print("3. Client Management")
        print("4. Timesheet Management")
        print("5. Billing Management")
        print("6. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            task_menu()
        elif choice == "2":
            employee_menu()
        elif choice == "3":
            client_menu()
        elif choice == "4":
            timesheet_menu()
        elif choice == "5":
            billing_menu()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def task_menu():
    while True:
        print("\nTask Management")
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Search Task")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Task Name: ")
            chargeable = input("Chargeable (yes/no): ") == "yes"
            rate = float(input("Rate Card: ")) if chargeable else 0
            task_id = task_mgr.create_task(name, chargeable, rate)
            print("Task Created! Task ID:", task_id)
        elif choice == "2":
            print(task_mgr.display_tasks())
        elif choice == "3":
            task_id = input("Enter Task ID: ")
            name = input("New Task Name (optional): ")
            chargeable_input = input("Chargeable? (yes/no, optional): ")
            chargeable = chargeable_input.lower() == "yes" if chargeable_input else None
            rate = float(input("New Rate Card (optional): ")) if chargeable else None
            task_mgr.update_task(task_id, name, chargeable, rate)
        elif choice == "4":
            task_id = input("Enter Task ID: ")
            task_mgr.delete_task(task_id)
        elif choice == "5":
            task_id = input("Enter Task ID: ")
            print(task_mgr.search_task(task_id))
        elif choice == "6":
            break

def employee_menu():
    while True:
        print("\nEmployee Management")
        print("1. Create Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            mail_id = input("Email: ")
            phone_number = input("Phone: ")
            bill_rate = float(input("Billing Rate: "))
            house_no = input("House No: ")
            building_number = input("Building Number: ")
            road_number = input("Road Number: ")
            street_name = input("Street Name: ")
            land_mark = input("Landmark: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")

            # Creating Address object
            address = Address(mail_id=mail_id, phone_number=phone_number, house_no=house_no, building_number=building_number,
                              road_number=road_number, street_name=street_name, land_mark=land_mark, city=city, state=state, zip_code=zip_code)

            emp_id = emp_mgr.create_employee(name, address, bill_rate)
            print("Employee Created! Employee ID:", emp_id)
        elif choice == "2":
            print(emp_mgr.display_employees())
        elif choice == "3":
            emp_id = input("Enter Employee ID: ")
            name = input("Name (optional): ")
            mail_id = input("Email (optional): ")
            phone_number = input("Phone (optional): ")
            bill_rate = input("Billing Rate (optional): ")
            bill_rate = float(bill_rate) if bill_rate else None
            address = None  # You would need to handle address updates similarly to creation
            emp_mgr.update_employee(emp_id, name, address)
        elif choice == "4":
            emp_id = input("Enter Employee ID: ")
            emp_mgr.delete_employee(emp_id)
        elif choice == "5":
            emp_id = input("Enter Employee ID: ")
            print(emp_mgr.search_employee(emp_id))
        elif choice == "6":
            break

def client_menu():
    while True:
        print("\nClient Management")
        print("1. Create Client")
        print("2. View Clients")
        print("3. Update Client")
        print("4. Delete Client")
        print("5. Search Client")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            mail_id = input("Email: ")
            phone_number = input("Phone: ")
            house_no = input("House No: ")
            building_number = input("Building Number: ")
            road_number = input("Road Number: ")
            street_name = input("Street Name: ")
            land_mark = input("Landmark: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")

            # Creating Address object for the client
            address = Address(mail_id=mail_id, phone_number=phone_number, house_no=house_no, building_number=building_number,
                              road_number=road_number, street_name=street_name, land_mark=land_mark, city=city, state=state, zip_code=zip_code)

            client_id = client_mgr.create_client(name, address)
            print("Client Created! Client ID:", client_id)
        elif choice == "2":
            print(client_mgr.display_clients())
        elif choice == "3":
            client_id = input("Enter Client ID: ")
            name = input("Name (optional): ")
            # Collect new address details similarly to creation if needed
            address = None  # For updating, you'd create a new Address object
            client_mgr.update_client(client_id, name, address)
        elif choice == "4":
            client_id = input("Enter Client ID: ")
            client_mgr.delete_client(client_id)
        elif choice == "5":
            client_id = input("Enter Client ID: ")
            print(client_mgr.search_client(client_id))
        elif choice == "6":
            break
def timesheet_menu():
    while True:
        print("\nTimesheet Management")
        print("1. Create Timesheet")
        print("2. View Timesheets")
        print("3. Update Timesheet")
        print("4. Delete Timesheet")
        print("5. Search Timesheet")
        print("6. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            employee_id = input("Employee ID: ")
            client_id = input("Client ID: ")
            task_id = input("Task ID: ")
            date = input("Date (YYYY-MM-DD): ")
            hours = float(input("Hours worked: "))
            timesheet_id = timesheet_mgr.create_timesheet(employee_id, client_id, task_id, date, hours)
            print("Timesheet Created! Timesheet ID:", timesheet_id)
        elif choice == "2":
            print(timesheet_mgr.display_timesheets())
        elif choice == "3":
            timesheet_id = input("Enter Timesheet ID: ")
            employee_id = input("Employee ID (optional): ")
            client_id = input("Client ID (optional): ")
            task_id = input("Task ID (optional): ")
            date = input("Date (YYYY-MM-DD, optional): ")
            hours = input("Hours worked (optional): ")
            hours = float(hours) if hours else None
            timesheet_mgr.update_timesheet(timesheet_id, employee_id, client_id, task_id, date, hours)
        elif choice == "4":
            timesheet_id = input("Enter Timesheet ID: ")
            timesheet_mgr.delete_timesheet(timesheet_id)
        elif choice == "5":
            timesheet_id = input("Enter Timesheet ID: ")
            print(timesheet_mgr.search_timesheet(timesheet_id))
        elif choice == "6":
            break

def billing_menu():
    while True:
        print("\nBilling Management")
        print("1. Generate Bill")
        print("2. View Bills")
        print("3. Back")
        choice = input("Enter choice: ")

        if choice == "1":
            timesheet_id = input("Timesheet ID: ")
            print(billing_mgr.generate_bill(timesheet_id, timesheet_mgr))
        elif choice == "2":
            print(billing_mgr.display_bills())
        elif choice == "3":
            break

# Creating Manager Instances
task_mgr = TaskManager()
emp_mgr = EmployeeManager()
client_mgr = ClientManager()
timesheet_mgr = TimeSheetManager()
billing_mgr = BillingManager()

# Run the main menu
if __name__ == "__main__":
    main_menu()

