Feature: Blog tests

  @blog
  Scenario Outline: Verify banners redirects
    Given Verify banners redirects in "<dropdown>" and "<dropdown_category>"

    Examples:
      | dropdown | dropdown_category  |
      | health   | 'Organs & Systems' |


  @blog @WIP
  Scenario: Verify banners in This Week articles
    Given Verify banners redirects in this week articles