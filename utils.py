import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    dataset_file = 'dataset_purchases.csv'
    data = pd.read_csv(dataset_file)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data['usd'] = data['usd'].round(2)
    data['hour'] = data['timestamp'].dt.hour
    data['week'] = data['timestamp'].dt.isocalendar().week
    data['day_of_week'] = data['timestamp'].dt.day_name()
    return data


def plot_purchases_per_user(df: pd.DataFrame):
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    total_purchases_per_user = df.groupby('user_id')['usd'].count().reset_index(name='total_purchases')
    total_purchases_per_user['log_total_purchases'] = np.log(total_purchases_per_user['total_purchases'] + 1)

    # Histogram and Box Plot for Total Purchases
    sns.histplot(total_purchases_per_user['total_purchases'], bins=30, kde=True, color='lightgreen', ax=axes[0, 0])
    axes[0, 0].set_title('Histogram of Total Purchases per User', fontsize=14)
    axes[0, 0].set_xlabel('Total Purchases', fontsize=12)
    axes[0, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=total_purchases_per_user['total_purchases'], color='lightblue', ax=axes[0, 1])
    axes[0, 1].set_title('Box Plot of Total Purchases per User', fontsize=14)
    axes[0, 1].set_ylabel('Total Purchases', fontsize=12)

    # Histogram and Box Plot for Log-Scaled Total Purchases
    sns.histplot(total_purchases_per_user['log_total_purchases'], bins=30, kde=True, color='salmon', ax=axes[1, 0])
    axes[1, 0].set_title('Histogram of Log-Scaled Total Purchases per User', fontsize=14)
    axes[1, 0].set_xlabel('Log of Total Purchases', fontsize=12)
    axes[1, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=total_purchases_per_user['log_total_purchases'], color='lightcoral', ax=axes[1, 1])
    axes[1, 1].set_title('Box Plot of Log-Scaled Total Purchases per User', fontsize=14)
    axes[1, 1].set_ylabel('Log of Total Purchases', fontsize=12)

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_features_values(df: pd.DataFrame):
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Create a figure with subplots
    fig, axes = plt.subplots(6, 2, figsize=(14, 20))

    df['usd_log'] = np.log(df['usd'] + 1)
    df['VFM_log'] = np.log(df['VFM'] + 1)
    df['coins_log'] = np.log(df['coins'] + 1)
    # Histogram and Box Plot for USD
    sns.histplot(df['usd'], bins=30, kde=True, color='lightgreen', ax=axes[0, 0])
    axes[0, 0].set_title('Histogram of USD Values', fontsize=14)
    axes[0, 0].set_xlabel('USD', fontsize=12)
    axes[0, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['usd'], color='lightblue', ax=axes[0, 1])
    axes[0, 1].set_title('Box Plot of USD Values', fontsize=14)
    axes[0, 1].set_ylabel('USD', fontsize=12)

    sns.histplot(df['usd_log'], bins=30, kde=True, color='lightgreen', ax=axes[1, 0])
    axes[1, 0].set_title('Histogram of Log-Scaled USD Values', fontsize=14)
    axes[1, 0].set_xlabel('Log of USD', fontsize=12)
    axes[1, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['usd_log'], color='lightblue', ax=axes[1, 1])
    axes[1, 1].set_title('Log of of USD Values', fontsize=14)
    axes[1, 1].set_ylabel('USD', fontsize=12)

    # Histogram and Box Plot for VFM
    sns.histplot(df['VFM'], bins=30, kde=True, color='salmon', ax=axes[2, 0])
    axes[2, 0].set_title('Histogram of VFM Values', fontsize=14)
    axes[2, 0].set_xlabel('VFM', fontsize=12)
    axes[2, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['VFM'], color='lightcoral', ax=axes[2, 1])
    axes[2, 1].set_title('Box Plot of VFM Values', fontsize=14)
    axes[2, 1].set_ylabel('VFM', fontsize=12)

    sns.histplot(df['VFM_log'], bins=30, kde=True, color='salmon', ax=axes[3, 0])
    axes[3, 0].set_title('Histogram of Log-Scaled VFM Values', fontsize=14)
    axes[3, 0].set_xlabel('Log of VFM', fontsize=12)
    axes[3, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['VFM_log'], color='lightcoral', ax=axes[3, 1])
    axes[3, 1].set_title('Log of of VFM Values', fontsize=14)
    axes[3, 1].set_ylabel('VFM', fontsize=12)

    sns.histplot(df['coins'], bins=30, kde=True, color='salmon', ax=axes[4, 0])
    axes[4, 0].set_title('Histogram of coins Values', fontsize=14)
    axes[4, 0].set_xlabel('Coins', fontsize=12)
    axes[4, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['coins'], color='lightcoral', ax=axes[4, 1])
    axes[4, 1].set_title('Box Plot of coins Values', fontsize=14)
    axes[4, 1].set_ylabel('coins', fontsize=12)

    sns.histplot(df['coins_log'], bins=30, kde=True, color='salmon', ax=axes[5, 0])
    axes[5, 0].set_title('Histogram of Log-Scaled Coins Values', fontsize=14)
    axes[5, 0].set_xlabel('Log of Coins', fontsize=12)
    axes[5, 0].set_ylabel('Frequency', fontsize=12)

    sns.boxplot(y=df['coins_log'], color='lightcoral', ax=axes[5, 1])
    axes[5, 1].set_title('Log of of Coins Values', fontsize=14)
    axes[5, 1].set_ylabel('Coins', fontsize=12)

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_purchase_count_per_pricing(df: pd.DataFrame):
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Calculate value counts and sort
    usd_counts = df.usd.value_counts().sort_index()

    # Create a larger figure for the histogram
    plt.figure(figsize=(16, 10))  # Increased size for better visibility

    # Horizontal Histogram
    bar_plot = sns.barplot(x=usd_counts.index, y=usd_counts.values, color='lightblue')
    plt.title('Frequency of USD Values', fontsize=20)  # Increased title font size
    plt.xlabel('USD Value', fontsize=16)  # Increased label font size
    plt.ylabel('Frequency', fontsize=16)  # Increased label font size
    plt.xticks(rotation=90, fontsize=12)  # Rotate x-axis labels to be vertical and increase font size

    # Add value labels on top of each bar, displayed vertically and shortened
    for p in bar_plot.patches:
        value = int(p.get_height())
        # Shorten the value
        if value >= 1_000_000:
            label = f'{value / 1_000_000:.1f}M'  # Millions
        elif value >= 1_000:
            label = f'{value / 1_000:.1f}K'  # Thousands
        else:
            label = str(value)  # No abbreviation

        # Adjust the vertical position of the label
        bar_plot.annotate(label,
                          (p.get_x() + p.get_width() / 2., p.get_height() + 115),  # Add an offset of 5
                          ha='center', va='bottom', fontsize=12, rotation=90)  # Set rotation to 90 for vertical text

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_unique_user_count_per_pricing(df: pd.DataFrame):
    # Set the style for the plots
    sns.set(style="whitegrid")

    # Calculate the number of unique users for each USD value
    unique_users_per_usd = df.groupby('usd')['user_id'].nunique().reset_index(name='unique_users')

    # Create a figure for the plot
    plt.figure(figsize=(16, 8))  # Adjust size as needed

    # Bar plot for unique users per USD value
    sns.barplot(x='usd', y='unique_users', data=unique_users_per_usd, color='lightblue')
    plt.title('Number of Unique Users per USD Value', fontsize=20)
    plt.xlabel('USD Value', fontsize=16)
    plt.ylabel('Number of Unique Users', fontsize=16)
    plt.xticks(rotation=90, fontsize=12)  # Rotate x-axis labels for better readability

    # Add value labels on top of each bar, displayed vertically
    for p in plt.gca().patches:
        plt.annotate(f'{int(p.get_height())}',
                     (p.get_x() + p.get_width() / 2., p.get_height()),
                     ha='center', va='bottom', fontsize=12, rotation=90)  # Set rotation to 90 for vertical text

    # Adjust layout
    plt.tight_layout()
    plt.show()


def plot_avg_purchase_per_user_per_hour(df: pd.DataFrame):
    # Step 2: Calculate the number of purchases and unique users for each price point and hour
    heatmap_data = df.groupby(['usd', 'hour']).agg(
        number_of_purchases=('user_id', 'count'),
        number_of_unique_users=('user_id', 'nunique')
    ).reset_index()

    # Step 3: Calculate normalized values
    heatmap_data['normalized_value'] = heatmap_data['number_of_purchases'] / heatmap_data['number_of_unique_users']

    # Step 4: Get the top 10 price points
    top_10_prices = heatmap_data.groupby('usd')['normalized_value'].sum().nlargest(15).index

    # Step 5: Filter the data for the top 10 price points
    heatmap_data_top10 = heatmap_data[heatmap_data['usd'].isin(top_10_prices)]

    # Step 6: Create a pivot table for the heatmap
    # Step 6: Create a pivot table for the heatmap using pivot_table
    heatmap_pivot = heatmap_data_top10.pivot_table(index='hour', columns='usd', values='normalized_value',
                                                   aggfunc='mean')

    # Step 7: Plot the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_pivot, cmap='YlGnBu', annot=True, fmt=".2f",
                cbar_kws={'label': 'Normalized Purchases per Unique User'})
    plt.title('Normalized Purchases per Unique User by Hour and Price Point', fontsize=16)
    plt.xlabel('Price Points', fontsize=14)
    plt.ylabel('Hour of the Day', fontsize=14)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()


def plot_avg_price_per_hour(df: pd.DataFrame):
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 12))

    # Count unique users and calculate metrics per hour
    user_count_by_hour = df.groupby('hour')['user_id'].nunique().reset_index(name='user_count')
    total_price_by_hour = df.groupby('hour')['usd'].sum().reset_index(name='total_price')
    merged_data = pd.merge(total_price_by_hour, user_count_by_hour, on='hour')
    merged_data['normalized_avg_price'] = merged_data['total_price'] / merged_data['user_count']

    # Plot line chart
    sns.lineplot(data=merged_data, x='hour', y='normalized_avg_price', marker='o', color='green', ax=ax1)
    ax1.set_title('Normalized Average USD Price per User by Hour of the Day', fontsize=12)
    ax1.set_xlabel('Hour of the Day', fontsize=10)
    ax1.set_ylabel('Normalized Average USD Price', fontsize=10)
    ax1.set_xticks(range(24))
    ax1.grid(True)

    # Calculate metrics per hour and week
    user_count_by_hour_week = df.groupby(['week', 'hour'])['user_id'].nunique().reset_index(name='user_count')
    total_price_by_hour_week = df.groupby(['week', 'hour'])['usd'].sum().reset_index(name='total_price')
    merged_week_data = pd.merge(total_price_by_hour_week, user_count_by_hour_week, on=['week', 'hour'])
    merged_week_data['normalized_avg_price'] = merged_week_data['total_price'] / merged_week_data['user_count']

    # Create heatmap data
    heatmap_data = merged_week_data.pivot_table(index='week', columns='hour', values='normalized_avg_price',
                                                aggfunc='mean')

    # Plot heatmap
    sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False, cbar_kws={'label': 'Normalized Average Price'}, ax=ax2)
    ax2.set_title('Heatmap of Normalized Average Price per User by Hour and Week', fontsize=12)
    ax2.set_xlabel('Hour of the Day', fontsize=10)
    ax2.set_ylabel('Week Number', fontsize=10)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)

    plt.tight_layout()
    plt.show()


def plot_avg_number_purchase_per_hour(df: pd.DataFrame):
    # Group by hour and count purchases
    hourly_counts = df.groupby(['hour', 'user_id']).size().reset_index(name='purchase_count')

    # Calculate average purchases per user for each hour
    avg_purchases = hourly_counts.groupby('hour')['purchase_count'].mean().reset_index()

    # Set up the plot
    plt.figure(figsize=(12, 6))

    # Create bar plot - updated to avoid deprecation warning
    sns.barplot(x='hour', y='purchase_count', hue='hour', data=avg_purchases, palette='viridis', legend=False)

    # Add reference line for overall average
    overall_avg = avg_purchases['purchase_count'].mean()
    plt.axhline(y=overall_avg, color='r', linestyle='--',
                label=f'Overall Average: {overall_avg:.2f} purchases per user')

    # Customize the plot
    plt.title('Average Number of Purchases per User by Hour of Day', fontsize=16)
    plt.xlabel('Hour of Day (24-hour format)', fontsize=12)
    plt.ylabel('Average Purchases per User', fontsize=12)
    plt.xticks(range(0, len(avg_purchases)), avg_purchases['hour'])
    plt.grid(axis='y', alpha=0.3)
    plt.legend()

    # Add value labels on top of bars
    for i, val in enumerate(avg_purchases['purchase_count']):
        plt.text(i, val + 0.05, f'{val:.2f}', ha='center')

    # Show plot
    plt.tight_layout()
    plt.show()

    max_hour = avg_purchases.loc[avg_purchases['purchase_count'].idxmax()]
    print(f"Peak hour: {max_hour['hour']} with {max_hour['purchase_count']:.2f} average purchases per user")


def plot_usd_per_dayofweek(df: pd.DataFrame):
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='day_of_week', y='usd', order=day_order)
    plt.title('Distribution of USD by Day of Week')
    plt.xticks(rotation=45)
    plt.show()
