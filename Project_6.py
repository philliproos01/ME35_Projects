from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
from picamera2 import Picamera2, Preview
from libcamera import controls
import os
import sys
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from irobot_create_msgs.msg import IrIntensityVector

picam2 = Picamera2()
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
picam2.start()

#rclpy.init(args=None)
#ir_subscriber = IrSubscriber()

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_Model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1

cond = True
cnt = 0

while(True):
    try:
        # rclpy.spin(ir_subscriber)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        img_name = 'input.jpg'
        picam2.capture_file(img_name)
		# Replace this with the path to your image
        image = Image.open("input.jpg").convert("RGB")

		# resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

		# turn the image into a numpy array
        image_array = np.asarray(image)

		# Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

		# Load the image into the array
        data[0] = normalized_image_array

		# Predicts the model
        prediction = model.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        #print(type(class_name))
        #print(type(confidence_score))
        #print(class_names[0])
        #print(class_names[1])
        #print(class_names[2])
        #print(class_names[3])
        #print(class_names[4])
        #print(class_names[5])
        #print(confidence_score)
        
        if class_name == class_names[0] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Nothing seen")
            os.system('ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.2,max_translation_speed: 0.5}"')

        elif class_name == class_names[6] and confidence_score >= np.float32(0.80): # and prox > 120:
            print("Rubix seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: -1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1

        elif class_name == class_names[3] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Bear seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: -1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1
        elif class_name == class_names[4] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Tractor seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1
        elif class_name == class_names[2] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Kiwi seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1
        elif class_name == class_names[5] and confidence_score >= np.float32(0.70): # and prox > 120:
            print("Jumbo seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: -1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1
        elif class_name == class_names[7] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Mug seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1   
        elif class_name == class_names[1] and confidence_score >= np.float32(0.90): # and prox > 120:
            print("Mario seen")
            os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: -1.57,max_rotation_speed: 0.5}"')
            cnt = cnt + 1
        else:
            print("Still nothing seen")
            os.system('ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.2,max_translation_speed: 0.5}"')

		# Print prediction and confidence score
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", confidence_score)
        print(cnt)
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
