# Tango - Home Assignment: Price Points Recommendation System

## Overview
This project implements a recommendation system to suggest optimal price points combinations to users based on their historical purchase patterns

## Key Findings from Data Analysis

### User Behavior
- **Purchase Distribution**: Highly skewed with most users making several dozen purchases while a small segment shows extremely high activity
- **Minimum Engagement**: All users have at least five purchases in the dataset
- **Rapid Transactions**: Some users make multiple purchases within short time windows

### Pricing & Value Patterns
- **Discrete Price Points**: USD values follow a categorical pattern with specific price tiers dominating transactions
- **Value for Money (VFM)**: Several distinct peaks in the distribution suggest commonly offered value propositions
- **Popular Price Points**: The $0.99 price point consistently shows the highest purchase frequency across all hours
- **Low-Volume Tiers**: Certain price points have very few purchases

### Temporal Patterns
- **Hourly Variation**: Average price per user (normalized by number of unique users) varies by hour, indicating time-based preferences
- **Evening Activity**: Slight increase in purchasing activity during evening hours (9-11 PM)
- **Weekday Consistency**: No significant difference in pricing patterns across different days of the week
- **Steady Purchase Rate**: Average number of purchases per user shows consistency across hours, suggesting price variations are due to preference rather than volume

## Implementation Approach

### Scope Decisions
1. **Limited to Existing Combinations**: For simplicity, the recommendation system focuses on existing USD-coin combinations rather than creating new ones
2. **Cold Start Handling**: The cold start problem is not addressed in the current implementation timeframe

### Data Preparation
- No null values in the dataset
- Timestamps converted to datetime format
- Dataset contains 127,217 unique users and 1,741,152 purchases

## Recommendation Strategy
The system leverages collaborative filtering techniques with the SVD algorithm to predict user preferences for USD-coin combinations, with time of day as a key contextual factor. The parallel processing implementation allows for efficient generation of recommendations at scale.

# Model Design Considerations

## Model Input and Evaluation Strategy

I faced a decision point regarding model inputs and evaluation metrics.

### Key Considerations:

1. **Contextual Factors**: The exploratory data analysis clearly showed that hour of day significantly influences user purchasing patterns, suggesting it should be included as an input feature.

2. **Evaluation Requirements**: The recommended metrics in the assignment, like Precision@k and Recall@k require a scenario where users choose multiple offers simultaneously and then compared to predicted offers. But in order to achieve it I need to agg by timestamp.

3. **Model Input Decision**: I chose to include hour as a contextual factor by creating user-hour combinations (rather than just user IDs) as the model input. This captures the temporal purchasing patterns observed in the data.

4. **Evaluation Approach**: With this model structure, the system generates personalized recommendations for each user-hour combination.

5. **Metric Selection**: Given this design, traditional Precision@k and Recall@k metrics weren't appropriate. Instead, I used Hit Rate as the primary evaluation metric, which measures whether the recommended item matches any item actually purchased by the user.


---
