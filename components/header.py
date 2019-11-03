import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        get_logo(),
        get_header("Company A"),
        html.Br([]),
        get_menu()
    ])

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='https://www.getlivewire.com/wp-content/uploads/2018/10/Your-Logo-here.png', height='80', width='125')
        ], className="ten columns padded"),

    ], className="row gs-header")
    return logo


def get_header(company_name):
    header = html.Div([

        html.Div([
            html.H5(
                company_name)
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header


def get_menu():
    menu = html.Div([

        dcc.Link('Overview   ', href='/overview', className="tab first"),

        dcc.Link('Exposure Summary   ', href='/exposure-summary', className="tab"),

        dcc.Link('EP curves   ', href='/ep-curves', className="tab"),

    ], className="row ")
    return menu