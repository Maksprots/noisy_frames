import cv2
import numpy as np
import statistics
import conf



class Chooser:
    def __init__(self, list_bright, deviation):
        self.med_bright = statistics.median(list_bright)
        self.abs_deviation = int(
            self.med_bright
            / 100) * deviation

        self.list_bright = list_bright

    def del_list_brm(self, avg_over_frames, nbr_of_fr):
        print('метод: отклонение кадра от средних значений ')
        del_frames = []
        for start in range(0, nbr_of_fr, avg_over_frames):
            pack = self.list_bright[start:
                                    start + avg_over_frames]
            if len(pack) == 0:
                break
            max_in_pack = np.max(pack)
            for each in range(len(pack)):
                if max_in_pack - self.list_bright[each + start] \
                        > self.abs_deviation:
                    del_frames.append(each + start)

        return del_frames

    def del_list_dif(self, list_frames):
        print("метод : отклонение разности яркостного канала")
        diferenses = []
        good_frame = cv2.cvtColor(list_frames[0],cv2.COLOR_BGR2GRAY)
        for i in range(1, len(list_frames)):

            gray = cv2.cvtColor(list_frames[i], cv2.COLOR_BGR2GRAY)
            diferenses.append(np.sum(cv2.absdiff(good_frame,gray)))

        bad = []
        for j in range(0, len(diferenses), conf.t_conf.averege_for_frames):
            if len(diferenses[j:])<10:
                break
            minf = np.min(diferenses[j:j+10])

            for i in range(j, j+10):
                if np.fabs(diferenses[i] -
                           minf) > conf.t_conf.dif_about_med*minf:
                    bad.append(i+1)

        return bad
