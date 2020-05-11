# confirm mtcnn was installed correctly
import mtcnn
from matplotlib import pyplot
# face detection with mtcnn on a photograph
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
import argparse


# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--dataset", required=True,
# 	help="path to input directory of faces + images")
# args = vars(ap.parse_args())

# draw an image with detected objects
# def draw_image_with_boxes(filename, result_list):
# 	# load the image
# 	data = pyplot.imread(filename)
# 	# plot the image
# 	pyplot.imshow(data)
# 	# get the context for drawing boxes
# 	ax = pyplot.gca()
# 	# plot each box
# 	for result in result_list:
# 		# get coordinates
# 		x, y, width, height = result['box']
# 		# create the shape
# 		rect = Rectangle((x, y), width, height, fill=False, color='red')
# 		# draw the box
# 		ax.add_patch(rect)
# 	# show the plot
# 	pyplot.show()

def detect_faces(image):
    detector = MTCNN()
    box = detector.detect_faces(image)[0]['box']
    confidence = detector.detect_faces(image)[0]['confidence']
    return box, confidence

