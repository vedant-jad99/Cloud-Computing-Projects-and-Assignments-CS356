#Main routes file. Only one route is required here. In this file, we are also taking input from the web and storing it in s3

from flask import render_template
from app.form import UploadPicture
from app import app
import secrets
import os
import boto3 as boto


# Opening the image file
def open_img(filename):
    data = open(filename, 'rb')
    app.logger.info('data '+ str(data))
    return data

#Opening and uploading to s3 bucket
def upload_to_s3(filename):
    s3 = boto.resource('s3')
    try:
        data = open_img(filename)
        key = filename.split('/')[-1]
        print(key)
        s3.Bucket('ubunturekbucket1').put_object(Key=key, Body=data)
        app.logger.info("Upload successful!")
    except Exception as e:
        app.logger.error(e)

#Function to store image in s3 and in temporary web folder
def save_picture(image):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image.filename)
    pic_fn = random_hex + f_ext
    pic_path = os.path.join(app.root_path, 'static', 'images', pic_fn)
    app.logger.info("Image path" + str(pic_path))
    image.save(pic_path)

    app.logger.info("Uploading to the s3 bucket")
    upload_to_s3(pic_path)
    return pic_fn


#Main home route. This page will be displayed as soon as user visits the app.

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    #Main home function

    form, pic_file = UploadPicture(), None
    if form.validate_on_submit():
        app.logger.info("File format verified")
        if form.image.data:
            pic_file = save_picture(form.image.data)
    return render_template("main.html", title="Rekognition demo app", form=form, name=pic_file)
