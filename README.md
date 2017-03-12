# UCL-DSSC-Hackaton Microsoft Azure Machine Learning Challenge

## Team: Hype Train
## Members:
Alex Young

Lukas Weiss

Utku Ozbulak

## Motivation:
We wanted to come up with a forward indicatior that Bloomberg doesn not offer right now but might help their business and product range.

We created an index out of defense firms that specialized in the sale of armanents and munitions and did not have exposure to other markets.

![Stock_Index](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/PowerBI_Image_Exports/1-defense-stocks-index.png "Stock_Index")


We analyzed different window sizes to predict the momentum of the index and finally decided to use window size of 30. In order to capture global political instability, we used global refugees per month, oil and gold prices as well as currencies that might be majorly affected from current turmoil.  


![refugees](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/PowerBI_Image_Exports/4-refugees.png "refugees")


![oil-gold](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/PowerBI_Image_Exports/5-oil-gold.png "oil-gold")


![currency](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/PowerBI_Image_Exports/6-currency.png "currency")

We found out that from these external features, only gold prices and total refugee count helped us with the prediction the index increase/decrease percentage.

We modeled our data as 30 days window size of index (average of sum of all defense industry stocks) then for each input vector we added gold price as an average of past 30 days and global refugee count of that month.

Out many algorithms that are available in Azure Machine Learning Studio, our Linear Regression with 0.005 regularisation rating gave the best result with 3% absolute error.

Unfortunately, many models we tried on Neural Nets did not converge to the solution which might be an indicator that we need more data.

Below, is the test result of 3 months, overall, we were able to capture trends but we overshoot the trends from time to time. The change(Y Axis) is the predicted percentage increase or decrease on defense industry(stocks) and the X xis is time represented in days.

![currency](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/PowerBI_Image_Exports/7-defence-index-trend-prediction.png "currency")

The model we used in Azure Studio is like below:

![model](https://raw.githubusercontent.com/utkuozbulak/UCL-DSSC-Hackaton/master/Azure_ML/Model.png "model")


-----------------------------


Azure-ML folder contains the images of model and the datasets.

Final_Datasets folder contains all the data we ended up using in our latest model with Train-Test-Full.csv having the final test data with window sizes and all additional features.

PowerBI_Image_Exports Contains all the images from PowerBI that we used to express the results and our reasoning.

Python_src contains the python code that we used in AzureML Studio and ipynb.



