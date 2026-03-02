from load import load
from plot import plot
from analysis import analysis


def main():
    df = load()
    res = analysis(df) 
    res.show()
    plot(df, res)
    

if __name__ == "__main__":
    main()
