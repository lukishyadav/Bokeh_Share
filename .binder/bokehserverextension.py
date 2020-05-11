from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the bokeh-app directory with bokeh server"""
    Popen(["bokeh", "serve", "bokeh-app", "--websocket-max-message-size=500000000","--allow-websocket-origin=*"])
