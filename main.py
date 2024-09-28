import pandas as pd

def load_data():
    credit_info = pd.read_csv('credit_card_customers_exported.csv')

    return credit_info

def find_low_income(credit_info):
    income_list = credit_info['Income_Category'].tolist()
    checked_income = "Less than $40K"
    excluded_list = []

    for income in income_list:
        if income != checked_income:
            excluded_list.append(income)

    return excluded_list

def remove_higher_income(credit_info):
    excluded_list = find_low_income(credit_info)
    filtered_credit = credit_info[~credit_info.Income_Category.isin(excluded_list)]

    return filtered_credit



def main():
    credit_info = load_data()
    filtered_credit = remove_higher_income(credit_info)
    print(filtered_credit)
    
main()