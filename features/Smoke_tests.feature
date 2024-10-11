Feature: Smoke tests

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

  @smoke @WIP
  Scenario Outline: Verify arrows scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element             | url                                                   | target_element |
      | SCROLL_ARROW_BUTTON | https://staging.zonia.com/ad-booster-packages-monthly | scroll_down    |

