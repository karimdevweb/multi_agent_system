from ollama import chat

# --- Définition des agents (Labo 1) ---

def researcher(task):
    basic_res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"Please give me some information about: {task}"}],
        stream=False
    )
    content = basic_res.message.content
    # print("\n--- response from Researcher agent ---\n", content)
    return content

def writer(data):
    basic_res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"Please summarize this text: {data}"}],
        stream=False
    )
    content = basic_res.message.content
    # print("\n--- response from Writer agent ---\n", content)
    return content

def reviewer(text):
    basic_res = chat(
        model="mistral:latest",
        messages=[{"role": "user", "content": f"Please clarify this point in a simpler way: {text}"}],
        stream=False
    )
    content = basic_res.message.content
    # print("\n--- response from Reviewer agent ---\n", content)
    return content

# Manager-Worker

class Manager:
    def __init__(self, workers):
        """
        workers : liste de tuples (nom_worker, fonction_worker)
        """
        self.workers = workers

    def run(self, mission):
        """
        Execute chaque worker en séquence, en passant le résultat au suivant
        """
        print(f"\n=== Mission du Manager : {mission} ===")
        data = mission
        for name, worker_func in self.workers:
            print(f"\n→ Délégation à {name}")
            data = worker_func(data)
        print("\n=== Mission terminée, résultat final ===\n", data)
        return data

# define all workets 
workers_chain = [
    ("Researcher", researcher),
    ("Writer", writer),
    ("Reviewer", reviewer)
]

manager = Manager(workers_chain)

# --- Lancer la mission ---
mission = "Les tendances IA 2025"
final_result = manager.run(mission)
