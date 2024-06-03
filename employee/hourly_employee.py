from .base_employee import BaseEmployee

class HourlyEmployee(BaseEmployee):
  def __init__(self, first_name, last_name, worked_hours, rate) -> None:
    super().__init__(first_name, last_name)
    self.worked_hours = worked_hours
    self.rate = rate

  def get_salary(self):
    return self.worked_hours * self.rate
