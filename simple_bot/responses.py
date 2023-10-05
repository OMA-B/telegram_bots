from datetime import datetime


def sample_response(input_text: str) -> str:
    '''takes user message and find suitable response'''

    user_message: str = input_text.lower()

    if 'hello' in user_message or 'hi' in user_message or 'sup' in user_message:
        now = datetime.now().strftime('%I:%M:%S %p')
        if 'PM' in now:
            return "Good PM!\nHow has your day been?"
        return "Hey!\nG'morning...\nHow's it going?"
    
    if 'who are you' in user_message:
        return "I'm just a simple bot."
    
    if 'time' in user_message:
        now = datetime.now().strftime('%I:%M:%S %p')
        return f"The time is: {now}."
    
    if 'date' in user_message:
        now = datetime.now().strftime('%d of %B, %Y')
        return f"Today's date is: {now}."
    
    return "Hey, gat no idea what you just said... speak my language!"