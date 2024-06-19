import os
from typing import Callable, Dict, Union
from models.gemini import GeminiModel
from models.openai import OpenaiModel

class CommandHandler:
    """
    A class to handle various commands, dispatching them to the appropriate models
    for response generation. This class manages the mapping between command keywords
    and their respective handler methods, facilitating the extension and maintenance
    of command handling capabilities.

    Attributes:
        commands (Dict[str, Callable[[str], str]]): A dictionary mapping command strings
            to their handling methods, allowing dynamic command processing.
        models (Dict[str, Union[GeminiModel, OpenaiModel]]): A dictionary mapping model
            identifiers to their initialized instances. This allows easy access and command
            dispatching to different generative models based on the provided command.

    Methods:
        handle_command(command: str, message: str) -> str:
            Dispatches the command to its handler method and returns the response.
        handle_gemini(message: str) -> str:
            Handles commands directed to the Gemini model.
        handle_openai(message: str) -> str:
            Handles commands directed to the OpenAI model.
        handle_default(message: str) -> str:
            Provides a default response for unrecognized commands.
    """

    def __init__(self):
        """
        Initializes the CommandHandler with mappings between commands and their handlers,
        as well as initializing the required models with their API keys.
        """
        self.commands: Dict[str, Callable[[str], str]] = {
            "gemini": self.handle_gemini,
            "openai": self.handle_openai
        }
        self.models: Dict[str, Union[GeminiModel, OpenaiModel]] = {
            "gemini": GeminiModel(api_key=os.getenv('GEMINI_API_KEY')),
            "openai": OpenaiModel(api_key=os.getenv('OPENAI_API_KEY'))
        }

    def handle_command(self, command: str, message: str) -> str:
        """
        Dispatches the command to its respective handler method based on the command keyword.
        If the command is unrecognized, it defaults to the `handle_default` method.

        Parameters:
            command (str): The command keyword to identify the handler.
            message (str): The full message or query associated with the command.

        Returns:
            str: The response generated by the command's handler method.
        """
        handler = self.commands.get(command, self.handle_default)
        try:
            return handler(message)
        except Exception as e:
            # Log and handle any error that occurs during command handling.
            print(f"Error handling command '{command}': {e}")
            return "An error occurred while processing your command."

    def handle_gemini(self, message: str) -> str:
        """
        Handles commands specifically directed to the Gemini model, generating a response
        based on the input message.

        Parameters:
            message (str): The message or question to be processed by the Gemini model.

        Returns:
            str: The response generated by the Gemini model.
        """
        model = self.models.get("gemini")
        if model:
            try:
                return model.generate_response(message)
            except Exception as e:
                print(f"Error generating response with Gemini model: {e}")
                return "An error occurred while generating a response."
        return "Gemini model is not available."

    def handle_openai(self, message: str) -> str:
        """
        Handles commands specifically directed to the OpenAI model, generating a response
        based on the input message.

        Parameters:
            message (str): The message or question to be processed by the OpenAI model.

        Returns:
            str: The response generated by the OpenAI model.
        """
        model = self.models.get("openai")
        if model:
            try:
                return model.generate_response(message)
            except Exception as e:
                print(f"Error generating response with OpenAI model: {e}")
                return "An error occurred while generating a response."
        return "OpenAI model is not available."

    def handle_default(self, message: str) -> str:
        """
        Provides a default response for unrecognized commands. This method acts as a fallback
        for any command not explicitly handled by the `commands` mapping.

        Parameters:
            message (str): The message associated with the unrecognized command.

        Returns:
            str: A default response indicating the command was not understood.
        """
        return "Sorry, I didn't understand that command."