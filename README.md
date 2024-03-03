# HATCH2024
Gene Gnomes 2024 HATCH Hackathon Project


## Inspiration

We chose the Exploration for Astronaut Nutrition challenge because of our love of space and technology. Tapping into the complexities of nutrigenomics to sustain astronauts during long-duration space missions not only fuels our passion but also serves a vital need.

From the historical Apollo missions to the contemporary endeavors of private space companies, the allure of space has inspired countless innovations. This project leverages advancements in both human genetics and space travel. But it is also a testament to how even the most advanced frontiers of exploration can directly intersect with our daily lives.

Just as Tang became a household name after being associated with astronauts, space exploration has the power to catapult products and technologies into the public eye, making the once distant and inaccessible feel close and personal.

## What it does

This project is a comprehensive web and mobile-accessible app designed to ensure the nutritional well-being of astronauts. It's a tool tailored for both highly trained astronauts and health-conscious individuals here on Earth. 

By inputting genomic data for an astronaut team, the length of the mission, and payload limits, the app uses a knap-sack algorithm to calculate which food items to bring on a space mission to optimally nourish every crew member and fall within payload limits. It considers individual genetic variations, like the MTHFR polymorphism, to tailor dietary recommendations that mitigate the risk of health issues such as hyperhomocysteinemia—especially crucial when fresh produce is scarce, and every gram of payload counts.

But this app is not just useful in space. It offers an option for the general public to receive nutrition recommendations based on their genetic information. In doing so, it not only democratizes access to personalized nutrition but also raises awareness about the importance of nutrigenomics. This slice of space-age technology fits right into your pocket, accessible on iOS, Android devices, computers, and tablets—connecting the cosmos to your kitchen.

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



## Details for Nerds (how to run this code)

To run the code that powers our web app deployed at:  locally follow these steps.

1. clone this repo:
2. set up a virtual environment
3. pip install the requirements.txt
4. run the command flask run 
For a video demo of how to run this code locally see [here](http://foo.bar). For more detailed instructions and our code documentation please see the [README.md](http://foo.bar).
