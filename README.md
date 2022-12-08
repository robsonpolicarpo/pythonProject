# Klue Tests
Python test automation
Pytest + Selenium


### Preconditions
- Python (>= 3.7)


### Installation:

1. You need some virtual environment
```commandline
virtualenv venv
source venv/bin/activate
```

2. Install requirements:
```commandline
pip install -r requirements.txt
```

### Run:

Run all tests with the command above:
```commandline
python3 -m pytest -k smoke --html-report=./reports/report.html
```
Add tags
```commandline
-k smoke
```
Run in parallel
```commandline
-n 2
```
Add report 
```commandline
--html-report=./reports/report.html
```


### References

* Pytest
  * https://docs.pytest.org/en/6.2.x/contents.html#toc

* Selenium framework used
  * https://github.com/yashaka/selene

* Faker
  * https://faker.readthedocs.io/en/master/fakerclass.html
