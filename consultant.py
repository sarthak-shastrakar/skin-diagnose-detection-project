import streamlit as st
from streamlit.components.v1 import html

def app():
    # st.set_page_config(page_title="Consult with Doctor", page_icon="👨‍⚕️", layout="wide")

    # Include Bootstrap CSS
    st.markdown("""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js"></script>
    """, unsafe_allow_html=True)
# Custom CSS for Enhanced Design
    st.markdown("""
        <style>
            .stApp {
                background-image: linear-gradient(to right, #141E30, #243B55);
                color: white;
                font-family: 'Arial', sans-serif;
            }
            .content-container {
                text-align: center;
                max-width: 800px;
                margin: auto;
                background: rgba(255, 255, 255, 0.1);
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
                backdrop-filter: blur(8px);
            }
            .title {
                font-size: 42px;
                font-weight: bold;
                color: #ffcc00;
                text-shadow: 2px 2px 5px rgba(255, 204, 0, 0.8);
            }
            .subtitle {
                font-size: 22px;
                color: #ffffff;
                margin-bottom: 20px;
            }
            .info-card {
                background: rgba(255, 255, 255, 0.1);
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.2);
            }
            .marquee {
                font-size: 18px;
                color: #ffcc00;
                font-weight: bold;
                white-space: nowrap;
                overflow: hidden;
                display: block;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main Content
    # st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.markdown('<div class="title">👨‍⚕️ Consult with a Doctor</div>', unsafe_allow_html=True)
    # st.markdown('<div class="subtitle">Get expert medical advice through live video consultation.</div>', unsafe_allow_html=True)
    st.markdown('<marquee class="marquee">📢 Get instant medical advice and expert consultation anytime, anywhere! 📢</marquee>', unsafe_allow_html=True)

   

    # Bootstrap Card Section
    st.markdown("""
    <div class="container mt-4 mb-4">
        <div class="row">
            <div class="col-md-4">
                <div class="card" style="background: rgba(255, 255, 255, 0.1);">
                    <img src="https://img.freepik.com/free-vector/hospital-service-concept-flat-illustration_1150-50287.jpg?ga=GA1.1.1716491593.1710255249&semt=ais_hybrid" class="card-img-top" alt="Doctor Consultation">
                    <div class="card-body">
                        <h5 class="card-title">Expert Consultation</h5>
                        <p class="card-text">Connect with certified dermatologists for a thorough skin analysis.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="background: rgba(255, 255, 255, 0.1);">
                    <img src="https://img.freepik.com/free-vector/hand-drawn-melanoma-illustration_23-2149357515.jpg?ga=GA1.1.1716491593.1710255249&semt=ais_hybrid" class="card-img-top" alt="AI Skin Analysis">
                    <div class="card-body">
                        <h5 class="card-title">CNN Skin Analysis</h5>
                        <p class="card-text">Utilize AI technology to get a preliminary diagnosis before consulting a doctor.</p>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card" style="background: rgba(255, 255, 255, 0.1);">
                    <img src="https://img.freepik.com/premium-vector/operator-man-working-with-laptop-flat-design-vector-illustration-flyer-design-support-service-concept_551425-2165.jpg?ga=GA1.1.1716491593.1710255249&semt=ais_hybrid" class="card-img-top" alt="AI Skin Analysis">
                    <div class="card-body">
                        <h5 class="card-title">24x7 Support</h5>
                        <p class="card-text">Get access to round-the-clock medical support for urgent skin concerns.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    🏥 **Why Consult a Doctor?**  
    - 📷 **Receive an accurate diagnosis** after CNN-based skin analysis.  
    - ⏳ **Instant medical advice** from certified dermatologists.  
    - 💊 **Personalized treatment recommendations** tailored to your condition.  
    - 🏡 **Convenience at your fingertips** – consult from anywhere.  
    
    🔗 **Click below to start a live video consultation with a doctor.**
    """)

    # Video Consultation Button
    VIDEO_CALL_LINK = "https://conectify-call-frontend.onrender.com"
    st.markdown(f'<a href="{VIDEO_CALL_LINK}" target="_blank"><button style="background:#ffcc00;color:black;padding:15px 30px;border:none;border-radius:8px;font-size:18px;font-weight:bold;cursor:pointer;">📞 Start Consultation</button></a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
