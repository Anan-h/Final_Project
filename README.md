## <p style="color:blue;">Trello Website API and UI Testing Project</p>
## Overview
This repository contains a set of automated tests for the Trello website, covering both API and UI testing. 
The goal of this project is to ensure the reliability and functionality of the website by verifying its API endpoints and user interface.
https://trello.com

### Table of Contents
1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Running Tests](#running-tests)
6. [Contributing](#contributing)
7. [Contact](#contact)
### Before running the tests, ensure that you have the following installed:
- [Selenium](https://www.selenium.dev/) for UI test automation
- [requests](https://docs.python-requests.org/) for API requests

### Clone the repository:
* git clone https://github.com/Anan-h/Final_Project.git

### Install Dependencies:
* pip install selenium
* pip install requests
* pip install pytest
* pip install allure-pytest

### Configuration
#### UI Tests
* Browser Configuration: Ensure you have the appropriate web driver installed (e.g., ChromeDriver for Chrome). Update the Browser in the configuration file located in config.json.

* Trello Acoount: Update the email and password in config.json to point to your Trello account.

#### API Tests
* create a file and name secret.json to include the identifieres.
* Identifier: Update the trello_api_key and trello_api_token to your identifieres 

### Running Tests:
#### open in terminal:
* for regular test runner insert the following command: pytest
* for allure report creation insert: pytest --alluredir=./{name of the file}
* for generating the allure report: allure serve {name of the file}

 
### Contributing:
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

### Contact
#### For any questions or issues, please contact:

* Name: Anan Husein
* Email: anan.hosien@gmail.com
*  GitHub: https://github.com/Anan-h


![Version](https://img.shields.io/badge/version-1.0.0-blue)
