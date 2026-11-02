Feature: Video playability tests

  @video_playback
  Scenario Outline: Verify playback of key videos
    Given user log in Zonia portal
    And user navigates to the "<video_title>" video page
    When user initiates the video play
    Then the video player is loaded on the page
    And the video is actively playing
    And the media stream network requests are successful

    Examples:
      | video_title                  |
      | AAC - Understanding Your Aging Trajectory  |
      | AAC - The Ultimate Diet for Aging Gracefully |
      | Cancer 360 - Comprehensive Protocol for Breast Self-Exam  |
