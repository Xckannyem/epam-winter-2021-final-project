"""
__init__.py file of rest module with
imported employee_api and department_api submodules
"""

# pylint: disable=cyclic-import
from . import employee_api
from . import department_api
