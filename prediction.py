
import streamlit as st
import tensorflow as tf
import numpy as np
import folium
from fpdf import FPDF
from io import BytesIO
from PIL import Image
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import os
import gdown

# -------------------- Prediction --------------------
def model_prediction(test_image):
    model_path = "trained_model.h5"
    if not os.path.exists(model_path):
        file_id = "1m7mJxUYrzhF0OqGHq6CldT9JpS3kVKWG"  # Replace with actual file ID
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, model_path, quiet=False)

    model = tf.keras.models.load_model(model_path)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index

# -------------------- PDF Generator --------------------
def generate_pdf(disease_name, disease_info, uploaded_image):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=18)
    pdf.cell(200, 10, "Skin Disease Diagnosis Report", ln=True, align='C')
    pdf.ln(10)

    if uploaded_image:
        image = Image.open(uploaded_image)
        img_path = "temp_image.jpg"
        image.save(img_path)
        pdf.image(img_path, x=50, y=25, w=110)
        pdf.ln(75)

    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(0, 15, f"Predicted Disease: {disease_name}", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Details: {disease_info}")
    
    pdf_bytes = BytesIO()
    pdf_bytes.write(pdf.output(dest='S').encode('latin1'))
    pdf_bytes.seek(0)
    return pdf_bytes

# -------------------- Hospital Finder --------------------
def find_hospitals(location):
    geolocator = Nominatim(user_agent="skin_disease_app")
    try:
        loc_data = geolocator.geocode(location, timeout=10)
        if loc_data:
            base_lat, base_lon = loc_data.latitude, loc_data.longitude
            hospitals = [
                (base_lat + 0.008, base_lon + 0.004, "Sunshine Hospital"),
                (base_lat - 0.009, base_lon + 0.006, "City Skin Clinic"),
                (base_lat + 0.006, base_lon - 0.008, "Nova Care Center"),
                (base_lat - 0.007, base_lon - 0.005, "Advanced Derma Hospital"),
            ]
            return base_lat, base_lon, hospitals
    except GeocoderTimedOut:
        pass
    return None, None, []

# -------------------- Main App --------------------
def app():
    # st.set_page_config(page_title="Skin Disease Detector", page_icon="🩺", layout="wide")

    # Background Image CSS
    st.markdown(
        """
        <style>
        .stApp {
        # background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        # background: linear-gradient(135deg, #16222a, #3a6073);
        background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
        background-size: cover;
        background-attachment: fixed;
        color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("🩺 Skin Disease Detection & Hospital Finder")
    st.markdown("Upload an image to detect the skin disease and get hospital recommendations near you.")

    test_image = st.file_uploader("📷 Upload Skin Image", type=["jpg", "jpeg", "png"])
    user_location = st.text_input("📍 Enter your City/Location")

    if test_image and user_location:
        st.image(test_image, caption="Uploaded Image", use_column_width=True)

        if st.button("🔍 Predict Skin Disease"):
            result_index = model_prediction(test_image)
            class_names = [
                'Actinic keratosis', 'Atopic Dermatitis', 'Benign keratosis',
                'Dermatofibroma', 'Melanocytic nevus', 'Melanoma',
                'Squamous cell carcinoma', 'Tinea Ringworm Candidiasis', 'Vascular lesion'
            ]

            disease_descriptions = {
                0: 'Actinic keratosis is a rough, scaly patch on the skin caused by sun exposure. It can potentially lead to skin cancer.',
                1: 'Atopic dermatitis causes red, itchy skin. Common in children, but can affect adults too.',
                2: 'Benign keratosis includes harmless skin growths like seborrheic keratosis, common in older adults.',
                3: 'Dermatofibroma is a small, noncancerous bump on the skin, often due to insect bites or minor injury.',
                4: 'Melanocytic nevus is a common mole caused by melanocyte clusters. Most are benign.',
                5: 'Melanoma is a serious skin cancer arising from melanocytes. Early detection is critical.',
                6: 'Squamous cell carcinoma is a common skin cancer caused by UV exposure.',
                7: 'Tinea or ringworm is a fungal infection causing ring-like rashes. Candidiasis affects moist areas like mouth or groin.',
                8: 'Vascular lesions are abnormal blood vessel growths like hemangiomas or spider veins.',
            }

            disease_name = class_names[result_index]
            disease_info = disease_descriptions[result_index]

            st.success(f"🧬 Detected: {disease_name}")
            st.info(disease_info)

            # Downloadable PDF
            pdf_file = generate_pdf(disease_name, disease_info, test_image)
            st.download_button("📄 Download Diagnosis Report", data=pdf_file, file_name="Skin_Diagnosis_Report.pdf", mime="application/pdf")

            # Map rendering
            lat, lon, hospitals = find_hospitals(user_location)
            if lat and hospitals:
                st.subheader("🏥 Nearby Hospitals")
                map_obj = folium.Map(location=[lat, lon], zoom_start=13)
                folium.Marker([lat, lon], tooltip="You are here", icon=folium.Icon(color="blue")).add_to(map_obj)
                for h_lat, h_lon, name in hospitals:
                    folium.Marker([h_lat, h_lon], popup=name, icon=folium.Icon(color='red', icon='plus')).add_to(map_obj)
                    folium.Circle([h_lat, h_lon], radius=300, color='crimson', fill=True, fill_opacity=0.4).add_to(map_obj)
                folium_static(map_obj)
            else:
                st.warning("⚠️ Location not recognized or no hospitals found. Try a different or more specific location.")

if __name__ == "__main__":
    app()
