import pandas as pd
import numpy as np

WINDOW_SIZE_inc_target = 31
    
def pandas_vector_to_list(pandas_df):
    py_list = [item[0] for item in pandas_df.values.tolist()]
    return py_list


def azureml_main(dataframe):
    
    stock_index = dataframe[['Stock_Index']]
    data_as_list = pandas_vector_to_list(stock_index)    
    data_size = len(data_as_list)
    data_matrix = np.zeros((data_size-WINDOW_SIZE_inc_target-28, WINDOW_SIZE_inc_target))
    
    # Index data modeling begings
    matrix_pos = 0
    for i in range(0, data_size - WINDOW_SIZE_inc_target-28):
        col_pos = 0
        for j in range(0, WINDOW_SIZE_inc_target):
                if j == WINDOW_SIZE_inc_target-1: # The target,
                    list_to_average = []
                    for target in range ((i+j),(i+j+30)):
                        list_to_average.append(data_as_list[target])
                        target_mean = sum(list_to_average)/len(list_to_average)
                        first_day = data_matrix[matrix_pos][0] 
                        data_matrix[matrix_pos][col_pos] = ( target_mean - first_day ) / first_day
                else:
                    data_matrix[matrix_pos][col_pos] = data_as_list[i+j]
                col_pos = col_pos + 1
        matrix_pos = matrix_pos + 1
    # Index data modeling ends
    
    # Currency data modeling begins
    # USD-RUB Currency
    usd_rub = dataframe[['USD_RUB']]
    rub_as_list = pandas_vector_to_list(usd_rub)
    rub_vector = np.zeros((data_size-WINDOW_SIZE_inc_target-28,1))

    for i in range(0, data_size - WINDOW_SIZE_inc_target-28):
        currency_data = []
        for day in range (0,(30)):
            currency_data.append(rub_as_list[i+day])
        target_mean = sum(currency_data) / len(currency_data)
        rub_vector[i] = (target_mean)
        
    # USD-TRY Currency
    usd_try = dataframe[['USD_TRY']]
    try_as_list = pandas_vector_to_list(usd_rub)
    try_vector = np.zeros((data_size-WINDOW_SIZE_inc_target-28,1))

    for i in range(0, data_size - WINDOW_SIZE_inc_target-28):
        currency_data = []
        for day in range (0,(30)):
            currency_data.append(try_as_list[i+day])
        target_mean = sum(currency_data) / len(currency_data)
        try_vector[i] = (target_mean)
    # Currency data modeling ends
    
    # Oil data modeling begins
    oil = dataframe[['Oil']]
    oil_as_list = pandas_vector_to_list(oil)
    oil_vector = np.zeros((data_size-WINDOW_SIZE_inc_target-28,1))

    for i in range(0, data_size - WINDOW_SIZE_inc_target-28):
        oil_data = []
        for day in range (0,(30)):
            oil_data.append(oil_as_list[i+day])
        target_mean = sum(oil_data) / len(oil_data)
        oil_vector[i] = (target_mean)
    # Oil data modeling ends
    
    # Gold data modeling begins
    gold = dataframe[['Gold']]
    gold_as_list = pandas_vector_to_list(gold)
    gold_vector = np.zeros((data_size-WINDOW_SIZE_inc_target-28,1))

    for i in range(0, data_size - WINDOW_SIZE_inc_target-28):
        gold_data = []
        for day in range (0,(30)):
            gold_data.append(gold_as_list[i+day])
        target_mean = sum(gold_data) / len(gold_data)
        gold_vector[i] = (target_mean)
    # Gold data modeling ends
    
    # Refugee data modeling begins
    refugee = dataframe[['TotalRefugee']]
    # Refugee data modeling ends
    
    # Refugee-German data modeling begins
    # german_refugee = dataframe[['GermanRefugee']]
    # Refugee data modeling ends
    
    #Doomsday data modeling begins
    doomsday = dataframe[['dday']]
    #Doomsday data modeling ends
    
    pandas_frame = pd.DataFrame(data_matrix)
    pandas_frame.loc[:,'Rub'] = pd.DataFrame(rub_vector)
    pandas_frame.loc[:,'Try'] = pd.DataFrame(try_vector)
    pandas_frame.loc[:,'Oil'] = pd.DataFrame(oil_vector)
    pandas_frame.loc[:,'Gold'] = pd.DataFrame(gold_vector)
    pandas_frame.loc[:,'Refugee'] = pd.DataFrame(refugee)
    ## pandas_frame.loc[:,'GermanRefugee'] = pd.DataFrame(german_refugee)
    pandas_frame.loc[:,'Doomsday'] = pd.DataFrame(doomsday)

    
    return pandas_frame,

