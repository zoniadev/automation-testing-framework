# Zonia Automation Testing framework
Latest results can be seen [here](https://zoniadev.github.io/automation-testing-framework)

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.7
- pip
- Java

### Installing
1. Clone the repository
2. Install the required packages
```
pip install -r requirements.txt
```
3. Run Playwright install
```
playwright install
```
3. Run the tests
```
behave --tags @WIP --no-capture -D headless=True -D start_page=restore_sleep_start_url -D funnel=restore_sleep_supplement -f allure_behave.formatter:AllureFormatter -o allure-results
```
4. Generate the Allure report
```
allure serve allure-results
```
