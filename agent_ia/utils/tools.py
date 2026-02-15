import os
from tavily import TavilyClient
from langchain_core.tools import tool

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def internet_search(query: str) -> str:
    """
    Effectue une recherche sur Internet via Tavily et retourne un résumé textuel. Le contenu ne doit pas dépasser le contexte du stage
    """
    response = tavily_client.search(
        query=query,
        max_results=5
    )

    results = []
    for r in response.get("results", []):
        title = r.get("title", "Sans titre")
        url = r.get("url", "")
        content = r.get("content", "")
        results.append(f"- {title}\n{content}\nSource: {url}")

    return "\n\n".join(results) if results else "Aucun résultat trouvé."

@tool
def write_report_tool(content: str, section_name: str):
    """Écrit ou met à jour une section du rapport dans le fichier local."""
    filename = "rapport_stage.md"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n\n## {section_name}\n{content}")
    return f"Section '{section_name}' enregistrée."

def read_report_tool():
    """Lit chaque section dans le fichier local et analyse les sections déjà rempli afin de le spécifier à l'utilisateur sur ce qui doit être écrit et ce qui peut être modifier"""
    filename = "rapport_stage.md"
    with open(filename, mode="r", encoding="utf-8") as fichier:
        contenu = fichier.read()
    return contenu

tools_question = [internet_search, read_report_tool]
tools_validation = [write_report_tool]