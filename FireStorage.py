import pyrebase

config = {
    "apiKey": "AIzaSyCed3bMsuEyN7yVYzTTRqhW-rcgrdwtAYY",
    "authDomain": "pysonic-2018.firebaseapp.com",
    "databaseURL": "https://pysonic-2018.firebaseio.com",
    "storageBucket": "pysonic-2018.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# storage = firebase.storage().child("samaki.jpg").put("es6.png")


def upload_file(file, id):
    try:
        print("the files is ", file)
        firebase.storage().child(id).put(file)
    except Exception as e:
        print("An Error occured while uploading an image")

