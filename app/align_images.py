import os
import sys
import bz2
from keras.utils import get_file
from ffhq_dataset.face_alignment import image_align
from ffhq_dataset.landmarks_detector import LandmarksDetector

if __name__ == "__main__":
    main(sys.argv[1],sys.argv[2])

def main(arg1, arg2):
    """
    Extracts and aligns all faces from images using DLib and a function from original FFHQ dataset preparation step
    python align_images.py /raw_images /aligned_images
    """

    # landmarks_model_path = unpack_bz2(LANDMARKS_LOCAL_FILE)

    landmarks_model_path = '/models/shape_predictor_68_face_landmarks.dat'

    RAW_IMAGES_DIR = arg1
    ALIGNED_IMAGES_DIR = arg2

    landmarks_detector = LandmarksDetector(landmarks_model_path)
    files = os.listdir(RAW_IMAGES_DIR)
    for j, img_name in enumerate(sorted(files)):
        if not img_name.startswith('.'):
            raw_img_path = os.path.join(RAW_IMAGES_DIR, img_name)
            print("Processing file " + str(j+1) + " of " + str(len(files)) + ": '" + raw_img_path + "'...")
            landmarks = landmarks_detector.get_landmarks(raw_img_path)
            aligned = list(landmarks)
            for i, face_landmarks in enumerate(aligned, start=1):
                face_img_name = '%s_%02d.jpg' % (os.path.splitext(img_name)[0], i)
                aligned_face_path = os.path.join(ALIGNED_IMAGES_DIR, face_img_name)
                image_align(raw_img_path, aligned_face_path, face_landmarks)
                print("Saving aligned image " + str(i) + " of " + str(len(aligned)) + ": " + aligned_face_path)