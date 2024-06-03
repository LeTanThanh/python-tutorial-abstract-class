from .base_employee import BaseEmployee

class FulltimeEmployee(BaseEmployee):
  def __init__(self, first_name, last_name, salary) -> None:
    super().__init__(first_name, last_name)
    self.salary = salary

  def get_salary(self):
    return self.salary
