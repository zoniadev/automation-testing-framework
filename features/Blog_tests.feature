Feature: Blog tests

  @blog
  Scenario Outline: Verify banners redirects
    Given Verify banners redirects in "<dropdown>" and "<dropdown_category>"

    Examples:
      | dropdown | dropdown_category  |
      | health   | 'Organs & Systems' |