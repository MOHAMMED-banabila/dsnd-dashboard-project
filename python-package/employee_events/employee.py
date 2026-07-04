# Import the QueryBase class
from .query_base import QueryBase

# Import dependencies needed for sql execution
# from the `sql_execution` module


# Define a subclass of QueryBase
# called Employee
class Employee(QueryBase):

    # Set the class attribute `name` to "employee"
    name = "employee"

    # Query 3: full name + id for all employees
    def names(self):
        return self.query("""
            SELECT first_name || ' ' || last_name AS full_name,
                   employee_id
            FROM employee
        """)

    # Query 4: full name for one employee by id
    def username(self, id):
        return self.query(f"""
            SELECT first_name || ' ' || last_name AS full_name
            FROM employee
            WHERE employee_id = {id}
        """)

    # model_data: returns a DataFrame for the ML model
    def model_data(self, id):
        return self.pandas_query(f"""
            SELECT SUM(positive_events) positive_events
                 , SUM(negative_events) negative_events
            FROM {self.name}
            JOIN employee_events
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
        """)