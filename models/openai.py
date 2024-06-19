import requests
from interfaces.model import ModelInterface
import os

class OpenaiModel(ModelInterface):
    """
    A concrete implementation of the ModelInterface that utilizes the OpenAI API
    to generate responses to questions.

    Attributes:
        api_key (str): The API key used for authenticating requests to the OpenAI API.
        model (str): The model identifier for OpenAI's API.
        word_limit (int): The maximum number of words expected in the response.

    Methods:
        generate_response(question: str) -> str:
            Generates a response to a given question using the specified OpenAI model.
    """

    def __init__(self, api_key: str):
        """
        Initializes the OpenaiModel with the necessary API key and model details.

        Parameters:
            api_key (str): The API key for accessing the OpenAI service.
        """
        
        self.api_key = api_key

        # Get the model, else use default - gpt-3.5-turbo-instruct.
        self.model = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo-instruct')

        # Max tokens that OpenAI should use.
        self.word_limit = 100

    def generate_response(self, question: str) -> str:
        """
        Generates a response to the given question using the OpenAI API.

        Parameters:
            question (str): The question to generate a response for.

        Returns:
            str: The generated response to the question or None if an error occurs.

        Raises:
            Exception: Describes the exception if the API request fails.
        """
        
        try:
            response = requests.post(
                f'https://api.openai.com/v1/engines/{self.model}/completions',
                json={
                    'prompt': question,
                    'max_tokens': self.word_limit * 5
                },
                headers={
                    'Authorization': f'Bearer {self.api_key}'
                }
            )

            # Raises an HTTPError for bad responses.
            response.raise_for_status()

            return response.json()['choices'][0]['text'].strip()

        except requests.exceptions.HTTPError as http_err:
            
            # Handle HTTP errors separately from other exceptions
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            
            # Handle other errors like connection problems, request timeouts, etc.
            print(f"An error occurred: {err}")
        return None
