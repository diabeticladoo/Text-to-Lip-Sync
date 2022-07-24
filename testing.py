import os
from subprocess import call
import urllib.request
from flask import Flask, flash, request, redirect, send_from_directory, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
	
@app.route('/',methods = ['GET'])
def upload_form():
	return render_template('upload1.html')

@app.route('/uploadvd', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_video filename: ' + filename)
		flash('Video successfully uploaded')
		return render_template('upload2.html', filename=filename)

@app.route('/uploadad', methods=['POST'])
def upload_audio():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_video filename: ' + filename)
		flash('Uploads successful results below:')
		# call(["python3", "inference.py" , "--checkpoint_path","checkpoints/wav2lip_gan.pth","--face" , "\"/Users/jatin2412/Desktop/Wav2Lip/static/uploads/input_video.mp4\"","--audio","\"/Users/jatin2412/Desktop/Wav2Lip/static/uploads/input_audio.wav\""])
		filename="result_voice.mp4"
		return render_template('upload3.html', filename=filename)

@app.route('/display/<filename>')
def display_video(filename):
	# print('display_video filename: ' + filename)
	# print(url_for('static', filename='uploads/' + filename),code = 301)
	return redirect(url_for('static', filename='results/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)