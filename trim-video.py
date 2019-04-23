from moviepy.editor import *
import sys

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='start frame')
parser.add_argument('--duration', type=int, default=30, help='number of frames', required=True)
parser.add_argument('--fps', type=int, default=28, help='frames per second')

parser.add_argument('--path', type=str, default='', help='path for input video', required=True)
parser.add_argument('--output', type=str, default='output.mp4', help='path for output video')

args = parser.parse_args()

video = VideoFileClip(args.path).subclip(args.start, args.start + args.duration)
video.write_videofile(args.output, fps=args.fps)
