import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from PlotAxesCollection import PlotAxesCollection
from Folder import Folder


folder = Folder(input('Please type the name of the folder you wish to access:'))
    # folder = Folder('General') #USE THIS FOR EASY STARTUP (no user input)
print(folder.display_files())
    #display file names for user to pick from

file = folder.select_file(input('Please type the name of the file you wish to use:'))
    # file = folder.select_file('Schools_DF') #USE THIS FOR EASY STARTUP (no user input)

columns = PlotAxesCollection(pd.read_csv("Resources/CSV/"+folder.folder_name+"/"+file+".csv"))
    #get list of headers in csv file and use them as column names
data = pd.read_csv("Resources/CSV/"+folder.folder_name+"/"+file+".csv", usecols=columns.plot_axes_list)
    #create pandas Dataframe from chosen csv file

app = dash.Dash()
app.layout = html.Div([
    dcc.Dropdown( #creates dropdown menu at top of webpage for user to choose from
        id='demo-dropdown',
        options=columns.plot_axes_list, #get possible column names from headers in chosen csv file
        value=[columns.plot_axes_list[0], columns.plot_axes_list[1]], #use first and second header as defaults
        multi=True #choose more than 1 chart element
    ),

    html.Hr(),
    dcc.Graph(id='display-selected-values'), #create graph

])

@app.callback(
    dash.dependencies.Output('display-selected-values', 'figure'), #update figure object
    [dash.dependencies.Input('demo-dropdown', 'value'), #first choice from dropdown
     dash.dependencies.Input('demo-dropdown', 'value2')]) #second choice from dropdown
def update_output(value,value2):
    fig = px.scatter(data, x=value, y=value2) #use first and second choice from dropdown as x and y axes
    return fig


if __name__ == '__main__':
    app.run_server()
