import io
from PIL import Image, ImageOps
import streamlit as st

st.set_page_config(page_title="Clothing Grayscale Converter", page_icon="👕", layout="wide")

st.title("👕 Clothing Image → Grayscale")
st.write("Upload a clothing photo to convert it to grayscale. Preview and download the result.")

uploaded_file = st.file_uploader(
    "Choose a clothing image",
    type=["png", "jpg", "jpeg", "webp", "bmp"],
    help="Use a clear photo of a shirt, dress, trousers, jacket, or other clothing item."
)

if uploaded_file is not None:
    try:
        original = Image.open(uploaded_file)
        original = ImageOps.exif_transpose(original).convert("RGB")
        grayscale = ImageOps.grayscale(original)

        left, right = st.columns(2)
        with left:
            st.subheader("Original image")
            st.image(original, use_container_width=True)
        with right:
            st.subheader("Grayscale result")
            st.image(grayscale, use_container_width=True)

        buffer = io.BytesIO()
        grayscale.save(buffer, format="PNG")
        st.download_button(
            label="⬇️ Download grayscale image",
            data=buffer.getvalue(),
            file_name="clothing_grayscale.png",
            mime="image/png",
            use_container_width=True,
        )
        st.success("Conversion complete!")
    except Exception as exc:
        st.error(f"Could not process this image. Please try another image. Details: {exc}")
else:
    st.info("Upload an image above to see the grayscale conversion.")
