# FashionMNIST clothing predictor and API

Hi! In this folder I create and train a convolutional neural network and create and API based on it for predicting type of clothing based on the fashionMNIST data set. 
We have:
- A .ipynb file, where the deep learning was trained;
- Some .png for metrics visualization;
- The model_50e folder, where the brain is;
- And the API folder (self-explanatory).

You can navigate between them, open the notebook and even run it! (just make sure to change the path variables). In the notebook, you will find some comments and explanations in the code. 

For the *API*, you need to run the *server_ferraz.py*, inside this folder, follow the dependencis instructions and edit the model_50e path! (SUPER IMPORTANT!).
To check the API (after its up and running), go to a web browser and type '*localhost:8000/docs*' and input an image there of some clothing. The API will reach the database to convert the image for a (1,28,28) image (grayscale) and predict it based on my model. 

Have fun!
