# Example Langchain Easy API Deployments

Occasionally you may need to deploy a Langchain script to do a simple task in a way that is publicly callable. For example, one may need to call a script from a 3rd party service like Zapier or may just want a temporary deploy for a proof of concept. These services offer easy ways to get up and running fast.

The examples in these repositories all do the same thing: deploy a simple chain as a publicly accessible endpoint. In this case, a chain that takes in a name and returns a fun title to go with it. For example, "John" could be "Jolly John."

The endpoints also take a key that is checked against an environment variable for a simple security safeguard.
