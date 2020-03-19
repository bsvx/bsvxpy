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
noah@noah:~$ python3 --version
Python 3.7.7
```

Next, install pip and activate the virtual environment in the parent directory of this repo.

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

You will now notice an env/ folder in your directory as well as the bsvxpy/ folder. You can enter the virtual environment by executing:
```
source env/bin/activate
```

Full instructions for how to enter a virtual environment [can be found here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

### Development note: 

bsvxpy has a requirements.txt file, you must execute ```pip install -r requirements.txt``` in the bsvxpy/ folder if you plan on developing the repo further. 

Once you have successfully entered the virtual environment and you are in a directory containing the top-level bsvxpy/ folder, you may install it using pip with the command 

```
pip install bsvxpy/
```

The trailing slash is important because pip knows to call a directory.

Once you are done installing, you may navigate to the tests/ folder and execute test.py in your virtual environment. If you get the output: ```<bsvxpy.bsvxBlank.Blank object at 0x7f6ff5bb4910>``` then you know you installed it properly.

## Running the tests

Explain how to run the automated tests for this system

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
