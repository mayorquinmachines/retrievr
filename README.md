# Retrievr

[![find my keys](https://img.youtube.com/vi/845WUuyAT_k/0.jpg)](https://www.youtube.com/watch?v=845WUuyAT_k)

An Amazon Alexa application to find lost items using bluetooth. It uses an xgboost model to locate the most likely place
the tagged keys were last left. The application runs using flask, flask-ask, and ngrok.

## Hardware
* [Any Amazon Alexa Echo](https://www.amazon.com/gp/product/B01DFKC2SO/ref=s9_acsd_al_bw_c_x_1_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=Q924P0APNQ9M7QVMV2D0&pf_rd_r=Q924P0APNQ9M7QVMV2D0&pf_rd_t=101&pf_rd_p=4dc5e960-6892-4959-a18f-2e32ecb3b2b6&pf_rd_p=4dc5e960-6892-4959-a18f-2e32ecb3b2b6&pf_rd_i=9818047011)
* [Bluetooth Beacons](https://www.amazon.com/gp/product/B077ZGGYY7/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)

## Software
* [XGBoost](https://xgboost.readthedocs.io/en/latest/)
* [Flask](http://flask.pocoo.org/)
* [Flask-Ask](http://flask-ask.readthedocs.io/en/latest/)
* [Ngrok](https://ngrok.com/download)
* pandas
* numpy

## Run
Go to our [Hackster.io post](https://www.hackster.io/home_skillet/alexa-where-are-my-keys-aa0e82) to see the full instructions on constructing this Alexa skill. 

The app.py file contains the application. You want to replace the appropriate file names for each dummy name. Running an ngrok server with ```sudo ./ngrok http 5000 ``` wherever you installed ngrok will run the server needed for the https address needed for the alexa skill. 

##TODO:
* front-end interface to designate spaces

