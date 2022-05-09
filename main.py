from website import create_app

app = create_app()

if __name__ == '__main__': # we are only executing this when we run the website
    app.run(debug=True) # this starts up a web server
    # debug = True will refresh the web server whenever you make a change