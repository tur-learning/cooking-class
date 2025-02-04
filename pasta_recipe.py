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
