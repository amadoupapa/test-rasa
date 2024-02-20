# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionExtractOffre(Action):

    def name(self) -> Text:
        return "action_extract_offre_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        #dispatcher.utter_message(text="Hello World!")
        offre_entity = next(tracker.get_latest_entity_values("offre"),None)

        if(offre_entity == 'sobox'):
            dispatcher.utter_message(response='utter_faq/probleme_internet_sobox')
        elif(offre_entity == 'mobile'):
            dispatcher.utter_message(response='utter_faq/probleme_internet_mobile')
        else:
            dispatcher.utter_message(response = "utter_preciser_probleme")

        return []
