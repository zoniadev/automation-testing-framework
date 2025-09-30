Feature: Supplement tests

  @restore_sleep @all_supplements
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


  @restore_sleep_b2g3 @all_supplements
  Scenario Outline: Restore Sleep - Buy 2, Get 3 Free bottles Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Sleep B2G3" Supplements page
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
      | 2       | no         | best_value     | yes        | no             | yes        | no             | accept        | annually  |
      | 2       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | monthly   |
      | 2       | no         | no             | no         | best_value     | no         | best_value     | accept        | quarterly |
      | 2       | yes        | no             | no         | most_popular   | no         | most_popular   | decline       | no        |
      | 2       | no         | most_popular   | no         | most_popular   | yes        | no             | accept        | quarterly |
      | 5       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |
      | 5       | no         | best_value     | no         | best_value     | no         | most_popular   | accept        | annually  |
      | 5       | yes        | no             | yes        | no             | no         | best_value     | accept        | quarterly |
      | 11      | no         | most_popular   | no         | best_value     | yes        | no             | decline       | no        |
      | 11      | yes        | no             | no         | most_popular   | yes        | no             | accept        | monthly   |


  @restore_gut @all_supplements
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


  @restore_gut_b2g3 @all_supplements
  Scenario Outline: Restore Gut - Buy 2, Get 3 Free bottles Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Gut B2G3" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Gut" Upsell page
      | upgrade      | last_chance      |
      | <vs_upgrade> | <vs_last_chance> |
    And user makes following decision in "second" supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in "third" supplement "Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | vs_upgrade | vs_last_chance | dt_upgrade | dt_last_chance | sl_upgrade | sl_last_chance | memb_decision | memb_plan |
      | 1       | no         | most_popular   | no         | no             | no         | best_value     | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 1       | no         | best_value     | no         | most_popular   | no         | most_popular   | accept        | quarterly |
      | 1       | no         | most_popular   | yes        | no             | no         | most_popular   | accept        | monthly   |
      | 1       | no         | best_value     | yes        | no             | no         | best_value     | decline       | no        |
      | 1       | yes        | no             | no         | best_value     | no         | no             | accept        | annually  |
      | 2       | no         | most_popular   | no         | most_popular   | yes        | no             | accept        | quarterly |
      | 2       | no         | best_value     | yes        | no             | yes        | no             | accept        | annually  |
      | 2       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | monthly   |
      | 2       | no         | no             | no         | best_value     | no         | best_value     | accept        | quarterly |
      | 2       | yes        | no             | no         | most_popular   | no         | most_popular   | decline       | no        |
      | 5       | yes        | no             | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 5       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |
      | 5       | no         | best_value     | no         | best_value     | no         | most_popular   | accept        | annually  |
      | 5       | yes        | no             | yes        | no             | no         | best_value     | accept        | quarterly |
      | 5       | no         | most_popular   | no         | best_value     | yes        | no             | decline       | no        |

  @restore_vision @all_supplements
  Scenario Outline: Restore Vision Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Vision" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Vision" Upsell page
      | upgrade      | last_chance      |
      | <vs_upgrade> | <vs_last_chance> |
    And user makes following decision in "second" supplement "Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "third" supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | vs_upgrade | vs_last_chance | sl_upgrade | sl_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
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


  @restore_vision_b2g3 @all_supplements
  Scenario Outline: Restore Vision - Buy 2, Get 3 Free bottles Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Vision B2G3" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Vision" Upsell page
      | upgrade      | last_chance      |
      | <vs_upgrade> | <vs_last_chance> |
    And user makes following decision in "second" supplement "Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "third" supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | vs_upgrade | vs_last_chance | sl_upgrade | sl_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | most_popular   | no         | no             | no         | best_value     | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 1       | no         | best_value     | no         | most_popular   | no         | most_popular   | accept        | quarterly |
      | 1       | no         | most_popular   | yes        | no             | no         | most_popular   | accept        | monthly   |
      | 1       | no         | best_value     | yes        | no             | no         | best_value     | decline       | no        |
      | 1       | yes        | no             | no         | best_value     | no         | no             | accept        | annually  |
      | 2       | no         | most_popular   | no         | most_popular   | yes        | no             | accept        | quarterly |
      | 2       | no         | best_value     | yes        | no             | yes        | no             | accept        | annually  |
      | 2       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | monthly   |
      | 2       | no         | no             | no         | best_value     | no         | best_value     | accept        | quarterly |
      | 2       | yes        | no             | no         | most_popular   | no         | most_popular   | decline       | no        |
      | 5       | yes        | no             | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 5       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |
      | 5       | no         | best_value     | no         | best_value     | no         | most_popular   | accept        | annually  |
      | 5       | yes        | no             | yes        | no             | no         | best_value     | accept        | quarterly |
      | 5       | no         | most_popular   | no         | best_value     | yes        | no             | decline       | no        |


  @restore_detox @all_supplements
  Scenario Outline: Restore Detox Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Detox" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in "second" supplement "Restore Life" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | dt_upgrade | dt_last_chance | lf_upgrade | lf_last_chance | memb_decision | memb_plan |
      | 1       | yes        | no             | yes        | no             | accept        | annually  |
      | 3       | no         | no             | no         | most_popular   | decline       | no        |
      | 6       | no         | most_popular   | no         | best_value     | accept        | quarterly |
      | 1       | no         | most_popular   | yes        | no             | decline       | no        |
      | 3       | no         | best_value     | no         | most_popular   | accept        | quarterly |
      | 1       | no         | best_value     | no         | best_value     | accept        | annually  |
      | 3       | no         | most_popular   | no         | most_popular   | accept        | annually  |
      | 1       | yes        | no             | no         | no             | accept        | quarterly |
      | 6       | no         | best_value     | yes        | no             | accept        | annually  |
      | 6       | yes        | no             | no         | best_value     | accept        | monthly   |
      | 3       | no         | most_popular   | yes        | no             | accept        | monthly   |
      | 3       | no         | best_value     | no         | best_value     | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 6       | yes        | no             | no         | most_popular   | decline       | no        |
      | 3       | yes        | no             | no         | most_popular   | accept        | quarterly |
      | 3       | no         | most_popular   | no         | best_value     | decline       | no        |
      | 1       | no         | no             | yes        | no             | accept        | quarterly |
