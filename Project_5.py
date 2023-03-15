import requests # you may need to run 'pip install requests' to install this library
import json
import os

''' This function makes a get request to the airtable API which will tell us how fast to spin the wheels'''

''' Put the URL for your Airtable Base here'''
URL = 'https://api.airtable.com/v0/apppBjvmZUBq05vKi/PlaygroundInfo?api_key=key96Z0ItfJ1P1gra'
#'https://api.airtable.com/v0/' + BaseID + '/' + tableName + '?api_key=' + APIKey

r = requests.get(url = URL, params = {})
'''
The get request data comes in as a json package. We will convert this json package to a python dictionary so that it can be parsed
'''
dataInitial = r.json()
print(dataInitial)
standby = '''{'records': [{'id': 'recQu7egM70QNYQUT', 'createdTime': '2023-03-07T21:07:59.000Z', 'fields': {'Name': 'Angular', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recYtpHwy4VMDd2Ky', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Forward', 'Notes': '1'}}, {'id': 'reckPmKGF0D8JCGOW', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Left', 'Notes': '1'}}, {'id': 'recsWn6G1YTgL8G5v', 'createdTime': '2023-03-07T06:16:17.000Z', 'fields': {'Name': 'Linear', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recuccpHJU8QH0qUQ', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Right', 'Notes': '1'}}]}'''
forwardCheck = '''{'records': [{'id': 'recQu7egM70QNYQUT', 'createdTime': '2023-03-07T21:07:59.000Z', 'fields': {'Name': 'Angular', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recYtpHwy4VMDd2Ky', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Forward', 'Notes': '2'}}, {'id': 'reckPmKGF0D8JCGOW', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Left', 'Notes': '1'}}, {'id': 'recsWn6G1YTgL8G5v', 'createdTime': '2023-03-07T06:16:17.000Z', 'fields': {'Name': 'Linear', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recuccpHJU8QH0qUQ', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Right', 'Notes': '1'}}]}'''
leftCheck = '''{'records': [{'id': 'recQu7egM70QNYQUT', 'createdTime': '2023-03-07T21:07:59.000Z', 'fields': {'Name': 'Angular', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recYtpHwy4VMDd2Ky', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Forward', 'Notes': '1'}}, {'id': 'reckPmKGF0D8JCGOW', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Left', 'Notes': '2'}}, {'id': 'recsWn6G1YTgL8G5v', 'createdTime': '2023-03-07T06:16:17.000Z', 'fields': {'Name': 'Linear', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recuccpHJU8QH0qUQ', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Right', 'Notes': '1'}}]}'''
rightCheck = '''{'records': [{'id': 'recQu7egM70QNYQUT', 'createdTime': '2023-03-07T21:07:59.000Z', 'fields': {'Name': 'Angular', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recYtpHwy4VMDd2Ky', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Forward', 'Notes': '1'}}, {'id': 'reckPmKGF0D8JCGOW', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Left', 'Notes': '1'}}, {'id': 'recsWn6G1YTgL8G5v', 'createdTime': '2023-03-07T06:16:17.000Z', 'fields': {'Name': 'Linear', 'Z': '0.0', 'Y': '0.0', 'X ': '0.0'}}, {'id': 'recuccpHJU8QH0qUQ', 'createdTime': '2023-03-07T06:06:44.000Z', 'fields': {'Name': 'Right', 'Notes': '2'}}]}'''
#print(checker)
while True:
        try:
                r = requests.get(url = URL, params = {})
                data = str(r.json())
                if data == standby:
                        print("On standby")
                if data == forwardCheck:
                        print("GO")
                        os.system('ros2 action send_goal /drive_distance irobot_create_msgs/action/DriveDistance "{distance: 0.25,max_translation_speed: 0.15}"')
                if data == leftCheck:
                        print("Going Left")
                        os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: 0.78,max_rotation_speed: 0.5}"')
                if data == rightCheck:
                        print("Going Right")
                        os.system('ros2 action send_goal /rotate_angle irobot_create_msgs/action/RotateAngle "{angle: -0.78,max_rotation_speed: 0.5}"')

        except:
                print('this should be a descriptive error message')
                break
