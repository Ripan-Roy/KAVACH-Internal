from detect import detect
import streamlit as st
from ultralytics import YOLO
from PIL import Image
model = YOLO('yolo_custom.pt')

st.sidebar.image(
    'logo.jpg',
    use_column_width=True,
    output_format='JPEG',
    caption='NIVAARAN',
)

st.title('NIVAARAN')
st.caption('An AI Based Solution for all you security needs')

if st.button('Detect Age and Gender', ):
    vid = detect()
    vid = vid.read()
    st.video(vid)
if st.button('Predict Violence', ):
    vid = model.predict(source=0, show=True, conf=0.5)
    vid = vid.read()
    st.video(vid)

