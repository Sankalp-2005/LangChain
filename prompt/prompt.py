from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
    You are an agent who job is to provided summaries on the topic {topic}""",
    input_variables=["topic"],
    validate_template=True
)
template.save("template.json")