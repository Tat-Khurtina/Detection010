from werkzeug.utils import secure_filename #
from flask import render_template, flash, redirect, url_for, request, jsonify, Response
from werkzeug.urls import url_parse
from app import app
from app.forms import FillingForm
import os
from app.detect import detect
import torchvision
from torchvision.models.detection.faster_rcnn import FastRCNNPredictor
import cv2
from app.camera import VideoCamera

UPLOAD_FOLDER = 'app/static/im'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = { 'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model = model.eval()
@app.route('/', methods=['GET', 'POST'])
@app.route('/ind', methods=['GET', 'POST'])
def ind():
    form = FillingForm()
    if form.submit0.data :
        if 'file' not in request.files:
            flash('No file part')
#            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('Нет файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'orig', filename))
        try:
            detect(filename, model)
            return render_template('ind.html', form=form, filen=filename,os=os,str=str)
        except Exception:
            flash("Не распознано")
        else:
            flash("Попробуйте расширения: 'png', 'jpg', 'jpeg' ")
    return render_template('ind.html', form=form, os=os,str=str)




@app.route('/str')
def str():
    # rendering webpage
    return render_template('str.html')
def gen(camera):
    while True:
        #get camera frame
        frame = camera.get_frame(model)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





