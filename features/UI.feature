Feature: UI tests


  @WIP
  Scenario Outline: Restore Sleep Supplement funnel
    Given user select to buy "<bottles>" bottles in Restore Sleep Supplements page
    When user makes following decision in "6 More bottles of Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "Restore Life" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | sl_upgrade | sl_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 3       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | no         | best_value     | yes        | no             | no         | most_popular   | decline       | no        |
      | 6       | no         | best_value     | yes        | no             | no         | most_popular   | decline       | no        |


