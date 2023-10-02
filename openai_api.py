import openai
openai.api_key = "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"
def text_complition(prompt: str):
    try:
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = f'Human: {prompt}\nAI: ',
            temperature = 0.9,
            max_token=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=['Human:', 'AI:']
        )
        return {
            'status':1,
            'response': response['choices'][0]['text']
            }
    except:
        return {
            'status': 0,
            'response': ''
        }