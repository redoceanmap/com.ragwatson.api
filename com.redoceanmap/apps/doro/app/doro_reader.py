import json
from pathlib import Path
import pandas as pd


_DATA_DIR = Path(__file__).resolve().parent
_CSV_PATH = _DATA_DIR / "한국도로공사_교통사고통계_20241231.csv"


class DoroReader:
    def __init__(self) :
        pass

    def get_data(self) :
        df = pd.read_csv(_CSV_PATH, encoding="cp949")
        return df.iloc[[1]].astype(object).where(df.iloc[[1]].notna(), None)