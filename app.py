from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from handlers.commands import CommandHandler

# Prepare the instance of the Flask Application.
app = Flask(__name__)
command_handler = CommandHandler()

@app.route('/bot', methods=['POST'])
def bot():
    
    """
    Handles incoming messages via a POST request to the '/bot' route.
    Extracts the first word of the incoming message to use as a command keyword
    and dispatches the command to the CommandHandler for processing.
    
    Parameters:
        None, but expects a POST request containing a 'Body' field with the incoming message.

    Returns:
        A TwiML response with the command processing result to be sent back to the sender.
    """
    
    try:

        # Get the whole message that is send by the user.
        incoming_msg = request.values.get('Body', '')

        # Extract the first word.
        first_word = str(incoming_msg.split()[0]).lower()

        # Message of the user.
        message = ' '.join(incoming_msg.split()[1:])

        # Get the response.
        response = command_handler.handle_command(first_word, message)

        # Prepare & return the response back to WhatsApp.
        resp = MessagingResponse()
        msg = resp.message()
        msg.body(response)
        return str(resp)

    # Handle any errors.
    except Exception as e:
        print(f"An error occurred while processing the request: {e}")
        return str(MessagingResponse().message("Sorry, an error occurred while processing your request."))

if __name__ == '__main__':
    app.run(debug=True)
