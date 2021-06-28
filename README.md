# Pose Estimation

Human pose estimation from video plays a critical role in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. 
For example, it can form the basis for yoga, dance, and fitness applications. 
It can also enable the overlay of digital content and information on top of the physical world in augmented reality.

## Models
The detector is inspired by our own lightweight BlazeFace model, used in MediaPipe Face Detection, as a proxy for a person detector.
It explicitly predicts two additional virtual keypoints that firmly describe the human body center, rotation and scale as a circle. 
Inspired by Leonardo’s Vitruvian man, we predict the midpoint of a person’s hips, the radius of a circle circumscribing the whole person, and the 
incline angle of the line connecting the shoulder and hip midpoints.



