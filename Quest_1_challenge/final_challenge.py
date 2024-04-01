import pandas as pd

def calculate_expenditures_by_department(file : str):

    df = pd.read_csv(file)
    expenditures_dict = df.groupby(["Department"])['2012 Actual'].sum().to_dict()

    for k,v in expenditures_dict.items():
        formatted_value = "${:,.2f}".format(v)
        print(k, formatted_value)


if __name__ == "__main__":
    calculate_expenditures_by_department("city-of-seattle-2012-expenditures-dollars.csv")