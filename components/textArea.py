import dash_core_components as dcc
import dash_html_components as html

# def TextArea(text, name):
#     return dcc.Textarea(
#         id = name,
#         placeholder='Enter a value...',
#         value=text,
#         className='text-area',
#         draggable=False,
#         disabled=True,
#         rows=8
# )

def TextArea(text, name):
    return html.P(children=text)