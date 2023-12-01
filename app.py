from flask import Flask, render_template, request
import pickle
import numpy as np

# setup application
app = Flask(__name__)

def prediction(lst):
    filename = 'model/rankspredictor.pickle'
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    pred_value = model.predict([lst])
    return pred_value

@app.route('/', methods=['POST', 'GET'])
def index():
    # return "Hello World"
    pred_value = 0
    if request.method == 'POST':
        cseGP= request.form['csresult']
        mathsGP = request.form['mathsresult']
        mechanicsGP = request.form['mechanicsresult']
        
        feature_list = []

        feature_list.append(float(cseGP))
        feature_list.append(float(mathsGP))
        feature_list.append(float(mechanicsGP))

        # cse_list = ['4','4','3.7','3.3','3','2.7','2.3','2','1.7','1.3','1','0']
        # maths_list = ['4','4','3.7','3.3','3','2.7','2.3','2','1.7','1.3','1','0']
        # mechanics_list = ['4','4','3.7','3.3','3','2.7','2.3','2','1.7','1.3','1','0']

        # for item in company_list:
        #     if item == company:
        #         feature_list.append(1)
        #     else:
        #         feature_list.append(0)

        # def traverse_list(lst, value):
        #     for item in lst:
        #         if item == value:
        #             feature_list.append(1)
        #         else:
        #             feature_list.append(0)
        
        # traverse_list(company_list, company)
        # traverse_list(typename_list, typename)
        # traverse_list(opsys_list, opsys)

        pred_value = prediction(feature_list)
        pred_value = int(np.round(pred_value[0]))

    return render_template('index.html', pred_value=pred_value)


# if __name__ == '__main__':
#     app.run(debug=True)
