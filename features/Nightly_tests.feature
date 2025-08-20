Feature: Nightly tests

  @nightly
  Scenario Outline: Unbroken live nightly
    Given user register in "ad_live" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
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
      | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | quarterly | no               | no                   | no         | no                 | no         | no                 |
      | monthly   | platinum         | buy                  | 3          | upgrade            | 6          | most_popular       |


  @nightly
  Scenario Outline: Unbroken evergreen funnel
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
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
      | opt_in_page | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | ad_ev       | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | ad_ev_detox | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: BB Live nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
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
      | opt_in_page   | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | bb_live       | quarterly | no               | no                   | no         | no                 | no         | no                 |
      | bb_live_detox | monthly   | silver           | buy                  | 1          | upgrade            | 1          | upgrade            |


  @nightly
  Scenario Outline: BB Evergreen nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
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
      | opt_in_page | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | bb_ev       | quarterly | no               | no                   | no         | no                 | no         | no                 |
      | bb_ev_detox | monthly   | silver           | buy                  | 1          | upgrade            | 1          | upgrade            |


  @nightly
  Scenario Outline: Ageless Evergreen nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page      | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | lg_ev            | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | lg_ev_metabolism | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: Ageless Live nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page        | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | lg_live            | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | lg_live_metabolism | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: KM Live nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page     | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | km_live         | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | km_live_mystery | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: KM Evergreen nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page     | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | km_live         | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | km_live_mystery | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: IS Evergreen nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page      | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | is_ev            | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | lg_ev_metabolism | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: TF Evergreen nightly
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia
    When user sign up for "<plan>" plan
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
      | opt_in_page | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | tf_ev       | quarterly | platinum         | buy                  | 3          | upgrade            | 1          | upgrade            |
      | tf_ev_meals | monthly   | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: TWL Evergreen direct nightly
    Given user register in "twl_ev" Opt In page
    And user join Zonia in screening page "directly"
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | plan    | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | monthly | platinum         | buy                  | 6          | upgrade            | 1          | upgrade            |
      | monthly | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: TWL Evergreen regular nightly
    Given user register in "twl_ev" Opt In page
    And user join Zonia in screening page "regular"
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Booster Packages" Upsell page
      | decision           |
      | <booster_packages> |
    And user makes following decision in docuseries "Masterclass Packages" Upsell page
      | decision               |
      | <masterclass_packages> |
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | plan    | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | monthly | platinum         | buy                  | 6          | upgrade            | 1          | upgrade            |
      | monthly | no               | no                   | no         | no                 | no         | no                 |


  @nightly
  Scenario Outline: Restore Sleep Supplement nightly
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
      | 1       | no         | most_popular   | no         | most_popular   | no         | best_value     | accept        | monthly   |


  @nightly
  Scenario Outline: Restore Sleep - Buy 2, Get 3 Free bottles Supplement nightly
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
      | 1       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | quarterly |


  @nightly
  Scenario Outline: Restore Gut Supplement nightly
    Given user select to buy "<bottles>" bottles in "Restore Gut" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Gut" Upsell page
      | upgrade      | last_chance      |
      | <rg_upgrade> | <rg_last_chance> |
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
      | bottles | rg_upgrade | rg_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |


  @nightly
  Scenario Outline: Restore Vision Supplement nightly
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
      | 1       | no         | best_value     | no         | most_popular   | yes        | no             | accept        | monthly   |


  @nightly
  Scenario Outline: Restore Detox Supplement nightly
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
      | 1       | no         | best_value     | no         | most_popular   | accept        | monthly   |


  @nightly
  Scenario Outline: Restore Vision - Buy 2, Get 3 Free bottles Supplement nightly
    Given user select to buy "<bottles>" bottles in "Restore Vision B2G3" Supplements page
    When user makes following decision in "first" supplement "6 More bottles of Restore Vision" Upsell page
      | upgrade      | last_chance      |
      | <vs_upgrade> | <vs_last_chance> |
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
      | bottles | vs_upgrade | vs_last_chance | lf_upgrade | lf_last_chance | dt_upgrade | dt_last_chance | memb_decision | memb_plan |
      | 1       | no         | no             | no         | no             | no         | no             | decline       | no        |
      | 1       | no         | most_popular   | no         | best_value     | no         | best_value     | accept        | quarterly |
