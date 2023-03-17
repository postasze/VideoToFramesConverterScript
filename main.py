# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from multiprocessing import Pool
import cv2


def process(arg):
    path_to_video = arg
    vidcap = cv2.VideoCapture(path_to_video)
    path_to_save = path_to_video[:-4]
    os.makedirs(path_to_save, exist_ok=True)
    count = 0
    while vidcap.isOpened():
        count += 1
        success, image = vidcap.read()
        cv2.imwrite(f"{path_to_save}/frame%d.png" % count, image)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    videos_list = []
    masks_list = []
    for root in os.walk('./Videos_to_convert'):
        for files in root[2]:
            videos_list.append(f'{root[0]}/{files}')
    masks_list.sort()
    videos_list.sort()

    pool = Pool(16)
    results = pool.map(process, videos_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
