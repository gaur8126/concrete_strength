# Concrete Compressive Strength Prediction 🏗️📊

## Overview
This project aims to predict **the compressive strength of concrete** based on various material properties such as cement content, water-cement ratio, and aggregate type. Using **machine learning models**, the project helps in estimating the durability and quality of concrete structures.


## Features:

- *`cement:`* The amount of cement used in the mix (in kg per cubic meter). Cement is a primary binder in concrete and contributes significantly to its strength.

- *`blast_furnace_slag:`* The amount of blast furnace slag (in kg per cubic meter). Slag is a byproduct of iron production and is often used as a cement substitute to enhance durability and reduce costs.

- *`fly_ash:`* The amount of fly ash (in kg per cubic meter). Fly ash is another industrial byproduct used as a supplementary cementitious material.

- *`water:`* The amount of water (in kg per cubic meter). Water content is crucial for the hydration of cement and influences the workability and strength of concrete.

- *`superplasticizer:`* The amount of superplasticizer (in kg per cubic meter). These are chemical additives that improve workability without increasing water content.

- *`coarse_aggregate:`* The amount of coarse aggregate (in kg per cubic meter). These are larger particles (e.g., gravel) that form the bulk of the concrete mix.

- *`fine_aggregate:`* The amount of fine aggregate (in kg per cubic meter). These are smaller particles (e.g., sand) that fill gaps between coarse aggregates.

- *`age:`* The age of the concrete (in days) when the compressive strength was measured. Concrete strength typically increases with age due to ongoing hydration. 

- *`concrete_compressive_strength:`* The target variable (in MPa), representing the compressive strength of the concrete. This is the key output used to evaluate the quality of the concrete mix. 

## Installation 🔧
1. Clone the repository:
   ```bash
   https://github.com/gaur8126/concrete_strength.git
   ```
2. Navigate to the project directory:
   ```bash
   cd concrete_strength
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the script:
   ```bash
   app.py

# Model Performance 📈
- **Achieved Accuracy**: **94.96%**
- **Best Performing Model**: CatBoost
- **Evaluation Metrics**: RMSE, R² Score, MAE

## Screenshots 🖼️
![screenshot](https://github.com/gaur8126/ProjectsImage/blob/main/Screenshot%202025-03-15%20083348.png)

## Usage 🚀
- Run the model on a sample dataset.
- Modify input parameters to test different scenarios.
- Visualize how different factors impact compressive strength.
