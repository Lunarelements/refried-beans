# RefriedBeans

A script that opens up various MBeans and then allows you to save the HTML output when done. It was created to automate a task at one of my jobs

## Getting Started

Clone the repo or copy the RefriedBeans.py script

### Prerequisites

Python 3 must be installed

### Installing

First configure the ip and port pairs

Replace "http://XXX.XXX.XXX.XXX:XXXX/" with your component ip and port

```
WDS = ["http://XXX.XXX.XXX.XXX:XXXX/", "http://XXX.XXX.XXX.XXX:XXXX/"]
WBI = ["http://XXX.XXX.XXX.XXX:XXXX/", "http://XXX.XXX.XXX.XXX:XXXX/"]
PI = ["http://XXX.XXX.XXX.XXX:XXXX/", "http://XXX.XXX.XXX.XXX:XXXX/"]
CS = ["http://XXX.XXX.XXX.XXX:XXXX/", "http://XXX.XXX.XXX.XXX:XXXX/"]
CPWERecognition = ["http://XXX.XXX.XXX.XXX:XXXX/", "http://XXX.XXX.XXX.XXX:XXXX/"]
```

## Running 

Run the program using the following command

```
python RefriedBeans.py
```

Enter in a string of numbers representing the MBeans you wish to watch and save separated by spaces

```
1.WDS
2.WBI
3.PI
4.CPWERecognition
5.Quit

1 3 4
```

Wait for the MBeans selected to open and then start your tests

When finished type "y" into the program and it will save the html for each MBean

```
Collect MBeans? (y/n)
y
```

## Authors

* **Bradley Leonard**
