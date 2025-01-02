from crewai import Agent, Task, Crew, Process, LLM
import os
import streamlit as st
from PIL import Image
import warnings


warnings.filterwarnings('ignore')
os.environ['GROQ_API_KEY'] = ''


#Agents
image_analyzer = Agent(
    llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.7
    ),
    role="Image Recognition Specialist",
    goal="Analyze {img} an ingredient image and identify the items present in the image. Do it precisely",
    backstory=(
        "You are an AI trained in computer vision and have expertise in recognizing "
        "food items from images. You excel in identifying ingredients with precision."
        ""
    ),
    verbose=True
)

recipe_predictor = Agent(
    llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.7
),
    role="Indian Grand Master Chef",
    goal="Analyze the list of ingredients and generate the possible recipe which user can cook only using these items. No extra items. Also remember that user is {veg} person.",
    backstory=(
        "You are an Indian Master Chef who can cook any recipe from the given ingridents"
        "food items and generating recipes based on available ingredients."
        "You always cook variety of recipes to your customers"
    ),
    verbose=True
)

indian_dietitian = Agent(
    llm = LLM(
    model="groq/llama3-8b-8192",
    temperature=0.7
),
    role="Indian Dietitian Specialist",
    goal="Analyze the recipe and provide detailed nutritional information including calories, fats, and proteins.",
    backstory=(
        "You are an AI trained in nutrition science with expertise in Indian cuisine. "
        "You excel in analyzing recipes and providing detailed nutritional information."
    ),
    verbose=True
)



#Tasks
analyze_image_task = Task(
    description="Analyze the uploaded image of ingredients and return a list of items.",
    expected_output="A structured list of identified ingredients with quantity only. No extra information",
    agent=image_analyzer,
)

generate_recipe_task = Task(
    description="Analyze the list of ingredients and generate a possible recipe for the user, considering their dietary preferences.",
    expected_output="A recipe suggestion based on the identified ingredients and user's preferences.",
    agent=recipe_predictor,
)

nutritional_analysis_task = Task(
    description="Analyze the generated recipe and provide detailed nutritional information including calories, fats, and proteins.",
    expected_output="A structured list of nutritional information for the recipe with the list of ingridents, recipe name and the recipe cooking procedure.",
    agent=indian_dietitian,
)


#Crew
crew = Crew(
    agents=[image_analyzer, recipe_predictor, indian_dietitian ],
    tasks=[analyze_image_task, generate_recipe_task, nutritional_analysis_task],
    process=Process.sequential, 
)


def save_uploaded_image(uploaded_image, save_folder="uploaded_images"):

    os.makedirs(save_folder, exist_ok=True)
    image_path = os.path.join(save_folder, uploaded_image.name)

    with open(image_path, "wb") as f:
        f.write(uploaded_image.getbuffer())
    
    return image_path

def main():
    st.title("Recipe Assistant")

    uploaded_image = st.file_uploader("Upload an image of ingredients", type=["jpg", "jpeg", "png"])
    if uploaded_image is not None:
        image_path = save_uploaded_image(uploaded_image)
        
        image = Image.open(image_path)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Image successfully uploaded and saved!")

        dietary_preference = st.radio(
            "Select your dietary preference:",
            ("Vegetarian", "Non-Vegetarian")
        )

        if dietary_preference:
            st.write(f"Processing the image for a {dietary_preference} recipe...")
            
            inputs = {"img": image_path, "veg": dietary_preference}
            result = crew.kickoff(inputs=inputs)
            st.write(result.raw)

if __name__ == "__main__":
    main()