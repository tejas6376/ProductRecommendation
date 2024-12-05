
# Product Recommendation System
## Overview
This project is a Product Recommendation System designed to recommend products from a catalog based on user preferences. The system supports the following functionalities:

Image-Based Recommendations: Upload an image, and the system recommends products based on visual similarity.
Title-Based Recommendations: Enter a product title, and the system recommends similar products based on textual similarity.
Title and Brand-Based Recommendations: Enter a product title and brand name, and the system recommends the most relevant products based on combined similarity scores.

## 🌟 Features
The system supports five product categories:

- Shirt
- Trousers
- Hats
- Shoes
- Watch
### Recommendation Methods

    1. Image Similarity:

    - Takes an image as input.
    - Extracts visual features using a pre-trained CNN model.
    - Computes similarity scores with the product catalog and returns the top recommendations.

    2. Title Similarity:

    - Takes a product title as input.
    - Uses text processing techniques
    - Matches similar products based on textual similarity scores.
    
    3. Title and Brand Similarity:

    - Takes a product title and brand name as input.
    - Combines title and brand information using a weighted similarity approach.
    - Recommends products with the highest combined similarity scores.
## Tech Stack
- Programming Language: Python
- Frameworks/Libraries:
    - Data Handling: pandas, numpy
    - Text Analysis: CountVectorizer, TfidfVectorizer, scipy.sparse, re
    - Image Processing: cv2, PIL.Image
    - Similarity Calculations: cosine_similarity, pairwise_distances
    - Visualization: matplotlib, seaborn, WordCloud
    - Machine Learning: sklearn.pipeline, sklearn.preprocessing, sklearn.model_selection, sklearn.metrics
    - Web Requests: requests, urllib
    - Warnings: warnings
- Data: Images are stores as hyperlinks to their respective amazon pages in the db.csv file.
## How to Run the Project
Step 1: Clone the Repository
```bash
    git clone https://github.com/tejas6376/ProductRecommendation.git
    cd product-recommendation-system
```

Step 2: Install all required Python libraries
```bash
    pip install -r requirements.txt
```

Step 3: Prepare the Data
- Ensure that your product data (titles, brands, images) is available in the data/ folder.
- Update the paths in the code if necessary.

## Usage Instructions
    1. Image-Based Recommendations
        Upload an image of a product.
        The system extracts features using computer vision techniques and recommends the top 5 visually similar products.
    2. Title-Based Recommendations
        Enter a product title (e.g., "Slim Fit Shirt").
        The system uses TF-IDF vectorization and cosine similarity to find the most similar products.
    3. Title and Brand-Based Recommendations
        Provide a product title and brand name.
        Combines textual similarity of the title with brand matching for more accurate recommendations.
## Project Workflow
    1. Data Preprocessing:

    - Clean and preprocess product titles using regular expressions and tokenization.
    - Extract features for both image and text inputs.
    2. Image Similarity:

    - Features are extracted from images using a pre-trained CNN (e.g., ResNet).
    - Visual features are compared using cosine_similarity.
    3. Text Similarity:

    - Titles are vectorized using TF-IDF or CountVectorizer.
    - Pairwise distances are calculated to find similar products.
    4. Combined Similarity:

    - Combines title-based and brand-based scores using a weighted approach for refined recommendations.
## Visualization
The project includes visualizations for:

- Similarity Distribution: Histograms of cosine similarity scores.
    ![image](https://github.com/user-attachments/assets/1dfab513-d23f-4a8d-8153-cc383aec5358)
    ![image](https://github.com/user-attachments/assets/2b9b0584-4db0-4cb1-ac16-4d86d255d687)
    ![image](https://github.com/user-attachments/assets/434ba35e-5497-4f84-b130-f6ae8f787059)
    ![image](https://github.com/user-attachments/assets/03d92578-6f5e-4fdc-be9a-cfc13e54bcd1)


- Word Clouds: Visualizing frequently used terms in product titles.
    ![image](https://github.com/user-attachments/assets/8499328b-3847-4075-9300-55fffafb3015)
    ![image](https://github.com/user-attachments/assets/cb055d67-1817-43a8-8a6e-0ea7513565f7)
## Future Enhancements
- Incorporate customer reviews to refine recommendations.
- Add support for real-time product catalog updates.
- Enhance the model with deep learning-based NLP techniques (e.g., BERT).
