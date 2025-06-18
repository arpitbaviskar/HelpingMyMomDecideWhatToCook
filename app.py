import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("indian_food.csv")
df = df.dropna(subset=['ingredients', 'course', 'region'])

# Clean ingredients
df['ingredients_clean'] = df['ingredients'].str.lower().str.replace('[^a-zA-Z, ]', '', regex=True)
df['course'] = df['course'].str.lower()

# Unique meal types and regions
available_meals = sorted(df['course'].dropna().unique())
available_regions = sorted(df['region'].dropna().unique())

# Ingredient list
common_ingredients = [
    "onion", "tomato", "potato", "rice", "turmeric", "cumin", "mustard", "ginger", "garlic",
    "green chili", "red chili", "salt", "oil", "ghee", "curd", "coriander", "curry leaves",
    "urad dal", "moong dal", "chana dal", "besan", "paneer", "wheat flour", "jeera"
]

# --- Streamlit UI ---
st.title("🍛 Indian Recipe Recommender")
st.subheader("Step 1: Select ingredients you have at home")

selected_ingredients = []
cols = st.columns(3)
for idx, ingredient in enumerate(common_ingredients):
    with cols[idx % 3]:
        if st.checkbox(ingredient):
            selected_ingredients.append(ingredient)

st.subheader("Step 2: Choose meal type")
meal_type = st.selectbox("Meal Type", ["Any"] + available_meals)

st.subheader("Step 3: Choose region")
region_options = ["Any", "North", "South", "East", "West"]
region_type = st.selectbox("Region", region_options)

st.subheader("Step 4: Set number of suggestions per page")
recipes_per_page = st.slider("Recipes per page", min_value=5, max_value=20, step=5, value=5)

st.subheader("Step 5: Select page")
if 'page' not in st.session_state:
    st.session_state.page = 1
page = st.number_input("Page number", min_value=1, value=st.session_state.page, step=1)
st.session_state.page = page

if st.button("Suggest Recipes"):
    if not selected_ingredients:
        st.warning("Please select at least one ingredient.")
    else:
        user_input = ", ".join(selected_ingredients)

        # Normalize region input
        region_map = {
            "North": "north india",
            "South": "south india",
            "East": "east india",
            "West": "west india"
        }

        # Start with all recipes
        filtered_df = df.copy()

        # Step 1: Apply both filters
        if meal_type != "Any":
            filtered_df = filtered_df[filtered_df['course'] == meal_type.lower()]
        if region_type != "Any":
            region_name = region_map.get(region_type, "").lower()
            filtered_df = filtered_df[filtered_df['region'].str.lower() == region_name]

        # Step 2: Relax region if no results
        if filtered_df.empty and meal_type != "Any":
            filtered_df = df[df['course'] == meal_type.lower()]

        # Step 3: Show all if still empty
        if filtered_df.empty:
            filtered_df = df.copy()
            st.warning("No exact match found. Showing best matches based on ingredients only.")

        # TF-IDF similarity
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(filtered_df['ingredients_clean'])
        user_vector = vectorizer.transform([user_input])
        similarities = cosine_similarity(user_vector, tfidf_matrix)

        # Pagination
        start = (page - 1) * recipes_per_page
        end = start + recipes_per_page
        top_indices = similarities.argsort()[0][::-1][start:end]

        top_recipes = filtered_df.iloc[top_indices][['name', 'ingredients', 'course', 'region']]

        if top_recipes.empty:
            st.error("No more recipes on this page.")
        else:
            st.success(f"Showing recipes {start + 1} to {min(end, len(similarities[0]))}:")
            for _, row in top_recipes.iterrows():
                st.markdown(f"### 🍽️ {row['name']}")
                st.markdown(f"**Course:** {row['course'].capitalize()} &nbsp;&nbsp;&nbsp; | &nbsp;&nbsp;&nbsp; **Region:** {row['region'].capitalize()}")
                st.markdown(f"**Ingredients:** {row['ingredients']}")
                st.markdown("---")
