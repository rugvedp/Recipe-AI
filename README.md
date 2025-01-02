# Recipe AI: Your AI-Powered Recipe Assistant with CrewAI and llama

**Description:**

Recipe AI leverages the power of CrewAI and Agentic AI to assist you in creating delicious and personalized meals.

**Key Features:**

-   **Ingredient Image Recognition:** Upload an image of your ingredients, and Recipe AI will identify them using computer vision.
-   **Dietary Preference Consideration:** Select your dietary preferences (vegetarian or non-vegetarian), and Recipe AI will generate recipes tailored to your needs.
-   **Recipe Generation:** Based on the identified ingredients and your preferences, Recipe AI suggests a delicious and feasible recipe.
-   **Nutritional Analysis:** Get detailed nutritional information about the generated recipe, including calories, fats, and proteins.

![Screenshot 2025-01-02 112721](https://github.com/user-attachments/assets/d6ce11aa-9c2d-481f-9208-209dfc92e6a1)
![Screenshot 2025-01-02 112756](https://github.com/user-attachments/assets/acc77ac2-349d-4663-a408-bab06fdfc766)
![Screenshot 2025-01-02 112805](https://github.com/user-attachments/assets/03e30ddc-2c73-4cb3-ab9d-5785db26e017)


**Workflow:**

1.  **Image Upload:** The user uploads an image of ingredients through a Streamlit interface.
2.  **Image Analysis (Image Analyzer Agent):** An AI agent specialized in image recognition analyzes the uploaded image and extracts a list of ingredients. This agent is defined with a specific role, goal, and backstory to guide its behavior.
3.  **Recipe Generation (Recipe Predictor Agent):** Another AI agent, acting as a "Grand Master Chef," receives the list of ingredients and the user's dietary preference. It then generates a recipe using only the provided ingredients.
4.  **Nutritional Analysis (Indian Dietitian Agent):** A third AI agent, acting as a "Dietitian Specialist," analyzes the generated recipe and provides detailed nutritional information.
5.  **Output:** The generated recipe and its nutritional information are displayed to the user.

**Key Components:**

-   **Agents:**
    -   `image_analyzer`: Responsible for analyzing images and identifying ingredients. Uses a large language model (LLM) for image understanding.
    -   `recipe_predictor`: Responsible for generating recipes based on ingredients and dietary preferences. Also uses an LLM.
    -   `indian_dietitian`: Responsible for providing nutritional analysis of the generated recipe. Uses an LLM.
-   **Tasks:**
    -   `analyze_image_task`: Defines the task for the `image_analyzer` agent.
    -   `generate_recipe_task`: Defines the task for the `recipe_predictor` agent.
    -   `nutritional_analysis_task`: Defines the task for the `indian_dietitian` agent.
-   **Crew:** The `Crew` object orchestrates the execution of the agents and tasks in a sequential process.
-   **Streamlit Interface:** Provides a user-friendly interface for image uploads and displaying results.


**Installation:**

While this project utilizes CrewAI and Agentic AI services, you can still learn from its structure and adapt it to similar AI libraries.

**Usage:**

1.  Clone this repository.
2.  Set up your GROQ_API_KEY and GEMINI_API_KEY using environment variables. Refer to their documentation for specific instructions.
3.  Run the `main.py` script.
4.  Upload an image of your ingredients using the Streamlit interface.
5.  Select your dietary preference.
6.  Recipe AI will analyze the image, generate a recipe suggestion, and provide nutritional information.

**Dependencies:**

-   CrewAI ([https://crew.ai/](https://crew.ai/))
-   Streamlit ([https://streamlit.io/](https://streamlit.io/))
-   Pillow (PIL Fork) ([https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/))

**Development Setup:**

1.  Install the required dependencies using `pip install crewai crewai_tools pillow streamlit`.
2.  Set up your GROQ_API_KEY, GEMINI_API_KEY
3.  Run `streamlit run main.py` to launch the Streamlit app.

**Contributing:**

We welcome contributions to this project! Please create a pull request to share your improvements.

**License:**

This project is licensed under the MIT License (see LICENSE.md for details).

