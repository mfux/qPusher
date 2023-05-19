Initially, concurrency was an issue of operating systems with concurrent languages. Why is it relevant to distributed systems?

---

## Chain of Thought Paradigms in LLMs

Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning. 

One Example for a strategy:

**Few-shot CoT.** Provide examples of Question-Answer pairs where the answer is explained "step by step."

> Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
> 
> A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 6 tennis balls. 5 + 6 = 11. The answer is 11.

---

## Chain of Thought Paradigms in LLMs

Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning. 

One Example for a strategy:

**Zero-shot CoT**. Prefix the Answer block with "Let's think step by step." to prompt the LLM to complete the output in that format.

---

## Chain of Thought Paradigms in LLMs

Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning. 

One Example for a strategy:

**Self-consistency CoT.** First, prompt the model with CoT, generate multiple completions, and choose the most consistent answer. You can think of this as a self-ensemble method.

---


## Chain of Thought Paradigms in LLMs

Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning. 

One Example for a strategy:

**Least-to-Most.** Borrowed from an idea in education psychology, generating a list of questions to answer and then sequentially solving the subquestions. Problem reduction followed by problem-solving.

---

## Chain of Thought Paradigms in LLMs

Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning. 

One Example for a strategy:

**ReAct.** Given a claim or question, generate a completion identifying an action to take, record the action, and make an observation from the result. Repeat until the task is finished, recognized by calling a special FINISH action.

> Thought:
> Action:
> Observation:
> Claim: Princess Mononoke is a film. 
> Thought 1: I need to search Princess Mononoke and find if it is a film. Action 1: Search[Princess Mononoke] Observation 1: Princess Mononoke ... Thought 2: From the observation, it says that Princess Mononoke is a film. Action 2: Finish[SUPPORTS] 
> Observation 2: Episode finished

---

## Agent Types

Agents use an LLM to determine which actions to take and in what order.
An action can either be using a tool and observing its output, or returning a response to the user.
Here are the agents available in LangChain.

### `zero-shot-react-description`

This agent uses the ReAct framework to determine which tool to use
based solely on the tool's description. Any number of tools can be provided.
This agent requires that a description is provided for each tool.

---

## Agent Types

Agents use an LLM to determine which actions to take and in what order.
An action can either be using a tool and observing its output, or returning a response to the user.
Here are the agents available in LangChain.

## `react-docstore`

This agent uses the ReAct framework to interact with a docstore. Two tools must
be provided: a `Search` tool and a `Lookup` tool (they must be named exactly as so).
The `Search` tool should search for a document, while the `Lookup` tool should lookup
a term in the most recently found document.
This agent is equivalent to the
original [ReAct paper](https://arxiv.org/pdf/2210.03629.pdf), specifically the Wikipedia example.

---

## Agent Types

Agents use an LLM to determine which actions to take and in what order.
An action can either be using a tool and observing its output, or returning a response to the user.
Here are the agents available in LangChain.

## `self-ask-with-search`

This agent utilizes a single tool that should be named `Intermediate Answer`.
This tool should be able to lookup factual answers to questions. This agent
is equivalent to the original [self ask with search paper](https://ofir.io/self-ask.pdf),
where a Google search API was provided as the tool.

---

## Agent Types

Agents use an LLM to determine which actions to take and in what order.
An action can either be using a tool and observing its output, or returning a response to the user.
Here are the agents available in LangChain.

### `conversational-react-description`

This agent is designed to be used in conversational settings.
The prompt is designed to make the agent helpful and conversational.
It uses the ReAct framework to decide which tool to use, and uses memory to remember the previous conversation interactions.