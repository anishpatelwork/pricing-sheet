import dash_core_components as dcc

def TextArea(text, name):
    return dcc.Textarea(
        id = name,
        placeholder='Enter a value...',
        value=text,
        style={'width': '100%'}
)