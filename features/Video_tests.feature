Feature: Video playability tests
  @WIP
  Scenario: Test
    Given user log in Zonia portal
    And user navigates to video "Break Away From Sugar"
    When user initiates the video play
    Then the video player is loaded on the page
    And the video is actively playing
    And the media stream network requests are successful