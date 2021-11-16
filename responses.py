from datetime import datetime
def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('naber','selam','hi','slm','nbr'):
        return "Hi!"

    if user_message in ('sen kimsin','?','kimsin'):
        return "Ben Saygunhan'ın kölesiyim"
