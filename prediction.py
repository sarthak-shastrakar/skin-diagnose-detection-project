
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

# def model_prediction(test_image):
#     model_path = r"skin_disease_detection/trained_model.h5"
#     model = tf.keras.models.load_model(model_path)

#     image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
#     input_arr = tf.keras.preprocessing.image.img_to_array(image)
#     input_arr = np.array([input_arr])

#     prediction = model.predict(input_arr)
#     result_index = np.argmax(prediction)
#     confidence_score = np.max(prediction) * 100
#     return result_index 
    
def model_prediction(test_image):
    model_path = "trained_model.h5"
    
    # Download the model if it doesn't already exist
    if not os.path.exists(model_path):
        file_id = "1m7mJxUYrzhF0OqGHq6CldT9JpS3kVKWG"  # Replace this with your actual file ID
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, model_path, quiet=False)

    # Load and predict
    model = tf.keras.models.load_model(model_path)
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(256, 256))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])
    prediction = model.predict(input_arr)
    result_index = np.argmax(prediction)
    return result_index
    
def generate_pdf(disease_name, disease_info, uploaded_image):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", style='B', size=18)
    pdf.cell(200, 10, "Skin Disease Diagnosis Report", ln=True, align='C')
    pdf.ln(10)

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        image_path = "temp_uploaded_image.jpg"
        image.save(image_path)
        pdf.image(image_path, x=50, y=25 , w=110)
        pdf.ln(75)

    pdf.set_font("Arial", style='B', size=15)
    pdf.cell(0, 25, f"Predicted Disease Name: {disease_name}", ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=13)
    pdf.multi_cell(0, 10, f"Detail Info: {disease_info}")
    pdf.ln(10)
    
    pdf_bytes = BytesIO()
    pdf_bytes.write(pdf.output(dest='S').encode('latin1'))
    pdf_bytes.seek(0)
    return pdf_bytes

def find_hospitals(location):
    geolocator = Nominatim(user_agent="hospital_locator")
    try:
        location_data = geolocator.geocode(location, timeout=10)
        if location_data:
            hospitals = [
                (location_data.latitude + 0.01, location_data.longitude, "City Hospital"),
                (location_data.latitude - 0.01, location_data.longitude + 0.01, "Medical Care Center"),
                (location_data.latitude, location_data.longitude - 0.02, "Health Clinic"),
                (location_data.latitude + 0.015, location_data.longitude - 0.01, "Advanced Skin Care Hospital")
            ]
            return location_data.latitude, location_data.longitude, hospitals
    except GeocoderTimedOut:
        return None, None, []
    return None, None, []

def app():
    st.title("🩺 Skin Disease Recognition")
    st.write("Upload an image to detect skin disease and find nearby hospitals.")
    
    test_image = st.file_uploader("📷 Choose an image for analysis", type=['png', 'jpg', 'jpeg'])
    user_location = st.text_input("📍 Enter your location (e.g., city name)")
    
    if test_image and user_location:
        st.image(test_image, caption="Uploaded Image", use_column_width=True)
        
        if st.button("🔍 Predict Disease"):
            result_index = model_prediction(test_image)
            
            class_name = [
                'Actinic keratosis', 'Atopic Dermatitis', 'Benign keratosis',
                'Dermatofibroma', 'Melanocytic nevus', 'Melanoma',
                'Squamous cell carcinoma', 'Tinea Ringworm Candidiasis', 'Vascular lesion'
            ]
            
            disease_info = {
                0: 'Actinic keratosis is a rough, scaly patch on the skin caused by prolonged sun exposure.It often appears on areas frequently exposed to the sun, such as the face, ears, scalp, and hands.These lesions can be red, pink, or brown and may feel dry or rough.Although not cancerous, actinic keratosis has the potential to develop into squamous cell carcinoma.Treatment options include cryotherapy (freezing), topical medications, and laser therapy.',
                1: 'Atopic dermatitis is a chronic inflammatory skin condition that causes dry, red, itchy skin, often leading to rashes or cracks. It can be triggered by allergens, irritants, stress, or weather changes, and is commonly seen in children but can persist into adulthood. Genetic factors, a weakened skin barrier, and immune system dysfunction contribute to its development. Preventing flare-ups involves keeping the skin moisturized, using mild soaps, avoiding allergens (such as dust and pet dander), and wearing soft, breathable fabrics.',
                2: 'A non-cancerous skin growth.Benign keratosis refers to non-cancerous skin growths, including seborrheic keratosis, which appear as rough, wart-like, brown or black patches. These growths are common in older adults and result from aging, genetic predisposition, and sun exposure. They are harmless but may be removed for cosmetic reasons. Prevention includes avoiding excessive sun exposure, maintaining good skincare habits, and using sunscreen to minimize sun-induced skin damage.',
                3: 'A benign fibrous nodule.Dermatofibromas are firm, small, reddish-brown nodules that commonly appear on the legs and arms. They develop due to an overgrowth of fibrous tissue in response to minor skin injuries such as insect bites or cuts. These nodules are usually painless but may feel tender when touched. While harmless, they can be removed surgically if they become bothersome. Prevention includes protecting the skin from injuries, maintaining proper hygiene, and avoiding excessive scratching or irritation.',
                4: 'A benign growth caused by melanocyte clusters.A melanocytic nevus, commonly known as a mole, is a benign skin growth caused by clusters of melanocytes (pigment-producing cells). Moles can be present from birth or develop later due to genetic factors and sun exposure. While most moles are harmless, changes in size, shape, or color may indicate melanoma, a dangerous form of skin cancer. Prevention includes limiting sun exposure, using sunscreen, and regularly monitoring moles for any abnormal changes.',
                5: 'A serious type of skin cancer.Melanoma is an aggressive form of skin cancer that develops in melanocytes, the cells responsible for skin pigmentation. It often appears as an irregularly shaped, dark-colored mole with uneven borders. Prolonged UV radiation exposure, fair skin, and a family history of melanoma are major risk factors. Early detection is crucial, as melanoma can spread rapidly. Prevention includes wearing protective clothing, applying broad-spectrum sunscreen, avoiding tanning beds, and performing regular skin checks to detect any suspicious changes.',
                6: 'A common form of skin cancer.Squamous cell carcinoma (SCC) is a common type of skin cancer that occurs due to uncontrolled growth of squamous cells in the skin"s outer layer. It often appears as scaly, red patches, open sores, or thickened skin on sun-exposed areas. The main causes are prolonged UV exposure, weakened immune systems, and exposure to harmful chemicals. Prevention includes using sunscreen, wearing sun-protective clothing, and avoiding excessive sun exposure, especially during peak hours.',
                7: 'A fungal infection of the skin.Tinea, commonly known as ringworm, is a contagious fungal infection that affects the skin, scalp, or nails, causing red, itchy, ring-shaped rashes. Candidiasis, caused by Candida fungi, often affects moist areas such as the mouth, groin, and under the breasts, leading to redness, itching, and discomfort. These infections spread through direct contact with infected individuals, animals, or contaminated objects. Prevention includes maintaining proper hygiene, keeping skin dry, avoiding sharing personal items, and using antifungal powders or creams when necessary.',
                8: 'An abnormality of the skin due to blood vessels.Vascular lesions are abnormalities of blood vessels that can appear as birthmarks, hemangiomas, or spider veins. They result from genetic factors, hormonal changes, or excessive sun exposure. While usually harmless, some vascular lesions may require laser therapy or medical treatment for cosmetic or medical reasons. Prevention includes avoiding prolonged sun exposure, using sunscreen, and leading a healthy lifestyle to maintain good vascular health.'
            }
            
            disease_name = class_name[result_index]
            st.success(f"✅ Prediction: {disease_name}")
            st.write(f"ℹ️ {disease_info[result_index]}")
            
            pdf_bytes = generate_pdf(disease_name, disease_info[result_index], test_image)
            st.download_button("📄 Download PDF Report", data=pdf_bytes, file_name="Diagnosis_Report.pdf", mime="application/pdf")
            
            lat, lon, hospitals = find_hospitals(user_location)
            
            if hospitals:
                st.subheader("🏥 Nearby Hospitals")
                m = folium.Map(location=[lat, lon], zoom_start=14, tiles='OpenStreetMap', attr='© OpenStreetMap contributors')
                folium.Marker([lat, lon], popup="Your Location", icon=folium.Icon(color='blue', icon='cloud')).add_to(m)
                
                for hosp_lat, hosp_lon, hosp_name in hospitals:
                    folium.Marker([hosp_lat, hosp_lon], popup=hosp_name, icon=folium.Icon(color='red', icon='plus-square')).add_to(m)
                    folium.CircleMarker(
                        location=[hosp_lat, hosp_lon],
                        radius=12,
                        color='red',
                        fill=True,
                        fill_color='red',
                        fill_opacity=0.7,
                    ).add_to(m)
                
                folium_static(m)
            else:
                st.warning("⚠️ Could not find hospitals for the given location. Try entering a more specific place.")

if __name__ == "__main__":
    app()

