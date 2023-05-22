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

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**python_repl**

- Tool Name: Python REPL
- Tool Description: A Python shell. Use this to execute python commands. Input should be a valid python command. If you expect output it should be printed out.
- Notes: Maintains state.
- Requires LLM: No

**serpapi**

- Tool Name: Search
- Tool Description: A search engine. Useful for when you need to answer questions about current events. Input should be a search query.
- Notes: Calls the Serp API and then parses results.
- Requires LLM: No

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**wolfram-alpha**

- Tool Name: Wolfram Alpha
- Tool Description: A wolfram alpha search engine. Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Input should be a search query.
- Notes: Calls the Wolfram Alpha API and then parses results.
- Requires LLM: No
- Extra Parameters: `wolfram_alpha_appid`: The Wolfram Alpha app id.

**requests**

- Tool Name: Requests
- Tool Description: A portal to the internet. Use this when you need to get specific content from a site. Input should be a specific url, and the output will be all the text on that page.
- Notes: Uses the Python requests module.
- Requires LLM: No

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**wolfram-alpha**

- Tool Name: Wolfram Alpha
- Tool Description: A wolfram alpha search engine. Useful for when you need to answer questions about Math, Science, Technology, Culture, Society and Everyday Life. Input should be a search query.
- Notes: Calls the Wolfram Alpha API and then parses results.
- Requires LLM: No
- Extra Parameters: `wolfram_alpha_appid`: The Wolfram Alpha app id.

**requests**

- Tool Name: Requests
- Tool Description: A portal to the internet. Use this when you need to get specific content from a site. Input should be a specific url, and the output will be all the text on that page.
- Notes: Uses the Python requests module.
- Requires LLM: No

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**terminal**

- Tool Name: Terminal
- Tool Description: Executes commands in a terminal. Input should be valid commands, and the output will be any output from running that command.
- Notes: Executes commands with subprocess.
- Requires LLM: No

**pal-math**

- Tool Name: PAL-MATH
- Tool Description: A language model that is excellent at solving complex word math problems. Input should be a fully worded hard word math problem.
- Notes: Based on [this paper](https://arxiv.org/pdf/2211.10435.pdf).
- Requires LLM: Yes

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**llm-math**

- Tool Name: Calculator
- Tool Description: Useful for when you need to answer questions about math.
- Notes: An instance of the `LLMMath` chain.
- Requires LLM: Yes

**open-meteo-api**

- Tool Name: Open Meteo API
- Tool Description: Useful for when you want to get weather information from the OpenMeteo API. The input should be a question in natural language that this API can answer.
- Notes: A natural language connection to the Open Meteo API (`https://api.open-meteo.com/`), specifically the `/v1/forecast` endpoint.
- Requires LLM: Yes

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**news-api**

- Tool Name: News API
- Tool Description: Use this when you want to get information about the top headlines of current news stories. The input should be a question in natural language that this API can answer.
- Notes: A natural language connection to the News API (`https://newsapi.org`), specifically the `/v2/top-headlines` endpoint.
- Requires LLM: Yes
- Extra Parameters: `news_api_key` (your API key to access this endpoint)

**tmdb-api**

- Tool Name: TMDB API
- Tool Description: Useful for when you want to get information from The Movie Database. The input should be a question in natural language that this API can answer.
- Notes: A natural language connection to the TMDB API (`https://api.themoviedb.org/3`), specifically the `/search/movie` endpoint.
- Requires LLM: Yes
- Extra Parameters: `tmdb_bearer_token` (your Bearer Token to access this endpoint - note that this is different from the API key)

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**google-search**

- Tool Name: Search
- Tool Description: A wrapper around Google Search. Useful for when you need to answer questions about current events. Input should be a search query.
- Notes: Uses the Google Custom Search API
- Requires LLM: No
- Extra Parameters: `google_api_key`, `google_cse_id`
- For more information on this, see [this page](../../../ecosystem/google_search.md)

**searx-search**

- Tool Name: Search
- Tool Description: A wrapper around SearxNG meta search engine. Input should be a search query. 
- Notes: SearxNG is easy to deploy self-hosted. It is a good privacy friendly alternative to Google Search. Uses the SearxNG API. 
- Requires LLM: No
- Extra Parameters: `searx_host`

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**google-serper**

- Tool Name: Search
- Tool Description: A low-cost Google Search API. Useful for when you need to answer questions about current events. Input should be a search query.
- Notes: Calls the [serper.dev](https://serper.dev) Google Search API and then parses results.
- Requires LLM: No
- Extra Parameters: `serper_api_key`
- For more information on this, see [this page](../../../ecosystem/google_serper.md)

**wikipedia**

- Tool Name: Wikipedia
- Tool Description: A wrapper around Wikipedia. Useful for when you need to answer general questions about people, places, companies, historical events, or other subjects. Input should be a search query.
- Notes: Uses the [wikipedia](https://pypi.org/project/wikipedia/) Python package to call the MediaWiki API and then parses results.
- Requires LLM: No
- Extra Parameters: `top_k_results`

---

## Agent Tools

Tools are functions that agents can use to interact with the world.
These tools can be generic utilities (e.g. search), other chains, or even other agents.

Below are examples of supported tools

**podcast-api**

- Tool Name: Podcast API
- Tool Description: Use the Listen Notes Podcast API to search all podcasts or episodes. The input should be a question in natural language that this API can answer.
- Notes: A natural language connection to the Listen Notes Podcast API (`https://www.PodcastAPI.com`), specifically the `/search/` endpoint.
- Requires LLM: Yes
- Extra Parameters: `listen_api_key` (your api key to access this endpoint)

**openweathermap-api**

- Tool Name: OpenWeatherMap
- Tool Description: A wrapper around OpenWeatherMap API. Useful for fetching current weather information for a specified location. Input should be a location string (e.g. London,GB).
- Notes: A connection to the OpenWeatherMap API (https://api.openweathermap.org), specifically the `/data/2.5/weather` endpoint.
- Requires LLM: No
- Extra Parameters: `openweathermap_api_key` (your API key to access this endpoint)

---

## Memory: Add State to Chains and Agents

**Concept**

- This process allows you to add state to chains and agents with chat models.
- Rather than condensing all previous messages into a string, we keep them as unique memory objects.

**Implementation**

- You will need to import the following:

  - ChatPromptTemplate, MessagesPlaceholder, SystemMessagePromptTemplate, HumanMessagePromptTemplate from `langchain.prompts`.
  - ConversationChain from `langchain.chains`.
  - ChatOpenAI from `langchain.chat_models`.
  - ConversationBufferMemory from `langchain.memory`.

**Code Example**

- Sample initialization and usage:

    ```python
    prompt = ChatPromptTemplate.from_messages([...])
    llm = ChatOpenAI(temperature=0)
    memory = ConversationBufferMemory(return_messages=True)
    conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)
    conversation.predict(input="Hi there!")
    ```

---

## ConversationChain

**Component**

- This is a part of the `langchain.chains` module.
- It's used for creating a conversation instance.

**Code Example**

- Here is how to initialize a ConversationChain:

    ```python
    conversation = ConversationChain(memory=memory, prompt=prompt, llm=llm)
    ```

**Usage**

- Use `conversation.predict(input="Your Message")` to interact with the ConversationChain.

---

## ConversationBufferMemory

**Component**

- This is a part of the `langchain.memory` module.
- It is used for managing the conversation memory.

**Code Example**

- Here is how to initialize a ConversationBufferMemory:

    ```python
    memory = ConversationBufferMemory(return_messages=True)
    ```

**Usage**

- It is passed to the ConversationChain upon initialization.

---

## Memory with Chains and Agents

Memory can be used with chains and agents initialized with chat models. Rather than condensing all previous messages into a string, Memory can keep them as their own unique memory object.

---

## Chat Models

Chat models are used to initialize chains and agents. They are trained on a large dataset of text from the internet, which allows them to understand and generate human-like language.

---

## ConversationBufferMemory

`ConversationBufferMemory` is a class that can be used to store conversation history in memory. It returns messages as a list of strings.

---

## ConversationChain

`ConversationChain` is a class that can be used to create a conversation chain with memory. It takes a memory object, a prompt, and a chat model as input.

---

## ChatOpenAI

`ChatOpenAI` is a class that can be used to initialize a chat model with OpenAI's GPT-3. It takes a temperature parameter as input, which controls the creativity of the model.

---

**LLMChain**

- Chain Type: LLMChain
- Description: An LLMChain consists of a PromptTemplate and an LLM.
- Example:

```python
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.9)
prompt = PromptTemplate(
input_variables=["product"],
template="What is a good name for a company that makes {product}?",
)
chain = LLMChain(llm=llm, prompt=prompt)
chain.run("colorful socks")
# -> '\n\nSocktastic!'
```

---

**PromptTemplate**

- Primitive Type: PromptTemplate
- Description: A PromptTemplate is used to format user input.
- Example:

```python
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
input_variables=["product"],
template="What is a good name for a company that makes {product}?",
)
```

---

**LLM**

- Primitive Type: LLM
- Description: An LLM is a Language Model that generates text.
- Example:

```python
from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)
```

---

## Chains in LangChain

**Concept**

- Chains are made up of links, which can be primitives like LLMs or other chains.
- Chains in LangChain are used to create multi-step workflows.

**Chain Types**

- The core type of chain is an `LLMChain`, which consists of a `PromptTemplate` and an `LLM`.

**Implementation**

- Chains are initialized with the following steps:

  - Import PromptTemplate from `langchain.prompts`.
  - Import OpenAI from `langchain.llms`.
  - Create an instance of OpenAI.
  - Create an instance of PromptTemplate.

---

## LLMChain

**Component**

- This is a part of the `langchain.chains` module.
- It's used for creating a chain that consists of a PromptTemplate and an LLM.

**Code Example**

- Here is how to initialize an LLMChain:

    ```python
    from langchain.chains import LLMChain
    chain = LLMChain(llm=llm, prompt=prompt)
    ```

**Usage**

- Use `chain.run("Your Input")` to interact with the LLMChain.
- Example: `chain.run("colorful socks")` -> 'Socktastic!'

---

## PromptTemplate and OpenAI

**Concept**

- `PromptTemplate` is used to format user input.
- `OpenAI` is an example of an LLM.

**Code Example**

- Here is how to initialize a PromptTemplate and an OpenAI instance:

    ```python
    from langchain.prompts import PromptTemplate
    from langchain.llms import OpenAI

    llm = OpenAI(temperature=0.9)
    prompt = PromptTemplate(
        input_variables=["product"],
        template="What is a good name for a company that makes {product}?",
    )
    ```

**Usage**

- The PromptTemplate and OpenAI instance are used to create an LLMChain.

---

## Building LLM applications for production

A question that I’ve been asked a lot recently is how large language models (LLMs) will change machine learning workflows. After working with several companies who are working with LLM applications and personally going down a rabbit hole building my applications, I realized two things:

1. It’s easy to make something cool with LLMs, but very hard to make something production-ready with them.

2. LLM limitations are exacerbated by a lack of engineering rigor in prompt engineering, partially due to the ambiguous nature of natural languages, and partially due to the nascent nature of the field.

---

## Building LLM applications for production

Challenges of productionizing prompt engineering

### The ambiguity of natural languages

The flexibility comes from two directions: how users define instructions, and how LLMs respond to these instructions.

- Programming languages are mostly exact.
- In prompt engineering, instructions are written in natural languages
- Natural languages are ambiguous and flexible.
- Flexibility is a problem in the input as well as the output.
- Flexibility in input may lead to silent failures instead of error messages.

---

## Building LLM applications for production

Challenges of productionizing prompt engineering

### The ambiguity of natural languages

LLMs’ generated responses can be a dealbreaker. It leads to two problems:

1. **Ambiguous output format**: downstream applications on top of LLMs expect outputs in a certain format so that they can parse. We can craft our prompts to be explicit about the output format, but there’s no guarantee that the outputs will _always_ follow this format.

    ![LLM Engineering](https://huyenchip.com/assets/pics/llmops/1_ambiguous_output.png)

2. **Inconsistency in user experience**: when using an application, users expect certain consistency. Imagine an insurance company giving you a different quote every time you check on their website. LLMs are stochastic – there’s no guarantee that an LLM will give you the same output for the same input every time.

    You can force an LLM to give the same response by setting **[temperature = 0](https://platform.openai.com/docs/api-reference/completions/create#completions/create-temperature)**, which is, in general, a good practice. While it [mostly solves the consistency problem](https://community.openai.com/t/observing-discrepancy-in-completions-with-temperature-0/73380), it doesn’t inspire trust in the system. Imagine a teacher who gives you consistent scores only if that teacher sits in one particular room. If that teacher sits in different rooms, that teacher’s scores for you will be wild.

    ![LLM Engineering](https://huyenchip.com/assets/pics/llmops/2_ambiguous_output.png)

---

## Building LLM applications for production

Challenges of productionizing prompt engineering

### The ambiguity of natural languages

#### Recap

The two problems with responses generated from LLMs are ambigious output format and inconsistency in user experience. These problems are exacerbated by the fact that LLMs are stochastic and that natural languages are ambiguous. The ambiguity of natural languages is a problem in both the input and the output. In the input, it leads to silent failures instead of error messages. In the output, it leads to ambiguous output format and inconsistency in user experience.

**How to solve this ambiguity problem?**

This seems to be a problem that OpenAI is actively trying to mitigate. They have a notebook with tips on how to increase their models’ reliability.

A couple of people who’ve worked with LLMs for years told me that they just accepted this ambiguity and built their workflows around that. It’s a different mindset compared to developing deterministic programs, but not something impossible to get used to.

This ambiguity can be mitigated by applying as much engineering rigor as possible.

---

## Building LLM applications for production

### Prompt Engineering

Techniques how to make prompt engineering, if not deterministic, systematic.

#### Prompt evaluation

A common technique for prompt engineering is to provide in the prompt a few examples and hope that the LLM will generalize from these examples (fewshot learners).

As an example, consider trying to give a text a controversy score – it was a fun project that I did to find the correlation between a tweet’s popularity and its controversialness. Here is the shortened prompt with 4 fewshot examples:

##### Example: controversy scorer

```txt
Given a text, give it a controversy score from 0 to 10.

Examples:

1 + 1 = 2
Controversy score: 0

Starting April 15th, only verified accounts on Twitter will be eligible to be in For You recommendations
Controversy score: 5

Everyone has the right to own and use guns
Controversy score: 9

Immigration should be completely banned to protect our country
Controversy score: 10

The response should follow the format:

Controversy score: { score }
Reason: { reason }

Here is the text.
```

When doing fewshot learning, two questions to keep in mind:

1. **Whether the LLM understands the examples given in the prompt**. One way to evaluate this is to input the same examples and see if the model outputs the expected scores. If the model doesn’t perform well on the same examples given in the prompt, it is likely because the prompt isn’t clear – you might want to rewrite the prompt or break the task into smaller tasks (and combine them together, discussed in detail in Part II of this post).
2. **Whether the LLM overfits to these fewshot examples.** You can evaluate your model on separate examples.

One thing I’ve also found useful is to ask models to give examples for which it would give a certain label. For example, I can ask the model to give me examples of texts for which it’d give a score of 4. Then I’d input these examples into the LLM to see if it’ll indeed output 4.

---

## Building LLM applications for production

### Prompt Engineering

Techniques how to make prompt engineering, if not deterministic, systematic.

#### Prompt versioning

Small changes to a prompt can lead to very different results. It’s essential to version and track the performance of each prompt. You can use git to version each prompt and its performance, but I wouldn’t be surprised if there will be tools like MLflow or Weights & Biases for prompt experiments.

---

## Building LLM applications for production

### Prompt Engineering

Techniques how to make prompt engineering, if not deterministic, systematic.

#### Prompt optimization

There have been many papers + blog posts written on how to optimize prompts. I agree with Lilian Weng in [her helpful blog post](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) that most papers on prompt engineering are tricks that can be explained in a few sentences. OpenAI has a great notebook that explains many [tips with examples](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md#how-to-improve-reliability-on-complex-tasks). Here are some of them:

- Prompt the model to explain or explain step-by-step how it arrives at an answer, a technique known as [Chain-of-Thought](https://arxiv.org/abs/2201.11903) or COT (Wei et al., 2022). **Tradeoff**: COT can increase both latency and cost due to the increased number of output tokens \[see **Cost and latency** section\]
- Generate many outputs for the same input. Pick the final output by either the majority vote (also known as [self-consistency technique](https://arxiv.org/abs/2203.11171) by Wang et al., 2023) or you can ask your LLM to pick the best one. In OpenAI API, you can generate multiple responses for the same input by passing in the argument [n](https://platform.openai.com/docs/api-reference/completions/create) (not an ideal API design if you ask me).
- Break one big prompt into smaller, simpler prompts.

Many tools promise to auto-optimize your prompts – they are quite expensive and usually just apply these tricks. One nice thing about these tools is that they’re no code, which makes them appealing to non-coders.

---

## Building LLM applications for production

### Prompt Engineering

#### Cost

The more explicit detail and examples you put into the prompt, the better the model performance (hopefully), and the more expensive your inference will cost.

OpenAI API charges for both the input and output tokens. Depending on the task, a simple prompt might be anything between 300 - 1000 tokens. If you want to include more context, e.g. adding your own documents or info retrieved from the Internet to the prompt, it can easily go up to 10k tokens for the prompt alone.

The cost with long prompts isn’t in experimentation but in inference.

Experimentation-wise, **prompt engineering is a cheap and fast way get something up and running**. For example, even if you use GPT-4 with the following setting, your experimentation cost will still be just over $300. The traditional ML cost of collecting data and training models is usually much higher and takes much longer.

- Prompt: 10k tokens ($0.06/1k tokens)
- Output: 200 tokens ($0.12/1k tokens)
- Evaluate on 20 examples
- Experiment with 25 different versions of prompts

**The cost of LLMOps is in inference.**

- If you use GPT-4 with 10k tokens in input and 200 tokens in output, it’ll be $0.624 / prediction.
- If you use GPT-3.5-turbo with 4k tokens for both input and output, it’ll be $0.004 / prediction or $4 / 1k predictions.
- As a thought exercise, in 2021, DoorDash ML models made [10 billion predictions a day](https://www.databricks.com/session_na21/scaling-online-ml-predictions-at-doordash). If each prediction costs $0.004, that’d be $40 million a day!
- By comparison, AWS personalization costs about [$0.0417 / 1k predictions](https://aws.amazon.com/personalize/pricing/) and AWS fraud detection costs about [$7.5 / 1k predictions](https://aws.amazon.com/fraud-detector/pricing/) \[for over 100,000 predictions a month\]. AWS services are usually considered prohibitively expensive (and less flexible) for any company of a moderate scale.

---

## Building LLM applications for production

### Prompt Engineering

#### Latency

Input tokens can be processed in parallel, which means that input length shouldn’t affect the latency that much.

However, output length significantly affects latency, which is likely due to output tokens being generated sequentially.

Even for extremely short input (51 tokens) and output (1 token), the latency for _gpt-3.5-turbo_ is around 500ms. If the output token increases to over 20 tokens, the latency is over 1 second.

Here’s an experiment I ran, each setting is run 20 times. All runs happen within 2 minutes. If I do the experiment again, the latency will be very different, but the relationship between the 3 settings should be similar.

This is another challenge of productionizing LLM applications using APIs like OpenAI: **APIs are very unreliable, and no commitment yet on when SLAs will be provided.**

table { border-collapse: collapse; width: 100%; } th, td { padding: 8px; text-align: left; border-bottom: 1px solid #ddd; }

| **\# tokens** | **p50 latency (sec)** | **p75 latency** | **p90 latency** |
| ------------- | --------------------- | --------------- | --------------- |
| input: 51 tokens, output: 1 token | 0.58 | 0.63 | 0.75 |
| input: 232 tokens, output: 1 token | 0.53 | 0.58 | 0.64 |
| input: 228 tokens, output: 26 tokens | 1.43 | 1.49 | 1.62 |

It is, unclear, how much of the latency is due to model, networking (which I imagine is huge due to high variance across runs), or some just inefficient engineering overhead. It’s very possible that the latency will reduce significantly in a near future.

While half a second seems high for many use cases, this number is incredibly impressive given how big the model is and the scale at which the API is being used. The number of parameters for gpt-3.5-turbo isn’t public but is guesstimated to be around 150B. As of writing, no open-source model is that big. Google’s T5 is 11B parameters and Facebook’s largest LLaMA model is 65B parameters. People discussed on [this GitHub thread](https://github.com/facebookresearch/llama/issues/79) what configuration they needed to make LLaMA models work, and it seemed like getting the 30B parameter model to work is hard enough. The most successful one seemed to be _randaller_ who was able to get the [30B parameter model work on 128 GB of RAM](https://github.com/randaller/llama-chat), which takes a few seconds just to generate one token.

---

## Building LLM applications for production

### Prompting vs. finetuning vs. alternatives

- Prompting: for each sample, explicitly tell your model how it should respond.
- Finetuning: train a model on how to respond, so you don’t have to specify that in your prompt.

![LLM Engineering: Prompting vs. finetuning](https://huyenchip.com/assets/pics/llmops/3_prompting_vs_finetuning.png)

There are 3 main factors when considering prompting vs. finetuning: data availability, performance, and cost.

If you have only a few examples, prompting is quick and easy to get started. **There’s a limit to how many examples you can include in your prompt due to the maximum input token length.**

The number of examples you need to finetune a model to your task, of course, depends on the task and the model. In my experience, however, you can expect a noticeable change in your model performance if you finetune on 100s examples. However, the result might not be much better than prompting.

In [How Many Data Points is a Prompt Worth?](https://arxiv.org/abs/2103.08493) (2021), ​​Scao and Rush found that a prompt is worth approximately 100 examples (caveat: variance across tasks and models is high – see image below). The general trend is that **as you increase the number of examples, finetuning will give better model performance than prompting**. There’s no limit to how many examples you can use to finetune a model.

![Prompting vs. finetuning: number of examples needed](https://huyenchip.com/assets/pics/llmops/4_prompting_vs_finetuning_data.png)

The benefit of finetuning is two folds:

1. You can get better model performance: can use more examples, examples becoming part of the model’s internal knowledge.
2. You can reduce the cost of prediction. The more instruction you can bake into your model, the less instruction you have to put into your prompt. Say, if you can reduce 1k tokens in your prompt for each prediction, for 1M predictions on _gpt-3.5-turbo_, you’d save $2000.

---

## Building LLM applications for production

### Prompting vs. finetuning vs. alternatives

- Prompting: for each sample, explicitly tell your model how it should respond.
- Finetuning: train a model on how to respond, so you don’t have to specify that in your prompt.

Here are some alternatives to prompting and finetuning:

#### Prompt tuning

A cool idea that is between prompting and finetuning is **[prompt tuning](https://arxiv.org/abs/2104.08691)**, introduced by Leister et al. in 2021. Starting with a prompt, instead of changing this prompt, you programmatically change the embedding of this prompt. For prompt tuning to work, you need to be able to input prompts’ embeddings into your LLM model and generate tokens from these embeddings, which currently, can only be done with open-source LLMs and not in OpenAI API. On T5, prompt tuning appears to perform much better than prompt engineering and can catch up with model tuning (see image below).

![LLM Engineering: Prompt tuning](https://huyenchip.com/assets/pics/llmops/5_prompt_tuning.png)

#### Finetuning with distillation

In March 2023, a group of Stanford students released a promising idea: finetune a smaller open-source language model (LLaMA-7B, the 7 billion parameter version of LLaMA) on examples generated by a larger language model (_text-davinci-003_ – 175 billion parameters). This technique of training a small model to imitate the behavior of a larger model is called distillation. The resulting finetuned model behaves similarly to _text-davinci-003_, while being a lot smaller and cheaper to run.

For finetuning, they used 52k instructions, which they inputted into _text-davinci-003_ to obtain outputs, which are then used to finetune LLaMa-7B. This costs under $500 to generate. The training process for finetuning costs under $100. See [Stanford Alpaca: An Instruction-following LLaMA Model](https://github.com/tatsu-lab/stanford_alpaca) (Taori et al., 2023).

![LLM Engineering: Alpaca](https://huyenchip.com/assets/pics/llmops/6_alpaca.png)

The appeal of this approach is obvious. After 3 weeks, their GitHub repo got almost 20K stars!! By comparison, [HuggingFace’s transformers](https://github.com/huggingface/transformers) repo took over a year to achieve a similar number of stars, and [TensorFlow](https://github.com/tensorflow/tensorflow) repo took 4 months.

![LLM Engineering: Alpaca GitHub stars](https://huyenchip.com/assets/pics/llmops/7_alpaca_github_stars.png)

---
