# Clothing Grayscale Converter (Streamlit)

## Run locally in VS Code

1. Put `app.py` and `requirements.txt` in the same folder.
2. Open a terminal in that folder.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the app:

   ```bash
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal (usually http://localhost:8501).

## Important note about the supplied model

`clothing_resnet18_finetuned.pth` is a ResNet-18 classification checkpoint, not a model trained to turn color images into grayscale images. The app uses standard grayscale image processing, which is the correct simple approach for this requirement. Your notebook's DCGAN generator creates synthetic fashion-like images; it is not an image-to-image grayscale conversion model, either.

The app does not need either model file to perform the requested conversion.
