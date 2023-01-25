# Langchain Vercel Example Deployment

This repository showcases a very simple deployment of a Langchain script as a
serverless function on Vercel.

The GET endpoint /api/generate_title takes two parameters: `name`, the name to be titled, and `key`, which is the 'api key.' (Actually just checks to see if the key submitted matches the one in the .env as a simple protection in
case the url is public.)

## Deployment

Simply upload the repo to vercel! The only configuration required is adding the two env variables,
OPENAI_API_KEY and ENDPOINT_AUTH_KEY, in the Vercel environment variables panel.

## Files

- api/index.py : defines api routes. Change this to add new routes.
- utilities/chain.py : Where the example Langchain call is made.

NB: If running locally, user `vercel dev` instead of running Flask. Vercel imports
files form the top directory so the import of files from /utilities won't work if you just
use the Flask command from index.py.
