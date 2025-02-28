Feature: Docuseries tests

  @unbroken_live @all_docuseries
  Scenario Outline: Unbroken live funnel
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
      | monthly   | silver           | buy                  | 6          | most_popular       | 1          | upgrade            |
      | annually  | no               | no                   | no         | no                 | no         | upgrade            |
      | quarterly | platinum         | buy                  | no         | no                 | 6          | most_popular       |
      | quarterly | silver           | no                   | 3          | most_popular       | 3          | most_popular       |
      | annually  | platinum         | buy                  | 1          | best_value         | 3          | no                 |
      | monthly   | no               | no                   | 1          | no                 | 1          | best_value         |
      | quarterly | no               | buy                  | 3          | upgrade            | no         | no                 |
      | annually  | silver           | no                   | 3          | best_value         | 6          | best_value         |
      | monthly   | platinum         | no                   | 6          | most_popular       | 6          | no                 |
      | annually  | platinum         | buy                  | 6          | no                 | 3          | best_value         |
      | monthly   | silver           | no                   | no         | no                 | no         | no                 |
      | quarterly | no               | no                   | 6          | best_value         | no         | upgrade            |
      | annually  | platinum         | no                   | no         | upgrade            | 1          | upgrade            |
      | monthly   | no               | buy                  | 6          | upgrade            | 1          | most_popular       |
      | quarterly | silver           | buy                  | 1          | upgrade            | 6          | upgrade            |
      | monthly   | platinum         | no                   | 3          | no                 | 3          | upgrade            |
      | quarterly | no               | buy                  | 3          | best_value         | 1          | no                 |
      | monthly   | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | quarterly | no               | buy                  | 1          | most_popular       | 1          | best_value         |
      | annually  | platinum         | buy                  | 3          | most_popular       | 1          | most_popular       |
      | annually  | platinum         | no                   | 1          | most_popular       | no         | upgrade            |


  @unbroken_evergreen @all_docuseries
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
      | opt_in_page        | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | ad_ev              | monthly   | silver           | buy                  | 6          | most_popular       | 1          | upgrade            |
      | ad_ev_detox        | annually  | no               | no                   | no         | no                 | no         | upgrade            |
      | ad_ev_gut          | quarterly | platinum         | buy                  | no         | no                 | 6          | most_popular       |
      | ad_ev_brain        | quarterly | silver           | no                   | 3          | most_popular       | 3          | most_popular       |
      | ad_ev_mindset      | annually  | platinum         | buy                  | 1          | best_value         | 3          | no                 |
      | ad_ev_inflammation | monthly   | no               | no                   | 1          | no                 | 1          | best_value         |
      | ad_ev_energy       | quarterly | no               | buy                  | 3          | upgrade            | no         | no                 |
      | ad_ev_pain         | annually  | silver           | no                   | 3          | best_value         | 6          | best_value         |
      | ad_ev              | monthly   | platinum         | no                   | 6          | most_popular       | 6          | no                 |
      | ad_ev_detox        | annually  | platinum         | buy                  | 6          | no                 | 3          | best_value         |
      | ad_ev_gut          | monthly   | silver           | no                   | no         | no                 | no         | no                 |
      | ad_ev_brain        | quarterly | no               | no                   | 6          | best_value         | no         | upgrade            |
      | ad_ev_mindset      | annually  | platinum         | no                   | no         | upgrade            | 1          | upgrade            |
      | ad_ev_inflammation | monthly   | no               | buy                  | 6          | upgrade            | 1          | most_popular       |
      | ad_ev_energy       | quarterly | silver           | buy                  | 1          | upgrade            | 6          | upgrade            |
      | ad_ev_pain         | monthly   | platinum         | no                   | 3          | no                 | 3          | upgrade            |
      | ad_ev              | quarterly | no               | buy                  | 3          | best_value         | 1          | no                 |
      | ad_ev_detox        | monthly   | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | ad_ev_gut          | quarterly | no               | buy                  | 1          | most_popular       | 1          | best_value         |
      | ad_ev_brain        | annually  | platinum         | buy                  | 3          | most_popular       | 1          | most_popular       |
      | ad_ev_mindset      | annually  | platinum         | no                   | 1          | most_popular       | no         | upgrade            |


  @bb_live @all_docuseries
  Scenario Outline: BB Live funnel
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
      | opt_in_page      | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | bb_live          | annually  | platinum         | no                   | 1          | upgrade            | no         | upgrade            |
      | bb_live_detox    | annually  | silver           | buy                  | 6          | no                 | 3          | no                 |
      | bb_live_gut      | monthly   | no               | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bb_live_memory   | lifetime  | silver           | buy                  | no         | upgrade            | 6          | best_value         |
      | bb_live_mood     | annually  | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | bb_live_sleep    | lifetime  | silver           | no                   | 1          | most_popular       | 1          | no                 |
      | bb_live_energy   | monthly   | no               | no                   | no         | no                 | 3          | upgrade            |
      | bb_live_immunity | quarterly | platinum         | buy                  | 3          | most_popular       | no         | no                 |
      | bb_live_detox    | quarterly | platinum         | no                   | 6          | best_value         | 1          | best_value         |
      | bb_live_gut      | quarterly | no               | buy                  | 6          | most_popular       | 6          | upgrade            |
      | bb_live_memory   | annually  | no               | no                   | 3          | most_popular       | 3          | best_value         |
      | bb_live_mood     | monthly   | platinum         | buy                  | 6          | upgrade            | 3          | most_popular       |
      | bb_live_sleep    | lifetime  | silver           | no                   | 3          | no                 | 6          | most_popular       |
      | bb_live_energy   | lifetime  | silver           | buy                  | 3          | best_value         | 3          | upgrade            |
      | bb_live_immunity | annually  | platinum         | buy                  | no         | upgrade            | 1          | upgrade            |
      | bb_live          | monthly   | silver           | buy                  | 1          | best_value         | 6          | no                 |
      | bb_live_detox    | lifetime  | no               | buy                  | 6          | best_value         | no         | no                 |
      | bb_live_gut      | quarterly | platinum         | no                   | no         | no                 | no         | no                 |
      | bb_live_memory   | quarterly | silver           | no                   | 1          | upgrade            | 3          | most_popular       |
      | bb_live_mood     | monthly   | no               | buy                  | 3          | upgrade            | no         | no                 |
      | bb_live_sleep    | lifetime  | platinum         | no                   | no         | no                 | 1          | most_popular       |
      | bb_live_energy   | monthly   | platinum         | buy                  | 1          | no                 | 6          | best_value         |
      | bb_live_immunity | annually  | silver           | no                   | no         | no                 | no         | upgrade            |

  @bb_evergreen @all_docuseries
  Scenario Outline: BB Evergreen funnel
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
      | opt_in_page    | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | bb_ev          | annually  | platinum         | no                   | 1          | upgrade            | no         | upgrade            |
      | bb_ev_detox    | annually  | silver           | buy                  | 6          | no                 | 3          | no                 |
      | bb_ev_gut      | monthly   | no               | buy                  | 3          | most_popular       | 1          | most_popular       |
      | bb_ev_memory   | lifetime  | silver           | buy                  | no         | upgrade            | 6          | best_value         |
      | bb_ev_mood     | annually  | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | bb_ev_sleep    | lifetime  | silver           | no                   | 1          | most_popular       | 1          | no                 |
      | bb_ev_energy   | monthly   | no               | no                   | no         | no                 | 3          | upgrade            |
      | bb_ev_immunity | quarterly | platinum         | buy                  | 3          | most_popular       | no         | no                 |
      | bb_ev          | quarterly | platinum         | no                   | 6          | best_value         | 1          | best_value         |
      | bb_ev_detox    | quarterly | no               | buy                  | 6          | most_popular       | 6          | upgrade            |
      | bb_ev_gut      | annually  | no               | no                   | 3          | most_popular       | 3          | best_value         |
      | bb_ev_memory   | monthly   | platinum         | buy                  | 6          | upgrade            | 3          | most_popular       |
      | bb_ev_mood     | lifetime  | silver           | no                   | 3          | no                 | 6          | most_popular       |
      | bb_ev_sleep    | lifetime  | silver           | buy                  | 3          | best_value         | 3          | upgrade            |
      | bb_ev_energy   | annually  | platinum         | buy                  | no         | upgrade            | 1          | upgrade            |
      | bb_ev_immunity | monthly   | silver           | buy                  | 1          | best_value         | 6          | no                 |
      | bb_ev          | lifetime  | no               | buy                  | 6          | best_value         | no         | no                 |
      | bb_ev_detox    | quarterly | platinum         | no                   | no         | no                 | no         | no                 |
      | bb_ev_gut      | quarterly | silver           | no                   | 1          | upgrade            | 3          | most_popular       |
      | bb_ev_memory   | monthly   | no               | buy                  | 3          | upgrade            | no         | no                 |
      | bb_ev_mood     | lifetime  | platinum         | no                   | no         | no                 | 1          | most_popular       |
      | bb_ev_sleep    | monthly   | platinum         | buy                  | 1          | no                 | 6          | best_value         |
      | bb_ev_energy   | annually  | silver           | no                   | no         | no                 | no         | upgrade            |


  @ageless_evergreen @all_docuseries
  Scenario Outline: LG Evergreen funnel
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
      | opt_in_page          | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | ageless              | monthly   | silver           | buy                  | 6          | most_popular       | 1          | upgrade            |
      | ageless_metabolism   | annually  | no               | no                   | no         | upgrade            | 3          | best_value         |
      | ageless_skin         | quarterly | platinum         | buy                  | no         | no                 | 6          | most_popular       |
      | ageless_exercise     | quarterly | silver           | no                   | 3          | most_popular       | 3          | most_popular       |
      | ageless_brain        | annually  | platinum         | buy                  | 1          | best_value         | 3          | no                 |
      | ageless_hormones     | monthly   | no               | no                   | 1          | no                 | 1          | best_value         |
      | ageless_energy       | quarterly | no               | buy                  | 3          | upgrade            | no         | no                 |
      | ageless_inflammation | annually  | silver           | no                   | 3          | best_value         | 6          | best_value         |
      | ageless_bones        | monthly   | platinum         | no                   | 6          | most_popular       | 6          | no                 |
      | ageless              | annually  | platinum         | buy                  | 6          | no                 | 3          | best_value         |
      | ageless_metabolism   | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | ageless_skin         | quarterly | silver           | no                   | no         | no                 | no         | upgrade            |
      | ageless_exercise     | annually  | platinum         | no                   | no         | upgrade            | 1          | upgrade            |
      | ageless_brain        | monthly   | no               | buy                  | 6          | upgrade            | 1          | most_popular       |
      | ageless_hormones     | quarterly | silver           | buy                  | 1          | upgrade            | 6          | upgrade            |
      | ageless_energy       | monthly   | platinum         | no                   | 3          | no                 | 3          | upgrade            |
      | ageless_inflammation | quarterly | no               | buy                  | 3          | best_value         | 1          | no                 |
      | ageless_bones        | monthly   | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | ageless              | quarterly | no               | buy                  | 1          | most_popular       | 1          | best_value         |
      | ageless_metabolism   | annually  | platinum         | buy                  | 3          | most_popular       | 1          | most_popular       |
      | ageless_skin         | annually  | platinum         | no                   | 1          | most_popular       | no         | upgrade            |


  @ageless_live @all_docuseries
  Scenario Outline: LG Live funnel
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
      | opt_in_page          | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | ageless              | monthly   | silver           | buy                  | 6          | most_popular       | 1          | upgrade            |
      | ageless_metabolism   | annually  | no               | no                   | no         | upgrade            | 3          | best_value         |
      | ageless_skin         | quarterly | platinum         | buy                  | no         | no                 | 6          | most_popular       |
      | ageless_exercise     | quarterly | silver           | no                   | 3          | most_popular       | 3          | most_popular       |
      | ageless_brain        | annually  | platinum         | buy                  | 1          | best_value         | 3          | no                 |
      | ageless_hormones     | monthly   | no               | no                   | 1          | no                 | 1          | best_value         |
      | ageless_energy       | quarterly | no               | buy                  | 3          | upgrade            | no         | no                 |
      | ageless_inflammation | annually  | silver           | no                   | 3          | best_value         | 6          | best_value         |
      | ageless_bones        | monthly   | platinum         | no                   | 6          | most_popular       | 6          | no                 |
      | ageless              | annually  | platinum         | buy                  | 6          | no                 | 3          | best_value         |
      | ageless_metabolism   | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | ageless_skin         | quarterly | silver           | no                   | no         | no                 | no         | upgrade            |
      | ageless_exercise     | annually  | platinum         | no                   | no         | upgrade            | 1          | upgrade            |
      | ageless_brain        | monthly   | no               | buy                  | 6          | upgrade            | 1          | most_popular       |
      | ageless_hormones     | quarterly | silver           | buy                  | 1          | upgrade            | 6          | upgrade            |
      | ageless_energy       | monthly   | platinum         | no                   | 3          | no                 | 3          | upgrade            |
      | ageless_inflammation | quarterly | no               | buy                  | 3          | best_value         | 1          | no                 |
      | ageless_bones        | monthly   | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | ageless              | quarterly | no               | buy                  | 1          | most_popular       | 1          | best_value         |
      | ageless_metabolism   | annually  | platinum         | buy                  | 3          | most_popular       | 1          | most_popular       |
      | ageless_skin         | annually  | platinum         | no                   | 1          | most_popular       | no         | upgrade            |


