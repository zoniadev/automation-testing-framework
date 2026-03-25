Feature: Video playability tests

  @video_playback @WIP
  Scenario Outline: Verify playback of key videos
    Given user log in Zonia portal
    And user navigates to the "<video_title>" video page
    When user initiates the video play
    Then the video player is loaded on the page
    And the video is actively playing
    And the media stream network requests are successful

    Examples:
      | video_title                  |
      | First Hardcoded Video Title  |
      | Second Hardcoded Video Title |
      | Third Hardcoded Video Title  |
