from flask import Flask, render_template, redirect, request
from pytube import YouTube
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def post_submit():
	yt = YouTube()
	url = request.form.get('url')
	print(url)
	yt.url = url
	video = yt.get('mp4', '360p')
	print(yt.get_videos())
	print(yt.filename)
	video.download('./')
	print('Yo')
	return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

