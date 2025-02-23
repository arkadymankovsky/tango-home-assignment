# tango-home-assignment

## Summary of Key Decision Points

### Problem Formulation
- **Analogy**: Treat the price recommendation task as a movie recommendation analog (where price = movie and VFM = movie features).
- **Data Usage**: Use existing price points only, as generating new prices is too complex.
- **Goal**: Recommend 6 prices to each user.

### Data Treatment
- **Burst Purchases**: Keep burst purchases (multiple purchases in 1 minute) as separate events for simplicity.
- **Aggregation**: Aggregate data to user-price level for main interactions.
- **Mean VFM Calculation**: Calculate the mean VFM per price point.
- **Temporal Features**: Include temporal features (hour, week) based on insights from heatmap analysis.

### Model Selection
- **Model Choice**: Choose LightFM for a hybrid approach.
  - Combines collaborative filtering with price features.
  - Features include VFM, hour, and week patterns.
  - Simpler than neural approaches for the 4-hour scope.

### Evaluation Strategy
- **Primary Metric**: Hit Rate@6 as the primary evaluation metric.
- **Baseline Comparison**: Compare against a baseline (most popular prices).
- **Hit Rate Lift**: Use `hit_rate_lift = model_hit_rate / baseline_hit_rate` for clarity.
- **Single Metric Preference**: A single metric makes comparison clear and straightforward.

### Considered But Rejected
- **New Price Point Generation**: Rejected due to complexity.
- **Burst Purchase Aggregation**: Kept to maintain data cleanliness.
- **Multiple Evaluation Metrics**: Preferred a single clear metric for evaluation.
- **Complex Temporal Evaluation Windows**: Avoided for simplicity.

---

This framework balances sophistication with the feasibility of a 4-hour task while maintaining reasonable evaluation standards.