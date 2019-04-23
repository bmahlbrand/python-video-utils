from moviepy.editor import *

import glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='start frame')
parser.add_argument('--fps', type=int, default=28, help='frames per second')

parser.add_argument('--path', type=str, default='', help='folder path for input images', required=True)
parser.add_argument('--output', type=str, default='output.mp4', help='path for output video')

args = parser.parse_args()

# clips = []

# for fn in glob.glob("*.png"):
#     clip = ImageClip(fn, duration=1./24.)
#     clips.append(clip)

# cc = CompositeVideoClip(clips)

ImageSequenceClip(args.path, fps=args.fps).write_videofile(args.output, fps=args.fps)