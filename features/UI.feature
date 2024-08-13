Feature: UI tests


  @WIP
  Scenario: Restore Sleep Supplement funnel
    Given user select to buy "1" bottles in Restore Sleep Supplements page
    When user makes following decision in "6 More bottles of Restore Sleep" Upsell page
      | upgrade | last_chance |
      | yes     | no          |
    And user makes following decision in "6 bottles of Restore Life" Upsell page
      | upgrade | last_chance |
      | no      | best_value  |
    And user makes following decision in "6 bottles of Restore Detox" Upsell page
      | upgrade | last_chance  |
      | no      | most_popular |
    And user makes following decision in 7 day free membership
      | decision | plan    |
      | accept   | monthly |
    Then user complete registration

