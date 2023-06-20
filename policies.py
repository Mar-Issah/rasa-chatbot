from rasa.core.policies.unexpected_intent_policy import UnexpecTEDIntentPolicy
from rasa.engine.graph import GraphComponent
from rasa.engine.storage.resource import Resource
from rasa.engine.storage.storage import ModelStorage
from rasa.engine.recipes.default_recipe import DefaultV1Recipe

@DefaultV1Recipe.register(
    "policies.CustomFallbackPolicy",is_trainable=True
)
class CustomFallbackPolicy(UnexpecTEDIntentPolicy, GraphComponent):
    # Policy configuration goes here
    pass

