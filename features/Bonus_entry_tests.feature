Feature: Bonus entry tests

  @bonus_entry @ad_ev_bonus_entry @WIP
  Scenario Outline: AD Evergreen funnel via bonus entry
    Given user starts "ad_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 1          | upgrade            | no         | no                 |
      | 6-ep11         | ep11    | annually  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | quarterly | no                   | 3          | no                 | no         | upgrade            |
      | 8-ep12         | ep12    | monthly   | buy                  | 6          | most_popular       | 3          | most_popular       |
      | 9-ep12         | ep12    | annually  | buy                  | 3          | best_value         | 1          | best_value         |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @bb_ev_bonus_entry
  Scenario Outline: BB Evergreen funnel via bonus entry
    Given user starts "bb_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep10         | ep10    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep10         | ep10    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep10         | ep10    | lifetime  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep11         | ep11    | annually  | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep11         | ep11    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep11         | ep11    | quarterly | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep10 | ep10    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @lg_ev_bonus_entry
  Scenario Outline: LG Evergreen funnel via bonus entry
    Given user starts "lg_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep11         | ep11    | annually  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | monthly   | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep12         | ep12    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep12         | ep12    | annually  | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @km_ev_bonus_entry
  Scenario Outline: KM Evergreen funnel via bonus entry
    Given user starts "km_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep11         | ep11    | lifetime  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | annually  | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep12         | ep12    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep12         | ep12    | quarterly | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @is_ev_bonus_entry
  Scenario Outline: IS Evergreen funnel via bonus entry
    Given user starts "is_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rl_bottles | rl_upsell_downsell | rs_bottles | rs_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | lifetime  | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep11         | ep11    | annually  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | monthly   | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep12         | ep12    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep12         | ep12    | lifetime  | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @tf_ev_bonus_entry
  Scenario Outline: TF Evergreen funnel via bonus entry
    Given user starts "tf_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep8          | ep8     | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep8          | ep8     | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep8          | ep8     | annually  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep9          | ep9     | monthly   | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep9          | ep9     | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep9          | ep9     | annually  | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep8  | ep8     | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep9  | ep9     | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @twl_ev_bonus_entry
  Scenario Outline: TWL Evergreen funnel via bonus entry
    Given user starts "twl_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-base         | base    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-base         | base    | quarterly | no                   | 1          | upgrade            | no         | no                 |
      | 6-base         | base    | annually  | buy                  | no         | upgrade            | 6          | most_popular       |
      | 7-base         | base    | quarterly | buy                  | 3          | most_popular       | 1          | best_value         |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @cr_ev_bonus_entry
  Scenario Outline: CR Evergreen funnel via bonus entry
    Given user starts "cr_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep11         | ep11    | lifetime  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | annually  | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep12         | ep12    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep12         | ep12    | quarterly | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |


  @bonus_entry @hh_ev_bonus_entry
  Scenario Outline: HH Evergreen funnel via bonus entry
    Given user starts "hh_ev" funnel from "<variant>" bonus entry page
    When user sign up for "<plan>" plan
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
      | outline        | variant | plan      | masterclass_packages | rs_bottles | rs_upsell_downsell | rc_bottles | rc_upsell_downsell |
      | 1-base         | base    | monthly   | no                   | no         | no                 | no         | no                 |
      | 2-base         | base    | quarterly | no                   | no         | no                 | no         | upgrade            |
      | 3-base         | base    | annually  | no                   | no         | no                 | 1          | no                 |
      | 4-ep11         | ep11    | monthly   | no                   | no         | upgrade            | no         | no                 |
      | 5-ep11         | ep11    | quarterly | no                   | 6          | no                 | no         | no                 |
      | 6-ep11         | ep11    | lifetime  | buy                  | no         | upgrade            | 6          | best_value         |
      | 7-ep12         | ep12    | annually  | no                   | 1          | best_value         | no         | upgrade            |
      | 8-ep12         | ep12    | quarterly | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9-ep12         | ep12    | quarterly | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bug-check-base | base    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep11 | ep11    | annually  | no                   | no         | no                 | no         | no                 |
      | bug-check-ep12 | ep12    | annually  | no                   | no         | no                 | no         | no                 |
