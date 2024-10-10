Feature: Funnel tests

  @restore_sleep
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
      | 1       | no         | no             | yes        | no             | yes        | best_value     | accept        | annually  |
      | 1       | yes        | no             | yes        | most_popular   | yes        | best_value     | accept        | monthly   |
      | 1       | yes        | most_popular   | no         | no             | yes        | most_popular   | accept        | quarterly |
      | 1       | yes        | best_value     | yes        | most_popular   | no         | no             | accept        | annually  |
      | 1       | yes        | best_value     | yes        | best_value     | no         | no             | decline       | no        |
      | 3       | no         | no             | no         | no             | yes        | most_popular   | accept        | annually  |
      | 3       | no         | no             | yes        | most_popular   | yes        | most_popular   | decline       | no        |
      | 3       | yes        | best_value     | yes        | best_value     | yes        | best_value     | accept        | quarterly |
      | 3       | yes        | most_popular   | no         | no             | no         | no             | accept        | monthly   |
      | 6       | yes        | best_value     | yes        | most_popular   | no         | no             | accept        | quarterly |
      | 6       | yes        | most_popular   | yes        | best_value     | yes        | most_popular   | accept        | annually  |
      | 6       | no         | no             | yes        | best_value     | yes        | most_popular   | accept        | monthly   |
      | 6       | yes        | most_popular   | yes        | most_popular   | yes        | best_value     | decline       | no        |
      | 6       | yes        | best_value     | no         | no             | yes        | most_popular   | accept        | monthly   |
      | 6       | no         | no             | no         | no             | yes        | best_value     | decline       | no        |
      | 6       | no         | no             | yes        | most_popular   | no         | no             | accept        | quarterly |
      | 6       | yes        | best_value     | yes        | best_value     | yes        | no             | accept        | no        |


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
      | 1       | no         | no             | yes        | no             | yes        | best_value     | accept        | annually  |
      | 1       | yes        | most_popular   | no         | no             | yes        | most_popular   | accept        | quarterly |
      | 1       | yes        | best_value     | yes        | most_popular   | no         | no             | accept        | annually  |
      | 1       | yes        | no             | yes        | most_popular   | yes        | best_value     | accept        | monthly   |
      | 1       | yes        | best_value     | yes        | best_value     | no         | no             | decline       | no        |
      | 3       | no         | no             | no         | no             | yes        | most_popular   | accept        | annually  |
      | 3       | no         | no             | yes        | most_popular   | yes        | most_popular   | decline       | no        |
      | 3       | yes        | best_value     | yes        | best_value     | yes        | best_value     | accept        | quarterly |
      | 3       | yes        | most_popular   | no         | no             | no         | no             | accept        | monthly   |
      | 6       | yes        | best_value     | yes        | most_popular   | no         | no             | accept        | quarterly |
      | 6       | yes        | most_popular   | yes        | best_value     | yes        | most_popular   | accept        | annually  |
      | 6       | no         | no             | yes        | best_value     | yes        | most_popular   | accept        | monthly   |
      | 6       | yes        | most_popular   | yes        | most_popular   | yes        | best_value     | decline       | no        |
      | 6       | yes        | best_value     | no         | no             | yes        | most_popular   | accept        | monthly   |
      | 6       | no         | no             | no         | no             | yes        | best_value     | decline       | no        |
      | 6       | no         | no             | yes        | most_popular   | no         | no             | accept        | quarterly |
      | 6       | yes        | best_value     | yes        | best_value     | yes        | no             | accept        | no        |

    @WIP
    Scenario: Test email
      Given user select to buy "1" bottles in "Restore Gut" Supplements page

