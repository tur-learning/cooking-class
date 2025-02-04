from pasta_recipe import PastaRecipe

# 🌿 Pesto Genovese Recipe
pesto_genovese = PastaRecipe(
    name="Pesto Genovese",
    ingredients={
        "pasta": {"quantity": "200g", "emoji": "🍝"},
        "basil": {"quantity": "50g", "emoji": "🌿"},
        "garlic": {"quantity": "1 clove", "emoji": "🧄"},
        "parmesan cheese": {"quantity": "50g", "emoji": "🧀"},
        "pine nuts": {"quantity": "30g", "emoji": "🌰"},
        "olive oil": {"quantity": "50ml", "emoji": "🫒"},
        "salt": {"quantity": "a pinch", "emoji": "🧂"}
    },
    recipe_steps=[
        {"action": "Boil water", "time": 10, "temperature": 100},
        {"action": "Cook pasta", "time": 10, "temperature": 90},
        {"action": "Pound basil, garlic, and pine nuts", "time": 5},
        {"action": "Mix with olive oil and parmesan cheese", "time": 2},
        {"action": "Combine with pasta", "time": 1}
    ],
    available_ingredients=["pasta", "basil", "garlic", "parmesan cheese", "pine nuts", "olive oil", "salt"]
)
