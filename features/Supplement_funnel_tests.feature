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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 6       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 2       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 5       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 11      | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 6       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 2       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 5       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 6       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 2       | yes        | no             | no         | best_value     | no         | most_popular   | accept        | monthly   |
      | 5       | no         | best_value     | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | annually  |


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
      | 1       | no         | no             | no         | no             | decline       | no        |
      | 3       | yes        | no             | no         | best_value     | accept        | monthly   |
      | 6       | no         | best_value     | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | most_popular   | accept        | annually  |


  @restore_collagen @all_supplements
  Scenario Outline: Restore Collagen Supplement funnel
    Given user select to buy "<bottles>" bottles in "Restore Collagen" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Collagen" Upsell page
      | upgrade      | last_chance      |
      | <rc_upgrade> | <rc_last_chance> |
    And user makes following decision in "second" supplement "Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in "third" supplement "Restore Life" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | rc_upgrade | rc_last_chance | sl_upgrade | sl_last_chance | lf_upgrade | lf_last_chance | memb_decision | memb_plan |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | no         | best_value     | no         | most_popular   | no         | best_value     | accept        | quarterly |
      | 6       | no         | most_popular   | no         | best_value     | no         | most_popular   | accept        | monthly   |
