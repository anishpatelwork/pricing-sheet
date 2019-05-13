def load_css(app):
    external_css = ["https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css", #responsive
                "https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css", # component layouts
                "https://codepen.io/bcd/pen/KQrXdb.css",] # majority of the styling
    for css in external_css:
        app.css.append_css({"external_url": css})