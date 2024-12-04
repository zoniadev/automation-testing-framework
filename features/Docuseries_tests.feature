Feature: Funnel tests

  @unbroken
  Scenario Outline: Unbroken funnel
    Given user register in "Unbroken" Opt In page
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
      | quarterly | platinum         | buy                  | 3          | no                 | 1          | no                 |
      | monthly   | silver           | no                   | 1          | upgrade            | 1          | upgrade            |
      | annually  | no               | no                   | 3          | most_popular       | no         | no                 |
      | monthly   | no               | buy                  | 3          | upgrade            | 6          | most_popular       |
      | annually  | silver           | no                   | no         | no                 | 1          | most_popular       |
      | quarterly | silver           | buy                  | 3          | most_popular       | 3          | upgrade            |
      | quarterly | no               | no                   | 6          | no                 | 1          | upgrade            |
      | annually  | platinum         | buy                  | 1          | upgrade            | no         | no                 |
      | monthly   | silver           | buy                  | 6          | most_popular       | no         | no                 |
      | monthly   | platinum         | no                   | 1          | no                 | 3          | most_popular       |
      | monthly   | no               | buy                  | no         | no                 | 3          | no                 |
      | quarterly | platinum         | no                   | no         | no                 | 6          | upgrade            |
      | annually  | platinum         | no                   | 6          | most_popular       | 6          | most_popular       |
      | annually  | no               | no                   | 6          | upgrade            | 3          | upgrade            |
      | quarterly | no               | no                   | 1          | most_popular       | 1          | most_popular       |
      | quarterly | silver           | no                   | 1          | upgrade            | 6          | no                 |
      | quarterly | no               | buy                  | no         | no                 | no         | no                 |


  @ageless
  Scenario Outline: Ageless Evergreen funnel
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
      | <rd_bottles> | <rd_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | opt_in_page          | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | ageless              | quarterly | platinum         | buy                  | 3          | no                 | 1          | no                 |
      | ageless_metabolism   | monthly   | silver           | no                   | 1          | upgrade            | 1          | upgrade            |
      | ageless_skin         | annually  | no               | no                   | 3          | most_popular       | no         | no                 |
      | ageless_exercise     | monthly   | no               | buy                  | 3          | upgrade            | 6          | most_popular       |
      | ageless_brain        | annually  | silver           | no                   | no         | no                 | 1          | most_popular       |
      | ageless_hormones     | quarterly | silver           | buy                  | 3          | most_popular       | 3          | upgrade            |
      | ageless_energy       | quarterly | no               | no                   | 6          | no                 | 1          | upgrade            |
      | ageless_inflammation | annually  | platinum         | buy                  | 1          | upgrade            | no         | no                 |
      | ageless_bones        | monthly   | silver           | buy                  | 6          | most_popular       | no         | no                 |
      | ageless              | monthly   | platinum         | no                   | 1          | no                 | 3          | most_popular       |
      | ageless_metabolism   | monthly   | no               | buy                  | no         | no                 | 3          | no                 |
      | ageless_skin         | quarterly | platinum         | no                   | no         | no                 | 6          | upgrade            |
      | ageless_exercise     | annually  | platinum         | no                   | 6          | most_popular       | 6          | most_popular       |
      | ageless_brain        | annually  | no               | no                   | 6          | upgrade            | 3          | upgrade            |
      | ageless_hormones     | quarterly | no               | no                   | 1          | most_popular       | 1          | most_popular       |
      | ageless_energy       | quarterly | silver           | no                   | 1          | upgrade            | 6          | no                 |
      | ageless_inflammation | quarterly | no               | buy                  | no         | no                 | no         | no                 |


  @bb
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
      | opt_in_page | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | bb          | quarterly | platinum         | buy                  | 3          | no                 | 1          | no                 |
      | bb_detox    | monthly   | silver           | no                   | 1          | upgrade            | 1          | upgrade            |
      | bb_gut      | annually  | no               | no                   | 3          | most_popular       | no         | no                 |
      | bb_memory   | monthly   | no               | buy                  | 3          | upgrade            | 6          | most_popular       |
      | bb_mood     | annually  | silver           | no                   | no         | no                 | 1          | most_popular       |
      | bb_sleep    | quarterly | silver           | buy                  | 3          | most_popular       | 3          | upgrade            |
      | bb_energy   | quarterly | no               | no                   | 6          | no                 | 1          | upgrade            |
      | bb_immunity | annually  | platinum         | buy                  | 1          | upgrade            | no         | no                 |
      | bb          | monthly   | silver           | buy                  | 6          | most_popular       | no         | no                 |
      | bb_detox    | monthly   | platinum         | no                   | 1          | no                 | 3          | most_popular       |
      | bb_gut      | monthly   | no               | buy                  | no         | no                 | 3          | no                 |
      | bb_memory   | quarterly | platinum         | no                   | no         | no                 | 6          | upgrade            |
      | bb_mood     | annually  | platinum         | no                   | 6          | most_popular       | 6          | most_popular       |
      | bb_sleep    | annually  | no               | no                   | 6          | upgrade            | 3          | upgrade            |
      | bb_energy   | quarterly | no               | no                   | 1          | most_popular       | 1          | most_popular       |
      | bb_immunity | quarterly | silver           | no                   | 1          | upgrade            | 6          | no                 |
      | bb          | quarterly | no               | buy                  | no         | no                 | no         | no                 |
