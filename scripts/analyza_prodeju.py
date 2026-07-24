"""Zakladni analyza prodejnich dat pro cvicne ucely (git/GitHub demo repo)."""

import pandas as pd

DATA_PATH = "data/prodeje.csv"


def nacti_data(cesta: str = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(cesta, parse_dates=["datum"])
    df["trzba"] = df["mnozstvi"] * df["cena_za_kus"]
    return df


def celkova_trzba(df: pd.DataFrame) -> float:
    return df["trzba"].sum()


def trzba_podle_kategorie(df: pd.DataFrame) -> pd.Series:
    return df.groupby("kategorie")["trzba"].sum().sort_values(ascending=False)


def trzba_podle_regionu(df: pd.DataFrame) -> pd.Series:
    return df.groupby("region")["trzba"].sum().sort_values(ascending=False)


def main() -> None:
    df = nacti_data()

    print(f"Celkova trzba: {celkova_trzba(df):,.0f} Kc")

    print("\nTrzba podle kategorie:")
    print(trzba_podle_kategorie(df).to_string())

    print("\nTrzba podle regionu:")
    print(trzba_podle_regionu(df).to_string())


if __name__ == "__main__":
    main()
