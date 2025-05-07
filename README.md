## Automated tests with Python and Selenium

Project contains automated UI tests for the open-source nopCommerce application.
Application run in a docker container with basic installation settings. Tests were written using Selenium with Python.
* [Prerequisites](#prerequisites)
* [Technologies](#technologies)
* [How to run the tests](#how-to-run-the-tests)

### Prerequisites

* Download the app from: https://github.com/nopSolutions/nopCommerce
* Run app in a docker container
```
docker-compose up -d
```

### Technologies

* Python 3.x

### How to run the tests
* Open the Tests project
* Run the tests + save results in results folder
```
python -m pytest run_tests.py --alluredir ./results
```
* Generate allure report
```
allure generate ./results --clean -o ./allure-report
```
* Open allure report 
```
allure open ./allure-report
```

