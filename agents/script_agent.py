# agents/script_agent.py

from core.agent_factory import create_script_chain
from langgraph.types import Command
from langgraph.graph import END


def script_node(state: dict) -> Command:
    """
    Script generation agent node: uses the script chain to generate the podcast script.
    Combines research output, podcast instructions, and speaker style.
    """
    research_output = state.get("research_output", "")
    direction = state.get("direction", "")
    speaker_style = state.get("speaker_style", "")
    knowledge_level = state.get("knowledge_level", "")  # Get knowledge level
    # Get new parameters
    desired_outcome = state.get("desired_outcome", "")
    preferred_length = state.get("preferred_length", "")
    format_preference = state.get("format_preference", "")

    script_chain = create_script_chain()
    # Run the chain with the necessary inputs.
    script_output = script_chain.run(
        research_output=research_output,
        direction=direction,
        speaker_style=speaker_style,
        knowledge_level=knowledge_level,
        desired_outcome=desired_outcome,
        preferred_length=preferred_length,
        format_preference=format_preference,
    )
    state["script_output"] = script_output.strip()
    print("Script Agent Output:", state["script_output"])
    # End the workflow.
    return Command(update=state, goto=END)
