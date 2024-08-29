Feature: UI tests


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
      | 3       | yes        | no             | yes        | no             | no         | best_value     | accept        | annual    |
      | 6       | no         | best_value     | yes        | no             | no         | most_popular   | decline       | no        |

  @smoke
  Scenario Outline: Verify button links
    Given Verify "<element>" links on "<url>" page are "<link>"

    Examples:
      | element           | url                                        | link       |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia    | /ad-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia-2  | /ad-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia-fb | /ad-signup |

  @smoke
  Scenario Outline: Verify buttons scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element                      | url                                                   | target_element            |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/unbroken                    | FIRST_NAME_REGISTER_FIELD |

  @smoke @WIP
  Scenario Outline: Verify arrows scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element                      | url                                                   | target_element            |
      | SCROLL_ARROW_BUTTON          | https://staging.zonia.com/ad-booster-packages-monthly | scroll_down               |
