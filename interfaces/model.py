class ModelInterface:
    """
    Interface that serves as a template for generative models like Gemini & OpenAI.

    This class defines the interface for generative models, ensuring that all
    concrete model implementations adhere to a standard structure for generating
    responses. Subclasses must implement the `generate_response` method.

    Methods:
        generate_response(question: str) -> str:
            Generates a response based on the input question.
    """

    def generate_response(self, question: str) -> str:
        """
        Generates a response to the given question. This method should be implemented
        by subclasses to return a meaningful response based on the model's capabilities.

        Parameters:
            question (str): The question to generate a response for.

        Returns:
            str: The generated response to the question.

        Raises:
            NotImplementedError: If the method hasn't been implemented by a subclass.
        """
        
        raise NotImplementedError("Subclasses must implement this method.")
