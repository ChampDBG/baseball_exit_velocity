import cv2
import glob
import os
from utils.file_io import check_dir
from utils.filename import get_basename_from_path

src_dir = "./videos/"
dst_dir = "./images/"
input_videos = glob.glob(src_dir, "*")

for input_video in input_videos:
    video_name = get_basename_from_path(input_video)
    dst_path = os.path.join(dst_dir, video_name)
    check_dir(dst_path)

    vidcap = cv2.VideoCapture(input_video)
    loaded, image = vidcap.read()
    counter = 0

    while loaded:
        savename = "{}_{:010d}.png".format(dst_path, counter)
        cv2.imwrite(savename, image)
        counter += 1
