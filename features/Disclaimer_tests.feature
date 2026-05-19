Feature: Disclaimer tests

  @disclaimer @WIP
  Scenario: Bulk verification of disclaimer text across Opt-in pages
    Given the target URLs are loaded from "data/Opt-in.csv"
    Then the following disclaimer text should be verified on all loaded pages:
      """
      By clicking "Register for Free Now" you agree to receive marketing emails from Zonia about products, events, and promotions. You may unsubscribe at any time. By proceeding with the registration, you agree to our Privacy Policy.
      """
