import json
from agents.time_agent import get_time_based_filter
from agents.ingredients_agent import filter_by_ingredients
from agents.mood_agent import get_mood_tags
from agents.weather_agent import get_weather_tags

def load_recipes():
    with open('recipes/recipes.json') as f:
        return json.load(f)

def filter_by_tags(recipes, desired_tags, key="tags"):
    return [
        r for r in recipes
        if any(tag in r.get(key, []) for tag in desired_tags)
    ]

def filter_by_weather(recipes, weather):
    return [
        r for r in recipes
        if "any" in r.get("weather_tags", []) or weather in r.get("weather_tags", [])
    ]

if __name__ == "__main__":
    all_recipes = load_recipes()

    print(f"\n[DEBUG] Total recipes loaded: {len(all_recipes)}")
    
    # --- TIME AGENT ---
    time_of_day = input("\n🕒 What time of day is it? (morning/afternoon/evening): ").lower()
    time_tags = get_time_based_filter(time_of_day)
    print(f"[DEBUG] Time tags: {time_tags}")
    time_filtered = filter_by_tags(all_recipes, time_tags, key='tags')
    print(f"[DEBUG] Time filtered: {len(time_filtered)} recipes")
    for r in time_filtered:
        print(f"  - {r['name']} (tags: {r.get('tags', [])})")

    # --- INGREDIENT AGENT ---
    user_ingredients = ["rice", "tomato", "onion", "turmeric"]  # Update as needed
    print(f"[DEBUG] User ingredients: {user_ingredients}")
    ingredient_filtered = filter_by_ingredients(all_recipes, user_ingredients, threshold=0.2)
    print(f"[DEBUG] Ingredient filtered: {len(ingredient_filtered)} recipes")
    for r in ingredient_filtered:
        print(f"  - {r['name']}")

    # --- MOOD AGENT ---
    mood_input = input("🍽️ How do you feel today? (lazy/happy/unwell): ")
    mood_tags = get_mood_tags(mood_input)
    print(f"[DEBUG] Mood tags: {mood_tags}")
    mood_filtered = filter_by_tags(all_recipes, mood_tags, key='mood_tags')
    print(f"[DEBUG] Mood filtered: {len(mood_filtered)} recipes")
    for r in mood_filtered:
        print(f"  - {r['name']} (mood_tags: {r.get('mood_tags', [])})")

    # --- WEATHER AGENT ---
    weather_input = input("🌦️ What's the weather like? (hot/cold/rainy): ")
    weather_tags = get_weather_tags(weather_input)
    print(f"[DEBUG] Weather tags: {weather_tags}")
    weather_filtered = filter_by_tags(all_recipes, weather_tags, key='weather_tags')
    print(f"[DEBUG] Weather filtered: {len(weather_filtered)} recipes")
    for r in weather_filtered:
        print(f"  - {r['name']} (weather_tags: {r.get('weather_tags', [])})")

    # --- Combine All Filters ---
    print(f"\n[DEBUG] Combining filters with threshold >= 3...")
    combined = []
    for recipe in all_recipes:
        match_count = sum([
            recipe in time_filtered,
            recipe in ingredient_filtered,
            recipe in mood_filtered,
            recipe in weather_filtered
        ])
        if match_count >= 3:  # Try lowering this to 2 or 1 if needed
            combined.append(recipe)
            print(f"[DEBUG] {recipe['name']} matches {match_count}/4 conditions")

    # If no recipes match 3+ conditions, try with 2+ conditions
    if not combined:
        print(f"[DEBUG] No recipes match 3+ conditions. Trying with 2+ conditions...")
        for recipe in all_recipes:
            match_count = sum([
                recipe in time_filtered,
                recipe in ingredient_filtered,
                recipe in mood_filtered,
                recipe in weather_filtered
            ])
            if match_count >= 2:
                combined.append(recipe)
                print(f"[DEBUG] {recipe['name']} matches {match_count}/4 conditions")

    # If still no recipes, try with 1+ conditions
    if not combined:
        print(f"[DEBUG] No recipes match 2+ conditions. Trying with 1+ conditions...")
        for recipe in all_recipes:
            match_count = sum([
                recipe in time_filtered,
                recipe in ingredient_filtered,
                recipe in mood_filtered,
                recipe in weather_filtered
            ])
            if match_count >= 1:
                combined.append(recipe)
                print(f"[DEBUG] {recipe['name']} matches {match_count}/4 conditions")

    # --- Display ---
    print("\n🍽️ Recommended Recipes:")
    if combined:
        for r in combined:
            print(f"- {r['name']}")
    else:
        print("No recipes match any conditions. Check your recipe data and agent functions.")
        