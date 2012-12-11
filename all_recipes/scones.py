#!/usr/bin/env python3

R = Recipe()

R.name("Scones")

R.serves(4)

R.ingredient(40, "g", "slightly salted butter")
R.ingredient(225, "g", "self-raising flour")
R.ingredient(25, "g", "caster sugar")
R.ingredient("A pinch of salt")
R.ingredient(150, "ml", "milk")

R.do("Mix flour and salt together and rub in butter.")
R.do("Mix in the sugar, then add milk until the dough is soft.")
R.do("Turn onto a floured board and knead very lightly.")
R.do("Make a round roughly 2cm thick.")
R.do("Use a scone cutter (about 5cm) to cut into circles.")
R.do("Brush the tops of the scones with milk or beaten egg (or a mixture of both).")
R.do("Bake for 12-15 minutes in the oven at 220\degc.")

add(R)

