"""
__init__.py file of service module with
imported employee_service and department_service submodules
"""

# pylint: disable=cyclic-import
# pylint: disable=import-self
from . import employee_service
from . import department_service
