import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.sandbox.stats.multicomp import TukeyHSDResults
from statsmodels.stats.multicomp import pairwise_tukeyhsd


class Result:
    anova_table: pd.DataFrame
    post_hoc: TukeyHSDResults

    def __init__(self, anova_table: pd.DataFrame, post_hoc: TukeyHSDResults) -> None:
        self.anova_table = anova_table
        self.post_hoc = post_hoc

    def show(self):
        print("ANOVA")
        print(self.anova_table)
        print()
        print(self.post_hoc)


def analysis(df: pd.DataFrame) -> Result:
    model = ols("area ~ C(perlakuan)", data=df).fit()
    anova_table = sm.stats.anova_lm(model, typ=2)
    post_hoc = pairwise_tukeyhsd(
        endog=df["area"],
        groups=df["perlakuan"],
        alpha=0.2,
    )
    return Result(anova_table, post_hoc)
