# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sagas.crmsfa.odoo_facade import odoo, login

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World, this is action response.")

        return []


# login()
login(db="demo", username="admin", password="admin")

def product_list():
    lang = 'en_US'
    # lang='zh_CN'

    Product = odoo.env['product.product']
    odoo.env.context['lang'] = lang
    product_ids = Product.search([])
    return [{'id':p[0], 'name':p[1]} for p in Product.name_get(product_ids)]

class ActionListProducts(Action):
    def name(self):
        return "action_list_products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # logging.info(json.dumps(tracker.current_slot_values(), indent=2, ensure_ascii=False))
        # prop = lambda attr: tracker.get_slot(attr) if attr in tracker.slots else ''
        dispatcher.utter_message(json_message={'result': 'success',
                                               'product_list': product_list()})
        return []
