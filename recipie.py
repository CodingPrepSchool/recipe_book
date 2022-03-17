from flask import Flask, redirect, render_template, request
from recipie_form import RecipieAdd
import sqlite3
from all_recipies import recipes

app=Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route("/", methods = ["GET", "POST"])
def homepage():
    add_recipie = RecipieAdd(csrf_enabled=False)
    return render_template("recipie_book.html", recipes=recipes, template_form = add_recipie)

@app.route("/recipe/<int:id>")
def recipe(id):
    recipes_dict = recipes[id-1]
    name = recipes_dict["name"]
    ingredients = recipes_dict["ingredients"]
    instructions = recipes_dict["instructions"]
    return render_template("recipie_template.html", recipes=recipes, name = name, ingredients = ingredients, instructions=instructions)

@app.route("/add_recipie", methods=["GET", "POST"])
def add_info():
    add_recipie = RecipieAdd(csrf_enabled = False)
    if add_recipie.validate_on_submit():
        id = len(recipes) + 1
        recipes.append({
            "id": id,
            "recipie_name": add_recipie.recipie_name.data,
            "ingrediants": add_recipie.ingrediants.data,
            "instructions": add_recipie.instructions.data})
    return redirect('/')