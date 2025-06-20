import streamlit as st
import json
from agents.time_agent import get_time_based_filter
from agents.ingredients_agent import filter_by_ingredients
from agents.mood_agent import get_mood_tags
from agents.weather_agent import get_weather_tags


def load_recipes():
    with open('recipes/recipes1.json') as f:
        return json.load(f)


def filter_by_tags(recipes, desired_tags, key="tags"):
    return [r for r in recipes if any(tag in r.get(key, []) for tag in desired_tags)]


# Load recipes once at the start
all_recipes = load_recipes()

# Extract unique ingredients for multiselect
all_ingredients = sorted({
    ingredient.strip().lower()
    for recipe in all_recipes
    for ingredient in recipe.get("ingredients", [])
})

# UI Inputs
st.title("Helping My Mom Decide What To Cook 🍛")
time_input = st.selectbox("🕒 What time of day is it?", ["morning", "afternoon", "evening"])
mood_input = st.selectbox("😊 How do you feel today?", ["lazy", "happy", "unwell"])
weather_input = st.selectbox("🌦️ What's the weather like?", ["hot", "cold", "rainy", "any"])
ingredients = st.multiselect("🧂 Select available ingredients", options=all_ingredients)

if st.button("🍽️ Recommend Recipes"):
    # Generate filters
    time_tags = get_time_based_filter(time_input)
    mood_tags = get_mood_tags(mood_input)
    weather_tags = get_weather_tags(weather_input)

    # Filter sets
    time_filtered = filter_by_tags(all_recipes, time_tags, key="tags")
    mood_filtered = filter_by_tags(all_recipes, mood_tags, key="mood_tags")
    weather_filtered = filter_by_tags(all_recipes, weather_tags, key="weather_tags")
    ingredient_filtered = filter_by_ingredients(all_recipes, ingredients, threshold=0.2)

    #st.write(f"Time matches: {len(time_filtered)}")
    #st.write(f"Mood matches: {len(mood_filtered)}")
    #st.write(f"Weather matches: {len(weather_filtered)}")
    #st.write(f"Ingredient matches: {len(ingredient_filtered)}")

    # Combine filters
    combined = []

    # Try finding recipes that match 3 or more filters
    for recipe in all_recipes:
        match_count = sum([
            recipe in time_filtered,
            recipe in mood_filtered,
            recipe in weather_filtered,
            recipe in ingredient_filtered
        ])
        if match_count >= 3:
            combined.append((recipe, match_count))

    # Fallback 1: Try recipes that match 2 out of 4 filters
    if not combined:
        for recipe in all_recipes:
            match_count = sum([
                recipe in time_filtered,
                recipe in mood_filtered,
                recipe in weather_filtered,
                recipe in ingredient_filtered
            ])
            if match_count == 2:
                combined.append((recipe, match_count))

    # Fallback 2: Comfort food
    if not combined:
        combined = [
            (r, 0) for r in all_recipes
            if "comfort" in r.get("mood_tags", []) and r.get("name")
        ][:3]
        st.warning("No strong matches found. Showing top comfort foods instead.")

    # Show results
    st.subheader("🍛 Recommended Recipes")
    for recipe, score in combined:
        st.markdown(f"- **{recipe['name']}**")
