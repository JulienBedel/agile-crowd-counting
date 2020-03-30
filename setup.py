from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="agile-crowd-counting",
    vesion="1.0",
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,

)
