# Import necessary libraries
import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "mission-082024"  # Make sure you have a project called "Gemini-Sample"
vertexai.init(
    project = project
)

config = generative_models.GenerationConfig(
    temperature = 0.4
)

# Load model with config
model = GenerativeModel(
    "gemini-pro",
    generation_config = config
)

chat = model.start_chat() 

# Helper function to to display and send streamlit messages
def llm_function(chat: ChatSession, query, user_name):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text
    
    # Personalize the response
    if user_name:
        output = f"Hello {user_name}! " + output
    
    with st.chat_message('model'):
        st.markdown(output)
        
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": output
        }
    )
    
# Set the title
st.title("Gemini Explorer")

# User name input
user_name = st.text_input("Please enter your name")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display and load chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
            role = message["role"],
            parts = [ Part.from_text(message["content"]) ]
        )
    
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    chat.history.append(content)

# For initial message startup
if len(st.session_state.messages) == 0:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": "Hi, I'm Gemini Explorer. How can I help you today?"
        }
    )
    st.session_state.messages.append(
        {
            "role": "model",
            "content": "Hello! I'm here to help you explore the Gemini universe."
        }
    )
    
# Get user input and call llm_function
query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
        
    llm_function(chat, query, user_name)
    
if len(st.session_state.messages) == 0:
   # initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    
    pirate_themed_initial_Prompt: "Arrr, matey! I be ReX, the jolly assistant powered by Google Gemini. I'll be talkin' to ye in emojis to keep things lively and interactive. What be yer name, landlubber?" # type: ignore
    
    llm_function(chat, pirate_themed_initial_Prompt, user_name)