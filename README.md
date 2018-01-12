# 📹 foggycam

![Foggycam logo](foggycam-logo.png)

(_Icon derivative from the [work of Steven Kuiper](https://www.iconfinder.com/icons/408402/camera_icon#size=256)_)

📹  A tool to capture Nest video streams locally, without having to pay for Nest Aware. The current release is tested on macOS. Windows and Linux adaptations coming soon (minor tweaks required).

>**NOTE:** Worth noting that we don't yet support audio recording, due to the fact that only the visual stream is captured.

## How To Configure

Make sure you rename `_config.json` to `config.json` and specify the following parameters:

|Parameter|Description|
|-----|-----|
|`username`|Nest account username.|
|`password`|Nest account password.|
|`path`|Absolute path to local folder where content needs to be stored.<br/><br/>Default is the script path.|
|`frame_rate`|Frame rate for the generated video.<br/><br/>Default is 24.|
|`width`|Image width for the capture image.<br/><br/>Default is 1280.|
|`clear_images`|Determines whether images are removed after video is produced.<br/><br/>Default is false.|
|`produce_video`|Determines whether a video is generated after a threshold of captured images is hit.<br/><br/>Default is false.|

In addition to the above, **if you want to capture video**, you will need to [download `ffmpeg`](https://www.ffmpeg.org/download.html) and place it in the `tools` folder, in the script root folder.

## How To Start

Run `python start.py` after you configured the settings above. Exit by pressing <kbd>Ctrl</kbd>+<kbd>C</kbd>.

## Disclaimer

I do not make any claims regarding the stability of the application, or its applicability for your own purposes. Use at your own risk. Code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

**DO NOT USE** in critical security/surveillance scenarios.
