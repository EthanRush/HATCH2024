import json
import csv
import pandas as pd
import random
import os

# Function to filter the DataFrame based on earthlings's gene variations and return relevant info
def get_nutrition_info(gene_mapping, df):
        # Filter for genes with True value in the astronaut's gene mapping
        relevant_genes = {gene: variation for gene, variation in gene_mapping.items() if variation}
        # Initialize an empty list to store the results
        nutrition_info = []
        # Loop through the filtered genes and fetch their respective nutrition information
        for gene in relevant_genes.keys():
            gene_info = df[df['Gene'] == gene][['Gene','rs number', 'problem', 'recommendation', 'reference']].dropna()
            nutrition_info.extend(gene_info.to_dict('records'))
        return nutrition_info


def make_random_people(num_people):
    def create_gene_dict():
        genes = [
            "MTHFR", "CYP1A2", "CYP2E1", "FADS1", "SOD2",
            "BCMO1", "SLC2A2", "PPARG", "GSTP1", "PCSK9",
            "UGT1A1", "NR1I2"
        ]
        return {gene: random.choice([True, False]) for gene in genes}
    return [create_gene_dict() for _ in range(num_people)]

def gen_earth(path=None):
    # Load the CSV file containing gene variations, problems, recommendations, and sources
    df = pd.read_csv(os.path.relpath("./flaskr/food_data/nutritionRules.csv"))

    # Example: Creating a team of 5 astronauts
    #team_of_5 = make_random_people(5)
    #for person in team_of_5:
    if path is not None:
        with open(path) as gene_vars:
            csvReader = csv.DictReader(gene_vars)
            return get_nutrition_info(csvReader[0], df)
    else:   
        person = make_random_people(1)[0]      
        return get_nutrition_info(person, df)






def gen_space(astro_ct):

    with open('./person_data/final_data.json') as foodf:
        foodjson = json.load(foodf)

       

    return None