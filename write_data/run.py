"""Development server.

To launch the server:
    $ virtualenv -p <path to your python> env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ python run.py
"""


from write_data import app

if __name__ == '__main__':

    import logging

    logging.basicConfig(
        filename='error.log', level=logging.DEBUG,
        format='%(asctime)s:%(levelname)s:%(message)s',
        datefmt='%m/%d/%Y %H:%M:%S')
    
    app.run(host='0.0.0.0', debug=True, port=5555)
