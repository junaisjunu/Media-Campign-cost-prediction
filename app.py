from src.components.prediction import Prediction
from src.config.configuration import Configuration
import pandas as pd
from src import logger

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')


@app.route('/submit',methods=['POST'])
def submit():
    form_data={
        'store_sales(in millions)': float(request.form['store_sales']),
        'unit_sales(in millions)': float(request.form['unit_sales']),
        'total_children': int(request.form['total_children']),
        'num_children_at_home': int(request.form['num_children_at_home']),
        'avg_cars_at home(approx).1': int(request.form['avg_cars_at_home']),
        'gross_weight': float(request.form['gross_weight']),
        'recyclable_package': int(request.form['recyclable_package']),
        'low_fat': int(request.form['low_fat']),
        'units_per_case': int(request.form['units_per_case']),
        'store_sqft': float(request.form['store_sqft']),
        'coffee_bar': int(request.form['coffee_bar']),
        'video_store': int(request.form['video_store']),
        'salad_bar': int(request.form['salad']),
        'prepared_food': int(request.form['food']),
        'florist': int(request.form['florist'])
    }
    data=pd.DataFrame([form_data])
    logger.info(data)
    logger.info(data.info())
    config=Configuration()
    pred_config=config.get_prediction_config()
    pred=Prediction(pred_config)
    prediction=round(pred.initiate_prediction(data=data)[0],2)
    logger.info(f"predicted value for id (0) - {prediction}")
    return render_template('pred.html',prediction=prediction)

   

if __name__ == '__main__':
    app.run(debug=True)

