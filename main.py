class PastaRecipe:
    def __init__(self, name, ingredients, recipe_steps, available_ingredients):
        self.name = name  # 🍝 Pasta dish name
        self.ingredients = ingredients  # 🛒 Required ingredients
        self.recipe_steps = recipe_steps  # 📖 List of cooking steps
        self.available_ingredients = available_ingredients  # 🏡 Ingredients we actually have
    
    def show_ingredients(self):
        """Displays the required ingredients for the selected pasta."""
        print(f"📜 Ingredients for {self.name}:")
        for ingredient, details in self.ingredients.items():
            print(f"  - {ingredient}: {details['quantity']} {details['emoji']}")

    def check_ingredients(self):
        """Checks if all required ingredients are available."""
        missing = []
        for ingredient in self.ingredients:
            if ingredient not in self.available_ingredients:
                missing.append(ingredient)
        
        if missing:
            print(f"⚠️ Missing ingredients for {self.name}: {', '.join(missing)} ❌")
        else:
            print(f"✅ You have all ingredients for {self.name}! Let's start cooking! 🍳")

    def cook_pasta(self):
        """Follows the recipe step by step."""
        print(f"👨‍🍳 Cooking {self.name} step by step:")
        for step in self.recipe_steps:
            action = step["action"]
            time = step["time"]
            temp = step.get("temperature", "N/A")  # Some steps may not have temperature
            print(f"🕒 {time} min - {action} (Temp: {temp}°C)")

        print(f"🎉 {self.name} is ready to serve! Enjoy your meal! 🍽️")


# 🎭 Different Pasta Recipes
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

# 🍝 Execute Recipe Steps
print("\n--- Carbonara Recipe ---")
carbonara.show_ingredients()
carbonara.check_ingredients()
carbonara.cook_pasta()

print("\n--- Pesto Genovese Recipe ---")
pesto_genovese.show_ingredients()
pesto_genovese.check_ingredients()
pesto_genovese.cook_pasta()
