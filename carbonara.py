from pasta_recipe import PastaRecipe

# 🎭 Carbonara Recipe
carbonara = PastaRecipe(
    name="Carbonara",
    ingredients={
        "pasta": {"quantity": "200g", "emoji": "🍝"},
        "egg yolk": {"quantity": "2", "emoji": "🥚"},
        "pancetta": {"quantity": "100g", "emoji": "🥓"},
        "pecorino cheese": {"quantity": "50g", "emoji": "🧀"},
        "black pepper": {"quantity": "a pinch", "emoji": "🌶️"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Fry pancetta", "time": 5, "temperature": 160},
        {"action": "Mix egg yolks and cheese", "time": 2},
        {"action": "Combine pasta, pancetta, and sauce", "time": 1}
    ],
    available_ingredients=["pasta", "egg yolk", "pancetta", "pecorino cheese"]  # Missing black pepper
)
