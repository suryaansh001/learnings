import cv2
import matplotlib.pyplot as plt
import numpy as np
import time

img=cv2.imread('/home/sury/learning/computervision/image.png')
#converting to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Display the RGB image
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("RGB Image")
plt.imshow(rgb)
plt.axis('off')

# Display the grayscale image
plt.subplot(1, 2, 2)
plt.title("Grayscale Image")
plt.imshow(gray, cmap='gray')
plt.axis('off')

# # Show the plots
# plt.show()

orb=cv2.ORB_create()
keypoints,descriptors=orb.detectAndCompute(gray,None)

#draw the keypoints on the image
im2=cv2.drawKeypoints(img,keypoints,None,color=(0,255,0),flags=0)
# Display the image with keypoints
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Keypoints")
plt.imshow(im2)
plt.show()


#now read the video and detect the keypoints in each framevi
video_path="videowolfy.mp4"
video=cv2.VideoCapture(video_path)
# Check if the video opened successfully
if not video.isOpened():
    print("Error opening video file")
    exit()
t0=time.time()
n_frame=1

orb=cv2.ORB_create()
#object matcher
bf =cv2.BFMatcher()

while True:
    ret,frame=video.read()
    if ret:
        #convert to grayscale
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #compute the keypoints and descriptors
        k2,d2=orb.detectAndCompute(gray_frame,None)
        """
        Compare the keypoints/descriptors extracted from the 
        first frame(from target object) with those extracted from the current frame.
        """
        matches=bf.match(descriptors,d2)
        for match in matches:
            query_idx=match.queryIdx
            train_idx=match.trainIdx
            #get the coordinates of the keypoints
            pt1=keypoints[query_idx].pt
            pt2=keypoints[train_idx].pt
            #draw the matches
            
            cv2.circle(frame,(int(pt1[0]),int(pt1[1])),5,(0,255,0),2)
        elapsed_time=time.time()-t0 
        fps=n_frame/elapsed_time
        # Display the frame with keypoints
        cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Keypoints",frame)
        n_frame+=1
        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("End of video")
        break
# Release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()

# 2
# → Radius of the circle (in pixels).

# (255, 0, 0)
# → Color of the circle in BGR format (not RGB!):

# (Blue, Green, Red)

# So this is blue

# 2
# → Thickness of the circle border (2 pixels thick).

