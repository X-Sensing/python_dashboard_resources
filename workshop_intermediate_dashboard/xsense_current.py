###################################################################################################
# IMPORTS
###################################################################################################
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output,State
import dash_auth
import numpy as np
import plotly.graph_objs as go


###################################################################################################
# Helper functions
###################################################################################################

def make_dash_option_list(name_list,  sort=False):
    '''
    Takes in a list of of categorical values and returns a unique list of dictionaries
    in the format required by dash-components
    '''
    if sort:
        s = pd.Series(name_list).sort_values(ascending=True).unique()
    else:
        s = pd.Series(name_list).unique()
    op_list = []
    for column_name in s:
        op_list.append({'label':str(column_name), 'value':str(column_name)})
    return op_list


def transform_value(value):
    return int(10 ** value)


###################################################################################################
# READ IN DATA and do some formatting
###################################################################################################


data_file = '../data/df_random_distributions.pickle'
df = pd.read_pickle(data_file)

# We want to obscure the columns names but keep the mappings
list_of_column_names = df.columns.tolist()
obscured_name_list = ['Mystery_'+str(i+1) for i, col in enumerate(list_of_column_names)]
distribution_options =	make_dash_option_list(obscured_name_list,  sort=False)

# Keep the mapping between obscured names and true names
distribution_name_map = dict(zip(list_of_column_names, obscured_name_list))

# Change the column names in the data-frame to the obscured ones
df.rename(columns=distribution_name_map, inplace=True)


# We will need a logarithmic scale and tick mark labels for changes the samples sizes with a slider:
max_sample_size = len(df)-1
log_range_max = int(np.log10(max_sample_size)) + 1
slider_marks = {i: {'label':str(10 ** i), 'style': {'color': 'white'}} for i in range(log_range_max)}


#############################################################################################################
# PASSWORDS should not be in the code (external file/database or hidden in environment variables are options)
##############################################################################################################

#VALID_USERNAME_PASSOWORD_PAIRS = [
#    ['user1','pass1'],
#    ['user2', 'pass2'],
#    ]


#app = dash.Dash('auth') ;
#auth = dash_auth.BasicAuth(app, VALID_USERNAME_PASSOWORD_PAIRS)
##############################################################################################################

app = dash.Dash()
app.title = 'Xsense workshop final'

###################################################################################################
# Style and colors
###################################################################################################

background_color = "#333333"

app.css.append_css({'external_url':'https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css'})
app.css.append_css({'external_url':'https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.0.0-beta/css/bootstrap.css'})
app.css.config.serve_locally = False


#################################################################################################################
# WARNING THIS DATAFRAME MUST NOT BE MODIFIED AFTER THIS POINT. FILTERING ETC NEEDS TO BE DONE ON A COPY OF THIS
#################################################################################################################

def make_layout():
    # Outermost open
    layout = html.Div(children=[


            ###################################################################################################
            #  ROW 1 Heading Section (white on black)
            ###################################################################################################
            html.Div(children=[
                html.H1(children='Xsensing Dashboard Demo',
                        className='mx-auto  text-white'
                        ),
            ],
            style={'background-color':  background_color},
            className='row rounded'
            ),
            #--------------------------------------------------------------------------------------------------



            ###################################################################################################
            #  ROW 2 (Set of Components Section)
            ###################################################################################################
            html.Div(children=[
                #%%%%%%%%%%%%%%%%%% START COLUMN 1 row 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                # COMPONENT 1 (heading)
                html.Div(children=[
                    html.H5(children='Mystery Distribution 1',
                            className='mx-auto  text-white'),
                    # COMPONENT 2 (dropdown)
                    html.Div(children=[
                        dcc.Dropdown(
                            id='Mystery_1',
                            options=distribution_options,
                            value=distribution_options[0]['label'],
                            className='text-center'
                        ),
                    ],
                    className = 'text-center col-xs-12 p-4 mx-auto',
                    ),


                    # COMPONENT 3 (rangeSlder)
                    html.Div(children=[
                        dcc.Slider(
                            id = 'sample_slider_1',
                            marks = slider_marks,
                            max = np.log10(max_sample_size),
                            value = np.log10(max_sample_size),
                            step = 0.1,
                            updatemode = "drag",
                            className = 'text-white',


                        )
                    ],
                    className = 'text-center col-xs-12 p-4 mx-auto',
                    ),
                    html.H5(children='Raster sample size',
                            className='mx-auto  text-white')
                ],
                # Column layout, width and behaviour is specified using Bootstrap CSS
                className='col-md-6 text-center col-xs-12 p-3',
                ),
                #%%%%%%%%%%%%%%%%%%%%% END COLUMN 1 (row 2) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


                #### COPY FIRST COLUMN AND EDIT
                #%%%%%%%%%%%%%%%%%%%%% START COLUMN 2 (row 2) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                html.Div(children=[
                    html.H5(children='Mystery Distribution 2',
                            className='mx-auto  text-white'),
                    # COMPONENT 2 (dropdown)
                    html.Div(children=[
                        dcc.Dropdown(
                            id='Mystery_2',
                            options=distribution_options,
                            value=distribution_options[1]['label'],
                            className='text-center'
                        ),
                    ],
                        className='text-center p-4 mx-auto',
                    ),

                    # COMPONENT 3 (rangeSlder)
                    html.Div(children=[
                        dcc.Slider(
                            id='sample_slider_2',
                            marks=slider_marks,
                            max=np.log10(max_sample_size),
                            value=np.log10(max_sample_size),
                            step=0.1,
                            updatemode="drag",
                            className='text-white',

                        )
                    ],
                        className='text-center p-4 mx-auto',
                    ),
                    html.H5(children='Raster sample size',
                            className='mx-auto  text-white')
                ],
                    # Column layout, width and behaviour is specified using Bootstrap CSS
                    className='col-md-6 text-center col-xs-12 p-3',
                ),
                # %%%%%%%%%%%%%%%%%%%%% END COLUMN 2  row 2 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




            ],
            style={'background-color': background_color},
            className='row rounded'
            ),
            #--------------------------------------------------------------------------------------------------




            ###################################################################################################
            #  ROW 3 (Distribution graph)
            ###################################################################################################

            html.Div(
                dcc.Graph(
                    id='distribution_graph_id',
                    style={'height': 600},
                        ),
                ),
            #--------------------------------------------------------------------------------------------------



    # Outermost close
    ]

    )
    return layout



app.layout = make_layout()


#############################################################################################################
# Callbacks
##############################################################################################################



@app.callback(
Output('distribution_graph_id', 'figure'),
[
Input('Mystery_1', 'value'),
Input('sample_slider_1', 'value'),
Input('Mystery_2', 'value'),
Input('sample_slider_2', 'value'),
]
)
def t_by_eye(name_sample_1, sample_size_1, name_sample_2, sample_size_2):
    x_1 = df[name_sample_1].sample(transform_value(sample_size_1)).values
    x_2 = df[name_sample_2].sample(transform_value(sample_size_2)).values

    layout = {
        'yaxis': dict(title='Density(X)'),
        'xaxis': dict(title='X'),
        'barmode': 'overlay',
        'bargap': 0,
        'bargroupgap': 0,
    }

    data_1 = go.Histogram(
        x=x_1,
        histnorm='probability',
        opacity=0.4,
        name=name_sample_1,
        bingroup='a',
        xbins=dict(
            start=0.0,
            end=100,
        ),

    )

    data_2 = go.Histogram(
        x=x_2,
        histnorm='probability',
        opacity=0.4,
        name=name_sample_2,
        bingroup='a',
        xbins=dict(
            start=0.0,
            end=100,
        ),
    )
    data = [data_1, data_2]
    figure = {'data': data, 'layout': layout}
    return figure


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8000)







