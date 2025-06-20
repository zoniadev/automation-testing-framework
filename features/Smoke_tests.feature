Feature: Smoke tests

  @smoke
  Scenario Outline: Verify buttons redirects
    Given Verify "<element>" button/s on "<url>" page navigate to "<expected_redirect>"

    Examples:
      | element           | url                       | expected_redirect |
      | JOIN_ZONIA_BUTTON | tf-join-zonia             | tf-signup         |
      | JOIN_ZONIA_BUTTON | tf-join-zonia-2           | tf-signup         |
      | JOIN_ZONIA_BUTTON | tf-join-zonia-fb          | tf-signup         |
      | JOIN_ZONIA_BUTTON | tf-join-zonia-expired     | tf-signup         |
      | JOIN_ZONIA_BUTTON | mb2/tf-join-zonia         | tf-signup         |
      | JOIN_ZONIA_BUTTON | mb2/tf-join-zonia-2       | tf-signup         |
      | JOIN_ZONIA_BUTTON | mb2/tf-join-zonia-fb      | tf-signup         |
      | JOIN_ZONIA_BUTTON | mb2/tf-join-zonia-expired | tf-signup         |
      | JOIN_ZONIA_BUTTON | ad-join-zonia             | ad-signup         |
      | JOIN_ZONIA_BUTTON | ad-join-zonia-2           | ad-signup         |
      | JOIN_ZONIA_BUTTON | ad-join-zonia-fb          | ad-signup         |

  @smoke
  Scenario Outline: Verify buttons scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element                      | url             | target_element            |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-detox        | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-gut-health   | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-brain-health | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-mindset      | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-inflammation | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-energy       | FIRST_NAME_REGISTER_FIELD |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-pain-relief  | FIRST_NAME_REGISTER_FIELD |

  @smoke @quick
  Scenario Outline: Verify arrows scrolling
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element             | url                         | target_element |
      | SCROLL_ARROW_BUTTON | ad-booster-packages-monthly | scroll_down    |

  @fast
  Scenario Outline: Verify buttons scrolling fast test
    Given Verify "<element>" scrolling to "<target_element>" on "<url>" page

    Examples:
      | element                      | url      | target_element            |
      | REGISTER_FOR_FREE_NOW_BUTTON | ad-detox | FIRST_NAME_REGISTER_FIELD |

