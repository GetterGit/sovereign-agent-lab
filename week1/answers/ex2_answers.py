"""
Exercise 2 — Answers
====================
Fill this in after running exercise2_langgraph.py.
Run `python grade.py ex2` to check for obvious issues.
"""

# ── Task A ─────────────────────────────────────────────────────────────────

# List of tool names called during Task A, in order of first appearance.
# Look at [TOOL_CALL] lines in your terminal output.
# Example: ["check_pub_availability", "get_edinburgh_weather"]

TASK_A_TOOLS_CALLED = ["check_pub_availability", "check_pub_availability", "calculate_catering_cost",
        "get_edinburgh_weather", "generate_event_flyer", "generate_event_flyer"]

# Which venue did the agent confirm? Must be one of:
# "The Albanach", "The Haymarket Vaults", or "none"
TASK_A_CONFIRMED_VENUE = "The Albanach"

# Total catering cost the agent calculated. Float, e.g. 5600.0
# Write 0.0 if the agent didn't calculate it.
TASK_A_CATERING_COST_GBP = 5600.0

# Did the weather tool return outdoor_ok = True or False?
TASK_A_OUTDOOR_OK = True

TASK_A_NOTES = """
    1. Assumption is that The Albanach was picked due to the primacy bias. 
    2. Also, sometimes due to the probabalistic nature of LLMs, it resolves without recommending a specific venue and suggesting both venues fit our requirements.
    3. Finally, the agent consistently calls flyer generation for both venues, not only for the chosen venue.
"""   # optional — anything unexpected

# ── Task B ─────────────────────────────────────────────────────────────────

# Has generate_event_flyer been implemented (not just the stub)?
TASK_B_IMPLEMENTED = True   # True or False

# The image URL returned (or the error message if still a stub).
TASK_B_IMAGE_URL_OR_ERROR = "https://pictures-storage.storage.eu-north1.nebius.cloud/text2img-153189a9-e345-44fe-9d9d-cb3b135bd064_00001_.webp"

# The prompt sent to the image model. Copy from terminal output.
TASK_B_PROMPT_USED = "Professional event flyer for Edinburgh AI Meetup, tech professionals, modern venue at The Haymarket Vaults, Edinburgh. 160 guests tonight. Warm lighting, Scottish architecture background, clean modern typography."

# ── Task C ─────────────────────────────────────────────────────────────────

# Scenario 1: first choice unavailable
# Quote the specific message where the agent changed course. Min 20 words.
SCENARIO_1_PIVOT_MOMENT = """
The Bow Bar does not meet the requirements for 160 vegan guests tonight.

I dunno what else to write here, but writing this to fill in the 20-word requirement.
"""

SCENARIO_1_FALLBACK_VENUE = "The Haymarket Vaults"

# Scenario 2: impossible constraint (300 guests)
# Did the agent recommend a pub name not in the known venues list?
SCENARIO_2_HALLUCINATED = False   # True or False

# Paste the final [AI] message.
SCENARIO_2_FINAL_ANSWER = """
None of the known venues meet the capacity and dietary requirements for 300 people with vegan options.
"""

# Scenario 3: out of scope (train times)
# Did the agent try to call a tool?
SCENARIO_3_TRIED_A_TOOL = False   # True or False

SCENARIO_3_RESPONSE = "I am not able to execute this task as it exceeds the limitations of the functions I have been given."

# Would this behaviour be acceptable in a real booking assistant? Min 30 words.
SCENARIO_3_ACCEPTABLE = """
It depends. If we position our booking assistant in a way that one can book any venue, including outside of their town,
then this will unlikely be acceptable, because trains is one of the means of transporation. Some guests might prefer trains,
and so but not having a train-checking tool, we cannot fulfil their expectations.

The booking assistant can still produce a result with a venue which fits our requirements outside of the train-related requirements.

But if trains was a critical dependency for me as organizer, I'd go search for another solution in the market.
"""

# ── Task D ─────────────────────────────────────────────────────────────────

# Paste the Mermaid output from `python exercise2_langgraph.py task_d` here.
TASK_D_MERMAID_OUTPUT = """
---
config:
  flowchart:
    curve: linear
---
graph TD;
        __start__([<p>__start__</p>]):::first
        agent(agent)
        tools(tools)
        __end__([<p>__end__</p>]):::last
        __start__ --> agent;
        agent -.-> __end__;
        agent -.-> tools;
        tools --> agent;
        classDef default fill:#f2f0ff,line-height:1.2
        classDef first fill-opacity:0
        classDef last fill:#bfb6fc
"""

# Compare the LangGraph graph to exercise3_rasa/data/rules.yml. Min 30 words.
TASK_D_COMPARISON = """
RASA agent is more deterministic and auditable compared to the Langgraph.

While Langgraph agent loop is a single-node loop, where LLM decides for or against tool calling under the hood (less predictability —
you can observe the trace after the fact, but you can't guarantee the path before it runs),
RASA agent picks a flow to follow depending on the context and then runs deterministic logic within the chosen flow.
The LLM's role in RASA is narrow — pick a flow, extract slot values from natural language. After that, there's just a programmatic
enforcment of business rules. Humans define logic depending on their use case - RASA executes.

That's why the booking call (money, deposits) goes through RASA — you don't want an LLM improvising there.
LangGraph is for more open-ended use cases where you can't predefine every path.
"""

# ── Reflection ─────────────────────────────────────────────────────────────

# The most unexpected thing the agent did. Min 40 words.
# Must reference a specific behaviour from your run.

MOST_SURPRISING = """
- Prompt-level guidance on choosing a single venue option doesn't always work - sometimes, LLM returns both options as equally eligible.
- Flyer generation loops until max turns exhausted without extra guardrails, presumably because the model doesn't understand that the successful
flyer URL return means we can break the loop. So, I had to add that as a note into the return object on successful image generation.
"""
