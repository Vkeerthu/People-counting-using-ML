# People-counting-using-deep learning
This project focuses on developing a crowd detection system using deep learning techniques. The goal is to accurately identify and analyze crowded scenes from images or video footage. This README file provides an overview of the project and instructions for running the code
# Description
Crowd counting is a difficult task in computer vision due to complex and crowded scenes in real-world scenarios. In this project, we propose a new crowd counting method that uses the YOLO
algorithm for object detection and density map estimation. Our method is designed to accurately estimate the number of crowds in a video given the temporal coherence of human motion between successive frames. First,we preprocess the input video and pass each frame to the YOLO human detection algorithm. Next, generate a density map for each frame by convolving a Gaussian kernel centered on the bounding box of each detected person. Then, estimate the number of crowds using a regression model trained on the density map of the training data set. Overall, the proposed method provides a robust and accurate solution for crowd counting in video. It uses the YOLO algorithm for people detection and density map estimation, and uses temporal consistency constraints to improve crowd count accuracy acrossframes.
# FLOW-DIAGRAM
<img width="132" alt="image" src="https://github.com/Vkeerthu/People-counting-using-ML/assets/118120941/b10f7da5-69b4-444d-91a8-ac97f6f4ffd0">

