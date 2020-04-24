# BSVXpy

A better value separation format over CSV

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
pip
python3.7
```

### Installing

First, ensure the lastest python is installed on your system 

```
python3 --version
Python 3.7.7
```

Next, install pip and activate the virtual environment.

```
python3 -m pip install --user --upgrade pip
```

```
python3 -m pip install --user virtualenv
```

Create and enter your virtual environment.

```
python3 -m venv env
```

You will now notice an env/ folder in your directory. You can enter the virtual environment by executing:
```
source env/bin/activate
```

Full instructions for how to enter a virtual environment [can be found here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### A note about Python Virtual Environments

If you are using an IDE such as VSCode, your virtual environment is most likely automatically initialized for you. If that is the case, you can skip the previous instructions from the Installing section.
It should also be noted that your machine may use a different command to execute python programs (e.i. '''py''''), in which case you should use that command instead of the default '''python3''' command used in this documentation.
If you are concerned about your python installation using a different version of python to build the module, use '''py --version''' to check the version of python your environment is using.

### Development note: 

bsvxpy has a requirements.txt file, you must execute ```pip install -r requirements.txt``` in the bsvxpy/ folder if you plan on developing the repo further. 

This can also be done by running the command ```make init```.

Once you have successfully entered the virtual environment, you may install bsvxpy using pip with the command 

```
pip install .
```

This will install the module in the current directory for use through the virutal environment and pip.

Once you are done installing, simply run each Makefile command in order to ensure your environment is fully working.

## The Makefile

The Makefile in this repo has three options: ```init```, ```remake```, and ```test```. Here are the usages for each:

> ```init```: simply runs ```pip install -r requirements.txt``` and is used to update requirements for development

> ```remake```: uninstalls bsvxpy from the virtual environment then installs it again, effectively "recompiling" the library. This should be done after changes are made in the bsvxpy/ folder and before testing begins.

> ```test```: simply runs ```pytest``` to run all tests in the test/ folder

## Running the tests

Before you run any tests, make sure to re-compile by running ```make remake```

Simply run ```make test``` or ```pytest``` and it will do everything automatically.


## Authors

* **Bryan Bean** - [GitHub](https://github.com/pataman3)
* **Noah Mezher** - [GitHub](https://github.com/NoahMezher)
* **Jack Summers** - [GitHub](https://github.com/Flannelz)
* **Dave Toomey** - [GitHub](https://github.com/davetoomey)

## License

This project is licensed under the Mozilla Public License Version 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Initially proposed by Prof. Daly at UMASS Lowell
