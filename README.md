# HATCH2024
Gene Gnomes 2024 HATCH Hackathon Project

See Marketing Site [here](https://mia-ktlk.github.io/nutrispace/)


## Inspiration

We chose the Exploration for Astronaut Nutrition challenge because of our love of space and technology. Tapping into the complexities of nutrigenomics to sustain astronauts during long-duration space missions not only fuels our passion but also serves a vital need.

From the historical Apollo missions to the contemporary endeavors of private space companies, the allure of space has inspired countless innovations. This project leverages advancements in both human genetics and space travel. But it is also a testament to how even the most advanced frontiers of exploration can directly intersect with our daily lives.

Just as Tang became a household name after being associated with astronauts, space exploration has the power to catapult products and technologies into the public eye, making the once distant and inaccessible feel close and personal.

## What it does

This project is a comprehensive web and mobile-accessible app designed to ensure the nutritional well-being of astronauts. It's a tool tailored for both highly trained astronauts and health-conscious individuals here on Earth. 

By inputting genomic data for an astronaut team, the length of the mission, and payload limits, the app uses a knap-sack algorithm to calculate which food items to bring on a space mission to optimally nourish every crew member and fall within payload limits. It considers individual genetic variations, like the MTHFR polymorphism, to tailor dietary recommendations that mitigate the risk of health issues such as hyperhomocysteinemia—especially crucial when fresh produce is scarce, and every gram of payload counts.

But this app is not just useful in space. It offers an option for the general public to receive nutrition recommendations based on their genetic information. In doing so, it not only democratizes access to personalized nutrition but also raises awareness about the importance of nutrigenomics. This slice of space-age technology fits right into your pocket, accessible on iOS, Android devices, computers, and tablets—connecting the cosmos to your kitchen.


-- 
## Details for Nerds

### Core Algorithm Overview

The algorithm iterates through available food options, calculating an optimized menu that meets daily nutritional needs—a critical task for space travel, where food efficiency and nutritional balance are paramount.

### Key Steps in the Algorithm

1. **Initialization**: Prepares structures for tracking food servings and cumulative nutritional content.

    ```python
    servings_dict = {food: 0 for food in food_options_df['foodname']}
    total_nutrients = {nutrient.lower(): 0.0 for nutrient in daily_values_df['nutrient']}
    ```

    Initializes dictionaries to keep track of how many servings of each food are in the menu and the total amount of each nutrient.

2. **Menu Construction Loop**: Adds food items to the menu, ensuring total calories are within a desired range.

    ```python
    for _, food_item in food_options_df.iterrows():
        # Check if adding this food item keeps calories within the desired range
        if 'calories' in total_nutrients and (total_nutrients['calories'] >= daily_value_calories * 0.9 and total_nutrients['calories'] <= daily_value_calories * 1.1):
            break
    ```

    Loops through each food item, stopping once the calorie content is optimized. This careful calorie management is crucial in space to prevent weight loss or gain.

3. **Nutritional Balance Check**: Ensures adding a food item doesn't exceed daily nutritional goals.

    ```python
    temp_nutrients = total_nutrients.copy()
    exceeds_daily_values = False
    for nutrient in temp_nutrients.keys():
        added_value = food_item[nutrient]
        # Prevent exceeding daily nutritional goals
        if nutrient == 'calories' and (temp_nutrients[nutrient] + added_value > daily_value_calories * 1.1):
            exceeds_daily_values = True
            break
    ```

    Evaluates whether adding another serving would unbalance the diet, crucial for maintaining health in space's constrained environment.

4. **Supplement Identification**: Calculates necessary supplements to meet any unmet daily requirements.

    ```python
    supplements_needed = {}
    for nutrient, value in total_nutrients.items():
        daily_value = daily_values_df[daily_values_df['nutrient'].str.lower() == nutrient]['value'].values[0]
        if value < daily_value * 0.9:
            supplements_needed[nutrient] = daily_value - value
    ```

    Identifies deficiencies and calculates supplements, ensuring astronauts receive all essential nutrients without overloading the spacecraft with unnecessary food weight.

### Conclusion

Through careful consideration of each food item's contribution to overall nutritional goals, the algorithm ensures an optimized menu for space travel. This methodical approach to meal planning ensures that astronauts maintain optimal health while conserving space and weight, crucial for the success of long-duration missions.

### Annotated Python Script for Pairwise Alignment

The Python script uses the Biopython library to perform pairwise alignments between astronaut gene sequences and a reference genome. This process is essential for identifying genetic variations, which can then be used to tailor nutrition plans for astronauts.

#### Script Explanation

```python
from Bio import SeqIO
from Bio.pairwise2 import align

# Load the reference genome for MTHFR gene
reference_genome = SeqIO.read("chromosome_1_full_human.fasta", "fasta")
```
- **Reference Genome Loading**: The `SeqIO.read` function reads the reference genome sequence for the MTHFR gene from a FASTA file, which is a text-based format for representing nucleotide sequences.

```python
# Load astronaut gene sequences
astronaut_sequences = [SeqIO.read(f"astronaut{i}.fasta", "fasta") for i in range(1, 6)]
```
- **Astronaut Gene Sequences Loading**: Loads the gene sequences of five astronauts from FASTA files into a list. The `SeqIO.read` function is used in a list comprehension to iterate through the filenames.

```python
# Align each astronaut's gene sequence with the reference genome
alignments = [align.globalxx(reference_genome.seq, astronaut.seq) for astronaut in astronaut_sequences]
```
- **Pairwise Alignment**: For each astronaut, the script performs a global pairwise alignment between the astronaut's gene sequence and the reference genome sequence. The `align.globalxx` method performs an alignment without considering scoring matrices, which means it simply aligns based on character matching.

```python
# Identify and report variants
for i, astronaut_alignments in enumerate(alignments):
    # Assuming we take the first alignment (usually the highest score)
    alignment = astronaut_alignments[0]
    print(f"Astronaut {i+1} alignment to reference:")
    print(alignment)
```
- **Variant Reporting**: Iterates over the alignments and prints the first (and presumably best) alignment for each astronaut. This step is critical for identifying differences between the astronaut's sequence and the reference, which can indicate genetic variants.

### Pairwise Alignment in Bioinformatics

**What Is Pairwise Alignment?**
Pairwise alignment is a bioinformatics method used to align two sequences (DNA, RNA, or protein) to identify regions of similarity. The sequences are aligned in a way that maximizes the number of matching characters and minimizes the number of gaps or mismatches.

**Why Is It Necessary?**
In the context of this challenge, pairwise alignment is necessary for several reasons:

- **Variant Identification**: By aligning the astronaut's gene sequences to a reference, we can pinpoint exact locations of genetic variations.
- **Nutrigenomic Analysis**: Understanding genetic variations is key to nutrigenomics—the study of how different nutrients affect health depending on an individual’s genetics.
- **Tailored Nutrition**: Once variations are identified, they can inform personalized nutrition plans that accommodate each astronaut's unique genetic makeup, which is vital for long-term space missions where efficiency and health are critical.

Pairwise alignments are foundational for many bioinformatics analyses and are particularly well-suited for tasks like the one described in the challenge, where individual genetic differences can have significant implications for health and nutrition.

### Accessing HealthKit Data for our Web App

HealthKit data is only accessible on iOS devices due to Apple's privacy and security guidelines. This means that when looking to use HealthKit data must run on an iOS device. The process starts with an iOS application (or shortcut) that requests permission to access HealthKit data:

```objective-c
// Request HealthKit permissions
HKHealthStore *healthStore = [[HKHealthStore alloc] init];
if ([HKHealthStore isHealthDataAvailable]) {
    NSSet *readTypes = [NSSet setWithObjects:[HKObjectType quantityTypeForIdentifier:HKQuantityTypeIdentifierStepCount], nil];
    
    [healthStore requestAuthorizationToShareTypes:nil readTypes:readTypes completion:^(BOOL success, NSError *error) {
        if (!success) {
            NSLog(@"You didn't get permission to access the health data.");
            return;
        }
        // Permission granted, proceed with accessing HealthKit data
    }];
}
```

### Querying HealthKit

Once permission is granted, the application can query HealthKit for the desired data:

```objective-c
// Query HealthKit for step count data
HKSampleType *sampleType = [HKSampleType quantityTypeForIdentifier:HKQuantityTypeIdentifierStepCount];
NSPredicate *predicate = [HKQuery predicateForSamplesWithStartDate:startDate endDate:endDate options:HKQueryOptionStrictStartDate];

HKSampleQuery *sampleQuery = [[HKSampleQuery alloc] initWithSampleType:sampleType predicate:predicate limit:HKObjectQueryNoLimit sortDescriptors:@[sortByDate] resultsHandler:^(HKSampleQuery *query, NSArray *results, NSError *error) {
    if (!results) {
        NSLog(@"An error occurred fetching the user's steps: %@", error.localizedDescription);
        return;
    }
    // Process and prepare data for Firebase upload
}];
[healthStore executeQuery:sampleQuery];
```

### Uploading to Firebase

After collecting the data, it's uploaded to Firebase, making it accessible from other platforms:

```objective-c
// Upload data to Firebase
- (void)uploadDataToFirebase:(NSArray *)data {
    FIRDatabaseReference *dbRef = [[FIRDatabase database] reference];
    
    for (NSDictionary *entry in data) {
        NSString *entryId = [NSString stringWithFormat:@"%@", entry[@"date"]];
        [[[dbRef child:@"healthData"] child:entryId] setValue:entry];
    }
}
```

### Retrieving Data in a Web App

Once the data is in Firebase, it can be accessed by a web application, enabling the integration of iOS-exclusive HealthKit data with web technologies:

```javascript
// Example JavaScript to retrieve data from Firebase in a web app
firebase.database().ref('/healthData').once('value').then((snapshot) => {
  const healthData = snapshot.val();
  // Use the health data in your web app
});
```

## How to Run this Code Locally

1. clone this repo:
2. set up a virtual environment
3. pip install the requirements.txt
4. run the command flask run 


## How we built it
The app was developed as a Python application using the Flask framework for the backend and Bootstrap for the frontend to ensure compatibility across various devices. For the alignment of FASTA files, we integrated a C-based BLAST algorithm that executes directly on the web server, providing quick and reliable sequence analysis for the user's genomic data.

## Data

### Genetic Data 

The "random" synthetic data options for creating astronauts for a mission were created using [NCBI’s Genome variation viewer] (https://www.ncbi.nlm.nih.gov/variation/view) as well as [NCBI’s Genome sequence viewer](https://www.ncbi.nlm.nih.gov/projects/sviewer/). 

We conducted pairwise alignments with BLAST on this synthetic data to identify astronauts who possess gene variants influencing nutritional absorption and dietary needs. The outcomes of these alignments are stored in the "example_alignments" array, which was utilized during the app's testing phase.

For users selecting the random data feature for either Earth or space missions, the app generates a random assortment of data. This showcases varied dietary recommendations tailored to the detected gene variants, illustrating how genetic differences can impact nutritional guidance.

The synthetic data generated for simulating astronaut missions utilizes a set of specific genes recommended by the challenge, including MTHFR (rs1801133), CYP1A2 (rs762551), and others listed. In this synthetic dataset, the occurrence of nutritional-related genetic variants is intentionally elevated compared to typical real-world frequencies. This approach allows us to extensively test the app's adaptability and demonstrate its capability to handle a wide range of dietary and nutritional scenarios based on genetic variations.

The selected genes for this purpose are:

Selected Genes

- **MTHFR** (rs1801133)
- **CYP1A2** (rs762551)
- **CYP2E1** (rs6413432)
- **FADS1** (rs174546)
- **SOD2** (rs4880)
- **BCMO1** (rs6564851)
- **SLC2A2** (rs5400)
- **PPARG** (rs1801282)
- **GSTP1** (rs762551)
- **PCSK9** (rs505151)
- **UGT1A1** (rs4148323)
- **NR1I2** (rs1523130)

This enriched prevalence of variants in the synthetic data is designed to showcase the app's comprehensive functionality and its ability to provide tailored dietary recommendations across a spectrum of genetic profiles.

However, it's important to note that when the app transitions to production and processes real astronaut data, the occurrence of these variants will likely be much lower. This discrepancy emphasizes the synthetic dataset's role in demonstrating the app's potential rather than reflecting the actual genetic diversity expected in a real astronaut population.

### Food Data

The food option database was developed by identifying plants that have been successfully cultivated in space. Not all plants can be included in this database due to various challenges associated with space farming. Moreover, the database also encompasses options for food items that are transported to space via payloads. This is because relying solely on in-space agriculture poses risks, such as the potential for plant diseases or failures, which could jeopardize the astronauts' food supply. Additionally, certain nutrients are more readily obtained from sources like meat than from space-grown crops alone. Therefore, the database represents a balanced mix of crops suitable for space cultivation and food items that can be effectively preserved and shipped to space.


## Our References

We calculated our recommended daily value amount using the guidelines recommended by the FDA.
We found the location of nucleotide variants affecting nutrition by using the following studies:

  - [Genetic Privacy and the Fourth Amendment: Unregulated Surreptitious DNA Harvesting](https://digitalcommons.unl.edu/lawfacpub/124/)
  - [Nutrigenomics and the Future of Nutrition](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9880799/)
  - [Cytochrome P450 2E1 - The Biological Pathway](https://sites.tufts.edu/alcoholmetabolism/the-biological-pathway/cytochrome-p450-2e1/#:~:text=Chronic%20alcohol%20consumption%20increases%20the,including%20certain%20drugs%20(3))
  - [The MTHFR Gene, Methylation, and Disease](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9464166/)
  - [Nutrition and Genes: An Interplay Complex](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3211030/)
  - [The Influence of FADS1 Genes on Omega-6 Polyunsaturated Fatty Acids](https://pubmed.ncbi.nlm.nih.gov/20599666/)
  - [SLC2A2 Gene on NCBI](https://www.ncbi.nlm.nih.gov/gene/6514)
  - [Dietary Patterns and Genetics of T2D](https://nutritionj.biomedcentral.com/articles/10.1186/1475-2891-13-17)
  - [Genetic Variants Influencing Biomarkers of Nutrition](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7902036/)
  - [Impact of Genetic Variants on Metabolism](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5728080/)
  - [Nutrigenomics: A Controversy Appraises](https://nutritionandmetabolism.biomedcentral.com/articles/10.1186/s12986-023-00738-z)
  - [Genetic Variants, Dietary Patterns, and Cardiometabolic Diseases](https://www.nature.com/articles/s41598-019-53101-9)

