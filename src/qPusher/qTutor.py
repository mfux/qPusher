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
                f"""Please read the following learning card and formulate an instant message to the student based on the information you read. The goal of the message is to make the student think about the content of the learning card and learn the information from the card. You are always providing the information your asking about in your message.
        Please use markdown for rich formatting of your message to the student. Provide only the message without any explanations.
        Here is the learning card:
        
        {card}"""
            )
        ]

        training_messages += [
            utils.assistant_message(
                f"""Hey there! 👋
        I hope you're doing well. I saw your learning card about React Prompt Structure Question. Can you tell me what are the different components of the React Prompt Structure Question?
        
        For reference here is the relevant learning card:
        
        **Question**: the input question you must answer  
        **Thought**: you should always think about what to do  
        **Action**: the action to take, should be one of [{{tool_names}}]  
        **Action Input**: the input to the action  
        **Observation**: the result of the action  
        ... (this Thought/Action/Action Input/Observation can repeat N times)  
        **Thought**: I now know the final answer  
        **Final Answer**: the final answer to the original input question  

        """
            )
        ]

        user_message = utils.user_message(
            f"""
        Thank you. You followed my instructions quite well. Can you please do the same for the following card:
        
        {card}"""
        )

        messages = [self.system_prompt] + training_messages + [user_message]

        result = utils.call_api(messages, temperature=0)

        return result


# test
if __name__ == "__main__":
    tutor = qTutor()
    print(tutor.get_msg("test"))
