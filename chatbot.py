# import streamlit as st
# import google.generativeai as genai

# # api_key = "AIzaSyD_N7VHKTfjcLXvLvO9eNfTq24EurdfhRI"
# # gemini-1.5-flash

# # Set up Google API Key
# genai.configure(api_key="AIzaSyD_N7VHKTfjcLXvLvO9eNfTq24EurdfhRI")  # Replace with your actual API key
# # Define the chatbot function
# def app():
#     # Page Configuration
#     # st.set_page_config(page_title="AI Chatbot", page_icon="💬", layout="wide")

#     # Custom CSS Styling with Background Image
#     st.markdown("""
#         <style>
#             /* Background Image */
#             .stApp {
#                 # background-image: url("https://img.freepik.com/free-vector/chatbot-concept-background-realistic-style_23-2147831748.jpg?t=st=1742305956~exp=1742309556~hmac=a23b0f7c5d7cbe1b1493da4d38408bc61f6d3208d6b3e43ba66d882205b8ae98&w=826");
#                 # background-size: cover;
#                   background-color: #403060;
#                 background-image: radial-gradient(
#                 circle,
#                 rgba(0, 0, 0, 0) 0%,
#                 rgba(0, 0, 0, 0.8) 100%
#                 );
#                 height:100%;
#                 background-position: center;
#                 background-attachment: fixed;
#                 color: white;
#             }
#             .container{
#             background-color:pink;}

#             /* Chat Container */
#             .chat-container {
#                 max-width: 700px;
#                 margin: auto;
#                 border:2px solid white;
#                 background-color: pink;
#                 padding: 20px;
#                 border-radius: 15px;
#                 color: white;
#             }

#             /* User & Bot Messages */
#             .user-message {
#                 background-color: #007bff;
#                 color: white;
#                 padding: 10px;
#                 border-radius: 10px;
#                 max-width: 75%;
#                 text-align: left;
#                 margin-bottom: 10px;
#             }

#             .bot-message {
#                 background-color: #28a745;
#                 color: white;
#                 padding: 12px;
#                 border-radius: 10px;
#                 max-width: 75%;
#                 text-align: left;
#                 margin-bottom: 10px;
#             }

#             /* Input Box */
#             .stTextInput {
#                 background-color: rgba(255, 255, 255, 0.1);
#                 color: white;
#             }

#             /* Buttons */
#             # .stButton>button {
#             #     border-radius: 8px;
#             #     padding: 10px 15px;
#             #     font-weight: bold;
#             # }
#         </style>
#     """, unsafe_allow_html=True)

#     # Title
#     st.title("💬 AI Chatbot (Gemini)")
#     st.write("🚀 Chat with an AI assistant! Ask anything.")

#     st.markdown('<div class="container">', unsafe_allow_html=True)
#     # Initialize session state for chat history
#     if "messages" not in st.session_state:
#         st.session_state["messages"] = []

#     # Chat Container
#     with st.container():
#         st.markdown('<div class="chat-container">', unsafe_allow_html=True)

#         for message in st.session_state["messages"]:
#             role = "user-message" if message["role"] == "user" else "bot-message"
#             st.markdown(f'<div class="{role}">{message["content"]}</div>', unsafe_allow_html=True)

#         st.markdown("</div>", unsafe_allow_html=True)

#     # User input
#     user_input = st.text_input("Type your message:", key="input")

#     col1, col2 = st.columns([4, 1])  # Layout for Send & Clear buttons

#     with col1:
#         if st.button("Send") and user_input:
#             # Add user message to chat history
#             st.session_state["messages"].append({"role": "user", "content": user_input})

#             # Generate response using Google Gemini AI
#             model = genai.GenerativeModel("gemini-1.5-flash")  # Correct model selection
#             response = model.generate_content(user_input)

#             # Extract bot response
#             bot_response = response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."

#             # Add bot response to chat history
#             st.session_state["messages"].append({"role": "bot", "content": bot_response})

#             # Refresh the page to display new messages
#             st.rerun()

#     with col2:
#         if st.button("Clear Chat"):
#             st.session_state["messages"] = []  # Clear chat history
#             st.rerun()  # Refresh UI

#         st.markdown("</div>", unsafe_allow_html=True)




# ----------------


import streamlit as st
import google.generativeai as genai
from main import load_bootstrap


# Set up Google API Key
genai.configure(api_key="AIzaSyD_N7VHKTfjcLXvLvO9eNfTq24EurdfhRI") 

# Define the chatbot function
def app():
    # Custom CSS Styling
    st.markdown("""
        <style>
            .stApp {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: #e0e0e0;
                background-color: #403060;
                background-image: radial-gradient(
                    circle,
                    rgba(0, 0, 0, 0) 0%,
                    rgba(0, 0, 0, 0.8) 100%
                );
            }
            .chat-container {
                width: 100%;
                max-width: 450px;
                border-radius: 10px;
                background: #212121;
                overflow: hidden;
                display: flex;
                flex-direction: column;
                height: 80vh;
                backdrop-filter: blur(30px);
                background-color: rgba(65, 65, 65, 0.308);
                border: 1px solid rgba(255, 255, 255, 0.089);
            }
        
            .chat-header {
                background: linear-gradient(lightblue, snow);
                color: purple;
                padding: 15px;
                text-align: center;
            }
            .chat-messages {
                flex-grow: 1;
                padding: 20px;
                overflow-y: auto;
            }
            .message {
                display: flex;
                align-items: flex-start;
                margin-bottom: 15px;
            }
            .message-content {
                padding: 10px;
                border-radius: 5px;
                max-width: 70%;
            }
            .user-message {
                flex-direction: row-reverse;
            }
            .user-message .message-content {
                background-color: #4a90e2;
                margin-right: 10px;
            }
            .bot-message .message-content {
                background-color: #3a3a3a;
                margin-left: 10px;
            }
            .chat-input-container {
                display: flex;
                padding: 15px;
                background-color: rgb(186, 222, 234);
            }
            #user-input {
                flex-grow: 1;
                padding: 10px;
                border: 2px solid white;
                border-radius: 5px;

                font-size: 1rem;
                color: #2a5a8a;
                outline: none;
            }
            button {
                color: #090909;
                padding: 0.7em 1.7em; 
                font-size: 18px;
                border-radius: 0.5em;
                background: #e8e8e8;
                cursor: pointer;
                border: 1px solid #e8e8e8;
                transition: all 0.3s;
                # box-shadow: 6px 6px 12px #c5c5c5, -6px -6px 12px #ffffff;
            }
            button:hover {
                border: 1px solid white;
            }
            button:active {
                box-shadow: 4px 4px 12px #c5c5c5, -4px -4px 12px #ffffff;
            }
        </style>
    """, unsafe_allow_html=True)

    # Load Bootstrap
    load_bootstrap()
    # Title
    st.markdown(f'<div class="font-monospace h2 "><div class="d-flex justify-content-left mt-3"><div class="spinner-grow text-primary" role="status"></div>  DermaCare AI Assistant</div>', unsafe_allow_html=True)
    st.write(f'<div class="shadow-none font-monospace p-2 mb-5 bg-body-primary rounded ">🚀 Your Personal Skin Health Consultant – Ask, Learn, and Get Expert Guidance!</div>', unsafe_allow_html=True)
 
    # Initialize session state for chat history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Chat Container
    # st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for message in st.session_state["messages"]:
        role = "user-message" if message["role"] == "user" else "bot-message"
        # st.markdown(f'<div class="message {role}"><div class="message-content">{message["content"]}</div></div>', unsafe_allow_html=True)
        st.markdown(f'<div class="alert alert-primary message {role}" role="alert">{message["content"]}</div>', unsafe_allow_html=True)
    # st.markdown('</div>', unsafe_allow_html=True)

    # User input
    user_input = st.text_input("Type your message:", key="input")
    col1, col2 = st.columns([4, 1])

    with col1:
        if st.button("Send") and user_input:
            st.session_state["messages"].append({"role": "user", "content": user_input})
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            bot_response = response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."
            st.session_state["messages"].append({"role": "bot", "content": bot_response})
            st.rerun()

    with col2:
        if  st.button("🗑️Clear Chat"):
            st.session_state["messages"] = []
            st.rerun()

# Run the chatbot app
if __name__ == "__main__":
    app()