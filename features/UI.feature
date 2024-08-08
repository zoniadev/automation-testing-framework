Feature: UI tests


  @WIP
  Scenario: Supplement funnel
    Given user select to buy "1" bottles in Restore Sleep Supplements page
    When user makes following decision in "first" Upsell page
      | upgrade | last_chance |
      | yes     | no          |
    And user makes following decision in "second" Upsell page
      | upgrade | last_chance |
      | no      | best_value  |
#    Then user select to "not upgrade" in "third" Upsell page
#    And user select to "not upgrade" in "fourth" Upsell page

