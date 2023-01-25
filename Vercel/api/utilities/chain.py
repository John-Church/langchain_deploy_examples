from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

template = """
Please give the given name a fun title that starts with the same letter. 

For example:
name: Jane; response: Jolly Jane
name: Roberto; response: Rambunctious Roberto

Please generate a fun title for the following name.

name: {name}; Response:
"""

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
    input_variables=["name"],
    template=template,
)

from langchain.chains import LLMChain

title_chain = LLMChain(llm=llm, prompt=prompt)


def generate_title(name):
    return title_chain.run(name=name)
