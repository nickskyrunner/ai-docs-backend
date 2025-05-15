def build_prompt(question: str, docs: str):
    return f"""
Documenti trovati:
{docs}

Domanda dell'utente:
{question}

Basandoti solo sui documenti forniti, genera una procedura passo-passo chiara e precisa.
"""