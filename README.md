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

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
