import os
import requests
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("SPOONACULAR_API_KEY")

if not API_KEY:
    raise ValueError("SPOONACULAR_API_KEY not found in .env file")


def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak ingredients clearly (comma-separated)...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return [i.strip() for i in text.split(",") if i.strip()]
    except:
        print("Voice recognition failed.")
        return []


def get_nutrition(recipe_id):
    try:
        response = requests.get(
            f"https://api.spoonacular.com/recipes/{recipe_id}/nutritionWidget.json",
            params={"apiKey": API_KEY},
            timeout=10
        )
        response.raise_for_status()
        data = response.json()

        return {
            "calories": data.get("calories", "N/A"),
            "carbs": data.get("carbs", "N/A"),
            "protein": data.get("protein", "N/A"),
            "fat": data.get("fat", "N/A")
        }
    except:
        return None


def passes_diet_filter(recipe, diet_choice):
    title = recipe["title"].lower()
    non_veg_keywords = ["chicken", "beef", "pork", "fish", "mutton", "shrimp"]
    dairy_keywords = ["milk", "cheese", "egg", "butter"]

    if diet_choice == "2":
        return not any(word in title for word in non_veg_keywords)

    if diet_choice == "3":
        return not any(word in title for word in non_veg_keywords + dairy_keywords)

    return True


def get_recipe(ingredients):
    print("\nSelect Diet Preference:")
    print("1. None")
    print("2. Vegetarian")
    print("3. Vegan")

    diet_choice = input("Enter choice (1-3): ").strip()

    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,
        "ranking": 1,
        "ignorePantry": True,
        "apiKey": API_KEY
    }

    try:
        response = requests.get(
            "https://api.spoonacular.com/recipes/findByIngredients",
            params=params,
            timeout=10
        )
        response.raise_for_status()
        recipes = response.json()
    except requests.exceptions.RequestException as e:
        print("API Error:", e)
        return

    if not recipes:
        print("No recipes found.")
        return

    recipes = sorted(recipes, key=lambda x: len(x.get("missedIngredients", [])))

    print("\nTop Recipes:\n")

    count = 0

    for recipe in recipes:
        if not passes_diet_filter(recipe, diet_choice):
            continue

        if count == 3:
            break

        print("=" * 60)
        print(f"🍽 Recipe: {recipe['title']}")
        print("=" * 60)

        used = [i["name"] for i in recipe.get("usedIngredients", [])]
        missed = [i["name"] for i in recipe.get("missedIngredients", [])]

        print("✅ You Have:", ", ".join(used) if used else "None")
        print("❌ You Need:", ", ".join(missed) if missed else "Nothing!")

        print(f"\n🔗 Link:")
        print(f"https://spoonacular.com/recipes/{recipe['title'].replace(' ', '-')}-{recipe['id']}")

        nutrition = get_nutrition(recipe["id"])
        if nutrition:
            print("\n📊 Nutrition:")
            print(f"Calories: {nutrition['calories']}")
            print(f"Carbs: {nutrition['carbs']}")
            print(f"Protein: {nutrition['protein']}")
            print(f"Fat: {nutrition['fat']}")

        print("\n")
        count += 1


if __name__ == "__main__":
    print("Smart Recipe Assistant")
    print("----------------------")

    choice = input("Enter 1 to type ingredients or 2 to speak: ").strip()

    if choice == "2":
        ingredients = get_voice_input()
    else:
        ingredients = input("Enter ingredients (comma-separated): ").split(",")
        ingredients = [i.strip() for i in ingredients if i.strip()]

    if ingredients:
        get_recipe(ingredients)
    else:
        print("No valid ingredients provided.")