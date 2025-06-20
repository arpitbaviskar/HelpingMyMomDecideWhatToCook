import pandas as pd
import json

def process_ingredients(ing):
    return [i.strip().lower() for i in ing.split(",") if i.strip()]

df = pd.read_csv("indian_food.csv")

recipes_json = []
for _, row in df.iterrows():
    recipe = {
        "name": row["name"],
        "tags": [str(row["course"]).lower(), str(row["flavor_profile"]).lower()],
        "ingredients": process_ingredients(row["ingredients"]),
        "mood_tags": ["comfort"],
        "weather_tags": ["any"]
    }
    recipes_json.append(recipe)

with open("recipes_from_csv.json", "w") as f:
    json.dump(recipes_json, f, indent=2)

print("✅ Converted CSV to recipes_from_csv.json")
