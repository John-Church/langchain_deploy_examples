import modal
import os
import chain

# create an image and install needed dependencies
image = modal.Image.debian_slim().pip_install("langchain", "openai", "python-dotenv")
stub = modal.Stub(image=image)

# create a webhook endpoint that calls the chain; import the chain module itself. Import secrets defined in the modal app.
@stub.webhook(mounts=modal.create_package_mounts(["chain"]), secret=modal.Secret.from_name("my-langchain-secrets"))
def evaluate_lead_endpoint(name: str, key: str):
    if key == os.environ.get("ENDPOINT_AUTH_KEY"):
        result = chain.generate_title(name)
        return {"result": result}
    else:
        return {"error": "not allowed"}
