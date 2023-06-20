# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted

class ActionDefaultFallback(Action):

    def name(self) -> Text:
       return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("Custom Fallback action is being executed.")

        dispatcher.utter_message(text="I'm not sure how to help with this. Can you please rephrase your question or provide more information?\n---\nYou can also contact our Support agent or send an email to support@alty.com for assistance.")

        return [UserUtteranceReverted()]
