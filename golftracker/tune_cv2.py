'''
Tune the parameters of cv2 for better detection
'''

def detect_line(frame, point):
    CannyEdgeDetector ce(1);
    HoughLineDetector hl(1);

    (x1, y1), (x2, y2) = geom.create_roi(point)
    roi = frame[y1:y2, x1:x2]

    ntries = 100
    for i in range(ntries):
        c_frame = ce.process(0, frame)
        lines = hl.process(0, c_frame)

        for line in lines:
            if geom.is_point_on_line(point, line, 10):
                break
            else:
                ce.param_lst[0].canny_threshold1 += 