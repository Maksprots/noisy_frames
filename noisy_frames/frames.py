import cv2
import numpy as np
import conf


class Frames:
    def __init__(self, video):
        self.video = cv2.VideoCapture(video)
        self.nuber_frames = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
        self.fps = int(self.video.get(cv2.CAP_PROP_FPS)) +1
        self.__lst_frames =[]

    def get_brightness_list(self):
        assert self.nuber_frames, conf.t_conf.opn_err

        self.bright_each_cadr = []
        cadr = self.video.read()[1]
        for fr in range(1, self.nuber_frames-1):
            self.__lst_frames.append(cadr)
            self.bright_each_cadr.append(np.sum(cadr))
            cadr = self.video.read()[1]
        return self.bright_each_cadr

    def get_lst_frames(self):
        if len(self.__lst_frames) == 0:
            self.get_brightness_list()
        return self.__lst_frames

