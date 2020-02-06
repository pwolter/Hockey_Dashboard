import pandas as pd
import plotly.graph_objs as go

# Set the number of decimals (precision) for the dataframe floats
pd.set_option("display.precision", 2)

# read the data into Pandas
PATH = '../../DashboardData/'

top_skaters = pd.read_csv(f'{PATH}skaters.csv')
top_goalies = pd.read_csv(f'{PATH}goalies.csv')

player_x = top_skaters.sort_values('Goals Per Game', ascending=False)\
            .head(10)['Player Name'].values.tolist()
player_y = top_skaters.sort_values('Goals Per Game', ascending=False)\
            .head(10)['Goals Per Game'].values.tolist()

goalie_x = top_goalies.sort_values('Avg Save Percentage', ascending=False)\
            .head(10)['Player Name'].values.tolist()
goalie_y = top_goalies.sort_values('Avg Save Percentage', ascending=False)\
            .head(10)['Avg Save Percentage'].values.tolist()

team_skaters = top_skaters.sort_values('Goals Per Game', ascending=False)\
            .head(10)['Team Name'].values.tolist()

team_goalies = top_goalies.sort_values('Avg Save Percentage', ascending=False)\
            .head(10)['Team Name'].values.tolist()

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies
    # as a line chart
    graph_one = []

    graph_one.append(
      go.Bar(
      x = player_x,
      y = player_y,
      hovertext = team_skaters
      )
    )

    layout_one = dict(title = 'Top 10 Players by Goals per Game (GPG)',
                xaxis = dict(title = 'Player Name'),
                yaxis = dict(title = 'Goals per Game'),
                )

    # second chart plots ararble land for 2015 as a bar chart
    graph_two = []

    graph_two.append(
      go.Bar(
      x = goalie_x,
      y = goalie_y,
      hovertext = team_goalies
      )
    )

    layout_two = dict(title = 'Top 10 Goalies vy Avg Save Percentage',
                xaxis = dict(title = 'Player Name',),
                yaxis = dict(title = 'Avg Save Percentage'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Scatter(
      x = [5, 4, 3, 2, 1, 0],
      y = [0, 2, 4, 6, 8, 10],
      mode = 'lines'
      )
    )

    layout_three = dict(title = 'Chart Three',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label')
                       )

# fourth chart shows rural population vs arable land
    graph_four = []

    graph_four.append(
      go.Scatter(
      x = [20, 40, 60, 80],
      y = [10, 20, 30, 40],
      mode = 'markers'
      )
    )

    layout_four = dict(title = 'Chart Four',
                xaxis = dict(title = 'x-axis label'),
                yaxis = dict(title = 'y-axis label'),
                )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
