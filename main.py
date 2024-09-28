import pandas as pd

def load_data():
    customer_credit_info = pd.read_csv('credit_card_customers_exported.csv')

    return customer_credit_info

def main():
    credit_info = load_data()
    print(credit_info)
main()