Feature: Bonus entry tests

  @bonus_entry @ad_ev_bonus_entry @WIP
  Scenario Outline: AD Evergreen funnel via bonus entry
    Given user starts "ad_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
#      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
#      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
#      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
#      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
#      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
#      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
#      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
#      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
#      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
#      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
#      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
#      | 4-ep12  | ep12    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
#      | 5-base  | base    | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
#      | 5-ep11  | ep11    | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
#      | 5-ep12  | ep12    | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
#      | 6-base  | base    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
#      | 6-ep11  | ep11    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
#      | 6-ep12  | ep12    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
#      | 7-base  | base    | quarterly | platinum         | no                   | 3          | no                 | no         | upgrade            |
      | 7-ep11  | ep11    | quarterly | platinum         | no                   | 3          | no                 | no         | upgrade            |
#      | 7-ep12  | ep12    | quarterly | platinum         | no                   | 3          | no                 | no         | upgrade            |
#      | 8-base  | base    | monthly   | silver           | buy                  | 6          | most_popular       | 3          | most_popular       |
#      | 8-ep11  | ep11    | monthly   | silver           | buy                  | 6          | most_popular       | 3          | most_popular       |
#      | 8-ep12  | ep12    | monthly   | silver           | buy                  | 6          | most_popular       | 3          | most_popular       |
#      | 9-base  | base    | annually  | platinum         | buy                  | 3          | best_value         | 1          | best_value         |
#      | 9-ep11  | ep11    | annually  | platinum         | buy                  | 3          | best_value         | 1          | best_value         |
#      | 9-ep12  | ep12    | annually  | platinum         | buy                  | 3          | best_value         | 1          | best_value         |


  @bonus_entry @bb_ev_bonus_entry
  Scenario Outline: BB Evergreen funnel via bonus entry
    Given user starts "bb_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep10  | ep10    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep10  | ep10    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep10  | ep10    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep10  | ep10    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep10  | ep10    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep10  | ep10    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep10  | ep10    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep10  | ep10    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep10  | ep10    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @lg_ev_bonus_entry
  Scenario Outline: LG Evergreen funnel via bonus entry
    Given user starts "lg_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep12  | ep12    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep12  | ep12    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep12  | ep12    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep12  | ep12    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep12  | ep12    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep12  | ep12    | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @km_ev_bonus_entry
  Scenario Outline: KM Evergreen funnel via bonus entry
    Given user starts "km_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep12  | ep12    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep12  | ep12    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep12  | ep12    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep12  | ep12    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep12  | ep12    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep12  | ep12    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @is_ev_bonus_entry
  Scenario Outline: IS Evergreen funnel via bonus entry
    Given user starts "is_ev" funnel from "<variant>" bonus entry page
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
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | variant | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rs_bottles | rs_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | lifetime  | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | lifetime  | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep12  | ep12    | lifetime  | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep12  | ep12    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep12  | ep12    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep12  | ep12    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep12  | ep12    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | lifetime  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | lifetime  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep12  | ep12    | lifetime  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @tf_ev_bonus_entry
  Scenario Outline: TF Evergreen funnel via bonus entry
    Given user starts "tf_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep8   | ep8     | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep9   | ep9     | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep8   | ep8     | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep9   | ep9     | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep8   | ep8     | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep9   | ep9     | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep8   | ep8     | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep9   | ep9     | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep8   | ep8     | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep9   | ep9     | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep8   | ep8     | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep9   | ep9     | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep8   | ep8     | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep9   | ep9     | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep8   | ep8     | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep9   | ep9     | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep8   | ep8     | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep9   | ep9     | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @twl_ev_bonus_entry
  Scenario Outline: TWL Evergreen funnel via bonus entry
    Given user starts "twl_ev" funnel from "<variant>" bonus entry page
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
      | outline | variant | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
      | 6-base  | base    | annually  | no               | buy                  | no         | upgrade            | 6          | most_popular       |
      | 7-base  | base    | quarterly | platinum         | buy                  | 3          | most_popular       | 1          | best_value         |


  @bonus_entry @cr_ev_bonus_entry
  Scenario Outline: CR Evergreen funnel via bonus entry
    Given user starts "cr_ev" funnel from "<variant>" bonus entry page
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
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | variant | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep12  | ep12    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep12  | ep12    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep12  | ep12    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep12  | ep12    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep12  | ep12    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep12  | ep12    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @bonus_entry @hh_ev_bonus_entry
  Scenario Outline: HH Evergreen funnel via bonus entry
    Given user starts "hh_ev" funnel from "<variant>" bonus entry page
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
    And user makes following decision in docuseries "Restore Collagen" Upsell page
      | bottles      | upsell_downsell      |
      | <rc_bottles> | <rc_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | variant | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rc_bottles | rc_upsell_downsell |
      | 1-base  | base    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep11  | ep11    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 1-ep12  | ep12    | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2-base  | base    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep11  | ep11    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 2-ep12  | ep12    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3-base  | base    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep11  | ep11    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 3-ep12  | ep12    | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4-base  | base    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep11  | ep11    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 4-ep12  | ep12    | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5-base  | base    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep11  | ep11    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 5-ep12  | ep12    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6-base  | base    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep11  | ep11    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 6-ep12  | ep12    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-base  | base    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep11  | ep11    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 7-ep12  | ep12    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8-base  | base    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep11  | ep11    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 8-ep12  | ep12    | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-base  | base    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep11  | ep11    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 9-ep12  | ep12    | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
