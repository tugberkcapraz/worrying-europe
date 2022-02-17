import pandas as pd
from chart_studio import plotly
from plotly.graph_objs import *
import numpy as np


plotly.sign_in('tugberkcapraz', 'yqgaWSu0i73M38RgBPrB')


# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`


def cleaner():
    link = "./data/solikris.dta"
    reader = pd.read_stata(link, iterator=True)

    df_num = reader.read(convert_categoricals=False)
    df_str = pd.read_stata(link)

    col_names = ["Country", "v_41", "v_42", "v_43", "v_44"]
    df = pd.DataFrame({"Country": df_str.Country,
                       "Climate": df_num.v_41,
                       "Terror": df_num.v_42,
                       "Covid": df_num.v_43,
                       "Economy": df_num.v_44})

    for i in df.columns[1:]:
        df[i] = df[i].map(lambda x: np.NaN if x > 5 else x)

    df.dropna(inplace=True)

    agg_df = df.groupby("Country")[df.columns[1:]].mean().reset_index()
    return agg_df


def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    agg_df = cleaner()
    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart
    ###-------------------------#####
    country_names = agg_df.Country
    z_Climate = agg_df.Climate
    z_Terror = agg_df.Terror
    z_Covid = agg_df.Covid
    z_Economy = agg_df.Economy


    # second chart plots ararble land for 2015 as a bar chart
    trace1 = {
        "geo": "geo",
        "type": "choropleth",
        "z": z_Climate,
        "showscale": True,
        "locationmode": "country names",
        "locations": country_names,
        "autocolorscale": True
    }
    data_one = Data([trace1])
    layout_one = {
        "geo": dict(scope="europe", domain={
            "x": [0, 1],
            "y": [0, 1]
        }, lataxis={"range": [35.0, 70.0]}, lonaxis={"range": [-9.0, 38.0]}, showland=True,
                    landcolor="rgb(229, 229, 229)", showframe=True, projection={"type": "mercator"}, resolution=50,
                    countrycolor="rgb(255, 0, 255)", coastlinecolor="rgb(0, 255, 255)", showcoastlines=True),
        "title": "Concerns About Climate Change <br> in European Countries",
        "legend": {"traceorder": "reversed"}
    }
    fig1 = Figure(data=data_one, layout=layout_one)

    # second chart plots ararble land for 2015 as a bar chart
    trace2 = {
        "geo": "geo",
        "type": "choropleth",
        "z": z_Terror,
        "showscale": True,
        "locationmode": "country names",
        "locations": country_names,
        "autocolorscale": True
    }
    data_two = Data([trace2])
    layout_two = {
        "geo": dict(scope="europe", domain={
            "x": [0, 1],
            "y": [0, 1]
        }, lataxis={"range": [35.0, 70.0]}, lonaxis={"range": [-9.0, 38.0]}, showland=True,
                    landcolor="rgb(229, 229, 229)", showframe=True, projection={"type": "mercator"}, resolution=50,
                    countrycolor="rgb(255, 0, 255)", coastlinecolor="rgb(0, 255, 255)", showcoastlines=True),
        "title": "Concerns About Global Terrorism <br> in European Countries",
        "legend": {"traceorder": "reversed"}
    }
    fig2 = Figure(data=data_two, layout=layout_two)
    # THIRD
    # second chart plots ararble land for 2015 as a bar chart
    trace3 = {
        "geo": "geo",
        "type": "choropleth",
        "z": z_Covid,
        "showscale": True,
        "locationmode": "country names",
        "locations": country_names,
        "autocolorscale": True
    }
    data_three = Data([trace3])
    layout_three = {
        "geo": dict(scope="europe", domain={
            "x": [0, 1],
            "y": [0, 1]
        }, lataxis={"range": [35.0, 70.0]}, lonaxis={"range": [-9.0, 38.0]}, showland=True,
                    landcolor="rgb(229, 229, 229)", showframe=True, projection={"type": "mercator"}, resolution=50,
                    countrycolor="rgb(255, 0, 255)", coastlinecolor="rgb(0, 255, 255)", showcoastlines=True),
        "title": "Concerns About Covid-19 <br> in European Countries",
        "legend": {"traceorder": "reversed"}
    }
    fig3 = Figure(data=data_three, layout=layout_three)

    ### Noch einmal
    trace4 = {
        "geo": "geo",
        "type": "choropleth",
        "z": z_Economy,
        "showscale": True,
        "locationmode": "country names",
        "locations": country_names,
        "autocolorscale": True
    }
    data_four = Data([trace4])
    layout_four = {
        "geo": dict(scope="europe", domain={
            "x": [0, 1],
            "y": [0, 1]
        }, lataxis={"range": [35.0, 70.0]}, lonaxis={"range": [-9.0, 38.0]}, showland=True,
                    landcolor="rgb(229, 229, 229)", showframe=True, projection={"type": "mercator"}, resolution=50,
                    countrycolor="rgb(255, 0, 255)", coastlinecolor="rgb(0, 255, 255)", showcoastlines=True),
        "title": "Concerns  About Economic Downturn <br> in European Countries",
        "legend": {"traceorder": "reversed"}
    }
    fig4 = Figure(data=data_four, layout=layout_four)
    # append all charts to the figures list
    figures = []
    #figures.append(dict(data=graph_one, layout=layout_one))
    #figures.append(dict(data=graph_two, layout=layout_two))
    #figures.append(dict(data=graph_three, layout=layout_three))
    #figures.append(dict(data=graph_four, layout=layout_four))

    figures.append(fig1)
    figures.append(fig2)
    figures.append(fig3)
    figures.append(fig4)

    return figures
