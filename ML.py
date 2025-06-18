# this is for ml 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

user_input = "potato, onion, tomato, rice, turmeric, cumin"


recipe_ingredients = df['ingredients']

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(recipe_ingredients)
user_vector = vectorizer.transform([user_input])
similarities = cosine_similarity(user_vector, tfidf_matrix)
top_indices = similarities.argsort()[0][-5:][::-1]
df.iloc[top_indices][['name', 'ingredients', 'meal_type']]