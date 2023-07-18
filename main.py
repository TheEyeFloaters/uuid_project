import cv2
import uuid
import os

def save_frames_with_uuid(input_file, output_directory):

    video_capture = cv2.VideoCapture(input_file)


    video_name = os.path.splitext(os.path.basename(input_file))[0]
    video_directory = os.path.join(output_directory, video_name)
    os.makedirs(video_directory, exist_ok=True)


    frame_counter = 0
    while True:

        ret, frame = video_capture.read()
        if not ret:
            break



        if frame_counter %5==0:
            filename = str(uuid.uuid4()) + ".jpg"

            cv2.imwrite(os.path.join(video_directory, filename), frame)

        frame_counter += 1


    video_capture.release()


input_directory = "Video Files/"

output_directory = "frames/"

# Dosya icerisindeki her bir videoyu gez
for filename in os.listdir(input_directory):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        input_file = os.path.join(input_directory, filename)
        save_frames_with_uuid(input_file, output_directory)
