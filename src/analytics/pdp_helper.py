import os
from matplotlib import pyplot as plt
from app.src.analytics.analyse import rescale_values
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.inspection import PartialDependenceDisplay, partial_dependence


def plot_pdp(model, x_train, savedir,
                        result_type="Likes", client_type= "Client", color="red", scaler=None):
    
    feature_names = x_train.columns
    scaler_cols = list(scaler.feature_names_in_)

    for f in feature_names:
        fig, ax = plt.subplots(figsize=(12, 8))
        pdp_result = partial_dependence(model, X=x_train, features=[f], grid_resolution=100)

        if scaler is not None:
            pdp_values = np.expm1(pdp_result['average'][0])
            if f in scaler_cols:
                feature_grid = pdp_result['grid_values'][0]
                if f in scaler.feature_names_in_:
                    idx = scaler_cols.index(f)
                
                mu = scaler.mean_[idx]
                std = scaler.scale_[idx]
                
                feature_grid = rescale_values(feature_grid, mu, std)

            else:
                feature_grid = pdp_result['grid_values'][0]
    
        else:
            pdp_values = pdp_result['average'][0]
            feature_grid = pdp_result['grid_values'][0]

        plt.plot(feature_grid, pdp_values, color = color, label = client_type)
        plt.suptitle(f"{f} {result_type} Partial Dependence Plot for {client_type}", fontsize=16, fontweight="bold")
        plt.legend()
        plt.tight_layout()
        if savedir:
            plt.savefig(f"{savedir}/{f}.png")
        else:
            plt.show()
            plt.close(fig)


def dual_pdp(model_1, model_2, original_df, x_train_1, x_train_2, feature, save_dir=None,  result_type="Likes", client_type="Client", color_1="orange", color_2="blue", scaler=None, segmentation_type=""):
    mu=None
    std=None
    pdp_result_1 = partial_dependence(model_1, X=x_train_1, features=[feature], grid_resolution=100)
    pdp_result_2 = partial_dependence(model_2, X=x_train_2, features=[feature], grid_resolution=100)

    scaler_cols = list(scaler.feature_names_in_)

    if scaler is not None:
        pdp_values_1 = np.expm1(pdp_result_1['average'][0])
        pdp_values_2 = np.expm1(pdp_result_2['average'][0])

        if feature in scaler_cols:
                feature_grid_1 = pdp_result_1['grid_values'][0]
                feature_grid_2 = pdp_result_2['grid_values'][0]
                if feature in scaler.feature_names_in_:
                    idx = scaler_cols.index(feature)
                
                mu = scaler.mean_[idx]
                std = scaler.scale_[idx]
                
                feature_grid_1 = rescale_values(feature_grid_1, mu, std)
                feature_grid_2 = rescale_values(feature_grid_2, mu, std)

        else:
            feature_grid_1 = pdp_result_1['grid_values'][0]
            feature_grid_2 = pdp_result_2['grid_values'][0]

        

    else:
        pdp_values_1 = pdp_result_1['average'][0]
        pdp_values_2 = pdp_result_2['average'][0]
        feature_grid_1 = pdp_result_1['grid_values'][0]
        feature_grid_2 = pdp_result_2['grid_values'][0]


    fig, ax = plt.subplots(figsize=(12, 8))


    ax.plot(feature_grid_1, pdp_values_1, color = color_1, label = "Client")
    ax.plot(feature_grid_2, pdp_values_2, color = color_2, label = "Competitor")
    ax2 = ax.twinx()

    if mu is not None and std is not None:
        original_df["unscaled_feature"] = rescale_values(original_df[feature], mu, std)
        max_x_axis = max(original_df["unscaled_feature"])
        min_x_axis = min(original_df["unscaled_feature"])
        if max_x_axis == min_x_axis:
            bins = [min_x_axis - 0.5, min_x_axis + 0.5]
            ax.set_xlim(-5, 5)


        else:
            binwidth = (max_x_axis - min_x_axis) / 30 
            if feature == "face_groups":
                max_x_axis += 0.5
            bins = np.arange(min_x_axis, max_x_axis + binwidth, binwidth) - binwidth / 2

        sns.histplot(x="unscaled_feature", hue="client_or_competitor", data=original_df, multiple = 'stack', ax=ax2, bins=bins)

    else:
        max_x_axis = max(original_df[feature])
        min_x_axis = min(original_df[feature])
        if max_x_axis == min_x_axis:
            bins = [min_x_axis - 0.5, min_x_axis + 0.5]
            ax.set_xlim(-5, 5)

        else:
            binwidth = (max_x_axis - min_x_axis) / 30  
            if feature == "face_groups":
                max_x_axis += 0.5
            bins = np.arange(min_x_axis, max_x_axis + binwidth, binwidth) - binwidth / 2 
            
        sns.histplot(x=feature, hue="client_or_competitor", data=original_df,  multiple = 'stack', ax = ax2, bins=bins)

    ax.set_title(f"Effect of {segmentation_type} {feature.replace('_',' ' '')} on {result_type}")
    ax.set_xlabel(feature, fontsize=14)
    ax.set_ylabel(result_type, fontsize=14)
    ax2.set_ylabel("Counts", fontsize=14)
    x_positions = {}
    for p in ax2.patches:
        x_position = p.get_x() + p.get_width() / 2 
        
        if p.get_height() > 0:  
            if x_position not in x_positions:
                ax2.text(x_position,
                        p.get_height() , 
                        f"{int(p.get_height())}",  
                        fontsize=12,
                        color='black',
                        ha='center',  
                        va='bottom')
                
                x_positions[x_position] = p.get_height()
            
            else:
                ax2.text(x_position,
                        p.get_height() + x_positions[x_position], 
                        f"{int(p.get_height())}",  
                        fontsize=12,
                        color='black',
                        ha='center',  
                        va='bottom')
            
    plt.legend(title='', loc='upper left', labels=['Client', 'Competitor'], bbox_to_anchor=(0.9, 1.1))

    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, f"{feature}_pdp.png")
        try:
            plt.savefig(file_path)
            print(f"Plot saved at {file_path}")
        except Exception as e:
            print(f"Error saving plot: {e}")
    else:
        plt.show()
        plt.close(fig)





