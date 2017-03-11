import os
import cv2
import random
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    newImagePath = ''
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print(os.path.join(app.config['UPLOAD_FOLDER']))
            imagePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            file.save(imagePath)
            # Get user supplied values
            cascPath = "haarcascade_frontalface_default.xml"
			# Create the haar cascade
            faceCascade = cv2.CascadeClassifier(cascPath)
            print(faceCascade)
			# # Read the image
            image = cv2.imread(imagePath)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

			# Detect faces in the image
            faces = faceCascade.detectMultiScale(
			   gray,
			   scaleFactor=1.2,
			   minNeighbors=5,
			   minSize=(30, 30),
			   flags = cv2.CASCADE_SCALE_IMAGE #flags = cv2.cv.CV_HAAR_SCALE_IMAGE
			)
            print(faces)
            print("Found {0} faces!".format(len(faces)))

            rnd = random.randint(0, 999999999999)
            img = str(rnd) + '.jpg'
            newImagePath = os.path.join(app.config['UPLOAD_FOLDER'], img)
			# Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                age = random.randint(18, 30)
                cv2.rectangle(image, (x + 3, y - 15), (x + 50, y - 50), (200, 187, 0), -1)
                cv2.putText(image, str(age), (x + 5, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 187), 2)
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.imwrite(newImagePath, image)
            print(newImagePath)

            return redirect(url_for('upload_file', img=img, result=len(faces)))

    img = request.args.get('img')
    result = request.args.get('result')
    if img and result != str(0):
        img = './static/images/' + request.args.get('img')
    else:
        img = ''

    return render_template('index.html', newImagePath=img)

if __name__ == "__main__":
    app.run()