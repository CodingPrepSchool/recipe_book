from flask import Flask, render_template, request, redirect
from flask_bootstrap import Bootstrap5
import json
from forms import RecipeForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'


file_connection = open("/Users/olganaymushina/code/github/recipe_book/all_recipes.json", 'r')
recipes_json = json.load(file_connection)
file_connection.close()

@app.route('/')
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  return render_template("index.html", recipes_json=recipes_json, template_form=recipe_form)



# Display All the Recipes #

@app.route("/recipe/<int:id>")
def recipe(id):
  recipes_dict=recipes_json[id-1]
  name = recipes_dict["name"]
  ingredients=recipes_dict["ingredients"]
  instructions = recipes_dict["instructions"]
  return render_template("recipe.html", recipes_dict=recipes_dict, ingredients=ingredients, name=name, instructions=instructions)

# Add a New Recipe #
file_connection = open("/Users/olganaymushina/code/github/recipe_book/all_recipes.json", 'r')
recipes_json = json.load(file_connection)
file_connection.close()

@app.route("/recipes/add-new", methods=["POST"])
def new_rec():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
      id = len(recipes_json)+1
      recipes_json.append({
        "id": id,
        "name": recipe_form.recipe_name.data,
        "ingredients": recipe_form.ingredients.data.split(","),
        "instructions": recipe_form.instructions.data.split(",")
      })
      file_connection = open("/Users/olganaymushina/code/github/recipe_book/all_recipes.json", 'w')
      json.dump(recipes_json, file_connection)
      file_connection.close()
  return redirect("/")


if __name__ == "__main__":
    app.run()
