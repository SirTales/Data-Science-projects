'''
Created by de Paula, Tales Ferraz, 2022.

Contact info: ferrazdepaula@ifsc.usp.br
'''
'''
Dependencies 
'''
# pip install fastapi
# pip install "uvicorn[standard]"
# pip install tensorflow
# pip install Pillow

# I recommend using google colab for running this script, as most of the libraries (if not all) will
# be pre-installed

from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()


MODEL = tf.keras.models.load_model('/home/depaula/job_test/model_50e') # EDIT ME (or I will not work!)

CLASS_NAMES = ['T-shirt/top', 
               'Trouser',
               'Pullover',
               'Dress',
               'Coat',
               'Sandal',
               'Shirt',
               'Sneaker',
               'Bag',
               'Ankle boot']

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.convert("L").resize((28, 28), Image.NEAREST)
    image = np.array(image.getdata(), dtype=np.float).reshape((28, 28))
    image = np.expand_dims(image, 0)
    image = image/255


    if image[0][0][0] >= 0.39: # if the image has white background, we need to correct that
        image = 1 - image      # otherwise our data will be biased for BAGS! (caused by the big
                               # white square that is the bag) 
    return image               # I've selected the gray scale 100 for applying the color inversion
                               # (100/255 ~= 0.39), that is, when the first pixel of the image
                               # is greater or equal than 0.39, the inversion will be applied


@app.post('/model/predict')
async def predict(
    file: UploadFile = File(...)):
    
    img_batch = read_file_as_image(await file.read())


    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port = 8000) # this is your site! (or mine (?))