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

