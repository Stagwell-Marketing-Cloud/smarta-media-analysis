import cv2
from retinaface import RetinaFace
from deepface import DeepFace
import numpy as np

def detect_unique_faces_with_retinaface(image_path:str) -> tuple[int,int]:
    """
    Detects and counts unique faces in an image using RetinaFace for face detection 
    and DeepFace for embedding comparison.
    
    Parameters:
    - image_path (str): Path to the input image.

    Returns:
    - int: Number of unique faces detected.
    """
    try:
        if not image_path or not isinstance(image_path, str):
            raise ValueError("Invalid image path. Provide a valid string path to the image.")

        try:
            detected_faces = RetinaFace.extract_faces(image_path, align=True)
        except Exception as e:
            raise RuntimeError(f"Failed to extract faces with RetinaFace: {e}")

        if not detected_faces:
            return (0,0)

        unique_faces = []

        for idx, face in enumerate(detected_faces):
            if face is None or face.size == 0:
                print(f"Skipping invalid face at index {idx}.")
                continue

            try:
                face_img = cv2.cvtColor(face, cv2.COLOR_RGB2BGR)
                embedding = DeepFace.represent(face_img, model_name='VGG-Face', enforce_detection=False)
                is_unique = True
                for existing_embedding in unique_faces:
                    distance = np.linalg.norm(np.array(embedding[0]["embedding"]) - np.array(existing_embedding))
                    if distance < 0.6:
                        is_unique = False
                        break

                if is_unique:
                    unique_faces.append(embedding[0]["embedding"])
            except Exception as e:
                print(f"Error processing a face at index {idx}: {e}")
                continue
            
        return (len(unique_faces), len(detected_faces))

    except Exception as e:
        print(f"Error in detect_unique_faces_with_retinaface: {e}")
        return (0,0)