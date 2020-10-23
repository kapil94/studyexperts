from flask import Flask,render_template,url_for,redirect,Response
import boto3
import os

app=Flask(__name__)

BUCKET_NAME = 'testproject2'


@app.route('/')
def index():
	return render_template("index.html")

@app.route('/aboutus')
def aboutus():
	return render_template('Aboutus.html')

@app.route('/polprev')
def polprev():
	return render_template("pol-prev.html")

@app.route('/politicalsc/previousyear/<int:year>')
def previousyr(year):
	
	s3_resource = boto3.resource('s3')
	my_bucket =s3_resource.Bucket(BUCKET_NAME)
	if year == 2015:
		key = "politicalsc/2015/Lorem Ipsum.pdf"
	
	elif year == 2016:
		key= "politicalsc/2016/dummy.pdf"

	file_obj = my_bucket.Object(key).get()
	
	return Response(
        	file_obj['Body'].read(),
        	mimetype='text/plain',
        	headers={"Content-Disposition": "attachment;filename={}".format(key)}
    		)

if __name__ == '__main__':	
	app.run(debug=True)
