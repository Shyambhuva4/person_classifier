
from flask import Flask ,request,jsonify
import utils

import util

app =Flask(__name__)
@app.route('/classify_img',methods=['GET','POST'])
def classify_images():
    image_data =request.form['image_data']
    response=jsonify(util.classify(image_data))
    response.headers.add('Access-Control-Allow-Origin','*')
    return response
if __name__ =='__main__':
    app.run(port=5000)