from flask import Flask, request, current_app
app = Flask(__name__)  #nowa instancja klasy Flask
from loaded_pickle import get_string, change_into_string


# @app.route('/')  # endpointy we Flasku
# def hello_world():
#     return 'Hello, World!'


@app.route('/', methods = ['POST', 'GET'])
def send_sentiment():
    current_app.logger.info(request.args)
    op = request.args.get('opinion')  # opinia wysłana
    sent = get_string(op)
    result=change_into_string(sent)
    return str(result)

if __name__ == "__main__":
    app.run(debug=True)  # uruchomienie aplikacji