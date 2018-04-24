The test implementation consists of two Flask microservices- data_fetch and data_write, and controller. Controller is a python script written in separate file.

## Getting Started
You need Python version 3.5 to run applications and controller
    
### Installation
To setup the environment for each microservice and launch the server you need to run following (in root microservice folder):
```bash
$ virtualenv -p <path to your python 3.5> env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Running  
```bash  
$ python run.py
```

The data_fetch microservice runs at port 5000, write_data runs at 5555.

When both microservices are running, you can start the controller. To execute code in controller.py the following should be entered in command line (you need to be in a root directory): 
```bash 
$ <path to python 3.5> controller.py 
```

## Each microservice has the following structure:
  *Directory with the name similar to microservice name: main service folder. 
  *There is handlers.py file in main folder with all endpoint handlers.
  *Directory logic contains the main logic of application.
  *File requirements.txt contains all requirements necessary to install in virtual environment.
  *File run.py contains the script to run the application.
  *All collected logs are gathered in error.log file in each microservice. The logs are formatted so there is the UTC time of each log is at the beginning of the log record.

## Features of data_fetch microservice:
The validation of data is performed with the help of trafaret library (http://trafaret.readthedocs.io/en/latest/intro.html). 
For logging all the exceptions there is the decorator @log_exception.
 	For constructing XML document there were several options available
(ElementTree, cElementTree, LXML). The library that was chosen is cElementTree, since it is a C implementation of the ElementTree API(Basic, pure-Python),
optimized for fast parsing and low memory use.

## Features of data_write microservice:
Each call the XML is written in the new file within the saved_xml_files directory. The name of the file is constructed with of current datetime formatted string.
