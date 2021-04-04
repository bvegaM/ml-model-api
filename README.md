# Machine Learning model with python and flask

In this project I generated a robust machine learning model. I used different models and with hyperparameter optimizer find the best model for this project. 
I used flask to deploy the model in an application that simulates a production output.

## Libraries

 * pandas
 * numpy
 * joblib
 * sklearn
 
## Dataset

  * Happiness dataset: https://www.kaggle.com/unsdsn/world-happiness

## Deploy project

I deployed this project in heroku. The link is: https://machinelearningmodel.herokuapp.com

## API
I had only one service method and is the predic service. The path is ```https://machinelearningmodel.herokuapp.com/predict```. In this case this service is static because is a little example about machine learning models.