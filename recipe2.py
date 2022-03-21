import sqlite3 
from flask import Flask, render_template, request, redirect
from all_recipes import recipes
from flask_bootstrap import Bootstrap5
from forms import RecipeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/', methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  return render_template("index2.html", template_recipes=recipes, template_form=recipe_form, recipes=recipes)


@app.route("/recipe/<int:id>", methods=["GET"])
def recipe(id):
  recipes_dict=recipes[id-1]
  name = recipes_dict["name"]
  ingredients=recipes_dict["ingredients"]
  instructions = recipes_dict["instructions"]

  return render_template("recipe2.html", recipes_dict=recipes_dict, ingredients=ingredients, name=name, instructions=instructions)


@app.route("/recipes/add-new", methods=["POST"])
def new_rec():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
      id = len(recipes)+1
      recipes.append({
        "id": id,
        "name": recipe_form.recipe_name.data,
        "ingredients": recipe_form.ingredients.data.split(","),
        "instructions": recipe_form.instructions.data.split(",")
      })
  return redirect("/")

if __name__ == "__main__":
  app.run()

