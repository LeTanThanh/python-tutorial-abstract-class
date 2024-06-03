from abc import ABC
from abc import abstractmethod

from employee.base_employee import BaseEmployee
from employee.fulltime_employee import FulltimeEmployee
from employee.hourly_employee import HourlyEmployee

from payroll import Payroll

# Python Abstract Classes

class AbstractClassName(ABC):
  @abstractmethod
  def abstract_method_name(self):
    pass

if __name__ == "__main__":
  ## Introduction to Python Abstract Classes

  payroll = Payroll()

  payroll.add(FulltimeEmployee("John", "Doe", 6000))
  payroll.add(FulltimeEmployee("Jane", "Doe", 6500))
  payroll.add(HourlyEmployee("Jenifer", "Smith", 200, 50))
  payroll.add(HourlyEmployee("David", "Wilson", 150, 100))
  payroll.add(HourlyEmployee("Kevin", "Miller", 100, 150))

  payroll.print()
