from flask import Flask, request, current_app, render_template, jsonify, redirect, url_for
from loaded_pickle_main import get_string, change_into_string

app = Flask(__name__)  #nowa instancja klasy Flask

@app.route('/', methods = ['POST', 'GET'])
def send_sentiment():
#     writen_opinion = request.args.get('opinion')  # opinia wysłana
    if request.method == 'POST':  # You need to write an if statement to check if the form was submitted or if the page is being loaded the first time.
        writen_opinion = request.form['wpisz_opinię'] # to jest name z templates html
        sent = get_string(writen_opinion)  # use function
        result = change_into_string(sent)
        # return redirect(request.url)  # redirects to the same page
        return render_template("answer.html", result=result) # return str(result)
        if "zagraj_jeszcze_raz" in request.form:
            return render_template("templates.html")
        else:
            pass

    else:
        return render_template("templates.html")

# @app.route('/', methods = ['POST', 'GET'])
# def send_sentiment():
#     if request.method == 'POST':
#     # current_app.logger.info(request.args) #To access parameters submitted in the URL (?key=value) you can use the args attribute:
#         writen_opinion = request.form['wpisz_opinie']  # opinia wysłana
#         sent = get_string(writen_opinion)  # use function
#         result = change_into_string(sent)
#         data = {'opinion':f'{writen_opinion}', 'result':f'{result}', 'result_int': int(sent)}
#         # print(data)
#         return jsonify(data) #str(result)
#     else:
#         return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)  # uruchomienie aplikacji  w trybie debugowania
