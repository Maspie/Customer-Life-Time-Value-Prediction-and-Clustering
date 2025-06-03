import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import detect_outliers


def test_detect_outliers_single_high():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 100]})
    out = detect_outliers(df, 'A')
    assert out['A'].tolist() == [100]


def test_detect_outliers_high_and_low():
    df = pd.DataFrame({'A': [-100, 1, 2, 3, 4, 5, 6, 7, 8, 100]})
    out = detect_outliers(df, 'A')
    values = sorted(out['A'].tolist())
    assert values == [-100, 100]
