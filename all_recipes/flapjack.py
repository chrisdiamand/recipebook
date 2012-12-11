
R = Recipe()

R.name("Flapjack")

R.ingredient(200, "g", "margarine")
R.ingredient(200, "g", "brown sugar")
R.ingredient(2, "tablespoons", "golden syrup")
R.ingredient(1.5, "teaspoons", "ginger")
R.ingredient(280, "g", "oats")

R.do("Heat everything apart from the oats in a pan.")
R.do("Add oats to the melted ingredients and mix thoroughly.")
R.do("Cook in oven at 160\degc for 22 minutes or until golden brown but not too solid.")

add(R)


