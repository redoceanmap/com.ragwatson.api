from fastapi import FastAPI
from apps.titanic.app.walter import Walter
from apps.titanic.app.rose import Rose

app = FastAPI(title="Titanic (James)")

class James:
    def __init__(self):
        pass

    def check_model(self):
        r = Rose()
        return r.model_exists()

    def get_tree(self):
        r = Rose()
        return r.model_exists()

    def get_data(self):
        w = Walter()
        return w.get_data()

    def get_count(self):
        w = Walter()
        return w.get_count()

    def get_survived(self):
        w = Walter()
        return w.get_survived()

    def get_dead(self):
        w = Walter()
        return w.get_dead()   