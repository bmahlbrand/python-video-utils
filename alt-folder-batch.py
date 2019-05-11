from moviepy.editor import *

import glob

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', type=int, default=0, help='start frame')
parser.add_argument('--fps', type=int, default=28, help='frames per second')

parser.add_argument('--path', type=str, default='', help='folder path for input images', required=True)
parser.add_argument('--output', type=str, default='output.mp4', help='path for output video')

args = parser.parse_args()

imagePaths = list(glob.glob(args.path + '/*.png'))
imagePaths.sort(key = os.path.getctime)

# print(imagePaths)

clips = [ImageClip(m).set_duration(1.0 / args.fps) for m in imagePaths]

concat_clip = concatenate_videoclips(clips, method="compose")
concat_clip.write_videofile(args.output, fps=args.fps)