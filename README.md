# Predict-the-Mode-of-Transport

This project used the SenseMyCity application to collect data from a set of users regarding their mode of transport (BIKE, BUS CAR, RUN, WALK, STILL). Although all the sensors of the cell phone were used, only the data from the Accelerometer, Gyroscope and Magnetometer sensors were considered for the study.

The raw data from the sensors were processed to transform the values of the three axes (X, Y and Z) from hexadecimal to decimal. And finally, they were stored in tables of a PostgreSQL database. 

The study was oriented with the objective of first training the classification algorithms (Random Forest, Multilayer Perceptron, K-Nearest Neighbors, Decision Tree and Support Vector Machine) with the Sussex-Huawei Locomotion dataset (http://www.shl-dataset.org/dataset/), using the same sensor data relative to User1. And, subsequently, clustering new unlabelled data to the collected dataset to predict the mode of transport.

