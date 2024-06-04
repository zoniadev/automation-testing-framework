
Feature: UI tests

  Scenario: Sign Up flow
    Given user fill opt-in form with name "John" and email "johnmarston@mailinator.com"
    When user join Zonia
    Then user sign-up with following data
      | name         | email                      | password | bill_cycle |
      | John Marston | johnmarston@mailinator.com | 123456   | monthly    |

  @WIP
  Scenario: test
    Given user sign-up with random data

