# Pose Estimation

Human pose estimation from video plays a critical role in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. 
For example, it can form the basis for yoga, dance, and fitness applications. 
It can also enable the overlay of digital content and information on top of the physical world in augmented reality.

![pose_tracking_example](https://user-images.githubusercontent.com/81274360/123645170-62a0e300-d826-11eb-9773-022c42a3a47c.gif)


## Models
The detector is inspired by our own lightweight BlazeFace model, used in MediaPipe Face Detection, as a proxy for a person detector.
It explicitly predicts two additional virtual keypoints that firmly describe the human body center, rotation and scale as a circle. 
Inspired by Leonardo’s Vitruvian man, we predict the midpoint of a person’s hips, the radius of a circle circumscribing the whole person, and the 
incline angle of the line connecting the shoulder and hip midpoints.

![edsds](https://user-images.githubusercontent.com/81274360/123645201-692f5a80-d826-11eb-9652-12f17cd415a2.PNG)


## Pose Landmark Model (BlazePose GHUM 3D)
The landmark model in MediaPipe Pose predicts the location of 33 pose landmarks (see figure below).

![dascs](https://user-images.githubusercontent.com/81274360/123645337-8b28dd00-d826-11eb-9595-edf1127a270b.PNG)



## Results
the results on person training on push up can be shown in the this picture

![asdsafsdf](https://user-images.githubusercontent.com/81274360/123646640-afd18480-d827-11eb-9869-6cb78df62140.PNG)

