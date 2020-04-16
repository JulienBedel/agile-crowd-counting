# Guide to our development framework

## Project collaboration

We will be using git as a version controller for this project, see the related guides to learn more about it :

- [How to use git](./guide-git/guide-git-usage-fr.md)
- [Git commit style guide](./guide-git/guide-git-style-fr.md)

## Dependencies and virtual environments

It is possible that you will have to work on various Python projects on your computer. To make sure that their dependencies won't interfere one with another we will use [Virtualenvs](https://docs.python-guide.org/dev/virtualenvs/), it is a virtualization method that allows you to work in an isolated Python environment for each project, including per-project dependencies.

You can create a new virtual environment called *venv* at the root of the project :

```bash
$ virtualenv -p /usr/bin/python3.6 venv
```

> Note that python 3 is required for this project, because Python 2 is  officially depreciated

And then activate it with :

```bash
$ source venv/bin/activate
```

The indication `(venv)` should be added at the beginning of your shell, indicating that you are actually working on the virtual environment. You can then install the project's required dependencies on the virtual environment with :

```bash
$ pip install -e .
```

## Testing

We will be using `pytest` for testing, here is a basic function and testing example :

**./src/math/add.py**

```python
def add(a, b):
	return a+b 
```

**./tests/tests_add/test_add_unit.py**

```python
import unittest
import random

from src.math import add

def test_add():
    assert(add(3, 5)==8)
```

We can then run our tests from the root folder with :

```bash
$ python -m pytest -v
```

Or if we want to specify a particular test :

```bash
$ python -m pytest -v ./tests/tests_add/test_add_unit.py
```

Here are more informations about testing in Python :

- [Getting Started With Testing in Python](https://realpython.com/python-testing/)

In the particular case of Flask we will use pytest *fixtures* that will allow us to create a virtual testing environment for  the web application, see [Flask Tutorial - Test Coverage](https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/) for a detailed example, and the files  in */tests/test_webapp/* for our implementation.

## Development practices

- See [Python Guide](../guide-python/guide-python.md) for more informations
- Is summarized in some resources and so-called "best practices" :
  - [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839)
  - [Python Guide (with anchor)](https://github.com/realpython/python-guide/blob/master/docs/writing/structure.rst#structure-of-code-is-key)

## Documentation

We will use Python docstrings to document our code, your can learn more [there (in french)](http://sametmax.com/les-docstrings/) and [there](https://www.geeksforgeeks.org/python-docstrings/).

A basic example for our `add` function would be as follow :

```python
def add(a, b):
    """
    	Adds two numbers and returns the result.

        :param a: the first number to add
        :param b: the second number to add
        :type a: int
       	:type b: int
       	:return: the result of the addition
       	:rtype: int
       	
       	:Example:
       	
       	>> add(5,3)
       	8	
    """
	return a+b 
```

Note that doc-strings can be way more complex, and also applied to modules, classes, etc.. see the linked resources for more informations.

## CI/CD

Continuous integration and either continuous delivery/deployment is a essential feature of an Agile project, you can learn more about CI/CD implementation here :

- [Continuous Integration With Python: An Introduction](https://realpython.com/python-continuous-integration/)

- [How to build a modern CI/CD pipeline](https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b)

In our case we will be using `travis-ci` framework.

## Deployment

We will use docker to deploy our code, but this will come in a further iteration of the project.