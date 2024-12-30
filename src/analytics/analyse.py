from src.analytics.pdp_helper import rescale_values
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


def rescale_values(scaled_values, mean, scale):
    """
    Rescale specific values from scaled to original values.

    Parameters:
    - scaled_values: List or array of scaled values.
    - mean: Mean value used for scaling.
    - scale: Scale (standard deviation) used for scaling.

    Returns:
    - Rescaled original values.
    """
    return (scaled_values * scale) + mean


def binary_boxplot(df, y="likes", title="Client vs Competitor", x="group"):
    plt.figure(figsize=(10, 6))
    plt.title(f"{title} Box Plot for {y} by {x}")

    sns.boxplot(x=x, y=y, data=df, palette=["blue", "orange"])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()
    plt.close()


def make_cross_tab(df: pd.DataFrame, col: str, save_dir=None, scaler=None):

    tmp_df = df.copy()

    if scaler is not None:
        scaler_cols = list(scaler.feature_names_in_)

        if col in scaler.feature_names_in_:
            idx = scaler_cols.index(col)
                
            mu = scaler.mean_[idx]
            std = scaler.scale_[idx]
                
            tmp_df[col] = rescale_values(tmp_df[col], mu, std)
            tmp_df[col] = tmp_df[col].apply(np.round, 2)


    crosstab = pd.crosstab(tmp_df[col], tmp_df["client_or_competitor"])
    percentages = crosstab.div(crosstab.sum(axis=0), axis=1) * 100
    result = crosstab.astype(str) + " (" + percentages.round(1).astype(str) + "%)"

    
    result.loc["Total"] = crosstab.sum(axis=0).astype(str) + " (" + (crosstab.sum(axis=0) / crosstab.values.sum() * 100).round(1).astype(str) + "%)"
    result["Total"] = crosstab.sum(axis=1).astype(str) + " (" + (crosstab.sum(axis=1) / crosstab.values.sum() * 100).round(1).astype(str) + "%)"
    result = result.rename(columns={0: "competitor", 1: "client"})
    result.columns.name = None

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, f"{col}.csv")
        result.to_csv(file_path, index=True) 
        print(f"Table saved to {file_path}")
    return result 