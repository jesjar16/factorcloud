# Automated tests for Factor Cloud

### This document refers to the details to run a suite of automated scripts written using Selenium with Python, for the Factor Cloud website

---
## Instructions for setting python virtual environment

1. On **Windows**, download **Git Bash**, a tool to run shell commands, from the [Official website](https://git-scm.com/downloads) and install it
   
2. Download the latest Python stable version from the [Official website](https://www.python.org/downloads/) and install it 
   
3. Open the Git Bash console and navigate to the folder which will contain the **python virtual environment** folder and run the following command: 

```bash
python -m venv MiEntorno
```
where “MiEntorno” is the **folder** for the virtual environment

4. Once the environment is created, it must be **activated**, using the following command:

```bash
source MiEntorno/Scripts/activate
```

5. If we want to **deactivate** the virtual environment, we can use the following command:

```bash
deactivate
```
6. Now, still using Git Bash console, download **selenium** using **pip** package manager:

```bash
pip install selenium
```
7. Navigate to the directory with the automation **scripts** and finally run the **.py file** to run the automated tests: 

```bash
python factor_cloud.py
```

---
## List of apps and versions used in project

* Google Chrome, version: 111.0.5563.65 (Build oficial) (64 bits)
* Python, version: 3.10.10
* Selenium, version: 4.8.2
  
---

## List of other package dependencies for python virtual environment

* async-generator==1.10
* attrs==22.2.0
* certifi==2022.12.7
* cffi==1.15.1
* exceptiongroup==1.1.1
* h11==0.14.0
* idna==3.4
* outcome==1.2.0
* pycparser==2.21
* PySocks==1.7.1
* sniffio==1.3.0
* sortedcontainers==2.4.0
* trio==0.22.0
* trio-websocket==0.10.0
* urllib3==1.26.15
* wsproto==1.2.0