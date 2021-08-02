# Bank Note Authentication 

This is an ML app for authenticating banknotes

![img_0](https://user-images.githubusercontent.com/41446634/127739328-af558629-7465-4a02-abb1-84d8e50dca37.png)

* All files for creating this app is in the 👉 testing branch, you can check it out like `BankNote_Authentication.csv`
* `main` branch is deployed on Heroku. This is the link : [Heroku](https://money-app-ashish.herokuapp.com/)
* This is a classification project, since the variable to be predicted is binary (fraudulent or legal).
* The goal here is to model the probability that a banknote is fraudulent, as a function of its features.


## About Data

Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tools were used to extract features from images.

The data file `banknote_authentication.csv` is the source of information for the classification problem. The number of instances (rows) in the data set is 1372, and the number of variables (columns) is 5.

In that way, this problem has the following variables of wavelet transformed:

- `variance`, used as input.
- `skewness`, used as input.
- `curtosis`, used as input.
- `entropy`, used as input.
- counterfeit, used as the target. It can only have two values: `0` (non-counterfeit) or `1` (counterfeit).

# Making the app

* I have already created the model you can check in `model_training.ipynb` file in `testing` branch
* From model training we get the pickle file which is used in predicting the output which is 0 or 1
* For creating this Heroku app we need `classifier.pkl` which is trained file, `app.py` which runs and gives output, `requirements.txt` which has all the libraries which are required to run the `app.py`, `setup.sh` which has script we will be using this script on the **Heroku**, help to run `app.py`. 
* Clone this repo to your local system.
* First you need to have Heroku account. You can sign-up if you don't have one.
* You should have **Heroku CLI**, if you don't have you can downlod from [here](https://devcenter.heroku.com/articles/heroku-cli#download-and-install).
* Now we are Ready to deploy.
* Run this command `$ heroku create money-app` it will ask you login credentials. You get login through browser.
* Now your app is created on Heroku, you have to put your code in Heroku.
* You have to run the following command in order to make it deoployable
* `$ git add .`
* `$ git commit -m "make it better"`
* `$ git push heroku master`
* Just simply `$ git push heroku master`. Before this command make sure you commit all your code.

### Your Heroku app is ready you can checkout Heroku link

# Contribute 
* You can contribute by folking this repo 
* Make changes, if you want to. 
* Push changes to this repo.
 
## 🤩Happy Contributing🤩