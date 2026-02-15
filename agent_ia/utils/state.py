from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode
from agent_ia.utils.nodes import (
    reponse_question, generate_section, validation, collect_human_input, collect_human_input_2, sauvegarde
)
from agent_ia.utils.tools import tools_question, tools_validation

def check_tools_question(state: MessagesState):
    if state["messages"][-1].tool_calls: return "tools_question"
    return "attente_humain"

def check_tools_redaction(state: MessagesState):
    if state["messages"][-1].tool_calls: return "tools_redaction"
    return "validation"

def check_tools_validation(state: MessagesState):
    if state["messages"][-1].tool_calls: return "tools_validation"
    return "attente_humain" 

def check_tools_sauvegarde(state: MessagesState):
    """Vérifie si le nœud sauvegarde a bien généré l'appel à l'outil."""
    if state["messages"][-1].tool_calls:
        return "tools_v"
    return "ia_question"

def check_redaction_output(state: MessagesState):
    last_msg = state["messages"][-1]
    if last_msg.tool_calls:
        return "tools_q"
    return "validation"

def router_apres_humain(state: MessagesState):
    last_message = state["messages"][-1]
    content = str(last_message.content).lower().strip()
    
    print(f"\n[DEBUG ROUTEUR] L'humain a dit : '{content}'")

    triggers = ["go", "génère", "genere", "rédige", "redige"]
    
    if any(kw in content for kw in triggers):
        print(">>> ACTION : DIRECTION NOEUD RÉDACTION")
        return "redaction"
    
    return "ia_question"

def router_apres_validation(state: MessagesState):
    """Décide si on valide la rédaction ou si on doit corriger."""
    last_message = state["messages"][-1]
    content = str(last_message.content).lower().strip()
    
    print(f"\n[DEBUG ROUTEUR VALIDATION] Analyse de : '{content}'")

    triggers_ok = ["oui", "ok", "valide", "sauvegarde", "marche", "super", "parfait"]
    
    if any(kw in content for kw in triggers_ok):
        return "validation" 
    
    return "ia_question"

def workflow_create(checkpointer):
    workflow = StateGraph(MessagesState)

    workflow.add_node("ia_question", reponse_question)
    workflow.add_node("attente_humain", collect_human_input)
    workflow.add_node("attente_humain_2", collect_human_input_2)
    workflow.add_node("redaction", generate_section)
    workflow.add_node("validation", validation)
    workflow.add_node("sauvegarde", sauvegarde)
    workflow.add_node("tools_q", ToolNode(tools_question))
    workflow.add_node("tools_v", ToolNode(tools_validation))

    workflow.add_edge(START, "ia_question")

    workflow.add_conditional_edges("ia_question", check_tools_question)
    workflow.add_edge("tools_q", "ia_question")

    workflow.add_conditional_edges("attente_humain", router_apres_humain, {
        "redaction": "redaction", 
        "ia_question": "ia_question"
    })

    workflow.add_edge("redaction", "validation")
    
    workflow.add_edge("validation", "attente_humain_2")

    workflow.add_conditional_edges(
        "attente_humain_2",
        router_apres_validation,
        {
            "validation": "sauvegarde",
            "ia_question": "ia_question" 
        }
    )

    workflow.add_conditional_edges(
        "sauvegarde", 
        check_tools_sauvegarde, 
        {
            "tools_v": "tools_v",
            "ia_question": "ia_question"
        }
    )

    return workflow.compile(checkpointer=checkpointer, interrupt_before=["attente_humain","attente_humain_2"])