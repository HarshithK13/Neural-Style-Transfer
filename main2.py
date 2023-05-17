# python3 -m venv venv
# . venv/bin/activate
# pip install streamlit
# pip install torch torchvision
# streamlit run main.py
import streamlit as st
from PIL import Image

import style

st.title('Dl ops project neural style transfer')



style_name = st.sidebar.selectbox(
    'Select Style',
    ('candy', 'mosaic', 'rain_princess', 'udnie')
)






image = "images/content-images/" + 'amber.jpg'
model= "saved_models/" + style_name + ".pth"
# input_image = st.file_uploader("Choose a file")
output_image = "images/output-images/" + style_name  + "jpg"

image = st.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'])

# if image is not None:
#     st.image(image)


st.write('### Source image:')


st.image(image, width=400) # image: numpy array

clicked = st.button('Stylize')

if clicked:
    model = style.load_model(model)
    style.stylize(model, image, output_image)

    st.write('### Output image:')
    image = Image.open(output_image)
    st.image(image, width=400)

