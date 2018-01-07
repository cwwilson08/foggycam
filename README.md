# foggycam

![Foggycam logo](foggycam-logo.png)

📹  A tool to capture Nest video streams locally, without having to pay for Nest Aware.

## How To Configure

Make sure you rename `_config.json` to `config.json` and add your Nest username and password to the file.

In `start.py`, additional configuration can be made to the `cam.captureImages` call. The following parameters can be specified:

- `produce_video` (**Boolean**) - determines whether a video is generated from the captured images. Default value is `False`.
- `clear_images` (**Boolean**) - if a video is being generated, determines whether images are being deleted after the video is generated. Default value is `False`.
- `custom_path` (**String**) - an absolute path to a local location (folder) where captured content should be stored. If left out, the default will be the location of the script.
- `width` (**Integer**) - the width of captured images. Default value is 1280.

## Disclaimer

I do not make any claims regarding the stability of the application, or its applicability for your own purposes. Use at your own risk. Code is licensed under the [MIT License](https://opensource.org/licenses/MIT).

**DO NOT USE** in critical security/surveillance scenarios.