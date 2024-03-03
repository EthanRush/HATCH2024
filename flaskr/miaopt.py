import pandas as pd

daily_values_df = pd.read_csv("dailyvalue.csv")
food_options_df = pd.read_csv("foods.csv")

import pandas as pd
def create_menu_with_supplements_and_values(daily_values_df, food_options_df):
    # Ensure all nutrient values in food_options_df are numeric
    for col in food_options_df.columns[2:]:  # Assuming the first two columns are 'foodname' and 'serving_size'
        food_options_df[col] = pd.to_numeric(food_options_df[col], errors='coerce').fillna(0)
    
    servings_dict = {food: 0 for food in food_options_df['foodname']}
    total_nutrients = {nutrient.lower(): 0.0 for nutrient in daily_values_df['nutrient']}
    daily_value_calories = daily_values_df[daily_values_df['nutrient'].str.lower() == 'calories']['value'].values[0]
    
    for _, food_item in food_options_df.iterrows():
        if 'calories' in total_nutrients and (total_nutrients['calories'] >= daily_value_calories * 0.9 and total_nutrients['calories'] <= daily_value_calories * 1.1):
            break

        if servings_dict[food_item['foodname']] < 1:
            temp_nutrients = total_nutrients.copy()
            exceeds_daily_values = False
            for nutrient in temp_nutrients.keys():
                nutrient_col = nutrient
                if nutrient_col in food_item:
                    added_value = food_item[nutrient_col]
                    if nutrient == 'calories' and (temp_nutrients[nutrient] + added_value > daily_value_calories * 1.1):
                        exceeds_daily_values = True
                        break
                    temp_nutrients[nutrient] += added_value
            
            if not exceeds_daily_values:
                servings_dict[food_item['foodname']] += 1
                total_nutrients = temp_nutrients.copy()
    
    supplements_needed = {}
    for nutrient, value in total_nutrients.items():
        daily_value = daily_values_df[daily_values_df['nutrient'].str.lower() == nutrient]['value'].values[0]
        if value < daily_value * 0.9:
            shortfall = daily_value - value
            supplements_needed[nutrient] = shortfall
    
    menu_with_servings = {food: servings for food, servings in servings_dict.items() if servings > 0}

    return menu_with_servings, total_nutrients, supplements_needed

# Assuming the CSV files have been read into daily_values_df and food_options_df DataFrames
menu_with_servings, total_nutrients, supplements_needed = create_menu_with_supplements_and_values(daily_values_df, food_options_df)
print("Menu with servings:")
print(menu_with_servings)
print("\nTotal nutrients provided by the menu:")
for nutrient, total in total_nutrients.items():
    print(f"{nutrient}: {total} mg")
print("\nSupplements needed for the following nutrients (mg needed to reach daily value):")
for nutrient, value in supplements_needed.items():
    print(f"{nutrient}: {value} mg")

