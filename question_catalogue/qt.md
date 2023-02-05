Assume you want to determine the maximal available bandwidth of your mobile connection. Which of TCP and UDP is suitable for this use case. Explain why?

Describe the purpose of Flow Control and Congestion Control.

Name and explain the strategies that are used in the congestion avoidance phase of TCP.

How could a TCP sender perceive that there is congestion on the path between itself and the destination?

How does TCP probe for the maximal available bandwidth? Provide and explain a figure to support your answer.

In slow start phase, what is the initial value of the congestion window? What is the increment rate for this window and when is it updated?

In slow start phase, when should the exponential growth of cwnd end?

What are the three states of TCP congestion control and which transitions between those states exist? (state diagram)

Host A is transferring an image with a size of 15MByte to Host B using a TCP connection. The roundtrip time RTT = 25ms and the link speed is LS = 1Gbit/s. The maximum segment size is equal to 2000 bytes, ss_th = ∞. The senders cwnd has a size of cwnd = ∞. How long does the transmission of the image take?

Host A is transferring an image with a size of 15MByte to Host B using a TCP connection. The roundtrip time RT T = 100ms and the link speed is LS = 2Gbit/s. The maximum segment size is equal to 500 bytes and ss_th = ∞. The senders cwnd has a size of 1MSS. How long takes the transmission of the image?

**What would *not* cause an MPTCP connection to fail?**
[ ] No sure, actually I think MPTCP is backwards compatible
[ ] Would make MPTCP to fail, because TCP options are used to implement it, and a router removing those would cause errors
[ ] MPTCP is built ontop of regular TCP therefore its ok if a router does only support regular TCP
[ ] Not sure if MPTCP is solely realized with TCP options or maybe also in the TCP payload

**What is *not* part of the MPTCP architecture**
[ ] Security (To some extend, because choosing the IDSN Initial Data Sequence Number randomly is good for security (higjacking))
[ ] Packet Scheduler ()
[ ] 4-Way Handshake (I only saw a 3-Way Handshake one Slide 31
[ ] Fast Close (On Slide 77. )

**MPTCP provides the following benefits over TCP**
[ ] Haven't found 'framing' in the slides
[ ] 'Multi Streaming' is not mentioned aswell.
[ ] Vanilla TCP comes with adaptive Flow Control aswell.
[ ] Yes, that is a very important feature of MPTCP. (Multi Homing = Connections via multiple different interfaces)

Why is mobile handover a challenge for normal TCP? How is MPTCP solving this challenge?

MPTCP uses the MP-CAPABLE flag in the connections establishment process. Why is that flag used and why is there an additional MP-CAPABLE flag in the third step of the handshake?

Name three network related advantages of MPTCP.

Each TCP Segment contains a checksum. Multipath TCP adds an additional checksum to each transferred segment. Why is this second checksum necessary?

What problems may occur if you use an application layer firewall or an intrusion detection system which is not MPTCP-aware, but does not block the MPTCP traffic and does not block the MPTCP option?

With which combination of protocols can Quic be compared? And why is this combination not as efficient as Quic?

**Which of the following statements are true for telephone networks?**
I: Connectionless service
II: Circuit switching is used
III: A dedicated line between caller and callee is maintained
IV: Communication not always follows same path
V: Packets are forwarded from sender to receiver via relay stations
(A) I, IV, V
(B) I, II, IV
(C) II and III
(D) II, III, IV
(E) III and V

Which Layer does NOT lie between Session layer and Physical layer in the OSI Layer model?
(A) Transport Layer
(B) Network Layer
(C) Presentation Layer
(D) Data Link Layer

What are functions of the Network Layer?
I: Reliable data transfer between adjacent stations
II: Connection between end systems
III: Connection between applications
IV: Flow control
V: Congestion control
VI: Addressing of stations
(A) II, IV, V
(B) III, IV, V
(C) I, II, III
(D) II, V, VI
(E) I, II, VI

Associate following tasks with corresponding layer in the OSI Layer model, in correct order.
• flow control
• initiation and termination of connection
• composing an email
• coordination of simultaneous processing of different applications
(A) application, session, presentation, physical
(B) data link, physical, application, session
(C) transport, physical, data link, session
(D) transport, physical, application, session

What's the difference in spacing in Baudot and Morse encoding? Why does it matter?

There are 6 households that want to communicate with each other. Consider the following two
scenarios:
• Phones are sold pairwise and hard-wired.
• Phones are connected to a central switchboard by which an arbitrarily chosen pair of phones can be connected.
Draw both scenarios.
How many phones are required per household? How many lines are required to connect the
phones? What is the complexity of the number of phones/number of lines?

What three types of switching do you know? Explain the differences and name an application scenario for each one. How has switching in telephone networks evolved over time?

What happens with user data when it is transmitted from a sending application on one system to a receiving application on a different system? Describe the process with respect to a layered architecture, with the help of an illustration.

What is the difference between a connectionless and a connection-oriented service? Which phases typically consititute a connection-oriented service?

You open the URL http://kom.tu-darmstadt.de in your browser. Which transport and application layer protocols are involved in the communication set-up from the moment you hit the enter button?

The NASA uses a digital camera video to remote monitor the Mars Rover Curiosity. This video stream is transmitted over an interplanetary network from Mars to Earth. The distance from Mars to Earth is currently d = 75,000,000km.
• A: What is the minimum travel time of a data packet transmitted from the Mars Rover back to Earth, assuming the speed of light, v = 300,000,000m/s?
• B: The control center on Earth requests a 10 MByte large sensor data chunk from Curiosity. How long does it take from sending the request until the response is fully received on Earth? Assume a bi-directional link speed of LS = 5 Mbit/s.
• C: Calculate the bandwidth delay product of the connection.
• D: Should human operators control every movement of Curiosity, remotely? Or would it be better if Curiosity drives to a specified destination autonomously? Briefly explain your answer.

**Which of the following statements are true for telephone networks?**
I: Connectionless service
II: Circuit switching is used
III: A dedicated line between caller and callee is maintained
IV: Communication not always follows same path
V: Packets are forwarded from sender to receiver via relay stations
(A) I, IV, V
(B) I, II, IV
(C) II and III
(D) II, III, IV
(E) III and V

**What does "IETF" stand for?**
(A) International Engineers Task Force
(B) Internet Evil Telephone Formation
(C) International Engineering Task Force
(D) Internet Engineering Task Force
(E) Institute of Electrical Telecommunication Formation

**Which Layer does not belong to the TCP/IP Layer model?**
(A) Transport Layer
(B) Network Layer
(C) Application Layer
(D) Session Layer
(E) Link Layer

**What are functions of the Network Layer?**
I: Reliable data transfer between adjacent stations
II: Connection between end systems
III: Connection between applications
IV: Flow control
V: Congestion control
VI: Addressing of stations
(A) II, IV, V
(B) III, IV, V
(C) I, II, III
(D) II, V, VI
(E) I, II, VI

Encode the text Communication Networks using Morse code. How many bits are required for the code?

Encode the text Communication Networks using Baudot code. How many bits are required for the code?

What is the fundamental difference between Morse code and Baudot code and how is it related to time multiplexing?

(A) Assume that phones are sold pairwise and hard-wired. Assume a scenario with 100 households in which an arbitrarily chosen pair of households shall be able to communicate via telephone. How many phones are required per household? How many lines are required to connect the phones? What is the complexity?
(B) Now assume that phones are connected to a central switchboard by which an arbitrarily chosen pair of phones can be connected. How do the numbers change?

What type of switching was used in telegraph networks? What is the difference to switching in today’s Internet?

Explain how switching in telephone networks changed from the beginning until today.

What kind of medium is television? What is the difference to telephony and telegraphy?

What are the fundamental differences between the ISO/OSI model, the TCP/IP model, and the 5-layer model for describing communication networks?

What happens with user data as it is transmitted from a sending application to a receiving application? Sketch the procedure subject to the layer models?

Describe the concept of Flow Control. Also describe the concept of Congestion Control. What are the differences between both principles?

How could a TCP sender limit the rate at which it sends traffic into its connection?

How could a TCP sender perceive that there is congestion on the path between itself and the destination?

How does TCP probe for the maximal available bandwidth?

What is the average throughput of a TCP connection in steady state? (Assume no slow start is happening and a constant path capacity)

What are the three states of TCP congestion control?

In slow start phase, what is the initial value of the congestion window? What is the increment rate for this window?

In slow start phase, when should the exponential growth of *cwnd* end?

In congestion avoidance phase, what is the initial value of the congestion window and what is the increment rate for this window?

In congestion avoidance phase, when should the congestion avoidance’s linear increase (of 1 MSS per RTT) end?

What happens in TCP fast recovery phase? Please give a detailed explaination.

There exists a stop-and-wait algorithm for reliable data transmissions which sends a segment and waits for its corresponding acknowledgment before sending the next segment. Discuss main disadvantages of this stop-and-wait algorithm in comparison to *cwnd* based approaches.

Simulate the congestion control algorithm of TCP. It is sufficient to implement the two states slow start and congestion avoidance.

Explain the general idea and the basic concept of MPTCP. What are MPTCPs two main applications?

Name and explain the three operating modes of MPTCP.

Fill in the schematic MPTCP message exchange on the next page, attempting to send ’abcdefg!’ from A to B. Assume no package loss. Note: You only need to add packages in the Connection Teardown phase.
(http://188.166.160.44:5555/img/mptcp_seq.png)

How are sequence numbers handled in MPTCP and why? What problem still persists, how is it detected and handled?

Complete the partially filled middleware characteristic table below.
(http://188.166.160.44:5555/img/middleware_table.png)

**What would not cause an MPTCP connection to fail?**
- [ ] One of the involved Endsystems does not support MPTCP.
- [ ] A middlebox on the path removes all unknown TCP options.
- [ ] A router on the path does not support MPTCP.
- [ ] The payload of packages is changed.

**What is not part of the MPTCP architecture?**
- [ ] Congestion Control
- [ ] Control Plane
- [ ] Data Plane
- [ ] 4-way Handshake
- [ ] Fast Close


**MPTCP provides the following benefits over TCP**
- [ ] Framing of Messages
- [ ] Multi Streaming
- [ ] Adaptive Flow Control
- [ ] Multi Homing


**What is not an objective of MPTCP?**
- [ ] To work on unmodified applications
- [ ] To work over all current networks
- [ ] To work where TCP works
- [ ] To reduce the latency of connections

Please explain the connection setup of the FTP protocol.

Why is there a strict distinction between a Control Channel and a Data Channel?

Please name and explain common problems of the FTP Protocol.

Compare telnet and ssh. What are the differences between those protocols?

What is the motivation for building distributed systems? Name four desired properties.

Which eight transparencies influence the design of a distributed system?

Please explain the location transparency and give an application example.

Remote Procedure Call systems are used to invoke procedures on remote hosts. To do so, some steps are necessary. Name and describe these steps. Also describe on which node these steps happen?

RPC usually uses UDP as transport layer protocol. As UDP is not reliable, some RPC packets might get lost. This loss causes the RPC call to fail. But there are four strategies (“failure semantics”) to handle those failures. Please name and explain these semantics.

Please name and describe the three main components of the RMI middleware. Please also draw an image that describes how these components communicate with each other.

Please name and describe the differences between local and distributed objects. Hint: Which operations exist in the object live cycle of local and remote objects? How do those operations differ for local and remote objects?

What does RTP/RTCP stand for and how do the 2 protocols interact? What is RTP used for? Why is there no retransmission mechanism integrated in RTP?
