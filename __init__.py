# Imports
import logging




# Relative imports
from . import example_python3_package




# ### Notes
# Importing a package essentially imports the package's __init__.py file as a module.




# Collect up the things that we want in the immediate namespace of this module when it is imported.
# This file allows a parent package to run this:
# import example_python3_package
# example_python3_package.hello()
hello = example_python3_package.code.hello.hello
validate = example_python3_package.util.validate
configure_module_logger = example_python3_package.util.module_logger.configure_module_logger
#submodules = example_python3_package.submodules




# Set up logger for this module. By default, it produces no output.
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.ERROR)
log = logger.info
deb = logger.debug




def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
  # Configure logger for this module.
  example_python3_package.util.module_logger.configure_module_logger(
    logger = logger,
    logger_name = __name__,
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
  deb('Setup complete.')
  # Configure modules further down in this package.
  example_python3_package.setup(
    log_level = log_level,
    debug = debug,
    log_timestamp = log_timestamp,
    log_file = log_file,
  )
