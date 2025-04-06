import streamlit as st


def app():
    st.markdown("""
        <style>
            /* Fullscreen Background */
            .stApp {
                background-image: url("https://img.freepik.com/free-photo/copy-space-glasses-stethoscope-desk_23-2148519795.jpg?t=st=1742308007~exp=1742311607~hmac=3a186984c40ed672d07e52869c9166732f4d3cfe4647e17feaa80de0f8f61cb3&w=1380");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: blue;
            }

            /* Center Content */
            .content-container {
                text-align: center;
                max-width: 800px;
                margin: auto;
                background: rgba(0, 0, 0, 0.7);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
            }

            /* Headings */
            .title {
                font-size: 40px;
                font-weight: bold;
                color: #ffcc00;
                text-shadow: 2px 2px 5px rgba(255, 204, 0, 0.7);
            }

            .subtitle {
                font-size: 20px;
                color: #ffffff;
                margin-bottom: 20px;
            }

            /* Buttons */
            .stButton>button {
                background: linear-gradient(to right, #ffcc00, #ff9900);
                color: black;
                border-radius: 8px;
                padding: 12px 20px;
                font-size: 18px;
                font-weight: bold;
                border: none;
                transition: 0.3s;
            }

            .stButton>button:hover {
                background: #ff6600;
                color: white;
                box-shadow: 0px 0px 15px rgba(255, 102, 0, 0.7);
            }
            .container {
            display:inline-flex;
            flex-direction:row;
            }

            .card {
                background: #ffffff;
                padding: 10px;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                max-width: 400px;
                text-align: center;
                margin: 10px auto;
                transition: transform 0.3s ease-in-out;
            }
            .card:hover {
                transform: scale(1.05);
            }
            .card__title {
                font-size: 22px;
                font-weight: bold;
                color: #333;
                margin: 10px 0;
            }
            .card__description {
                font-size: 14px;
                color: #666;
            }
            .icon {
                height: 50px;
                width: 50px;
                margin: 10px auto;
                color: #4CAF50;
            }



        </style>
    """, unsafe_allow_html=True)

    # Main Content
    st.markdown(
    """
    <h1 style="text-align: center; color: #2c3e50;">🩺 DermaCare Hub</h1>
    <h3 style="text-align: center; color: #7f8c8d;">Your Trusted Partner for Healthy, Glowing Skin</h3>
    <p style="text-align: center; font-size: 18px;">
        🔬 CNN-based skin analysis | 👩‍⚕️ Expert consultations | 💡 Personalized skincare insights
    </p>
    """, unsafe_allow_html=True)


    def display_card_1(img_url, title, text, btn_text, btn_link):
        st.markdown(f"""
    <div class="row container ms-0" >
    <div class="col-sm-6 mb-2 mb-sm-0 " style="width: 23rem;">
    <div class="card ">
    <img src="{img_url}" class="card-img-top" style="border-radius:10px;" alt="{title}">
      <div class="card-body card__content">
        <h5 class="card-title card__title">{title}</h5>
        <p class="card-text card__description">{text}</p>
        <a href="https://www.healthline.com/health/skin/acne?utm_source=chatgpt.com#types-of-acne" class="btn btn-primary">Read Full Article...</a>
      </div>
    </div>
    </div>
    <div class="col-sm-6" style="width: 23rem;margin-left:10px;">
    <div class="card">
    <img src="https://img.freepik.com/premium-photo/woman-with-dry-irritated-skin-hands-showing-dermatitis-symptoms_1274999-7657.jpg" class="card-img-top" alt="Eczema (Atopic Dermatitis)">
      <div class="card-body card__content">
        <h5 class="card-title card__title">Eczema (Atopic Dermatitis)</h5>
        <p class="card-text card__description"> A chronic skin condition causing inflammation, redness, itching, and dryness. It can flare up due to allergens or irritants.</p>
        <a href="https://www.mayoclinic.org/diseases-conditions/atopic-dermatitis-eczema/diagnosis-treatment/drc-20353279" class="btn btn-primary">Read Full Article...</a>
      </div>
    </div>
    </div>
      <div class="col-sm-6 mb-3 mb-sm-0" style="width: 23rem;margin-left:10px;">
    <div class="card" >
    <img src="https://tse3.mm.bing.net/th?id=OIP.Xh_gDAXIvD0w56OG8sye4AHaE8&pid=Api&P=0&h=310" class="card-img-top" alt="Actinic Keratosis">
      <div class="card-body card__content">
        <h5 class="card-title card__title">Actinic Keratosis</h5>
        <p class="card-text card__description">A rough, scaly patch on the skin caused by years of sun exposure, which can sometimes progress to skin cancer (Squamous Cell Carcinoma).</p>
        <a href="https://www.mayoclinic.org/diseases-conditions/actinic-keratosis/symptoms-causes/syc-20354969" class="btn btn-primary">Read Full Article...</a>
      </div>
    </div>
    </div>
    </div>
    """,unsafe_allow_html=True)


    display_card_1("https://tse4.mm.bing.net/th?id=OIP.Vfhfk1iT6WZbrJuWc_WqIwHaE7&pid=Api&P=0&h=180/300", "Acne", "Acne is a common skin condition that occurs when hair follicles get clogged with oil and dead skin cells, leading to pimples, blackheads, and whiteheads.", "Try Now", "#")
    # display_card("https://tse1.mm.bing.net/th?id=OIP.egT9mb1kijfI9EEtK9tdmAHaD4&pid=Api&P=0&h=180/300", "Personalized Skincare", "Customized skincare routines just for you.", "Get Started", "#")



# Run the app function when the script is executed
if __name__ == "__main__":
    app()




















# import streamlit as st
# import base64

# # Function to encode the local background image as base64
# def get_base64_image(image_path):
#     with open(image_path, "rb") as img_file:
#         encoded = base64.b64encode(img_file.read()).decode()
#     return f"data:image/png;base64,{encoded}"

# # Load the Ghibli-style background image
# bg_image = get_base64_image("static/ghibli_bg.jpg")

# # Custom CSS for Styling
# st.markdown(f"""
#     <style>
#         /* Fullscreen Background */
#         .stApp {{
#             background-image: url("{bg_image}");
#             background-size: cover;
#             background-position: center;
#             background-attachment: fixed;
#             color: white;
#             font-family: 'Arial', sans-serif;
#         }}

#         /* Centered Container */
#         .container {{
#             text-align: center;
#             max-width: 900px;
#             margin: auto;
#             background: rgba(0, 0, 0, 0.7);
#             padding: 30px;
#             border-radius: 15px;
#             box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
#         }}

#         /* Headline Styling */
#         .title {{
#             font-size: 45px;
#             font-weight: bold;
#             color: #ffcc00;
#             text-shadow: 2px 2px 10px rgba(255, 204, 0, 0.7);
#         }}

#         .subtitle {{
#             font-size: 20px;
#             color: #ffffff;
#             margin-bottom: 20px;
#         }}

#         /* Bootstrap-like Cards */
#         .card-container {{
#             display: flex;
#             justify-content: center;
#             gap: 20px;
#             flex-wrap: wrap;
#         }}

#         .card {{
#             background: #ffffff;
#             padding: 15px;
#             border-radius: 12px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
#             max-width: 300px;
#             text-align: center;
#             transition: transform 0.3s ease-in-out;
#         }}

#         .card:hover {{
#             transform: scale(1.05);
#         }}

#         .card__image {{
#             width: 100%;
#             height: 180px;
#             object-fit: cover;
#             border-radius: 10px;
#         }}

#         .card__title {{
#             font-size: 22px;
#             font-weight: bold;
#             color: #333;
#             margin-top: 10px;
#         }}

#         .card__description {{
#             font-size: 14px;
#             color: #666;
#         }}

#         .btn {{
#             display: inline-block;
#             margin-top: 10px;
#             padding: 8px 15px;
#             background: linear-gradient(to right, #ffcc00, #ff9900);
#             color: black;
#             font-weight: bold;
#             border-radius: 5px;
#             text-decoration: none;
#             transition: 0.3s;
#         }}

#         .btn:hover {{
#             background: #ff6600;
#             color: white;
#             box-shadow: 0px 0px 10px rgba(255, 102, 0, 0.7);
#         }}

#     </style>
# """, unsafe_allow_html=True)

# # Main Content
# st.markdown(
#     """
#     <div class="container">
#         <h1 class="title">🩺 DermaCare Hub</h1>
#         <h3 class="subtitle">AI-Powered Skin Disease Detection for a Healthier You</h3>
#         <p style="font-size: 18px;">
#             Our cutting-edge AI model, powered by **CNN, ML, and DL**, analyzes skin images 
#             to detect potential conditions. Get **fast, accurate, and reliable** skin disease insights 
#             at your fingertips!
#         </p>
#         <p>🔬 AI-based skin analysis | 👩‍⚕️ Virtual consultations | 💡 Personalized skincare tips</p>
#     </div>
#     """, unsafe_allow_html=True
# )

# # Display Bootstrap-like Cards
# st.markdown(
#     """
#     <div class="card-container">

#         <div class="card">
#             <img class="card__image" src="https://tse4.mm.bing.net/th?id=OIP.Vfhfk1iT6WZbrJuWc_WqIwHaE7&pid=Api&P=0&h=180/300" alt="Acne">
#             <h5 class="card__title">Acne Detection</h5>
#             <p class="card__description">AI-powered acne detection helps identify different types of acne and suggests treatments.</p>
#             <a href="https://www.healthline.com/health/skin/acne" class="btn">Learn More</a>
#         </div>

#         <div class="card">
#             <img class="card__image" src="https://img.freepik.com/premium-photo/woman-with-dry-irritated-skin-hands-showing-dermatitis-symptoms_1274999-7657.jpg" alt="Eczema">
#             <h5 class="card__title">Eczema Insights</h5>
#             <p class="card__description">Detect and understand eczema symptoms to manage flare-ups effectively.</p>
#             <a href="https://www.mayoclinic.org/diseases-conditions/atopic-dermatitis-eczema" class="btn">Learn More</a>
#         </div>

#         <div class="card">
#             <img class="card__image" src="https://tse3.mm.bing.net/th?id=OIP.Xh_gDAXIvD0w56OG8sye4AHaE8&pid=Api&P=0&h=310" alt="Actinic Keratosis">
#             <h5 class="card__title">Skin Cancer Screening</h5>
#             <p class="card__description">Identify early signs of Actinic Keratosis and prevent future complications.</p>
#             <a href="https://www.mayoclinic.org/diseases-conditions/actinic-keratosis" class="btn">Learn More</a>
#         </div>

#     </div>
#     """, unsafe_allow_html=True
# )
