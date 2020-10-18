from flask import Flask, request, current_app, render_template
app = Flask(__name__)  #nowa instancja klasy Flask
from loaded_pickle_main import get_string, change_into_string


# @app.route('/')  # endpointy we Flasku
# def hello_world():
#     # return 'Hello, World!'
#     return render_template("base.html")

#
# @app.route('/', methods = ['POST', 'GET'])
# def send_sentiment():
#     current_app.logger.info(request.args) #To access parameters submitted in the URL (?key=value) you can use the args attribute:
#     writen_opinion = request.args.get('opinion')  # opinia wysłana
#     sent = get_string(writen_opinion)  # use function
#     result = change_into_string(sent)
#     # # return str(result)
#     return render_template("base.html")

@app.route('/', methods = ['POST', 'GET'])
def send_sentiment():
    if request.method == 'POST':
    # current_app.logger.info(request.args) #To access parameters submitted in the URL (?key=value) you can use the args attribute:
        writen_opinion = request.form['wpisz_opinie']  # opinia wysłana
        sent = get_string(writen_opinion)  # use function
        result = change_into_string(sent)
        return str(result)
    else:
        return render_template("base.html")


if __name__ == "__main__":
    app.run(debug=True)  # uruchomienie aplikacji  w trybie debugowania
