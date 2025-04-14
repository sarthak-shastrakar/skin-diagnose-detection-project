import streamlit as st
def app():
    st.markdown("""
        <style>
            /* Fullscreen Background */
            .stApp {
                background-image: url("https://img.freepik.com/free-vector/abstract-medical-wallpaper-template-design_53876-61808.jpg?ga=GA1.1.1716491593.1710255249&semt=ais_hybrid&w=740");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: blue;
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

            .card {
                background: linear-gradient(135deg, #16222a, #3a6073);
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
    <div class="row col-sm-12 container" >
    <div class="col-sm-6 mb-2 mb-sm-0 ">
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
