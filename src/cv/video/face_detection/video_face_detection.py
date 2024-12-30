import cv2
import numpy as np
from retinaface import RetinaFace
from deepface import DeepFace
from typing import List, Optional
from dataclasses import dataclass
from tqdm import tqdm


@dataclass
class FaceDetectionResults:
    unique_faces: int
    total_detections: int
    unique_face_images: List[np.ndarray]
    processing_time: float
    frames_processed: int

def is_face_match(new_face: np.ndarray, existing_faces: List[np.ndarray], 
                 model_name: str = "VGG-Face", threshold: float = 0.8) -> bool:
    """
    Check if a face matches any existing faces using DeepFace verify.
    Lower threshold means more strict matching (DeepFace verify uses distance, not similarity)
    """
    if not existing_faces:
        return False
        
    for existing_face in existing_faces:
        try:
            result = DeepFace.verify(
                img1_path=new_face,
                img2_path=existing_face,
                model_name=model_name,
                enforce_detection=False,
                distance_metric="cosine"
            )
            
            if result["verified"]:
                return True
        except Exception as e:
            continue
            
    return False

def detect_unique_faces_in_video(
    video_path: str, 
    frame_skip: int = 30,
    batch_size: int = 4,
    min_face_size: int = 40,
    model_name: str = "VGG-Face"
) -> Optional[FaceDetectionResults]:
    """
    Detects and counts unique faces in a video using RetinaFace and DeepFace verification.
    
    Parameters:
        video_path (str): Path to the input video file
        frame_skip (int): Process every nth frame (default=30)
        batch_size (int): Number of frames to process in parallel (default=4)
        min_face_size (int): Minimum face size in pixels to consider (default=40)
        model_name (str): Model to use for face verification (default="VGG-Face")
    
    Returns:
        FaceDetectionResults: Contains detection statistics and unique face images
    """
    import time
    start_time = time.time()
    
    try:
        if not isinstance(video_path, str) or not video_path:
            raise ValueError("Invalid video path")
        
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise RuntimeError(f"Failed to open video: {video_path}")
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frames_to_process = total_frames // frame_skip
        
        unique_faces = []
        total_faces_detected = 0
        frames_processed = 0
        
        pbar = tqdm(total=frames_to_process, desc="Processing video")
        
        while frames_processed < total_frames:
            frames_batch = []
            for _ in range(batch_size):
                for _ in range(frame_skip):
                    ret, frame = cap.read()
                    if not ret:
                        break
                if ret:
                    frames_batch.append(frame)
                    frames_processed += frame_skip
            
            if not frames_batch:
                break
                
            for frame in frames_batch:
                try:
                    detected_faces = RetinaFace.extract_faces(
                        frame, 
                        align=True,
                        allow_upscaling=False
                    )
                    
                    if detected_faces:
                        total_faces_detected += len(detected_faces)
                        
                        for face in detected_faces:
                            if (face is None or face.size == 0 or 
                                face.shape[0] < min_face_size or face.shape[1] < min_face_size):
                                continue
                                
                            try:
                                face_img = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
                                
                                if not is_face_match(face_img, unique_faces, model_name):
                                    unique_faces.append(face_img)
                                        
                            except Exception as e:
                                continue
                                
                except Exception as e:
                    continue
                    
            pbar.update(len(frames_batch))
        
        pbar.close()
        cap.release()
        
        processing_time = time.time() - start_time
        
        return FaceDetectionResults(
            unique_faces=len(unique_faces),
            total_detections=total_faces_detected,
            unique_face_images=unique_faces,
            processing_time=processing_time,
            frames_processed=frames_processed
        )
        
    except Exception as e:
        print(f"Error in face detection: {str(e)}")
        return None

def save_unique_faces(results: FaceDetectionResults, output_dir: str):
    """Save the unique faces found to separate image files."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    for idx, face in enumerate(results.unique_face_images):
        output_path = os.path.join(output_dir, f"unique_face_{idx}.jpg")
        cv2.imwrite(output_path, face)