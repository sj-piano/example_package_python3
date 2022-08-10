# example_python3_package

This is a reusable template for a Python 3 package.



# Aspects:

- Designed to be a component of a tree of other python packages, arranged using `git submodule`.  
- pytest  
- `cli.py`: A script that provides a command-line interface to the package's functionality.  
- Explicit import approach  
- Granular logging



# More detail

- All indentation is two spaces. No exceptions. Configure your editor to use tab to insert two spaces and backspace to delete two spaces.

- Command-line options are kebab-case and start with two dashes e.g. `--log-level`. They may have a short version e.g. `-l`.

- Logging: Every code file has its own namespaced logger, which records the function name and line number of the log call. Logging settings are set at the top (via cli.py or by the calling of `setup()` by a parent package) and propagate down. Manual adjustments (e.g. setting the log level of a noisy submodule to `error`) can be made via an extra explicit call to the submodule's `setup()` method.

- Using keyword function arguments, each of which is on its own line, makes Python code easier to maintain. It's easier to read and diffs are easier to check. New arguments can be added without having to think about line wrapping.

Example:

```
def setup(
    log_level = 'error',
    debug = False,
    log_timestamp = False,
    log_file = None,
    ):
```

vs

```
def setup(log_level = 'error', debug = False, log_timestamp = False, log_file = None):
```

Test data is always stored in the `data` subdirectory. This means that multiple tests can use the same data easily.






# Sample commands


```bash

python3 cli.py

python3 cli.py --help

python3 cli.py --task hello

python3 cli.py --task hello --log-level=info

python3 cli.py --task hello --log-level=debug

python3 cli.py --task hello2

python3 cli.py --task hello3

python3 cli.py --task get_python_version



```


Tests:

```bash

# Run all tests, including submodule tests.
pytest3

# Run all tests in a specific test file
pytest3 example_python3_package/test/test_hello.py

# Run tests with relatively little output
pytest3 --quiet example_python3_package/test/test_hello.py

# Run a single test
pytest3 example_python3_package/test/test_hello.py::test_hello

# Print log output in real-time during a single test
pytest3 --capture=no --log-cli-level=INFO example_python3_package/test/test_hello.py::test_hello

# Note: The --capture=no option will also cause This will also cause print statements within the test code to produce output.

```



Code style:


```bash

pycodestyle example_python3_package/code/hello.py

pycodestyle --filename=*.py

pycodestyle --filename=*.py --statistics

pycodestyle --filename=*.py --exclude example_python3_package/submodules

```

Settings for pycodestyle are stored in the file `tox.ini`.




# Development

Developed with:
- Ubuntu 16.04 on WSL on Windows 10
- Python 3.5.2
- pytest 6.1.2






