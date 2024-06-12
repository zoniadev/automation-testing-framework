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
  Scenario: Restore Sleep Supplements
    Given user select to buy "one" bottles in Restore Sleep Supplements page
    When user select to "upgrade" in "first" Upsell page
    And user select to "upgrade" in "second" Upsell page
    Then user select to "not upgrade" in "third" Upsell page
    And user select to "not upgrade" in "fourth" Upsell page

