#!/usr/bin/env python
import freenect
import matplotlib.pyplot as mp
import signal
import frame_convert
k = Kinect()
k.getImage().show()
Image(k.getDepthMatrix(), cv2image=True).show()