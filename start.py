"""Module to start FoggyCam processing."""

import json
from foggycam import FoggyCam

print 'Welcome to FoggyCam 1.0 - Nest video/image capture tool'

CONFIG = json.load(open('config.json'))

CAM = FoggyCam(username=CONFIG['username'], password=CONFIG['password'])
CAM.capture_images(produce_video=True, clear_images=True, custom_path=CONFIG['path'], frame_rate=CONFIG['frame_rate'], width=CONFIG['width'])
