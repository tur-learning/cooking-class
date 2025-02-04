# cooking-class
Cooking with(-in) Python Classes 🥘

### Objective
This assignment is designed to help you practice working with **Git branches**, **object-oriented programming** in Python, and **collaborative code merging**. You’ll extend the existing `PastaRecipe` class to include your very own pasta recipe, then work on a custom branch to commit those changes. Finally, we’ll merge everyone’s work together in class for one giant pasta feast!

---

### Instructions

#### Part 1: Cloning the Repository
1. **Accept the Assignment**  
   - Use the provided link in GitHub Classroom to accept this assignment. This will create your own copy of the repository.

2. **Clone the Repo**  
   - Clone your assignment repository to your local machine:
     ```bash
     git clone <YOUR_REPO_URL>
     ```
   - Change into the repository directory:
     ```bash
     cd <REPO_FOLDER>
     ```

---

#### Part 2: Branching for Your New Recipe
1. **Create a New Branch**  
   - The branch name should be:  
     ```
     studentname-recipename
     ```  
     For example: `alex-smokedsalmonpasta`.
   - Create and switch to your new branch:
     ```bash
     git checkout -b studentname-recipename
     ```

2. **Extend the `PastaRecipe` Class**  
   - Open the files (e.g., `PastaRecipe.py` and/or `main.py`, depending on project structure).
   - Create your **own recipe** by adding:
     - A unique `name` for your pasta dish.
     - A `ingredients` dictionary with quantity and emoji references.
     - A `recipe_steps` list, each step is a dictionary containing `action`, `time`, and (optionally) `temperature`.
     - Update the `available_ingredients` list accordingly.

3. **Instantiate and Cook Your Pasta**  
   - In `main.py`, instantiate your new `PastaRecipe` object with the attributes you’ve created.
   - Call the methods:  
     ```python
     my_recipe.show_ingredients()
     my_recipe.check_ingredients()
     my_recipe.cook_pasta()
     ```
   - Ensure the program prints the steps and any missing ingredients just like the example recipes do.

---

#### Part 3: Committing and Pushing Your Changes
1. **Stage and Commit**  
   - Add your modified files and commit them with a meaningful message:
     ```bash
     git add .
     git commit -m "Add new pasta recipe: <your dish name>"
     ```
2. **Push the Branch**  
   - Push your local branch to GitHub:
     ```bash
     git push -u origin studentname-recipename
     ```

---

### Merge Party in Class
In our next session, we’ll:
1. **Review** each student’s recipe on their custom branch.
2. **Discuss** how to open Pull Requests and merge changes into the main branch.
3. End up with a **multi-recipe** project, where we can cook everyone’s pasta simultaneously!

---

### Additional Guidance
- **Branching**: Always create a new branch when adding features. It helps keep main clean and makes merging simpler.
- **OOP in Python**: Ensure you properly add new attributes or methods if needed. Revisit the `PastaRecipe` structure for guidance.
- **GitHub Documentation**: If you get stuck, refer to  
  - [Creating and using branches](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches)  
  - [Cloning a repository](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

---

### Evaluation
You’ll be assessed on:
1. **Branch Creation**: Correctly named branch and proper usage of Git.
2. **Recipe Accuracy**: A complete set of ingredients, steps, and an instantiation in `main.py`.
3. **Participation**: Merging and discussing your work in the next class.

Enjoy expanding our pasta repertoire! 🍝