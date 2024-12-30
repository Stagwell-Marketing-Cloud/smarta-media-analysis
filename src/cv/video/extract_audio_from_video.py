from moviepy.video.io.VideoFileClip import VideoFileClip

def extract_audio_from_video(video_path):
    """
    Extracts audio from a video file and saves it as a WAV file.

    Args:
        video_path (str): Path to the input video file.

    Returns:
        str: Path to the extracted audio file.
    """
    try:
        # Generate audio file path
        audio_path = video_path.replace(".mp4", ".wav")
        
        # Load video and extract audio
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        
        # Clean up resources
        audio.close()
        video.close()
        
        print(f"Audio successfully extracted to: {audio_path}")
        return audio_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None