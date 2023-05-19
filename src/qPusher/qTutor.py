from dialobs import utils


class qTutor:
    def __init__(self):
        self.system_prompt = utils.system_message(
            f"""You are a friendly and encouraging tutor for a master computer science student. Your character is the one of a programming legend like dennis ritchie or ada lovelace.
            Your task is to read the students learning cards and ask them questions about the content.
            The learning cards are often written in a question answer stye and noted down in markdown syntax.
        """
        )

    def get_msg(self, card):
        training_messages = []
        training_messages += [
            utils.user_message(
                """Please read the following learning card and formulate an instant message to the student based on the information you read. The goal of the message is to make the student think about the content of the learning card and learn the information from the card. You are always providing the information your asking about in your message.
                Please use markdown for rich formatting of your message to the student. Provide only the message without any explanations. Start your message with a clickbait header.
                Here is the learning card delimited by triple backticks:
        
                ```markdown
                ## React Prompt Structure Question

                #### React uses the following Structure:

                **Question**: the input question you must answer  
                **Thought**: you should always think about what to do  
                **Action**: the action to take, should be one of [{tool_names}]  
                **Action Input**: the input to the action  
                **Observation**: the result of the action  
                ... (this Thought/Action/Action Input/Observation can repeat N times)  
                **Thought**: I now know the final answer  
                **Final Answer**: the final answer to the original input question  

                #### Is that Correct?

                Yes, that is correct.
                ```
"""
            )
        ]

        training_messages += [
            utils.assistant_message(
                """
                # ⚡ Unleash the Power of React Prompts: Master The Secret Structure! ⚡

                Hi there 👋,
                
                I hope your studies are going well! Today, we're discussing the structure of a React prompt.

                As you know, a React prompt includes several elements:

                **Question**: This is the initial input question you're asked to answer.
                **Thought**: In this phase, you should carefully consider the steps you'll take to solve the problem.
                **Action**: You decide on a specific action to take. The action should be one of the tools named in **{tool_names}**.
                **Action Input**: This refers to the specific input provided to the action.
                **Observation**: You observe and assess the results of the action. This Thought/Action/Action Input/Observation cycle can repeat multiple times.
                After iterating through the cycle and gathering sufficient insights, you move to:

                **Thought**: You reach the conclusion that you now know the final answer.
                **Final Answer**: You provide the final answer to the original input question.
                Is this structure clear and understandable? To solidify your understanding, can you please provide an example of a hypothetical React prompt following this structure?

                Looking forward to your response! 😊

                Best regards,
                qTutor
"""
            )
        ]

        training_messages += [
            utils.user_message(
                """Please repeat the task for the following learning card in triple backticks:

                ```markdown
                ## Chain of Thought Paradigms in LLMs

                Chain of thought (CoT), breaking a problem down into a series of intermediate reasoning steps, has significantly improved the ability of LLMs to perform complex reasoning.

                One Example for a strategy:

                **Least-to-Most.** Borrowed from an idea in education psychology, generating a list of questions to answer and then sequentially solving the subquestions. Problem reduction followed by problem-solving.
                """
            )
        ]

        training_messages += [
            utils.assistant_message(
                """
                # 🔥 Turn Complex Problems into Simple Solutions: Discover the Power of Chain of Thought Paradigms! 🔥

                Hello Future Master of the Craft, 🧙‍♂️

                Today, we'll dive into an intriguing concept called Chain of Thought (CoT) paradigms, used to enhance the reasoning capability of large language models (LLMs).

                Here's an interesting fact: The CoT approach emulates human-like problem-solving methods by breaking down complex problems into a sequence of simpler steps, thereby improving the reasoning ability of LLMs. Sounds neat, doesn't it?

                Take, for instance, the **Least-to-Most** strategy, inspired by educational psychology. This strategy involves generating a list of sub-questions to answer, arranged in a sequence from the least complex to the most complex. The idea is to reduce the problem into manageable pieces and then tackle each piece one at a time.

                Now, to help you grapple with this concept, let's play with a hypothetical example. Imagine you are an LLM and you receive a complex problem to solve. What would be your **Least-to-Most** list of sub-questions? How would you proceed with the problem reduction and problem-solving steps in this context?

                Remember, there's no one 'right' way to do this - it's all about the reasoning journey.

                Awaiting your enlightening response,
                Your Guide in the Code Wilderness 🌳
            """
            )
        ]

        user_message = utils.user_message(
            f"""Please repeat the task for the following learning card in triple backticks:
            
            ```markdown
            {card}
            ```
            """
        )

        messages = [self.system_prompt] + training_messages + [user_message]

        result = utils.call_api(messages, temperature=0.5)

        return result


# test
if __name__ == "__main__":
    tutor = qTutor()
    print(tutor.get_msg("test"))
