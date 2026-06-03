Feature: Disclaimer tests

  @disclaimer @WIP
  Scenario: Bulk verification of disclaimer text across Opt-in pages
    Given the target URLs are loaded from "data/Opt-in.csv"
    Then the corresponding disclaimers should be verified on all loaded pages
