import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    
    # Clean data
    df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]
    
    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df["value"], color="r")
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.savefig("line_plot.png")
    plt.close()

def draw_bar_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    
    # Clean data
    df["year"] = df.index.year
    df["month"] = df.index.month_name()
    df_bar = df.groupby(["year", "month"])["value"].mean().unstack()
    
    # Plot
    fig = df_bar.plot(kind="bar", figsize=(10, 6)).get_figure()
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.savefig("bar_plot.png")
    plt.close()

def draw_box_plot():
    # Import data
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")
    
    # Clean data
    df["year"] = df.index.year
    df["month"] = df.index.month_name()
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x="year", y="value", data=df, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    sns.boxplot(x="month", y="value", data=df, ax=axes[1], order=[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    plt.tight_layout()
    plt.savefig("box_plot.png")
    plt.close()

draw_line_plot()
draw_bar_plot()
draw_box_plot()