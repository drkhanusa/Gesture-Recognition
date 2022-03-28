# Real-Time Continuous Gesture Recognition with Wireless Wearable IMU Sensors

The general overview of the proposed action recognition framework is shown as follows. It can be regarded as two stages. First, i project each channel signal as a square matrix using modified RP(recurence plot) respectively and combine them into a color image. After normalization, we implement a tiny ResNet to do the classification task end to end.

![General overview of proposed action recognition framework](https://user-images.githubusercontent.com/102515240/160377604-fe98c49f-08f1-4c33-bf27-d6cb297da4bc.png)

Dataset consist of 42 persons, 35 persons to training and 7 persons to testing.
Each of person have 12 gestures. 
Graph.py get data from csv file and generate graph.

![histogram](https://user-images.githubusercontent.com/102515240/160377947-ce3382f6-e176-4f43-9efa-f1f66cb4a428.png)


Matrix get data from csv file and generate image, dataset has 4,379 Files.
For example at a single measurement of 1 person with 12 gestures.

![image-dataset](https://user-images.githubusercontent.com/102515240/160379410-d38215a7-8497-4f9f-ac7a-c40278f8a35a.png)



Finally, divide the above dataset into 2 parts and put it into Resnet-18.

This is my result: 76%. Not-pretrained.

![result](https://user-images.githubusercontent.com/102515240/160379805-a4033d75-b200-4e40-a51e-c7edf4261117.jpg)

