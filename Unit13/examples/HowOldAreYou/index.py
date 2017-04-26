import cv2
from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	filename = request.args.get('filename')
	result = request.args.get('result')

	return render_template('index.html', filename=filename, result=result)

@app.route('/upload', methods=['POST'])
def upload():
	if request.method == 'POST':
		file = request.files['img']

		file.save('./' + file.filename)

		cascPath = 'haarcascade_frontalface_default.xml'

		faceCascade = cv2.CascadeClassifier(cascPath)

		image = cv2.imread(file.filename)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.2,
			minNeighbors=5,
			minSize=(30, 30),
			flags= cv2.CASCADE_SCALE_IMAGE
		)

		for (x, y, w, h) in faces:
			age = random.randint(18, 30)
			cv2.rectangle(image, (x + 3, y - 15), (x + 50, y - 50), (200, 187, -1), -1)
			cv2.putText(image, str(age), (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 187), 2)
			cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.imwrite('./static/images/' + file.filename, image)
		newImage = file.filename

	return redirect(url_for('index', filename=newImage, result=len(faces)))

if __name__ == '__main__':
	app.run()