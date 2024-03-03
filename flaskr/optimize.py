from scipy.optimize import linprog
import csv
import json
from random import randint

def convert_nutrition_metric(metric_name, value, current_unit):
    # Dictionary mapping metric names to the units in the table
    nutrition_metrics_units = {
            "portion": "g",
            "Calories": "calories",
            "biotin": "µg",
            "calcium": "mg",
            "chloride": "mg",
            "choline": "mg",
            "cholesterol": "mg",
            "chromium": "mg",
            "copper": "mg",
            "dietary fiber": "g",
            "Total lipid (fat)": "g",
            "folate": "µg",
            "iodine": "µg",
            "iron": "mg",
            "magnesium": "mg",
            "manganese": "mg",
            "molybdenum": "µg",
            "niacin": "mg",
            "pantothenic acid": "mg",
            "phosphorus": "mg",
            "potassium": "mg",
            "protein": "g",
            "riboflavin": "mg",
            "saturated fat": "g",
            "selenium": "µg",
            "sodium": "mg",
            "thiamin": "mg",
            "total carbohydrates": "g",
            "Vitamin A": "µg",
            "Vitamin B6": "mg",
            "Vitamin B12": "µg",
            "Vitamin C": "mg",
            "Vitamin D": "µg",
            "Vitamin E": "mg",
            "Vitamin K": "µg",
            "Zinc": "mg"
        }
    # Conversion factors between units
    conversion_factors = {
        
        
        ("mcg", "µg"): 1,
        ("µg", "mcg"): 1,

        ("µg", "mg"): 0.001,
         ("mg", "µg"): 1000,

        ("mcg", "mg"): 0.001,
        ("mg", "mcg"): 1000,

        ("g", "mg"): 1000,
        ("mg", "g"): 0.001,

        ("C", "calories"): 1
    }
    # Check if conversion is necessary
    desired_unit = nutrition_metrics_units.get(metric_name)
    if not desired_unit:
        return f"No unit conversion needed or metric unknown for {metric_name}."
    if current_unit == desired_unit:
        return f"{value} {current_unit}"
    # Perform conversion if applicable
    conversion_key = (current_unit, desired_unit)
    conversion_factor = conversion_factors.get(conversion_key)
    if conversion_factor:
        converted_value = float(value) * float(conversion_factor)
        return f"{converted_value} {desired_unit}"
    else:
        return f"{current_unit} {desired_unit} Conversion not supported."


#### INPUTS: replace these hard-coded values with the actual data

# units:
# any units can be used as long as you are consistent.
# all portion sizes must have the same units.
# for a nutrient, anywhere it appears should have the same unit.
# so all protein measurements should be in the same units.
# whatever units you use in this input are the units of the output.
# For example,
# food_portions['chicken'] = 100g
# food_nutrients['chicken']['fat'] = 10 g fat / 100g of chicken
# for all food nutrients, you need to measure fat in grams
# for the nutrient requirements, you need to measure fat in grams
# but if you measure calcium in milligrams, that's fine. you just need to be consistent and always use mg for calcium.
foods = []
nutrients = []

astroNum = 5

base_nutrition_requirements = {}
nutrients = []
astro_nutrition_requirements = {}
food_nutrients = {}
food_portions = {}

# totals
nutrition_requirements = {}

astro_conditions = {}

astro_count = 5

with open('./flaskr/food_data/base_dailyValue.csv', encoding='utf-8') as csvf:
    csvReader = csv.DictReader(csvf)
    for row in csvReader:
        key = row['nutrient']
        nutrition_requirements[key] = 0
        nutrients.append(key)
        base_nutrition_requirements[key] = convert_nutrition_metric(key, float(row['value']), row['unit'])

with open('./flaskr/food_data/foods.csv', encoding='utf-8') as fd:
    csvReader = csv.DictReader(fd)
    for row in csvReader:
        key = row['Food Name']
        foods.append(key)
        food_nutrients[key] = row
        food_portions[key] = float(row['portion (g)'])

nutrition_rules = {}

with open("./flaskr/food_data/nutritionRules.csv") as nr:
    csvReader = csv.DictReader(nr)
    for row in csvReader:
        key = row['Gene']
        nutrition_rules[key] = row


# MTHFR	CYP1A2	CYP2E1	FADS1	SOD2	BCMO1	SLC2A2	PPARG	GSTP1	PCSK9	UGT1A1	NR1I2

with open('./flaskr/food_data/people.csv') as csvp:
    random_astro_genes = csv.DictReader(csvp)
    ind = 0
    for row in random_astro_genes:
        val = 0
        astro_nutrition_requirements[ind] = base_nutrition_requirements.copy()
        for gene, value in row.items():
            if value == 'TRUE':
                split_adj = nutrition_rules[gene]['adjustments'].replace("{", "").replace("}", "")
                if split_adj.find(":") >0:
                    split_adj = split_adj.split(":")
                    adj_k = split_adj[0].strip()
                    adj_val = 0
                    if split_adj[1].find("+") >0:
                        adj_val = float(split_adj[1].replace("+", "").strip())
                    elif split_adj[1].find("-") > 0:
                        adj_val = -float(split_adj[1].replace("-", "").strip())
                    
                    split_val = astro_nutrition_requirements[ind][adj_k].split(" ")
                    val = float(split_val[0])
                    unit = split_val[1]
                    print(val, " ", adj_val, " ", val + adj_val)
                    astro_nutrition_requirements[ind][adj_k] = str(val + adj_val) + " " + unit

        
        
        
        ind += 1

print("Astro Requirements: \n", json.dumps(astro_nutrition_requirements, indent=4))

# map each food to how much there is in each portion (the denominator of food_nutrients units)
'''
food_portions = {
    'chicken': 100, # 100g per portion
    'peanut butter': 100,
}
'''
# maps each food and nutrient to how much of the nutrient is present in 1 portion of the food
# Map<Food, Map<Nutrient, Number>>
'''
food_nutrients = {
    'chicken': {
        'fat': 10, # 10g fat / portion of chicken
        'protein': 70,
    },
    'peanut butter': {
        'fat': 50,
        'protein': 30,
    },
}
'''

final_astros = {}
#total for ship
for i in range(astro_count):
    final_astros[i] = astro_nutrition_requirements[randint(0, len(astro_nutrition_requirements) -1)]

for astro in final_astros.values():
    for nutrient, val in astro.items():
        split_val = val.split(" ")
        temp_val = float(split_val[0])
        unit = split_val[1]
        nutrition_requirements[nutrient] += temp_val



# maps each nutrient to how much is needed for the whole trip



# the problem is modeled as linear programming
# we must minimize the weight of food while meeting the nutrition requirements
# the variables are how many portions of each food, and nutrient will have a constraint equation
# for example
'''
minimize (100 * chicken + 100 * peanut_butter)
fat constraint:
10 * chicken + 50 * peanut_butter >= 2000
protein constraint:
70 * chicken + 30 * peanut_butter >= 4000
bounds:
chicken >= 0
peanut_butter >= 0
'''

# see the example here https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html
MIN = [food_portions[food] for food in foods]

# we need to negate the coefficients and values because the inequalities are all <= in the solver


for key, value in food_nutrients.items():
        for t,v in value.copy().items():
            value[(t.split("(")[0]).strip()] = value.pop(t)
      



CONSTRAINT_COEFFICIENTS = [[-float(food_nutrients[food].get(nutrient, 0)) for food in foods] for nutrient in nutrients]
CONSTRAINT_VALUES = [-float(nutrition_requirements[nutrient]) for nutrient in nutrients]
BOUNDS = [(0, None) for _ in foods]
res = linprog(MIN, A_ub=CONSTRAINT_COEFFICIENTS, b_ub=CONSTRAINT_VALUES, bounds=BOUNDS)


### OUTPUTS

# the program outputs how many grams of each food are needed. or whatever unit you used in your portion sizes.
# it also outputs the total mass of food

