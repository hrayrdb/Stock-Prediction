import numpy as np
import pandas as pd
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error


#fuzzy variables
profit_margin_fuzz = ctrl.Antecedent(np.arange(-200, 201, 1), 'Profit Margin')
debt_ratio_fuzz = ctrl.Antecedent(np.arange(0, 101, 1), 'Debt Ratio')
roa_fuzz = ctrl.Antecedent(np.arange(-100, 101, 1), 'ROA')
price_var_fuzz = ctrl.Consequent(np.arange(-100, 201, 1), 'PRICE VAR [%]')

##TRIANGLUAR
# profit_margin_fuzz['very low'] = fuzz.trimf(profit_margin_fuzz.universe, [-200, -200, 0])
# profit_margin_fuzz['low'] = fuzz.trimf(profit_margin_fuzz.universe, [-50, 0, 50])
# profit_margin_fuzz['medium'] = fuzz.trimf(profit_margin_fuzz.universe, [0, 50, 100])
# profit_margin_fuzz['high'] = fuzz.trimf(profit_margin_fuzz.universe, [50, 100, 150])
# profit_margin_fuzz['very high'] = fuzz.trimf(profit_margin_fuzz.universe, [100, 200, 200])


# debt_ratio_fuzz['very low'] = fuzz.trimf(debt_ratio_fuzz.universe, [0, 0, 20])
# debt_ratio_fuzz['low'] = fuzz.trimf(debt_ratio_fuzz.universe, [10, 30, 50])
# debt_ratio_fuzz['medium'] = fuzz.trimf(debt_ratio_fuzz.universe, [30, 50, 70])
# debt_ratio_fuzz['high'] = fuzz.trimf(debt_ratio_fuzz.universe, [50, 70, 90])
# debt_ratio_fuzz['very high'] = fuzz.trimf(debt_ratio_fuzz.universe, [70, 100, 100])


# roa_fuzz['very low'] = fuzz.trimf(roa_fuzz.universe, [-100, -100, -25])
# roa_fuzz['low'] = fuzz.trimf(roa_fuzz.universe, [-50, -25, 0])
# roa_fuzz['medium'] = fuzz.trimf(roa_fuzz.universe, [-25, 0, 25])
# roa_fuzz['high'] = fuzz.trimf(roa_fuzz.universe, [0, 25, 50])
# roa_fuzz['very high'] = fuzz.trimf(roa_fuzz.universe, [25, 50, 100])


# price_var_fuzz['big decrease'] = fuzz.trimf(price_var_fuzz.universe, [-200, -140, -80])
# price_var_fuzz['decrease'] = fuzz.trimf(price_var_fuzz.universe, [-100, -50, 0])
# price_var_fuzz['stable'] = fuzz.trimf(price_var_fuzz.universe, [-20, 0, 20])
# price_var_fuzz['increase'] = fuzz.trimf(price_var_fuzz.universe, [0, 50, 100])
# price_var_fuzz['big increase'] = fuzz.trimf(price_var_fuzz.universe, [80, 140, 200])

##TRAPEZOIDAL
profit_margin_fuzz['very low'] = fuzz.trapmf(profit_margin_fuzz.universe, [-200, -200, -150, -50])
profit_margin_fuzz['low'] = fuzz.trapmf(profit_margin_fuzz.universe, [-100, -50, 0, 50])
profit_margin_fuzz['medium'] = fuzz.trapmf(profit_margin_fuzz.universe, [0, 25, 75, 100])
profit_margin_fuzz['high'] = fuzz.trapmf(profit_margin_fuzz.universe, [50, 100, 150, 200])
profit_margin_fuzz['very high'] = fuzz.trapmf(profit_margin_fuzz.universe, [150, 200, 200, 200])

debt_ratio_fuzz['very low'] = fuzz.trapmf(debt_ratio_fuzz.universe, [0, 0, 10, 20])
debt_ratio_fuzz['low'] = fuzz.trapmf(debt_ratio_fuzz.universe, [10, 20, 40, 50])
debt_ratio_fuzz['medium'] = fuzz.trapmf(debt_ratio_fuzz.universe, [30, 40, 60, 70])
debt_ratio_fuzz['high'] = fuzz.trapmf(debt_ratio_fuzz.universe, [50, 60, 80, 90])
debt_ratio_fuzz['very high'] = fuzz.trapmf(debt_ratio_fuzz.universe, [80, 90, 100, 100])

roa_fuzz['very low'] = fuzz.trapmf(roa_fuzz.universe, [-100, -100, -75, -25])
roa_fuzz['low'] = fuzz.trapmf(roa_fuzz.universe, [-50, -25, 0, 25])
roa_fuzz['medium'] = fuzz.trapmf(roa_fuzz.universe, [0, 10, 30, 40])
roa_fuzz['high'] = fuzz.trapmf(roa_fuzz.universe, [20, 30, 50, 60])
roa_fuzz['very high'] = fuzz.trapmf(roa_fuzz.universe, [50, 60, 100, 100])

price_var_fuzz['big decrease'] = fuzz.trapmf(price_var_fuzz.universe, [-100, -100, -75, -75])
price_var_fuzz['decrease'] = fuzz.trapmf(price_var_fuzz.universe, [-75, -60, -40, -10])
price_var_fuzz['stable'] = fuzz.trapmf(price_var_fuzz.universe, [-10, -10, 10, 10])
price_var_fuzz['increase'] = fuzz.trapmf(price_var_fuzz.universe, [10, 40, 60, 80])
price_var_fuzz['big increase'] = fuzz.trapmf(price_var_fuzz.universe, [80, 120, 200, 200])

# Plotting membership functions for each variable
profit_margin_fuzz.view()
plt.title('Profit Margin Membership Functions')
plt.show()

debt_ratio_fuzz.view()
plt.title('Debt Ratio Membership Functions')
plt.show()

roa_fuzz.view()
plt.title('ROA Membership Functions')
plt.show()

price_var_fuzz.view()
plt.title('PRICE VAR [%] Membership Functions')
plt.show()

rules = [

    # Profit Margin: Very Low
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very low'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very low'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very low'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very low'] & roa_fuzz['high'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very low'] & roa_fuzz['very high'], price_var_fuzz['decrease']),
    
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['low'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['low'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['low'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['low'] & roa_fuzz['high'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['low'] & roa_fuzz['very high'], price_var_fuzz['decrease']),
    
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['medium'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['medium'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['medium'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['medium'] & roa_fuzz['high'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['medium'] & roa_fuzz['very high'], price_var_fuzz['decrease']),
    
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['high'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['high'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['high'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['high'] & roa_fuzz['high'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['high'] & roa_fuzz['very high'], price_var_fuzz['decrease']),
    
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very high'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very high'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very high'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very high'] & roa_fuzz['high'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['very low'] & debt_ratio_fuzz['very high'] & roa_fuzz['very high'], price_var_fuzz['big decrease']),
    
    # Profit Margin: Low
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very low'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very low'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very low'] & roa_fuzz['medium'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very low'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very low'] & roa_fuzz['very high'], price_var_fuzz['stable']),
    
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['low'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['low'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['low'] & roa_fuzz['medium'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['low'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['low'] & roa_fuzz['very high'], price_var_fuzz['stable']),
    
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['medium'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['medium'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['medium'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['medium'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['medium'] & roa_fuzz['very high'], price_var_fuzz['stable']),
    
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['high'] & roa_fuzz['medium'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['high'] & roa_fuzz['high'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['high'] & roa_fuzz['very high'], price_var_fuzz['stable']),
    
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very high'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very high'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very high'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very high'] & roa_fuzz['high'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['low'] & debt_ratio_fuzz['very high'] & roa_fuzz['very high'], price_var_fuzz['stable']),
    
    # Profit Margin: Medium
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very low'] & roa_fuzz['very low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very low'] & roa_fuzz['low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very low'] & roa_fuzz['medium'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very low'] & roa_fuzz['high'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very low'] & roa_fuzz['very high'], price_var_fuzz['increase']),

    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['low'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['low'] & roa_fuzz['low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['low'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['low'] & roa_fuzz['high'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['low'] & roa_fuzz['very high'], price_var_fuzz['increase']),

    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['medium'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['medium'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['medium'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['medium'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['medium'] & roa_fuzz['very high'], price_var_fuzz['stable']),

    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['high'] & roa_fuzz['medium'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['high'] & roa_fuzz['high'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['high'] & roa_fuzz['very high'], price_var_fuzz['decrease']),

    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very high'] & roa_fuzz['very low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very high'] & roa_fuzz['low'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very high'] & roa_fuzz['medium'], price_var_fuzz['big decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very high'] & roa_fuzz['high'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['medium'] & debt_ratio_fuzz['very high'] & roa_fuzz['very high'], price_var_fuzz['decrease']),

    # Profit Margin: High
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very low'] & roa_fuzz['very low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very low'] & roa_fuzz['low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very low'] & roa_fuzz['medium'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very low'] & roa_fuzz['high'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very low'] & roa_fuzz['very high'], price_var_fuzz['big increase']),

    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['low'] & roa_fuzz['very low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['low'] & roa_fuzz['low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['low'] & roa_fuzz['medium'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['low'] & roa_fuzz['high'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['low'] & roa_fuzz['very high'], price_var_fuzz['big increase']),

    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['medium'] & roa_fuzz['very low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['medium'] & roa_fuzz['low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['medium'] & roa_fuzz['medium'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['medium'] & roa_fuzz['high'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['medium'] & roa_fuzz['very high'], price_var_fuzz['increase']),

    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['high'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['high'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['high'] & roa_fuzz['very high'], price_var_fuzz['stable']),

    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very high'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very high'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['high'] & debt_ratio_fuzz['very high'] & roa_fuzz['very high'], price_var_fuzz['stable']),

    # Profit Margin: Very High
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very low'] & roa_fuzz['very low'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very low'] & roa_fuzz['low'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very low'] & roa_fuzz['medium'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very low'] & roa_fuzz['high'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very low'] & roa_fuzz['very high'], price_var_fuzz['big increase']),

    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['low'] & roa_fuzz['very low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['low'] & roa_fuzz['low'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['low'] & roa_fuzz['medium'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['low'] & roa_fuzz['high'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['low'] & roa_fuzz['very high'], price_var_fuzz['big increase']),

    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['medium'] & roa_fuzz['very low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['medium'] & roa_fuzz['low'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['medium'] & roa_fuzz['medium'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['medium'] & roa_fuzz['high'], price_var_fuzz['big increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['medium'] & roa_fuzz['very high'], price_var_fuzz['big increase']),

    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['high'] & roa_fuzz['medium'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['high'] & roa_fuzz['high'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['high'] & roa_fuzz['very high'], price_var_fuzz['increase']),

    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very high'] & roa_fuzz['very low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very high'] & roa_fuzz['low'], price_var_fuzz['decrease']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very high'] & roa_fuzz['medium'], price_var_fuzz['stable']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very high'] & roa_fuzz['high'], price_var_fuzz['increase']),
    ctrl.Rule(profit_margin_fuzz['very high'] & debt_ratio_fuzz['very high'] & roa_fuzz['very high'], price_var_fuzz['increase']),

]

stock_ctrl = ctrl.ControlSystem(rules)
stock_simulation = ctrl.ControlSystemSimulation(stock_ctrl)

data = pd.read_csv('sorted_final.csv')

predictions = []
          

for index, row in data.iterrows():

    stock_simulation.input['Profit Margin'] = row['Profit Margin']
    stock_simulation.input['Debt Ratio'] = row['Debt Ratio']
    stock_simulation.input['ROA'] = row['ROA']
    

    stock_simulation.compute()
    

    predicted_price_var = stock_simulation.output['PRICE VAR [%]']
    predictions.append(predicted_price_var)


data['Predicted PRICE VAR [%]'] = predictions


mae = mean_absolute_error(data['2019 PRICE VAR [%]'], data['Predicted PRICE VAR [%]'])
print(f"Mean Absolute Error: {mae:.2f}")


mse = mean_squared_error(data['2019 PRICE VAR [%]'], data['Predicted PRICE VAR [%]'])
print(f"Mean Squared Error: {mse:.2f}")


plt.figure(figsize=(10, 5))
plt.plot(data['2019 PRICE VAR [%]'], label='Actual')
plt.plot(data['Predicted PRICE VAR [%]'], label='Predicted')
plt.legend()
plt.show()
