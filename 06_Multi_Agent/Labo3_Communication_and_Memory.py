from ollama import chat

shared_memory = {}

# Researcher agent: collect raw information
def researcher(task):
    res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"pls, give me some information about: {task}"}],
        stream=False
    )
    content = res.message.content
    print("\n--- Researcher output ---")
    print(content)
    return content

# Writer agent: summarize collected data
def writer(data):
    res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"pls, could you resume this text: {data}"}],
        stream=False
    )
    content = res.message.content
    print("\n--- Writer output ---")
    print(content)
    return content

# Reviewer agent: clarify and simplify the summary
def reviewer(text):
    res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"pls, clarify this point in a more simple way: {text}"}],
        stream=False
    )
    content = res.message.content
    print("\n--- Reviewer output ---")
    print(content)
    return content


shared_memory["data"] = researcher("black clover")
shared_memory["summary"] = writer(shared_memory["data"])
shared_memory["feedback"] = reviewer(shared_memory["summary"])

print("\n--- Shared memory content ---")
print(shared_memory)
