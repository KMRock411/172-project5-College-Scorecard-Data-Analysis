import pytest
import pandas as pd
from Folder import Folder
from PlotAxesCollection import PlotAxesCollection

def test_create_collection():
    columns = PlotAxesCollection(pd.read_csv("Resources\CSV\General\Schools_DF.csv"))
    assert str(columns.plot_axes_list[0]) == '150% Completion Rate at 4Yr (%)'
    assert str(columns.plot_axes_list[-1]) == 'Student Enrollment Size'

def test_display_files():
    folder = Folder('General')
    folder2 = Folder('Selectiveness')
    assert folder.display_files() == ['Schools_DF.csv']
    assert folder2.display_files() == ['SAT_Aggregation_DF.csv', 'SAT_Bottom_Earnings_DF.csv', 'SAT_School_Count_DF.csv', 'SAT_Top_Earnings_DF.csv', 'Selectiveness_DF.csv']

def test_select_file():
    folder = Folder('General')
    folder2 = Folder('Selectiveness')
    assert str(folder.select_file('Schools_DF')) == 'Schools_DF'
    assert str(folder2.select_file('SAT_Aggregation_DF.csv')) == 'SAT_Aggregation_DF.csv'
