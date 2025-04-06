import streamlit as st

def app():
    # Set page config for full width
    # st.set_page_config(layout="wide")

    # Custom CSS with Glassmorphism and transitions
    st.markdown("""
        <style>
            .stApp {
                background: linear-gradient(135deg, #2c003e, #1a1a40, #0f3460);
                color: white;
                font-family: 'Arial', sans-serif;
                user-select: none;
            }

            .title {
                font-size: 45px;
                font-weight: bold;
                color: #FFD700;
                text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.8);
                margin-bottom: 10px;
            }

            .subtitle {
                font-size: 22px;
                font-weight: 500;
                color: #f1f1f1;
                margin-bottom: 20px;
            }

            .section {
                margin-top: 30px;
                padding-top: 20px;
                border-top: 2px solid rgba(255, 255, 255, 0.3);
                font-size: 20px;
                font-weight: bold;
                color: #ffcc00;
            }

            .content {
                font-size: 17px;
                color: #e0e0e0;
                line-height: 1.6;
            }

            .icon {
                font-size: 30px;
                margin-right: 5px;
                color: #FFD700;
            }

            .custom-button {
                display: inline-block;
                padding: 12px 24px;
                margin-top: 20px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                background: linear-gradient(45deg, #ff9800, #ff5722);
                border: none;
                border-radius: 25px;
                cursor: pointer;
                transition: transform 0.2s, background 0.3s;
                text-decoration: none;
            }

            .custom-button:hover {
                transform: scale(1.05);
                background: linear-gradient(45deg, #ff5722, #e91e63);
            }
            </style>
        """, unsafe_allow_html=True)

    # Page Content
    # st.markdown('<div class="glass-container">', unsafe_allow_html=True)

    st.markdown('<div class="title">🩺 DermaCare Hub</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Skin Disease Detection Using ML, CNN & Deep Learning</div>', unsafe_allow_html=True)

    st.markdown('<div class="section"><i class="icon">🔍</i> Overview</div>', unsafe_allow_html=True)
    st.markdown('<p class="content">DermaCare Hub leverages advanced AI, Machine Learning (ML), Deep Learning (DL), and Convolutional Neural Networks (CNNs) technology to detect skin diseases accurately. Using deep learning algorithms, it provides fast and reliable diagnosis, helping users seek timely medical advice.</p>', unsafe_allow_html=True)

    st.markdown('<div class="section"><i class="icon">🚀</i> Key Features</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="content">
        <li>🧠 <b>CNN based Skin Analysis:</b> Deep Learning-based predictions with high accuracy.</li>
        <li>📸 <b>Real-Time Image Processing:</b> Instantly analyze uploaded skin images.</li>
        <li>🤖 <b>AI Chatbot Support:</b> Get instant answers to symptoms & treatments.</li>
        <li>🎥 <b>Live Doctor Consultation:</b> Video conferencing for expert advice.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"><i class="icon">💡</i> How It Works</div>', unsafe_allow_html=True)
    st.markdown("""
    <ol class="content">
        <li><b>Upload</b> an image of the affected skin area.</li>
        <li><b>ML Model Analyzes</b> the image and predicts the condition.</li>
        <li><b>View Diagnosis</b> with confidence levels.</li>
        <li><b>Consult a Dermatologist</b> for further guidance via video call.</li>
    </ol>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"><i class="icon">🔮</i> Future Enhancements</div>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="content">
        <li>✅ <b>Expanded AI Training:</b> Continuous learning with new datasets.</li>
        <li>✅ <b>Mobile App Integration:</b> Bringing AI skin analysis to smartphones.</li>
        <li>✅ <b>Multilingual Support:</b> Breaking language barriers.</li>
        <li>✅ <b>Blockchain for Medical Records:</b> Secure patient history storage.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"><i class="icon">💙</i> Join Us in Revolutionizing Skin Health!</div>', unsafe_allow_html=True)
    st.markdown('<p class="content">**DermaCare Hub** is your **ML&DL-powered skin health assistant**. Take control of your skin health today with advanced **ML, DL, CNN, and AI-driven solutions!**</p>', unsafe_allow_html=True)

    # st.markdown('<a href="#" class="custom-button">Explore More</a>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    app()



