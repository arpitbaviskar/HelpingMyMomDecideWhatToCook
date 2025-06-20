def filter_by_ingredients(recipes, user_ingredients, threshold=0.7):
    filtered = []

    for recipe in recipes:
        required = set(i.lower() for i in recipe.get("ingredients", []))
        available = set(i.lower() for i in user_ingredients)

        if not required:
            continue

        match_ratio = len(required & available) / len(required)

        if match_ratio >= threshold:
            filtered.append(recipe)

    return filtered