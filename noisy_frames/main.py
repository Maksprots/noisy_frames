import cv2
import numpy as np
import statistics
import conf
import frames
import chooser

import time
from tqdm import tqdm


def deliting(lst_fr, cadr_to_dl):
    new = []
    for i in range(len(lst_fr)):
        flag = False
        for dl in cadr_to_dl:
            if i == dl:
                flag = True
        if not flag:
            new.append(lst_fr[i])
    return new


def save_from_frames(list, fps):


    file = cv2.VideoWriter(conf.t_conf.out,
                           cv2.VideoWriter_fourcc(*'mp4v'),
                           fps,
                           (1920, 1080))
    for frame in list:
        file.write(frame)
    file.release()


frames = frames.Frames(conf.t_conf.t_video)


chooser = chooser.Chooser(frames.get_brightness_list(), conf.t_conf.deviation)

if conf.t_conf.METHOD:
    cadr_to_dl = chooser.del_list_brm(
        conf.t_conf.averege_for_frames,
        frames.nuber_frames)

    list_fr = frames.get_lst_frames()

    new = deliting(list_fr, cadr_to_dl)

    save_from_frames(new,
                 frames.fps)

else:
    list_fr = frames.get_lst_frames()
    bad= chooser.del_list_dif(list_fr)

    new =deliting(list_fr, bad)
    save_from_frames(new, frames.fps)
