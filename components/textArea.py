import dash_core_components as dcc

def TextArea(text, name):
    return dcc.Textarea(
        id = name,
        placeholder='Enter a value...',
        value=text,
        className='text-area',
        draggable='false',
        disabled='true',
        rows=8
)