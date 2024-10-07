Feature: UI tests

  @restore_sleep
  Scenario Outline: Restore Sleep Supplement funnel
    Given user select to buy "<bottles>" bottles in Restore Sleep Supplements page
    When user makes following decision in supplement "6 More bottles of Restore Sleep" Upsell page
      | upgrade      | last_chance      |
      | <sl_upgrade> | <sl_last_chance> |
    And user makes following decision in supplement "Restore Life" Upsell page
      | upgrade      | last_chance      |
      | <lf_upgrade> | <lf_last_chance> |
    And user makes following decision in supplement "Restore Detox" Upsell page
      | upgrade      | last_chance      |
      | <dt_upgrade> | <dt_last_chance> |
    And user makes following decision in 7 day free membership
      | decision        | plan        |
      | <memb_decision> | <memb_plan> |
    Then user complete registration

    Examples:
      | bottles | sl_upgrade | sl_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | best_value     | no         | most_popular   | no         | no             | decline       | no        |
      | 1       | no         | best_value     | no         | best_value     | no         | most_popular   | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 1       | no         | no             | no         | best_value     | no         | best_value     | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 1       | no         | most_popular   | no         | no             | no         | best_value     | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 1       | no         | no             | no         | most_popular   | no         | no             | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 1       | no         | most_popular   | no         | best_value     | no         | most_popular   | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 1       | no         | most_popular   | no         | no             | no         | most_popular   | decline       | no        |
      | 1       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 1       | no         | best_value     | no         | most_popular   | no         | best_value     | decline       | no        |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 3       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 3       | no         | best_value     | no         | most_popular   | no         | no             | decline       | no        |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 3       | no         | best_value     | no         | best_value     | no         | most_popular   | decline       | no        |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 3       | no         | no             | no         | best_value     | no         | best_value     | decline       | no        |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 3       | no         | no             | no         | no             | no         | best_value     | decline       | no        |
      | 3       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 6       | no         | no             | no         | most_popular   | no         | best_value     | decline       | no        |
      | 6       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 6       | no         | most_popular   | no         | best_value     | no         | best_value     | decline       | no        |
      | 6       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |
      | 6       | no         | best_value     | no         | best_value     | no         | no             | decline       | no        |
      | 6       | yes        | no             | yes        | no             | yes        | no             | accept        | annually  |
      | 6       | no         | best_value     | no         | no             | no         | most_popular   | decline       | no        |
      | 6       | yes        | no             | yes        | no             | yes        | no             | accept        | quarterly |
      | 6       | yes        | no             | yes        | no             | yes        | no             | accept        | monthly   |


  @smoke
  Scenario Outline: Verify buttons redirects
    Given Verify "<element>" button/s on "<url>" page navigate to "<expected_redirect>"

    Examples:
      | element           | url                                                 | expected_redirect                   |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/tf-join-zonia             | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/tf-join-zonia-2           | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/tf-join-zonia-fb          | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/tf-join-zonia-expired     | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/mb2/tf-join-zonia         | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/mb2/tf-join-zonia-2       | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/mb2/tf-join-zonia-fb      | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/mb2/tf-join-zonia-expired | https://staging.zonia.com/tf-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia             | https://staging.zonia.com/ad-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia-2           | https://staging.zonia.com/ad-signup |
      | JOIN_ZONIA_BUTTON | https://staging.zonia.com/ad-join-zonia-fb          | https://staging.zonia.com/ad-signup |

  @smoke
  Scenario Outline: Verify buttons scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element                      | url                                       | target_element            |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-detox        | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-gut-health   | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-brain-health | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-mindset      | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-inflammation | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-energy       | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | https://staging.zonia.com/ad-pain-relief  | FIRST_NAME_REGISTER_FIELD |

  @smoke
  Scenario Outline: Verify arrows scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element             | url                                                   | target_element |
      | SCROLL_ARROW_BUTTON | https://staging.zonia.com/ad-booster-packages-monthly | scroll_down    |

  @WIP @unbroken
  Scenario Outline: Unbroken funnel
    Given user register in "Unbroken" Opt In page
    And user join Zonia
    When user sign up for "MONTHLY" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | silver           | buy                  | 1          | upgrade            | 1          | best_value         |
      | platinum         | buy                  | 3          | most_popular       | 6          | no                 |
      | no               | no                   | no         | no                 | no         | upgrade            |
