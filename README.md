Please install weights of embedding facenet model from here: https://github.com/pyannote/pyannote-data/blob/master/openface.nn4.small2.v1.t7 

Another face_detection_model weights (facenet's): mtcnn_weights.npy

Download weights into face_detection_model: deploy.prototxt and res10_300x300_ssd_iter_140000.caffemodel (try from here: https://github.com/nhatthai/opencv-face-recognition/tree/master/src/face_detection_model)

Download these if they don't exist into 'train' folder:
    1. haarcascade_frontalface_default.xml
    2. mmod_human_face_detector.dat
    3. shape_predictor_68_face_landmarks.dat
    4. shape_predictor_68_face_landmarks.dat.bz2

Create dataset, output, test_images folders if they don't exist.

Follow the # USAGE comments inside the python files to run the python files.