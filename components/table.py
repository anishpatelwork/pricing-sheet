import dash_html_components as html

def Table(df, display_header = False, print_index = False):
    ''' Return a dash definition of an HTML table for a Pandas dataframe '''
    table = []
    header = []
    if display_header == True:
        a = []
        if print_index == True:
            a.append(html.Th(df.index.name))
        [a.append(html.Th(col)) for col in df.columns]
        header.append(html.Tr(a))
    
    body = []
    for index, row in df.iterrows():
        html_row = []
        if print_index == True:
            html_row.append(html.Td(index))
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        body.append(html.Tr(html_row))
    
    table.append(html.Thead(
        header
    ))
    table.append(html.Tbody(
        body
    ))

    return html.Div(children=html.Table(table, className="highlight"), className="col s11")
    