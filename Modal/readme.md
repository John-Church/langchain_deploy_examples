# Langchain Modal Example Deployment

This repository showcases a very simple deployment of a Langchain script as a
webhook on Modal.

The endpoint can be tested locally with `modal serve example.py` and deployed with `modal deploy example --name example_deployment_name`

this particular example takes two parameters, a `name` to title and a `key` to verify the request. The key is just a string stored in a secret.
