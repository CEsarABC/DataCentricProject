import os
from flask import Flask, render_template, redirect, request, url_for,session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'recipes'
app.config["MONGO_URI"] = 'mongodb://recipes:Mongo3@ds021026.mlab.com:21026/recipes'

mongo = PyMongo(app)



''' testing author with form, we send author name and dob, the system creates
a new search with those two values and gets the document'''

'''first page has the form which has as action the function which 
interects with the form '''

@app.route('/')
def myrecipes():
    return render_template('myrecipes.html')

@app.route('/')
@app.route('/testauthor', methods=['POST','GET'])
def test_author():
    authorCollection =  mongo.db.authors
    return render_template('myrecipes.html')
    
'''this function takes the imput from a form and replace the 
values in the query with the vales in the new dictionary created 
from the form '''
    

@app.route('/authors', methods=['POST','GET'])
def check_author():
    recipe =  mongo.db.nesting
    authorCollection =  mongo.db.authors
    if request.method == "POST":
        authorform=request.form.to_dict()## why to dictionary just bring the values?????
        print(authorform)
        items = authorform.items()
        print(items)
        ggg = authorform.get('author')
        kkk = authorform.get('dob')
        searchfile = authorCollection.find_one({'author':ggg, 'dob':kkk})
        print(searchfile.get('recipe_name'))
        print(authorform.get('author'))
    return redirect(url_for('test_aller'))
    
@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')
    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)