# USD-Coins Recommendation System

## Overview
This recommendation system predicts USD-coin combinations to offer users at specific hours based on their historical purchase patterns. The system uses SVD (Singular Value Decomposition) to learn user preferences and make personalized recommendations.

## Implementation Highlights

### Data Preparation
The system creates unique identifiers for items (USD-coins combinations) and user contexts (user-hour combinations). We explored different rating approaches to capture user preferences, including binary ratings, Value for Money (VFM) based ratings, and personalized combined ratings.

### Model Training
We use Surprise's SVD algorithm with 30 latent factors to capture the patterns in user purchasing behavior. The model learns the relationship between user-hour combinations and their preferred USD-coin packages.

### Recommendation Generation
The recommendation function generates predictions for all possible USD-coin combinations for a given user at a specific hour, then returns the top N options with the highest predicted ratings.

### Parallel Processing
To improve performance, the system implements parallel processing using Python's multiprocessing module. This allows multiple user recommendations to be generated simultaneously, significantly reducing overall processing time.

## Alternative Rating Approaches

### Binary Ratings
The simplest approach where all purchases receive a rating of 1. This captures the basic signal that a purchase occurred without differentiating between purchases.

### VFM-Based Ratings
Uses the Value for Money (coins per USD) as the rating metric. This approach helps the model learn which combinations provide better objective value.

### Personalized Combined Ratings
This sophisticated approach calculates personalized weights for different factors (USD amount, coins amount, and VFM) based on each user's behavior patterns. It captures the complex tradeoffs between preferring certain USD amounts, specific coin amounts, or higher VFM.

## Performance Optimizations
Several optimizations were implemented to improve recommendation generation speed:
- Pre-computing unique items to avoid repeated calculations
- Using numpy for faster vector operations
- Implementing partial sorting for better performance
- Direct matrix operations using the model's internal matrices

## Future Work

1. **Experiment with Different Rating Approaches**
   - Test which rating strategy produces the best recommendations
   - Consider incorporating purchase frequency and recency

2. **Add Temporal Features**
   - Implement time decay for older purchases
   - Model day-of-week patterns

3. **Feature Engineering**
   - Add more contextual features
   - Create user segments based on purchase behavior

4. **Advanced Models**
   - Test neural network-based recommenders
   - Explore ensemble approaches

5. **Evaluation Framework**
   - Implement comprehensive offline evaluation metrics
   - Prepare for A/B testing in production