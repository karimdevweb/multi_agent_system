# Labo 5 : Consensus et résolution de conflits avec Ollama

from ollama import chat

# Writer agent: summarize text
def writer(text):
    basic_res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"Please summarize this text in 2 or 3 sentences: {text}"}],
        stream=False
    )
    return basic_res.message.content


# Example responses from different agents
responses = [
    writer("black clover anime"),
    writer("anime black clover"),
    writer("black clover")
]

# -----------------
# Vote majoritaire (simple, exact match)
final_vote = max(set(responses), key=responses.count)
print("")
print("-----------Vote majoritaire:--------------\n", final_vote)

# -----------------
# Agent arbitre (simulé avec Ollama)
judge_prompt = f"Analyze these responses and pick the best one: {responses}"
final_judge = chat(
    model="mistral:latest",
    messages=[{"role": "user", "content": judge_prompt}],
    stream=False
).message.content
print("")
print("---------Agent arbitre:-----------\n", final_judge)

# -----------------
# Score de confiance (scoring par un agent)
scored_responses = []
for r in responses:
    prompt = f"Rate this response on clarity and relevance from 0 to 1, no words no sentece, just the rate: '{r}'"
    score_text = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": prompt}],
        stream=False
    ).message.content
    try:
        score = float(score_text.strip())
    except:
        score = 0.5  # default score
    scored_responses.append({"text": r, "score": score})

final_score = sorted(scored_responses, key=lambda x: x["score"], reverse=True)[0]["text"]
print("")
print("-------------Score de confiance:-------------\n", final_score)
