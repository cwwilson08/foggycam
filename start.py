from foggycam import *
import json

print 'Welcome to FoggyCam 1.0 - Nest video/image capture tool'

config = json.load(open('config.json'))

cam = FoggyCam(username=config['username'],password=config['password'])
cam.captureImages(produce_video=True,clear_images=True,custom_path=config['path'],frame_rate=config['frame_rate'])
