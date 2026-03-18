from pages.base_page_object import BasePage
from locators import *

class VideoPlayerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)
        self.video_locator = self.context.page.locator(VIDEO_ELEMENT)

    def play_video(self):
        # Locates the specific 'start watching' button
        play_btn = self.context.page.locator(PLAY_VIDEO_BUTTON).first
        play_btn.wait_for(state="visible", timeout=5000)
        play_btn.click()
        print('===> Clicked the Play button to initiate video')

    def verify_video_is_loaded(self):
        """Waits for the video element to have enough data to begin playback."""
        self.video_locator.wait_for(state="attached", timeout=10000)
        # readyState 3 (HAVE_FUTURE_DATA) or 4 (HAVE_ENOUGH_DATA)
        self.page.wait_for_function("document.querySelector('video').readyState >= 3")

    def verify_video_is_playing(self):
        """Verifies the video is not paused and the playback time is advancing."""
        # 1. Check native paused property
        is_paused = self.video_locator.evaluate("node => node.paused")
        if is_paused:
            raise AssertionError("The video player is currently paused.")

        # 2. Check if currentTime advances over a 2-second interval
        initial_time = self.video_locator.evaluate("node => node.currentTime")
        self.page.wait_for_timeout(2000)
        current_time = self.video_locator.evaluate("node => node.currentTime")

        if current_time <= initial_time:
            raise AssertionError(f"Video is not playing. Playback stuck at {initial_time} seconds.")

    def verify_hls_stream_network(self):
        """Monitors network traffic to ensure HLS playlist/chunks are downloading."""
        # Intercepts successful HTTP 200 responses for .m3u8 or .ts files
        response = self.context.page.wait_for_response(
            lambda res: (".m3u8" in res.url or ".ts" in res.url) and res.status == 200,
            timeout=10000
        )
        if not response:
            raise AssertionError("No active HLS media stream network requests detected.")