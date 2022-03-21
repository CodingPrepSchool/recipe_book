recipes = {1: "Mushroom Omelet", 2: "French Toast", 3: "Grilled Cheese Sandwich"}

descriptions = {1: 'Mushroom Omelet', 2: 'French Toast', 3: 'Grilled Cheese Sandwich'}

ingredients = {1: ['2 tablespoons extra-virgin olive oil', '1 minced shallot', 
'¼ pound white or cremini mushrooms', 'rinsed briefly and wiped dry', 'Salt', 
'freshly ground pepper (to taste)', '1 to 2 garlic cloves (to taste)', 
'2 teaspoons minced flat-leaf parsley', '4 eggs, 1 tablespoon minced chives', '2 teaspoons low-fat milk', 
'3 tablespoons grated Gruyère cheese'], 
2: ['1 egg', '1 teaspoon Vanilla Extract', '1/2 teaspoon Ground Cinnamon', '1/4 cup milk', '4 slices bread'],
3: ['4 slices white bread', '3 tablespoons butter, divided', '2 slices Cheddar cheese' ]}

instructions = {1: {'Step 1': ' Trim off the ends of the mushrooms, and cut into thick slices. Heat a large, heavy frying pan over medium-high heat, and add 1 tablespoon of the olive oil. Add the shallot, and cook, stirring, until it begins to soften, two or three minutes. Add the mushrooms, and cook, stirring or tossing in the pan, for a few minutes, until they begin to soften and sweat. Add salt to taste and the garlic, and cook, stirring often, until the mushrooms are tender, about five minutes. Stir in the parsley, season to taste with salt and pepper, and remove from the heat.',
'Step 2': ' Heat a 10-inch nonstick pan over medium-high heat. Beat all 4 eggs in a bowl with the milk, salt and pepper, and the chives. Heat the remaining tablespoon of olive oil in the pan, and follow the instructions for the 2-egg omelet, pouring all of the eggs into the pan. The eggs will take longer to set, and you may want to flip the omelet in the pan again after it’s rolled, if the middle seems too runny. Roll the finished omelet onto a platter, or cut in half in the pan, and serve.', 
'Step 3': ' Add 2 teaspoons of the olive oil to the pan. When the pan feels hot as you hold your hand above it, pour in the eggs, scraping every last bit into the pan. Tilt the pan to distribute the eggs evenly over the surface. Tilt it slightly again, and gently shake with one hand while lifting up the edges of the omelet with the spatula in your other hand so as to let the eggs run underneath during the first few minutes of cooking.',
'Step 4': ' Spread half the mushrooms down the middle of the eggs. Top with half the cheese. As soon as the eggs are set on the bottom (the top will still be runny), jerk the pan quickly away from you then back towards you so that the omelet folds over on itself. Shake in the pan for another minute if you don’t like the omelet soft on the inside; for a moist omelet, tilt the pan at once and roll out onto a plate. Keep warm in a low oven while you repeat with the remaining eggs and herbs, and serve.', 
'Step 5': ' Serve warm.'
},
 2: {'Step 1': ' Beat egg, vanilla and cinnamon in shallow dish with wire whisk. Stir in milk.', 
'Step 2': ' Dip bread in egg mixture, turning to coat both sides evenly.',
'Step 3': ' Cook bread slices on lightly greased nonstick griddle or skillet on medium heat until browned on both sides. Serve with Easy Spiced Syrup, if desired. Voila, easy French toast.',
'Step 4': ' Easy Spiced Syrup: Add 1 teaspoon Vanilla Extract and 1/4 teaspoon Ground Cinnamon to 1 cup pancake syrup; stir well to mix. Serve warm, if desired.'},
3: {'Step 1':'Preheat skillet over medium heat.', 
'Step 2': 'Generously butter one side of a slice of bread. Place bread butter-side-down onto skillet bottom and add 1 slice of cheese.',
'Step 3': 'Butter a second slice of bread on one side and place butter-side-up on top of sandwich.',
'Step 4': 'Grill until lightly browned and flip over; continue grilling until cheese is melted.',
'Step 5': ' Repeat with remaining 2 slices of bread, butter and slice of cheese.' }
}

for item in ingredients.values():
    print(item)