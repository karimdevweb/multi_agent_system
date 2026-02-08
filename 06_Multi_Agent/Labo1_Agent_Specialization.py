
from ollama import chat


def agent(task, role, instruction):
    basic_res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"{instruction}: {task}"}],
        stream=False
    )
    content = basic_res.message.content
    print(f"\n--- response from {role} agent ---\n")
    print(content)
    return content




# prompt for each agent
searcher_prompt = "i need some info about black clover."
# call all my agents, one after another
searcher_res = agent(searcher_prompt, "Searcher", "give me some information")
writer_res = agent(searcher_res, "Writer", "please summarize this text")
reviewer_res = agent(writer_res, "Reviewer", "please clarify this in a simpler way")
