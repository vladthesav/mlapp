from flask import Flask, request

from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:HACKRUpassword@cluster0-d2rxd.gcp.mongodb.net/test?retryWrites=true&w=majority")

db = client.test
app = Flask(__name__)

#MongoDB scheme
#image
#name
#model output
#comment

#returns list of images
@app.route('/all_images', methods=['GET'])
def retrieve_all():
	rows = db.inventory.find({})
	return rows

#inserts posted image into db
@app.route('/upload', methods=['POST'])
def save():
	json = request.get_json()
	model_output = [] #this will be the resut of feeding the image to the model
	db.inventory.insert({'image': json['image'], 'name': json['name'], 'comment': '', 'output': model_output})

#retrieves data for a specific image
@app.route('/image', methods=['GET'])
def retrieve():
	json = request.get_json()
	image = db.inventory.find({'name': json['name']})
	return image

#add comment to image
@app.route('/comment', methods=['POST'])
def add_comment():
	json = request.json()
	db.inventory.update({"name": json['name']}, {"$set": {"comment": json['comment']}})