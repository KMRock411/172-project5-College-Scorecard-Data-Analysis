class PlotAxesCollection:
    def __init__(self,dataframe):
        self.plot_axes_list = []

        for column in dataframe:
            self.plot_axes_list.append(column)

    def __str__(self):
        return "A collection of column names to choose from"
