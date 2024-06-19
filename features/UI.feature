
Feature: UI tests

  Scenario: Sign Up flow
    Given user fill opt-in form with name "John" and email "johnmarston@mailinator.com"
    When user join Zonia
    Then user sign-up with following data
      | name         | email                      | password | bill_cycle |
      | John Marston | johnmarston@mailinator.com | 123456   | monthly    |


  Scenario: test
    Given user verify Opt In register buttons

  @WIP
  Scenario: GitHub Actions
    Given user fill opt-in form with random name and email
    When user join Zonia
    Then user sign-up with random user data and bill cycle "monthly"

