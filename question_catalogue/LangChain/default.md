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