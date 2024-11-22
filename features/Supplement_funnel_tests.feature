Feature: Funnel tests

  @restore_sleep @WIP
  Scenario Outline: Restore Sleep Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Sleep" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "second" supplement "Restore Life" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in "third" supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | sl_upgrade | sl_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | best_value     | no         | most_popular   | no         | most_popular   | accept        | quarterly |
      | 1       | no         | most_popular   | no         | no             | no         | best_value     | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 1       | yes        | no             | no         | best_value     | no         | no             | accept        | annually  |
      | 1       | no         | best_value     | yes        | no             | no         | best_value     | decline       | no        |
      | 1       | no         | most_popular   | yes        | no             | no         | most_popular   | accept        | monthly   |
      | 3       | no         | best_value     | yes        | no             | yes        | no             | accept        | annually  |
      | 3       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | monthly   |
      | 3       | no         | no             | no         | best_value     | no         | best_value     | accept        | quarterly |
      | 3       | yes        | no             | no         | most_popular   | no         | most_popular   | decline       | no        |
      | 3       | no         | most_popular   | no         | most_popular   | yes        | no             | accept        | quarterly |
      | 6       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |
      | 6       | no         | best_value     | no         | best_value     | no         | most_popular   | accept        | annually  |
      | 6       | yes        | no             | yes        | no             | no         | best_value     | accept        | quarterly |
      | 6       | no         | most_popular   | no         | best_value     | yes        | no             | decline       | no        |
      | 6       | yes        | no             | no         | most_popular   | yes        | no             | accept        | monthly   |


  @restore_gut
  Scenario Outline: Restore Gut Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Gut" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Gut" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "second" supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in "third" supplement "Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | sl_upgrade | sl_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | most_popular   | no         | no             | no         | best_value     | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 1       | no         | best_value     | no         | most_popular   | no         | most_popular   | accept        | quarterly |
      | 1       | no         | most_popular   | yes        | no             | no         | most_popular   | accept        | monthly   |
      | 1       | no         | best_value     | yes        | no             | no         | best_value     | decline       | no        |
      | 1       | yes        | no             | no         | best_value     | no         | no             | accept        | annually  |
      | 3       | no         | most_popular   | no         | most_popular   | yes        | no             | accept        | quarterly |
      | 3       | no         | best_value     | yes        | no             | yes        | no             | accept        | annually  |
      | 3       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | monthly   |
      | 3       | no         | no             | no         | best_value     | no         | best_value     | accept        | quarterly |
      | 3       | yes        | no             | no         | most_popular   | no         | most_popular   | decline       | no        |
      | 6       | yes        | no             | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 6       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |
      | 6       | no         | best_value     | no         | best_value     | no         | most_popular   | accept        | annually  |
      | 6       | yes        | no             | yes        | no             | no         | best_value     | accept        | quarterly |
      | 6       | no         | most_popular   | no         | best_value     | yes        | no             | decline       | no        |

