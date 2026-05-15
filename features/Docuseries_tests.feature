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
      | outline | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
      | 6       | annually  | no               | buy                  | no         | upgrade            | 6          | most_popular       |
      | 7       | quarterly | platinum         | buy                  | 3          | most_popular       | 1          | best_value         |


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
      | outline | opt_in_page        | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | ad_ev              | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | ad_ev_detox        | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | ad_ev_gut          | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | ad_ev_brain        | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | ad_ev_mindset      | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
      | 6       | ad_ev_inflammation | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | ad_ev_energy       | quarterly | platinum         | no                   | 3          | no                 | no         | upgrade            |
      | 8       | ad_ev_pain         | monthly   | silver           | buy                  | 6          | most_popular       | 3          | most_popular       |
      | 9       | ad_ev              | annually  | platinum         | buy                  | 3          | best_value         | 1          | best_value         |


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
      | outline | opt_in_page      | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | bb_live          | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | bb_live_detox    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | bb_live_gut      | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | bb_live_memory   | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | bb_live_mood     | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | bb_live_sleep    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | bb_live_energy   | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | bb_live_immunity | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | bb_live          | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |

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
      | outline | opt_in_page    | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | bb_ev          | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | bb_ev_detox    | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | bb_ev_gut      | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | bb_ev_memory   | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | bb_ev_mood     | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | bb_ev_sleep    | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | bb_ev_energy   | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | bb_ev_immunity | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | bb_ev          | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |



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
      | outline | opt_in_page        | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | lg_ev              | monthly   | no               | no                   | no         | no                 | no         | no                 | 
      | 2       | lg_ev_metabolism   | quarterly | no               | no                   | no         | no                 | no         | upgrade            | 
      | 3       | lg_ev_skin         | annually  | no               | no                   | no         | no                 | 1          | no                 | 
      | 4       | lg_ev_exercise     | monthly   | no               | no                   | no         | upgrade            | no         | no                 | 
      | 5       | lg_ev_brain        | quarterly | no               | no                   | 6          | no                 | no         | no                 | 
      | 6       | lg_ev_hormones     | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | lg_ev_energy       | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | lg_ev_inflammation | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            | 
      | 9       | lg_ev_bones        | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


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
      | outline | opt_in_page          | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | lg_live              | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | lg_live_metabolism   | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | lg_live_skin         | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | lg_live_exercise     | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | lg_live_brain        | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | lg_live_hormones     | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | lg_live_energy       | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | lg_live_inflammation | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | lg_live_bones        | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @km_live @all_docuseries
  Scenario Outline: KM Live funnel
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
      | outline | opt_in_page     | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | km_live         | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | km_live_toxins  | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | km_live_sleep   | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | km_live_gut     | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | km_live_adhd    | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | km_live_mystery | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | km_live_mood    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | km_live_autism  | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | km_live         | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @km_evergreen @all_docuseries
  Scenario Outline: KM Evergreen funnel
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
      | outline | opt_in_page   | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | km_ev         | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | km_ev_toxins  | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | km_ev_sleep   | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | km_ev_gut     | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | km_ev_focus   | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | km_ev_mystery | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | km_ev_mood    | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | km_ev_autism  | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | km_ev         | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


#  @is_live @all_docuseries
#  Scenario Outline: IS Live funnel
#    Given user register in "<opt_in_page>" Opt In page
#    And user join Zonia
#    When user sign up for "<plan>" plan
#    And user makes following decision in docuseries "Booster Packages" Upsell page
#      | decision           |
#      | <booster_packages> |
#    And user makes following decision in docuseries "Masterclass Packages" Upsell page
#      | decision               |
#      | <masterclass_packages> |
#    And user makes following decision in docuseries "Restore Life" Upsell page
#      | bottles      | upsell_downsell      |
#      | <rl_bottles> | <rl_upsell_downsell> |
#    And user makes following decision in docuseries "Restore Detox" Upsell page
#      | bottles      | upsell_downsell      |
#      | <rd_bottles> | <rd_upsell_downsell> |
#    Then user complete registration
#
#    Examples:
#      | opt_in_page          | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rd_bottles | rd_upsell_downsell |
#      | is_live              | annually  | platinum         | no                   | 1          | upgrade            | no         | upgrade            |
#      | is_live_brain        | annually  | silver           | buy                  | 6          | no                 | 3          | no                 |
#      | is_live_cancer       | monthly   | no               | buy                  | 3          | most_popular       | 1          | most_popular       |
#      | is_live_autoimmunity | lifetime  | silver           | buy                  | no         | upgrade            | 6          | best_value         |
#      | is_live_gut          | annually  | no               | no                   | 1          | best_value         | 6          | most_popular       |
#      | is_live_heart        | lifetime  | silver           | no                   | 1          | most_popular       | 1          | no                 |
#      | is_live_obesity      | monthly   | no               | buy                  | no         | no                 | 3          | upgrade            |
#      | is_live_trauma       | quarterly | platinum         | buy                  | 3          | most_popular       | no         | no                 |
#      | is_live              | quarterly | platinum         | no                   | 6          | best_value         | 1          | best_value         |
#      | is_live_brain        | quarterly | no               | buy                  | 6          | most_popular       | 6          | upgrade            |
#      | is_live_cancer       | annually  | no               | no                   | 3          | most_popular       | 3          | best_value         |
#      | is_live_autoimmunity | monthly   | platinum         | buy                  | 6          | upgrade            | 3          | most_popular       |
#      | is_live_gut          | lifetime  | silver           | no                   | 3          | no                 | 6          | most_popular       |
#      | is_live_heart        | lifetime  | silver           | buy                  | 3          | best_value         | 3          | upgrade            |
#      | is_live_obesity      | annually  | platinum         | buy                  | no         | upgrade            | 1          | upgrade            |
#      | is_live_trauma       | monthly   | silver           | buy                  | 1          | best_value         | 6          | no                 |
#      | is_live              | lifetime  | no               | buy                  | 6          | best_value         | no         | no                 |
#      | is_live_brain        | quarterly | platinum         | no                   | no         | no                 | no         | no                 |
#      | is_live_cancer       | quarterly | silver           | no                   | 1          | upgrade            | 3          | most_popular       |
#      | is_live_autoimmunity | monthly   | no               | buy                  | 3          | upgrade            | no         | no                 |
#      | is_live_gut          | lifetime  | platinum         | no                   | no         | no                 | 1          | most_popular       |
#      | is_live_heart        | monthly   | platinum         | buy                  | 1          | no                 | 6          | best_value         |
#      | is_live_obesity      | annually  | silver           | no                   | no         | no                 | no         | upgrade            |


  @is_evergreen @all_docuseries
  Scenario Outline: IS Evergreen funnel
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
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | opt_in_page        | plan      | booster_packages | masterclass_packages | rl_bottles | rl_upsell_downsell | rs_bottles | rs_upsell_downsell |
      | 1       | is_ev              | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | is_ev_brain        | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | is_ev_cancer       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | is_ev_autoimmunity | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | is_ev_gut          | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | is_ev_heart        | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | is_ev_obesity      | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | is_ev_trauma       | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | is_ev              | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @tf_evergreen @all_docuseries
  Scenario Outline: TF Evergreen funnel
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
      | outline | opt_in_page          | plan      | booster_packages | masterclass_packages | rd_bottles | rd_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | tf_ev                | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | tf_ev_meals          | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | tf_ev_detoxification | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | tf_ev_autoimmunity   | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | tf_ev_cancer         | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | tf_ev_liver          | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | tf_ev_hormones       | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | tf_ev_allergies      | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | tf_ev                | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @twl_evergreen @all_docuseries
  Scenario Outline: TWL Evergreen regular funnel
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
      | outline | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
      | 6       | annually  | no               | buy                  | no         | upgrade            | 6          | most_popular       |
      | 7       | quarterly | platinum         | buy                  | 3          | most_popular       | 1          | best_value         |


  @twl_evergreen @all_docuseries
  Scenario Outline: TWL Evergreen direct funnel
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
      | outline | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | quarterly | no               | no                   | 1          | upgrade            | no         | no                 |
      | 6       | annually  | no               | buy                  | no         | upgrade            | 6          | most_popular       |
      | 7       | quarterly | platinum         | buy                  | 3          | most_popular       | 1          | best_value         |


  @cr_live @all_docuseries
  Scenario Outline: CR Live funnel
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
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | opt_in_page          | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | cr_live              | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | cr_live_immune       | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | cr_live_toxins       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | cr_live_female       | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | cr_live_emotions     | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | cr_live_inflammation | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | cr_live_stress       | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | cr_live_obesity      | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | cr_live              | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @cr_screening @all_docuseries
  Scenario Outline: CR Live screening funnel
    Given user is on the "cr_live" episode "<episode>" page
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
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | episode | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | annually  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | monthly   | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | annually  | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 10      | quarterly | no               | buy                  | 6          | most_popular       | 6          | upgrade            |
      | 11      | annually  | no               | no                   | 3          | most_popular       | 3          | best_value         |
      | 12      | monthly   | platinum         | buy                  | 6          | upgrade            | 3          | most_popular       |


  @cr_evergreen @all_docuseries
  Scenario Outline: CR Evergreen funnel
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
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | opt_in_page   | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | cr_ev         | monthly   | no               | no                   | no         | no                 | no         | no                 |
      | 2       | cr_ev_immune  | quarterly | no               | no                   | no         | no                 | no         | upgrade            |
      | 3       | cr_ev_toxins  | annually  | no               | no                   | no         | no                 | 1          | no                 |
      | 4       | cr_ev_female  | monthly   | no               | no                   | no         | upgrade            | no         | no                 |
      | 5       | cr_ev_trauma  | quarterly | no               | no                   | 6          | no                 | no         | no                 |
      | 6       | cr_ev_aging   | lifetime  | no               | buy                  | no         | upgrade            | 6          | best_value         |
      | 7       | cr_ev_stress  | annually  | platinum         | no                   | 1          | best_value         | no         | upgrade            |
      | 8       | cr_ev_obesity | quarterly | platinum         | no                   | 3          | upgrade            | 3          | upgrade            |
      | 9       | cr_ev         | quarterly | silver           | buy                  | 3          | most_popular       | 1          | most_popular       |


  @cr_1ep @all_docuseries
  Scenario Outline: CR 1 episode funnel
    Given user register in "<opt_in_page>" Opt In page
    And user join Zonia in 1 episode page
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
    And user makes following decision in docuseries "Restore Life" Upsell page
      | bottles      | upsell_downsell      |
      | <rl_bottles> | <rl_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | opt_in_page    | plan      | booster_packages | masterclass_packages | rs_bottles | rs_upsell_downsell | rl_bottles | rl_upsell_downsell |
      | 1       | cr_1ep         | annually  | platinum         | no                   | 1          | upgrade            | no         | upgrade            |
      | 2       | cr_1ep_immune  | annually  | silver           | buy                  | 6          | no                 | 3          | no                 |
      | 3       | cr_1ep_toxins  | monthly   | no               | buy                  | 3          | most_popular       | 1          | most_popular       |
      | 4       | cr_1ep_female  | lifetime  | silver           | buy                  | no         | upgrade            | 6          | best_value         |
      | 5       | cr_1ep_trauma  | annually  | no               | no                   | 1          | best_value         | 6          | most_popular       |
      | 6       | cr_1ep_aging   | lifetime  | silver           | no                   | 1          | most_popular       | 1          | no                 |
      | 7       | cr_1ep_stress  | monthly   | no               | no                   | no         | no                 | 3          | upgrade            |
      | 8       | cr_1ep_obesity | quarterly | platinum         | buy                  | 3          | most_popular       | no         | no                 |


  @pc_live @all_docuseries
  Scenario Outline: Patient Care funnel
    Given user is on the Patient Care sales page
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | plan      | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell |
      | 1       | monthly   | no         | no                 | no         | no                 |
      | 3       | annually  | no         | no                 | 1          | no                 |
      | 4       | lifetime  | no         | no                 | 3          | upgrade            |
      | 5       | quarterly | 1          | upgrade            | no         | no                 |
      | 6       | annually  | 6          | no                 | 6          | no                 |
      | 7       | quarterly | 3          | upgrade            | 1          | upgrade            |


  @face_scan @all_docuseries
  Scenario Outline: Face Scan funnel
    Given user fills face scan form with
      | height   | weight   | smoke   | blood_pressure   | diabetic   | age   | gender   |
      | <height> | <weight> | <smoke> | <blood_pressure> | <diabetic> | <age> | <gender> |
    And user join Zonia
    When user sign up for "<plan>" plan
    And user makes following decision in docuseries "Restore Sleep" Upsell page
      | bottles      | upsell_downsell      |
      | <rs_bottles> | <rs_upsell_downsell> |
    And user makes following decision in docuseries "Restore Detox" Upsell page
      | bottles      | upsell_downsell      |
      | <rd_bottles> | <rd_upsell_downsell> |
    Then user complete registration

    Examples:
      | outline | plan      | rs_bottles | rs_upsell_downsell | rd_bottles | rd_upsell_downsell | height | weight | smoke | blood_pressure | diabetic | age | gender |
      | 1       | monthly   | no         | no                 | no         | no                 | 175    | 72     | Yes   | Yes            | Type 2   | 37  | male   |
      | 2       | quarterly | no         | no                 | no         | upgrade            | 165    | 60     | No    | No             | No       | 28  | female |
      | 3       | annually  | no         | no                 | 1          | no                 | 180    | 85     | No    | Yes            | Type 1   | 45  | male   |
      | 4       | lifetime  | no         | upgrade            | no         | no                 | 160    | 55     | Yes   | No             | No       | 30  | female |
      | 5       | quarterly | 1          | upgrade            | no         | no                 | 170    | 70     | No    | No             | Type 2   | 50  | male   |
      | 6       | annually  | no         | upgrade            | 6          | most_popular       | 155    | 50     | No    | Yes            | No       | 60  | female |
      | 7       | quarterly | 3          | most_popular       | 1          | best_value         | 185    | 90     | Yes   | No             | Type 1   | 40  | male   |
