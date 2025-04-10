import os
import requests
from botbuilder.core import ActivityHandler, TurnContext
from dotenv import load_dotenv

load_dotenv()

class QnABot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        question = turn_context.activity.text

        url = f"{os.getenv('LANGUAGE_ENDPOINT')}/language/:query-knowledgebases?projectName={os.getenv('PROJECT_NAME')}&deploymentName={os.getenv('DEPLOYMENT_NAME')}&api-version=2021-10-01"
        print(url)
        headers = {
            "Ocp-Apim-Subscription-Key": os.getenv("LANGUAGE_KEY"),
            "Content-Type": "application/json"
        }
        data = {
            "question": question,
            "top": 1
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            print("Status Code:", response.status_code)
            print("Response JSON:", response.json())
        except Exception as e:
            print("Error calling QnA:", str(e))
            await turn_context.send_activity("There was an error processing your question.")
            return

        result = response.json()
        answer = result.get("answers", [{}])[0].get("answer", "Sorry, I don't know that.")
        await turn_context.send_activity(answer)