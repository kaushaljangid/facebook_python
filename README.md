# facebook_python
using Facebook Graph API and extract data using Python

pip install facebook
pip install pyautogui

once read document on python facebook

1. friendlist
2. only post a message
3. id maps friend view post
4. Get all of the authenticated user's friends
5. Get all the comments from a post
6. Writes 'message' to the active user's wall	
7. like a post
8. comment on post	
9. Upload an image with a caption
10. wall post

Getting the Access Token:

To be able to extract data from Facebook using a python code you need to register as a developer on Facebook and then have an access token. Here are the steps for it.

Go to link developers.facebook.com, create an account there.
Go to link developers.facebook.com/tools/explorer.
Go to “My apps” drop down in the top right corner and select “add a new app”. Choose a display name and a category and then “Create App ID”.
Again get back to the same link developers.facebook.com/tools/explorer. You will see “Graph API Explorer” below “My Apps” in the top right corner. From “Graph API Explorer” drop down, select your app.
Then, select “Get Token”. From this drop down, select “Get User Access Token”. Select permissions from the menu that appears and then select “Get Access Token.”
Go to link developers.facebook.com/tools/accesstoken. Select “Debug” corresponding to “User Token”. Go to “Extend Token Access”. This will ensure that your token does not expire every two hours.
Python Code to Access Facebook Public Data:

Go to link https://developers.facebook.com/docs/graph-api if want to collect data on anything that is available publicly. See https://developers.facebook.com/docs/graph-api/reference/v2.7/. From this documentation, choose any field you want from which you want to extract data such as “groups” or “pages” etc. Go to examples of codes after having selected these and then select “facebook graph api” and you will get hints on how to extract information. This blog is primarily on getting events data.

First of all, import ‘urllib3’, ‘facebook’, ‘requests’ if they are already available. If not, download these libraries. Define a variable token and set its value to what you got above as “User Access Token”.

token= ‘aiufniqaefncqiuhfencioaeusKJBNfljabicnlkjshniuwnscslkjjndfi’
