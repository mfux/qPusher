Apply the algorithm “Routing with Advertisements” on the router network in illustration 1. Write down which messages are flowing step-by-step (similar to the presented method in the lecture).
1) Publisher P sends an advertisement to router 1.
2) Subscriber S1 sends a subscription to router 5. Later, S2 sends a subscription to router 6.
3) Publisher P sends a notification to router 1.
(http://188.166.160.44:5555/img/router_network.png)


1) Discuss the pros and cons about “Routing with Advertisements” and “Routing with Subscriptions” in the context of a matchmaking system of a video game (i.e., publishers provide information on currently running gaming sessions to the clients).
2) In general, which type of routing is more suitable for which type of application? Explain your decision.

Consider the Router Network in Illustration 1. Apply the algorithm “Routing with Subscriptions”.
1) Subscriber S sends a subscription to router 1 with filter F. Describe the flow of the subscriptions between the routers, i.e. write down all routing tables in each step and paint the graph with the current flowing subscription also in each step. (Note: you can merge a step if a router sends multiple subscriptions concurrently)
2) Which problem arises and why? Give a solution to avoid this problem.
3) Does an equivalent problem arise if P sends a notification? Give also a solution if this is the case.
(http://188.166.160.44:5555/img/router_network2.png)

Define the term “Cloud Computing” in your own words. Give a real-world example of a cloud computing application.

Explain the terms SaaS, PaaS and IaaS. Give an example application for each of them.

Why is node replication a good idea? Describe the replica placement policy and list 3 advantages of using node replication.

You want to analyze multiple terabytes of webserver access logs. These logs are text files and they enlist one access per line. The third column (separated by semicolons) contains the URL of the accessed page. The aim is to create a report that lists all the URLs together with the number of hits. Please, write pseudocode for each step and make use of MapReduce. Note: You can omit the pseudocode for the Input Reader.

Give your own definition of what a Distributed System is. Name three basic problems and requirements of a distributed system.

Describe the two different system models that were presented during the lecture.

Describe the four principles of programming abstractions wrt. distributed software development.

Describe the pros and cons of the Distributed Pogramming Language Approach.

You want to implement RPC with at-least-once failure semantics. What are the implications of that failure semantic?
Please give an example when this failure semantic is fine to use, and one example in which the at-least-once failure semantic is not sufficient (both with short explanation!). Considering a function that is responsible for receiving and performing bank transfers. Is the at-least-once failure semantic sufficient? If not, which failure semantic should be implemented and why?

a) Define the term “Marshalling”. Why is it a necessity in (some) distributed systems?

b) There are two possibilities to approach marshalling. Explain and compare them with their pros and cons.

Describe the difference between Request-Reply (RR) and Request-Reply-Acknowledge (RRA) protocols. What are the advantages and disadvantages of RRA in comparison to RR?

Initially, concurrency was an issue of operating systems with concurrent languages. Why is it relevant to distributed systems?

Explain in a few sentences (with your own words) the introduced concepts of a Monitor.

Describe for each type of transparency (cmp. Chapter 1) if it is provided by RMI and give a short explanation why.

A client executes RMI on a server. The client requires 3 ms to compute the arguments for each request, and the server requires 10 ms to process each request. The process time of the local operating system of each send or receive operation is 0.4 ms and the network time to transfer the request or response is 3.5 ms. The Marshalling and Demarshalling takes 1 ms in total per message.
Estimate the time, which the client requires to generate two requests and obtain a refund, if
1. it is single-threaded
2. it has two threads, which can generate concurrent requests on a single processor. The server, which has also one processor, processes the requests in order of the received message.

Give your own definition of what a distributed System is,
and describe three (from the seven) requirements of a distributed system.

Mention and explain the three basic problems that a distributed system has that a single-processor system does not have. For each of the three problems of distributed systems, give a concrete example.

Name and describe the four different distributed software development approaches.
Why do you think the Distributed Programming Approach is the most widespread
approach of all?
Describe the pros and cons of the Distributed Programing Language approach

Describe the two different system models that were presented during the lecture.

What is the role of a Directory Server in the binding process?

Name the RPC failure semantics.

What are the implications of at-least-once semantic?
Which semantic would you use for bank transfers function? Why?

Describe the Monitor concept in your words. How to apply this concept in Java?

Describe the basic operations that can be performed for a resource in REST APIs.

A client executes RMI on a server. The client requires 7 ms to compute the arguments for each request, and the server requires 15 ms to process each request. The process time of the local operating system of each send or receive operation is 0.6 ms and the network time to transfer the request or response is 2.5 ms. The Marshalling takes 1.4 ms per message, and the same time is required for Demarshalling.
Estimate the time, which the client requires to generate two requests and obtain a refund, if
1. it is single-threaded
2. it has two threads, which can generate concurrent requests on a single processor. The server, which has also one processor, processes the requests in order of the received message.
