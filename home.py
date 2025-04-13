#home
class Home:
    def __init__(self, **ambientes):
        for nome, ambiente in ambientes.items():
            setattr(self, nome, ambiente)