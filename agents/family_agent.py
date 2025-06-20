def get_family_friendly_tags(family_likes, family_dislikes):
    return {
        "include": [tag.lower() for tag in family_likes],
        "exclude": [tag.lower() for tag in family_dislikes],
    }

def filter_by_family_preferences(recipes, preferences):
    included = preferences.get("include", [])
    excluded = preferences.get("exclude", [])
    filtered = []
    for recipe in recipes:
        tags = [tag.lower() for tag in recipe.get("tags", [])]
        if any(tag in tags for tag in included) and not any(tag in tags for tag in excluded):
            filtered.append(recipe)
    return filtered
