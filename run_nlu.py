from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter


def run_nlu():
	interpreter = Interpreter.load('./models/nlu/default/shopnlu')
	print(interpreter.parse("hey"))


run_nlu()