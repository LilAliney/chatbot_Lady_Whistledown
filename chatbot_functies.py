import cohere

API_key = "JOixD8p8NSj4c8Y5Nd4jdo22esAsf8FDQTJ9VpBr"

co = cohere.Client(API_key)

def chatbot_response(prompt):
    '''This function takes a prompt as input, sends the prompt to the Cohere API, and returns the response.'''
    response = co.chat(message=prompt)
    return response.text
