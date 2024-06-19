# API Setup Guide

## How you can get the Google's Gemini API key.

1. Go to[Google AI Studio](https://aistudio.google.com/app)
2. On the left hand side, click on *Get API KEY*
3. Now click on *Create API Key*
4. The API Key will be generated. Copy that and set the API key in *.studiorc* file.

## How you can get the OpenAI's API key.

1. Log in into [OpenAI Platform](https://platform.openai.com)
2. Click on API (On the right hand side.)
3. On the left hand side, click on *API Keys*
4. Click on *Create new secret key*
5. Copy the key and set that in *.studiorc* file.

## How you can setup callback URL on Twilio's Dashboard.

1. Log in into [Twilio Console](https://console.twilio.com)
2. On the left hand side, click on *Messaging* > *Try It Out* > *Send a WhatsApp Message*
3. Click on *Sandbox Settings* tab.
4. Click on *API Builder* plugin in this studio.
5. Click on *Create New API* - set the name and port 5000.
6. Copy the URL and page that in Twilio's Dashboard and add */bot* route.
7. Click on save.

## Start the Application

1. Open the terminal.
2. Run - *python app.py*
