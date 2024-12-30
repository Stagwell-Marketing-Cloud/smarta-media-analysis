from moviepy import VideoFileClip
from scenedetect import detect, AdaptiveDetector

def get_video_duration(file_name):
    with VideoFileClip(file_name) as video:
        duration = video.duration  # Duration in seconds
        return duration

### Scene Detection
def scene_num(video_path):
    if video_path.endswith(".mp4"):
        scene_list = detect(video_path, AdaptiveDetector())
        if len(scene_list) == 0:
            return 1
        else:
            return len(scene_list)
    else:
        return 1
    

### Rule answering -> Duration
def duration_less_than(duration, threshold):
    return 1 if duration <= threshold else 0

def duration_more_than(duration, threshold):
    return 1 if duration > threshold else 0

def duration_between(duration, lower_threshold, upper_threshold):
    lower_duration = duration_more_than(duration, upper_threshold)
    upper_duration = duration_less_than(duration, lower_threshold)
    return 1 if (upper_duration and lower_duration) else 0 

# Call this function to answer if duration between eg 15 and 20 seconds
def call_duration(filename, lower_threshold, upper_threshold):
    file_duration = get_video_duration(filename)
    return duration_between(file_duration, lower_threshold, upper_threshold)



# Integration 
# 1. Integration: Between 90 - 240
# 2. Integration: After 10 seconds
# 3. Integration: First half of the video and after 10 seconds

