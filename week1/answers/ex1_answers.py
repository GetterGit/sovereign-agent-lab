"""
Exercise 1 — Answers
====================
Fill this in after running exercise1_context.py.
Run `python grade.py ex1` to check for obvious issues before submitting.
"""

# ── Part A ─────────────────────────────────────────────────────────────────

# The exact answer the model gave for each condition.
# Copy-paste from your terminal output (the → "..." part).

PART_A_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_A_XML_ANSWER      = "The Albanach"
PART_A_SANDWICH_ANSWER = "The Albanach"

# Was each answer correct? True or False.
# Correct = contains "Haymarket" or "Albanach" (both satisfy all constraints).

PART_A_PLAIN_CORRECT    = True   # True or False
PART_A_XML_CORRECT      = True
PART_A_SANDWICH_CORRECT = True

# Explain what you observed. Minimum 30 words.

PART_A_EXPLANATION = """
Newer models with billions of weights are well-aligned to be able not to skip information
in the middle regardless of prompting technique (plan, XML or sandwich), especially when the prompt contains as little as hundreds tokens.

Seems that the plain prompting just might be less susceptible to the primacy bias compared to the other two, because it returned not The Albanach
but the next right answer consistently across several runs, while XML and sandwich returned The Albanach.
"""

# ── Part B ─────────────────────────────────────────────────────────────────

PART_B_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_B_XML_ANSWER      = "The Albanach"
PART_B_SANDWICH_ANSWER = "The Albanach"

PART_B_PLAIN_CORRECT    = True
PART_B_XML_CORRECT      = True
PART_B_SANDWICH_CORRECT = True

# Did adding near-miss distractors change any results? True or False.
PART_B_CHANGED_RESULTS = False

# Which distractor was more likely to cause a wrong answer, and why?
# Minimum 20 words.
PART_B_HARDEST_DISTRACTOR = """
The Holyrood Arms is the hardest distractor because it satisfies all criteria we are looking for except for being full at the time of our enquiry.

Hence, our LLMs are most likely to confuse it for the right answer, especially if their don't choose The Albanach and decide to check alternatives.
Because this distractor is localted just above The Hayarket Vaults - the second right answer.
"""

# ── Part C ─────────────────────────────────────────────────────────────────

# Did the exercise run Part C (small model)?
# Check outputs/ex1_results.json → "part_c_was_run"
PART_C_WAS_RUN = True   # True or False

PART_C_PLAIN_ANSWER    = "The Haymarket Vaults"
PART_C_XML_ANSWER      = "The Haymarket Vaults"
PART_C_SANDWICH_ANSWER = "The Haymarket Vaults"

# Explain what Part C showed, or why it wasn't needed. Minimum 30 words.
PART_C_EXPLANATION = """
Part C didn't change the outcome of all 3 prompting techniques returning a correct answer. Thought, none returned
The Albanach across tuns, creating an assumption that the chosen smaller model can be less prone to the primacy bias compared to our 
first-choice larger model.
"""

# ── Core lesson ────────────────────────────────────────────────────────────

# Complete this sentence. Minimum 40 words.
# "Context formatting matters most when..."

CORE_LESSON = """
Context formatting is the thing to experiment with when we want to avoid primacy bias. We might wanna see which technique allows us to 
avoid it better across multiple experiments.

At the same time, worth noting that modern models are already good enough not to skip / misinterpret / hallucinate on the key info hidden
in the middle of the context window when this context window is filled only for hundreds of tokens.

For example, to be able to reproduce the effect of distracting a model from the info we were looking for,
we'd need bloat the prompt to thousands of tokens to decrease the signal-to-noise ratio. In that case, our smaller models (e.g. 8B Llama or 2B Gemma)
would likely be the first to bring us wrong extration results.
"""
