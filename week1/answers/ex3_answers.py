"""
Exercise 3 — Answers
====================
Fill this in after completing the three Rasa conversations.

CALM vs Old Rasa — what changed
---------------------------------
The old open-source Rasa approach used:
  - nlu.yml: intent training examples
  - rules.yml: explicit dialogue rules
  - FormValidationAction: Python class to parse slot values

Rasa Pro CALM uses:
  - flows.yml: natural language descriptions of what each flow does
  - from_llm slots: the LLM extracts values from conversation
  - ONE custom action: ActionValidateBooking for the business rules

The conversation is the same from the manager's perspective.
The machinery underneath is completely different.

CONVERSATION SCRIPTS
---------------------
Conversation 1 (happy path):
  You:    calling to confirm a booking
  Agent:  [asks guest count]
  You:    160 guests
  Agent:  [asks vegan count]
  You:    about 50 need vegan
  Agent:  [asks deposit]
  You:    £200 deposit
  Agent:  [confirms or escalates?]

Conversation 2 (deposit too high):
  Same as above but use a deposit above £300 (e.g. "£500 deposit").

Conversation 3 (out of scope):
  Start normally, then when asked for vegan count say something like
  "can you arrange parking for the speakers?" and observe what happens.
  Does CALM handle this differently than the old rules approach?
"""

# ── Conversation 1: Happy path ─────────────────────────────────────────────

CONVERSATION_1_TRACE = """
Your input ->  calling to confirm a booking                   
How many guests are you confirming for tonight's event?
Your input ->  160 guests                                     
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan                            
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £200 deposit                                   
Thank you — booking confirmed. 160 guests, 50 requiring vegan meals, £200 deposit accepted. I'll send written confirmation to the organiser shortly.
Is there anything else I can help you with?
"""

CONVERSATION_1_OUTCOME = "confirmed"   # "confirmed" or "escalated"

# ── Conversation 2: Deposit too high ───────────────────────────────────────

CONVERSATION_2_TRACE = """
Your input ->  calling to confirm a booking
How many guests are you confirming for tonight's event?
Your input ->  160 guests  
And how many of those guests will need vegan meals?
Your input ->  about 50 need vegan
What deposit amount in GBP are you proposing to secure the booking?
Your input ->  £500 deposit                                   
I need to check one thing with the organiser before I can confirm. The issue is: a deposit of £500 exceeds the organiser's authorised limit of £300. Can I call you back within 15 minutes?
Is there anything else I can help you with?
"""

CONVERSATION_2_OUTCOME = "escalated"   # "confirmed" or "escalated"
CONVERSATION_2_REASON  = "a deposit of £500 exceeds the organiser's authorised limit of £300"   # the reason the agent gave for escalating

# ── Conversation 3: Out of scope ───────────────────────────────────────────

CONVERSATION_3_TRACE = """
Your input ->  calling to confirm a booking    
How many guests are you confirming for tonight's event?
Your input ->  160 guests
And how many of those guests will need vegan meals?
Your input ->  can you arrange parking for the speakers?      
I'm sorry, I'm not trained to help with that.
I can only help with confirming tonight's venue booking. For anything else, please contact the event organiser directly.
Would you like to continue with confirm booking? 
"""

# Describe what CALM did after the out-of-scope message. Min 20 words.
CONVERSATION_3_WHAT_HAPPENED = """
Out-of-the-scope message immediately hit the guardrail, and the agent raised that it cannot help with the request
outside of the configured scope.
"""

# Compare Rasa CALM's handling of the out-of-scope request to what
# LangGraph did in Exercise 2 Scenario 3. Min 40 words.
OUT_OF_SCOPE_COMPARISON = """
Actually, both Rasa and LangGraph implementations rejected the request, suggesting they don't have enough capabilities.
LangGraph agent suggested it doesn't have functionality to check for trains, while Rasa agent suggested that it's not trained to help with
out-of-scope questions.

Though, my intuition suggests that across many runs, LangGraph agent would be more prone to hallucinate the response, because it doesn't have existing
programmatic guardrails to handle out-of-scope questions, so it's response remains probabalistic.
"""

# ── Task B: Cutoff guard ───────────────────────────────────────────────────

TASK_B_DONE = True   # True or False

# List every file you changed.
TASK_B_FILES_CHANGED = ["exercise3_rasa/actions.py"]

# How did you test that it works? Min 20 words.
TASK_B_HOW_YOU_TESTED = """
1. For tests, set up my local time, minus an hour, to hit the IF condition
2. Re-ran the happy-path
3. Got the expected time-related exception, suggesting it escalated the issue
"""

# ── CALM vs Old Rasa ───────────────────────────────────────────────────────

# In the old open-source Rasa (3.6.x), you needed:
#   ValidateBookingConfirmationForm with regex to parse "about 160" → 160.0
#   nlu.yml intent examples to classify "I'm calling to confirm"
#   rules.yml to define every dialogue path
#
# In Rasa Pro CALM, you need:
#   flow descriptions so the LLM knows when to trigger confirm_booking
#   from_llm slot mappings so the LLM extracts values from natural speech
#   ONE action class (ActionValidateBooking) for the business rules
#
# What does this simplification cost? What does it gain?
# Min 30 words.

CALM_VS_OLD_RASA = """
- LLM now handles slot extraction and decision-making re which dialogue path to follow, so it makes
our workflow less rigid, by naturally being able to cover more natural language patterns
- We also don't need to train a separate classified to pick a flow, LLM does it out of the box
- Python still handle the workflow steps execution, allowing for determinism and better auditability
- I'd say I trust regex results more than LLM parsing when it comes to actually matching strings. But the problem with regex, 
it can't cover all natural language patterns, so we have to reside to LLM here
"""

# ── The setup cost ─────────────────────────────────────────────────────────

# CALM still required: config.yml, domain.yml, flows.yml, endpoints.yml,
# rasa train, two terminals, and a Rasa Pro licence.
# The old Rasa ALSO needed nlu.yml, rules.yml, and a FormValidationAction.
#
# CALM is simpler. But it's still significantly more setup than LangGraph.
# That setup bought you something specific.
# Min 40 words.

SETUP_COST_VALUE = """
Some things Rasa CALM cannot do that LangGraph can:
- Improvise if the user sends something outside of the preconfigured flow. In more creative and risk-tolerant tasks this enables a better UX
- Call tools dynamically - Rasa picks encoded steps only, while LangGraph picks tools at runtime from the tool registry
- Re-plan - if a new requirement or unexpected user request appears mid-conversation, Rasa CALM will escalate, while LangGraph is capable of replanning, again, enabling a better UX in more risk-tolerant scenarios

For our specific booking confirmation use case though, those are not drawbacks but rather features. We want tighter control and strict programmatic execution to bring determinism
in this relatively less risk-tolerant use case, where non-reversible decisions, like making a deposit, are involved.
"""
