import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from analysis import Result


def plot(df: pd.DataFrame, result: Result):
    plt.figure(figsize=(10, 7))
    sns.barplot(
        data=df,
        x="perlakuan",
        y="area",
        errorbar="se",
    )
    plt.title("Distribusi Area per Perlakuan")
    plt.xlabel("Perlakuan")
    plt.ylabel("Area")
    plt.savefig("../result/dist.png")

    fig = result.post_hoc.plot_simultaneous()
    plt.savefig("../result/post.png")
