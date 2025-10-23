def check_ingredient_match(recipe, ingredients):
    missing_ingredients = []
    has_ingredient_counter = 0
    
    for item in recipe:
        if item not in ingredients:
            missing_ingredients.append(item)
        else:
            has_ingredient_counter += 1
        
    percentage = has_ingredient_counter / len(recipe) * 100

    return percentage, missing_ingredients
