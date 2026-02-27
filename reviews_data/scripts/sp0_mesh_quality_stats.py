import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

reviews_data_dir = Path(__file__).parent.parent

def main():
    filename = reviews_data_dir / 'mesh_quality_summary.csv'
    df = pd.read_csv(filename)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(df['mean'], bins=30, edgecolor='black', alpha=0.7)
    ax.set_xlabel('Mean Element Quality per Mesh')
    ax.set_ylabel('Number of Meshes')
    ax.set_title('Distribution of Mesh Quality (n=50)')
    ax.axvline(df['mean'].mean(), color='red', linestyle='--', 
               label=f"Cohort mean: {df['mean'].mean():.3f}")
    ax.legend()
    plt.tight_layout()
    plt.savefig(reviews_data_dir / 'deliverables/sp0_supp_mesh_quality_dist.pdf')

if __name__ == "__main__":
    main()