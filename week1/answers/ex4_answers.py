"""
Exercise 4 — Answers
====================
Fill this in after running exercise4_mcp_client.py.
"""

# ── Basic results ──────────────────────────────────────────────────────────

# Tool names as shown in "Discovered N tools" output.
TOOLS_DISCOVERED = ['search_venues', 'get_venue_details']

QUERY_1_VENUE_NAME    = "The Haymarket Vaults"
QUERY_1_VENUE_ADDRESS = "1 Dalry Road, Edinburgh"
QUERY_2_FINAL_ANSWER  = "This function call will return a list of venues in Edinburgh that can accommodate at least 300 people and have vegan options. The response will include the names of the venues that match these criteria."

# ── The experiment ─────────────────────────────────────────────────────────
# Required: modify venue_server.py, rerun, revert.

EX4_EXPERIMENT_DONE = True   # True or False

# What changed, and which files did or didn't need updating? Min 30 words.
EX4_EXPERIMENT_RESULT = """
Changed:
- The Albanach wasn't returned as one of the matching venues based on min capacity and required vegan because it was marked as full and hence excluded

Didn't change:
- Tool calling sequence didn't change
- The final recommendation didn't change neither
"""

# ── MCP vs hardcoded ───────────────────────────────────────────────────────

LINES_OF_TOOL_CODE_EX2 = 4  # count in exercise2_langgraph.py
LINES_OF_TOOL_CODE_EX4 = 2   # count in exercise4_mcp_client.py

# What does MCP buy you beyond "the tools are in a separate file"? Min 30 words.
MCP_VALUE_PROPOSITION = """
- Tools are decoupled from agent - if we wanna edit tools, we don't need to redeploy our agent. At the same time, our agent will auto-discover all new tools (or removed/updated old tools)
- Different agents built with different frameworks can share the same tools
"""

# ── Week 5 architecture ────────────────────────────────────────────────────
# Describe your full sovereign agent at Week 5 scale.
# At least 5 bullet points. Each bullet must be a complete sentence
# naming a component and explaining why that component does that job.

WEEK_5_ARCHITECTURE = """
- Agent loop - the core of our agent, responsible for completing user task, including recalling relevant context, planning the task completion strategy and executing the plan, including calling relevant tools
- Agent tools - tools for our agent, exposed via MCP, to execute to acquire context required for decision-making and furthering the task completion
- Planner-Executor split - Planner as a heavier reasoning model to decompose the user task into milestones with deps, and orchestrate smaller Executor models, including re-planning mode in case the plan breaks at any point
- Agent memory - working, short-term and long-term agent memory which enables it to remember relevant context fron the previous user interactions to make the next interaction more cost- and time-efficient, while ensuring successful user request completion (or user-friendly fallback)
- Agent guardrails - prompt-level and programmatic guardrails for our agent to keep within the scope of its main purpose (venue booking / booking confirmation) while not producing undersirable content (including hallucinations) or deviating from the topic. Besides, it includes memory-level guardrails to prevent memory poisoning.
- Agent observability - logging human<>agent interactions to be able to trace any reported issues and devise agent improvement backlog
"""

# ── The guiding question ───────────────────────────────────────────────────
# Which agent for the research? Which for the call? Why does swapping feel wrong?
# Must reference specific things you observed in your runs. Min 60 words.

GUIDING_QUESTION_ANSWER = """
LangGraph agent for the research, Rasa CALM agent for the call, because:
- We want our research agent to be flexible with venue search because there can be many venues satisfying our criteria. However, while our research agent goes down the path, it can encounter that a matching venue
is fully booked or located in a remote place. So, it will need to re-plan and pick another matching venue as a fallback. Rasa agent cannot re-plan in the middle of the execution workflow.
- We want our call agent to be able to confirm an already chosen venue. So, we don't need creativity here - we just need our agent to follow pre-defined config, including planned guests number, vegan meals quota and budget limitations. Rasa shines here by employing an LLM
to parse the natural language of the caller and translate it into relevant slots of available tools for deterministic execution.

Swapping feels wrong, because Rasa research agent would fail mid-way if the first venue didn't satisfy any criteria, while LangGraph call agent could technically get creative and negotiate a deposit price above our budget (e.g. the pub manager suggests a part of deposit as 'deposit' and then obfuscates a larger part of the deposit as 'insurance' to trick the LangGraph agent).
"""
