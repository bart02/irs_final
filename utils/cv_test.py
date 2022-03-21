from libs.CVProcessImage import CVProcessImage



im = CVProcessImage('clouds/1647866047.9190776.jpg')
rects = im.get_rects(im.blue_thresh)

print(rects)

