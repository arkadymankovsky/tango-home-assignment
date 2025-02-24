# Tango - Home Assignment: USD-Coins Recommendation System

## Overview
This project implements a recommendation system to suggest optimal USD-coin combinations to users based on their historical purchase patterns and contextual factors such as time of day.

## Key Findings from Data Analysis

### User Behavior
- **Purchase Distribution**: Highly skewed with most users making several dozen purchases while a small segment shows extremely high activity
- **Minimum Engagement**: All users have at least five purchases in the dataset
- **Rapid Transactions**: Some users make multiple purchases within short time windows

### Pricing & Value Patterns
- **Discrete Price Points**: USD values follow a categorical pattern with specific price tiers dominating transactions
- **Value for Money (VFM)**: Several distinct peaks in the distribution suggest commonly offered value propositions
- **Popular Price Points**: The $0.99 price point consistently shows the highest purchase frequency across all hours
- **Low-Volume Tiers**: Certain price points have very few purchases, suggesting less market appeal

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

---

*Note: This implementation demonstrates how historical purchase patterns and time-based factors can be used to create personalized recommendations in a virtual economy system.*