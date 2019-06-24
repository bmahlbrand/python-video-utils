from moviepy.editor import *

import glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='start frame')
parser.add_argument('--fps', type=int, default=28, help='frames per second')

parser.add_argument('--path', type=str, default='', help='input video', required=True)
parser.add_argument('--output', type=str, default='output.mp4', help='path for output video')

args = parser.parse_args()

clip = VideoFileClip(args.path)

clip.write_gif(args.output)