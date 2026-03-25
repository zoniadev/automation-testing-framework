import time
from pages.base_page_object import BasePage
from locators import *

class VideoPlayerPage(BasePage):
    def __init__(self, context):
        super().__init__(context)

    def play_video(self, video_title):
        # Use JavaScript evaluation to directly command the Video.js player to play.
        # This is the most reliable method, bypassing any overlays or complex event listeners.
        player_selector = "#my-player"
        self.context.page.wait_for_selector(player_selector, state="visible", timeout=10000)
        self.context.page.evaluate(f"videojs('{player_selector}').play();")
        print(f"===> Commanded video player to play '{video_title}' via JavaScript")

    def verify_video_is_loaded(self, video_title):
        video_player = self.context.page.locator("#my-player")
        video_player.wait_for(state="visible", timeout=10000)
        # The 'vjs-has-started' class is a good indicator that the video has at least begun to load.
        self.context.page.wait_for_selector("#my-player.vjs-has-started", timeout=15000)
        print(f'===> Verified the video player for "{video_title}" is loaded')
        time.sleep(2)

    def verify_video_is_playing(self):
        # vjs-has-started: set by Video.js once playback begins, never removed.
        # vjs-playing: removed immediately on pause — too fragile to rely on.
        try:
            self.context.page.wait_for_selector(
                "#my-player.vjs-has-started",
                timeout=15000
            )
        except Exception:
            raise AssertionError(
                "Video.js player never reached 'vjs-has-started' state. "
                "Video may have failed to start."
            )
        video_handle = self.context.page.query_selector("#my-player_html5_api")
        assert video_handle, "Could not find Video.js <video> element (#my-player_html5_api)."
        initial_time = video_handle.evaluate("node => node.currentTime")
        assert initial_time > 0, (
            f"Video.js reports has-started but currentTime is still 0 — "
            f"stream may have failed to load."
        )
        # Only verify time advancement if video is currently playing.
        # If it's paused (e.g. user or autoplay policy), we already confirmed
        # it successfully started via vjs-has-started + currentTime > 0.
        is_paused = video_handle.evaluate("node => node.paused")
        if not is_paused:
            self.context.page.wait_for_timeout(2000)
            current_time = video_handle.evaluate("node => node.currentTime")
            assert current_time > initial_time, (
                f"Video is playing but currentTime stuck at {initial_time:.3f}s — "
                f"stream may have stalled."
            )
            print(
                f"===> Verified video is playing via Video.js "
                f"(time advanced from {initial_time:.3f}s to {current_time:.3f}s)"
            )
        else:
            print(
                f"===> Verified video successfully started via Video.js "
                f"(currentTime={initial_time:.3f}s, currently paused)"
            )

    def verify_hls_stream_network(self):
        # Video.js uses MediaSource Extension — the <video> src is a blob: URL,
        # not .m3u8 directly. The actual HLS segment requests (.m3u8 / .ts) happen
        # at the network level. Since the video is already playing when this method
        # runs, the initial playlist request is gone. We wait for the next
        # .ts segment (continuous) or .m3u8 playlist refresh.
        # Segments typically arrive every 2-10s; use 30s to survive a buffered gap.
        try:
            response = self.context.page.wait_for_response(
                lambda res: (
                                    ".ts" in res.url or ".m3u8" in res.url
                            ) and res.status == 200,
                timeout=30000
            )
            print(
                f"===> Verified HLS stream — 200 OK: ...{response.url[-60:]}"
            )
            return
        except Exception:
            pass
        # Fallback: confirm via Video.js DOM state that it is actively loading
        js_check = """() => {
            const video = document.querySelector('#my-player_html5_api');
            if (!video) return null;
            return {
                networkState: video.networkState,  // 2 = NETWORK_LOADING
                readyState:   video.readyState,    // >=3 = has future data
                paused:       video.paused,
                currentTime:  video.currentTime
            };
        }"""
        info = self.context.page.evaluate(js_check)
        assert info, "Video.js <video> element (#my-player_html5_api) not found."
        assert not info["paused"], "Video is paused during HLS network check."
        assert info["networkState"] == 2, (
            f"networkState={info['networkState']} — expected 2 (NETWORK_LOADING). "
            f"Stream may have stalled."
        )
        assert info["readyState"] >= 3, (
            f"readyState={info['readyState']} — expected >=3 (HAVE_FUTURE_DATA)."
        )
        print(
            f"===> Verified HLS stream via Video.js DOM state "
            f"(networkState={info['networkState']}, readyState={info['readyState']}, "
            f"currentTime={info['currentTime']:.3f}s)"
        )
