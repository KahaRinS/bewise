# rest-boilerplate

skeleton for python projects

## Requirements
`python 3.10`

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

```
$ python3 -m venv venv
$ . venv/bin/activate
```

Install all dependencies:

```
pip install -r requirements.txt
```

### Run linters
```bash
flake8
```

Also you can install git hook for running linters before each commit
```bash
pre-commit install
```

Use `isort` for automatically sorting imports separated into sections and by type.

```bash
# From the command line:
isort mypythonfile.py mypythonfile2.py

# or recursively:
isort . 

# or to see the proposed changes without applying them:
isort mypythonfile.py --diff
```


### Start App

```shell script
python main.py start
```

### Run Tests
```shell script
python -m pytest
```
