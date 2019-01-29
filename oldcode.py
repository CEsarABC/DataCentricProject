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

#@app.route('/')
def myrecipes():
    return render_template('my_recipes.html')

#@app.route('/')
@app.route('/testauthor', methods=['POST','GET'])
def test_author():
    nestingCollection =  mongo.db.nesting
    return render_template('my_recipes.html')
    
'''this function takes the imput from a form and replace the 
values in the query with the vales in the new dictionary created 
from the form, the new cursor is sent back to the page '''
    

@app.route('/authors', methods=['POST','GET'])
def check_author():
    recipe =  mongo.db.nesting
    nestingCollection =  mongo.db.nesting
    nesting=request.form.to_dict()## why to dictionary just bring the values?????
    items = nesting.items()
    author = nesting.get('author')
    dob = nesting.get('dob')
    print(nesting.get('author'))
    return render_template('my_recipes.html', searchfile = nestingCollection.find({'author':author, 'dob':dob}), authorName=author.capitalize())
    
@app.route('/test_aller')
def test_aller():
    return render_template('allergens.html')
    
@app.route('/edit_recipe/<item_id>')
def edit_recipe(item_id):
    the_recipe =  mongo.db.nesting.find_one({"_id": ObjectId(item_id)})
    #all_categories =  mongo.db.categories.find()
    return render_template('edit_recipe.html', recipe=the_recipe)
    
''''''''''''''''''''''''''''''''''''''''''''''''''''''

# @app.route('/')
# @app.route('/testauthor', methods=['POST','GET'])
# def test_multi():
#     cuisine =  mongo.db.cuisine
#     new_docs = [{'cuisine': 'Arab'},{'cuisine': 'Bangladeshi'},{'cuisine': 'Bengali'},{'cuisine': 'British'}
#     ,{'cuisine': 'Buddist'},{'cuisine': 'Bulgarian'},{'cuisine': 'Cajun'},{'cuisine': 'Chinese'}
#     ,{'cuisine': 'Danish'},{'cuisine': 'Estonian'},{'cuisine': 'French'},{'cuisine': 'Filipino'}
#     ,{'cuisine': 'Georgian'},{'cuisine': 'Greek'},{'cuisine': 'Indian'},{'cuisine': 'Indonesian'}
#     ,{'cuisine': 'Italian-American'},{'cuisine': 'Italian'},{'cuisine': 'Japanese'}
#     ,{'cuisine': 'Jewish'},{'cuisine': 'Korean'},{'cuisine': 'Lithuanian'},{'cuisine': 'Malaysian'}
#     ,{'cuisine': 'Mediterranean'},{'cuisine': 'Mexican'},{'cuisine': 'Native American'}
#     ,{'cuisine': 'Nepalese'},{'cuisine': 'Pakistani'},{'cuisine': 'Thai'},{'cuisine': 'Turkish'}]
#     cuisine.insert_many(new_docs)
#     return render_template('my_recipes.html')
    

    
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
debug=True)


<form action="{{ url_for('update_task', task_id=task._id)}}" method="POST" class="col s12">
        <div class="row">
            <div class="input-field col s12">
                <select id="category" name="category_name">
                  <option value="" disabled selected>Choose Category</option>
                  {% for cat in categories %}
                      {% if cat.category_name == task.category_name%}
                      <option value="{{cat.category_name}}" selected >{{cat.category_name}}</option>
                      {% else %}
                       <option value="{{cat.category_name}}">{{cat.category_name}}</option>
                    {% endif %}
                  {% endfor %}
                </select>
                <label>Task Category</label>
            </div>
        </div>
        
        
<form action="{{ url_for('insert_task') }}" method="POST" class="col s12">
        
        <div class="row">
            <div class="input-field col s12">
                <select id="category" name="category_name">
                  <option value="" disabled selected>Choose Category</option>
                  {% for cat in categories %}
                  <option value="{{cat.category_name}}">{{cat.category_name}}</option>
                  {% endfor %}
                </select>
                <label>Task Category</label>
             </div>
        </div>
        

<div class="form-group">
    <label for="exampleFormControlSelect1">Example select</label>
    <select class="form-control" id="exampleFormControlSelect1">
      <option>1</option>
      <option>2</option>
      <option>3</option>
      <option>4</option>
      <option>5</option>
    </select>
  </div>
  
<div class="card" style="width: 18rem;">
  <img class="card-img-top" src="..." alt="Card image cap">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
    <a href="#" class="btn btn-primary">Go somewhere</a>
  </div>
</div>

<!--{% if item in searchfile == "image" %}-->
              <!--<img class="card-img-top" src="{{item.image}}" alt="Card image cap">-->
              <!--{% endif %}-->
              
 {% if 'milk' in recipe.allergens %}
              {% else %}
              {% endif %}
              
              db.inventory.find( { price: { $not: { $gt: 1.99 } } } )
              db.inventory.find( { $nor: [ { price: 1.99 }, { sale: true } ]  } )
              db.test.find({'post': {$ne : ""}})
              
<div><h1 class='handlee'>Kimberley's Cook Book </h1></div>
    <div><h1 class='yellowtail'>Kimberley's Cook Book </h1></div>
    <div><h1 class='playball'>Kimberley's Cook Book </h1></div>
    <div><h1 class='reenie'>Kimberley's Cook Book </h1></div>
    <div><h1 class='oleo'>Kimberley's Cook Book</h1></div>
    
    {{url_for('delete_recipe', item_id=item._id, author=author, dob=dob)}}