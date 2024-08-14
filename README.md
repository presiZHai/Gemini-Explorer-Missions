# Gemini-Explorer-Missions

## Presentation and Demo

- **Presentation Slides:** [View Presentation](https://app.pitch.com/app/presentation/05c2f455-37c5-4a07-9eee-433ea410f602/e8c8ddb1-59b5-4322-bfa1-a76fcc1c9164)
- **Video Demo:** [Watch Video](https://www.loom.com/share/1ec832c8a6f54e2aaa0c5605cb9b5a7a?sid=e0946c44-4754-42f9-87c5-6e93839ba63b)

## Gemini Explorer

### Overview
Gemini Explorer is an interactive chat interface that utilizes Google's advanced large language model, Gemini, to facilitate an accessible exploration of LLM applications. This project showcases how to integrate Google's generative models into a Streamlit-based application, providing a seamless user experience to interact with cutting-edge language processing technologies.

### Technology Stack
  * Google's Vertex AI Platform: Enables advanced machine learning capabilities using pre-trained models.
  * Streamlit: A powerful framework for building and deploying interactive web applications in Python.
  * Python 3.10: The programming language used for developing this application.

### Key Features
  * User-Friendly Chat Interface: A responsive chat interface designed for ease of interaction with the Gemini model.
  * Customized Responses: The chat interface personalizes responses based on user input, enhancing the user experience.
  * Configurable Model Settings: Ability to adjust model parameters such as temperature for fine-tuning response creativity and relevance.
  * Session History: Keeps track of the conversation history within the session, allowing for context-aware interactions.

### Installation
  
#### Prerequisites
* Python 3.10
* Streamlit
* Google Vertex AI Platform

#### Step-by-Step Installation Guide
1. Clone the GitHub Repository - Open your terminal and clone the project repository:

```bash
    git clone https://github.com/presiZHai/Gemini-Explorer-Missions.git
```

2. Create and Activate Virtual Environment - Navigate to the project directory, create a virtual environment, and activate it:

```bash
    conda create -p ./env python==3.10 -y
```

```bash
    conda activate ./env
```

3.  Install Requirements - Install the required Python packages:

```bash
    pip install -r requirements.txt
```

4. Run the Streamlit App - Launch the Streamlit application and view it in your browser at http://localhost:8501:

```bash
    streamlit run gemini_explorer.py
```

### Usage
#### GCloud authentication
* Create a new Google Cloud project.
* Enable the Vertex AI API for the project.
* Create a service account with necessary roles (e.g., Owner, AI Platform Admin, Vertex AI Administrator, Vertex AI Model Creator).
* Initialize Google Cloud in the terminal with `gcloud init`, follow the steps shown in the terminal, and run `gcloud auth application-default login` to log in to your Google Cloud account.


#### Importing Necessary Libraries - Ensure all necessary libraries are imported:

```bash
    import vertexai
    import streamlit as st
    from vertexai.preview import generative_models
    from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
```

#### Initializing the Vertex AI Model - Set up the project configuration and initialize the Gemini model:

```bash
    project = "project-id"  # The project id in the google.cloud console
    vertexai.init(project=project)

    config = generative_models.GenerationConfig(
    temperature=0.4
    )

    model = GenerativeModel(
    "gemini-pro",
    generation_config=config
    )

    chat = model.start_chat()
```
#### Creating the Chat Interface - Use Streamlit to build the interactive chat interface:

```bash
    # Helper function to display and send Streamlit messages
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
        role=message["role"],
        parts=[Part.from_text(message["content"])]
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
```

#### Sample Interaction
Upon running the app, users are greeted and prompted to enter their queries. The model responds with informative and context-aware answers. Personalization is integrated, providing a friendly and engaging interaction.

### Contribution
We welcome contributions to enhance the features and functionality of Gemini Explorer. Please follow these steps to contribute:
    1. Fork the repository.
    2. Create a new branch for your feature or bug fix.
    3. Commit your changes and push them to your branch.
    4. Open a pull request with a detailed description of your changes.

### License
This project is licensed under the MIT License. See the LICENSE file for more details.

### Contact
For any questions or feedback, feel free to reach out at abiodungndj@gmail.com.