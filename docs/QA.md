Q: 403 forbidden

A: check conf file in apache2-conf directory. The notes.conf file has most updated content for the latest apache server version, which shouldn't incur problems.


Q: WSGISciptAlias undefined or ...

A: sudo apt-get install libapache2-mod-wsgi


Q: ImportError: No module named app

A: Config path to environment


Q: Access Denied, Address in use, no literal '...'

A: In app.wsgi, don't add the line: "application.run(debug=True)"
   In app.py, it's

   ```python
def run_app():
    #...
    app.run(debug=True)

if __name__ == '__main__':
        run_app()
   ```