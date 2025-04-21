from openai import OpenAI



def get_sentiment(text: list) -> list:
    """
    args
        text: A list of strings

    return
        Strings: A list of sentiments sorted into Negative, Positive, Neutral, irrelevant

    """
    

    if len(text) == 0:
        return "Wrong input. text must be an array of strings."
    for elm in text:
        if not isinstance(elm, str):  
            return "Wrong input. text must be an array of strings."

    system_prompt = f"""
        It's May 2025, you are an expert at interpreting negative, positive, irrelevant and neutral emotions across languages and cultures. 
        If you do this correctly I will give you a 30 percent tip.
         
    """
    
    
    prompt = f"""
        For each line of text in the string below, please categorize the review
        as either positive, neutral, negative, or irrelevant.
    
        Use only negative, positive, irrelevant or neutral. Do not include any numbers. Please return a list of strings in single quotes.
    {text} 
    """

    client = OpenAI()
    completion = client.chat.completions.create(
        model= 'gpt-4o-mini',    
        messages=[{'role': 'developer', 'content': system_prompt}, 
                    {'role': 'user', 'content': prompt}]
    )
    
    completion = completion.choices[0].message.content

    return completion
        
        
    

    #Save it i
