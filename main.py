# main.py

from flask import Flask, render_template, request
from api_call import ingredient_search
from meat import veggie

app = Flask(__name__)

found_meat = []


# @app.route('/')
# def recipes_site():
#     return render_template('index.html')
#
# app.run(debug=True)a


# ingredient_name = input('What ingredient? ')
#
# recipes = ingredient_search(ingredient_name)
#
# pprint(recipes)


@app.route('/send', methods=["GET", "POST"])
def send():
    if request.method == "POST":
        ingredient = request.form["ingredient"]
        vegetarian = request.form.get('vegetarian')

        recipes = ingredient_search(ingredient)

        veggie_recipes = [recipe for recipe in recipes if veggie(recipe['source_url'].lower())]

        if not recipes:
            return render_template("empty.html", ingredient=ingredient)

        if vegetarian:
            return render_template("ingredient.html", ingredient=ingredient, recipes=veggie_recipes)
        else:
            return render_template("ingredient.html", ingredient=ingredient, recipes=recipes)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=8080)
