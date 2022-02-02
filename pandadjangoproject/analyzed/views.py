from re import M
import pandas as pd
from django.shortcuts import render

# Create your views here.
def home(request):
    data = pd.read_csv(r"C://Users//rober//pandadjango//pandadjangoproject//csvData.csv", on_bad_lines='skip', nrows=10)
    all_data = pd.read_csv(r"C://Users//rober//pandadjango//pandadjangoproject//csvData.csv")
    all_data.drop('rank', inplace=True, axis=1)
    all_data.index = all_data.index + 1
    smallest_five = pd.read_csv(r"C://Users//rober//pandadjango//pandadjangoproject//csvData.csv", on_bad_lines='skip').tail(5)
    data.drop('rank', inplace=True, axis=1)
    data.index = data.index + 1

    only_city = data[['Name', 'Population']]
    smallest_five = smallest_five[['Name', 'Population']]

    context = {
        "all_data": all_data.to_html(),
        "only_city": only_city.to_html(),
        "smallest_five": smallest_five.to_html()
        #'population': population.to_html(index=False) #How to remove a index
    }
    return render(request, 'analyzed/home.html', context)