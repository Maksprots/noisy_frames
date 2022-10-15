import conf
import cv2

def video_to_frames():
    video_сapture = cv2.VideoCapture(conf.t_conf.t_video)
    # fps = video_сapture.get(cv2.CAP_PROP_FPS)
    frames = video_сapture.get(cv2.CAP_PROP_FRAME_COUNT)
    for i in range(int(frames)):
        frame = video_сapture.read()[1]
        cv2.imwrite("out/%d.jpg" % i, frame)



