from doro_reader import Doro_reader

class Doro_diretor:
    def __init__(self):
        pass

if __name__ == "__main__":
    print("한국도로공사데이터")
    d = Doro_reader()
    d.get_data()
