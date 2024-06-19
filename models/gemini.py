import google.generativeai as genai
from interfaces.model import ModelInterface
import os

class GeminiModel(ModelInterface):
    """
    A concrete implementation of the ModelInterface that uses Google's generative AI,
    specifically the Gemini model, to generate responses to questions.

    This class encapsulates the functionality to interact with the Gemini API, providing
    a method to generate responses to given questions using the specified model.

    Attributes:
        api_key (str): The API key used to authenticate requests to the Gemini API.

    Methods:
        generate_response(question: str) -> str:
            Generates a response to a given question using the Gemini generative model.
    """

    def __init__(self, api_key: str):
        """
        Initializes the GeminiModel with the necessary API key for authentication.
        Get the model that should be used for Generating response.
        Set the word limit of teh response - 100

        Parameters:
            api_key (str): The API key for accessing the Gemini generative AI service.
        """
        
        self.api_key = api_key
        self.model = os.getenv('GEMINI_MODEL')
        self.word_limit = 100
        
        try:
            genai.configure(api_key=self.api_key)
        except Exception as e:
            
            # Handle exceptions related to API configuration errors.
            print(f"Failed to configure Gemini API with provided API key: {e}")
            
            # Optionally, re-raise the exception if the application cannot recover.
            raise

    def generate_response(self, question: str) -> str:
        """
        Generates a response to the given question using the Gemini model.

        This method calls the Gemini generative AI service to generate a response
        to the input question, handling any potential errors during the process.

        Parameters:
            question (str): The question to generate a response for.

        Returns:
            str: The generated response to the question.

        Raises:
            Exception: If there is an error in generating the response from the Gemini model.
        """

        try:
            # Prepare the model instance.
            model = genai.GenerativeModel(self.model)

            # Get the content and return it.
            response = model.generate_content(f'Answer this question in {self.word_limit} words: ' + question)
            return response.text

        except Exception as e:
            
            # Handle exceptions related to the model generation process.
            print(f"Error generating response from Gemini model: {e}")
            
            # Optionally, re-raise the exception if the application cannot recover.
            raise
