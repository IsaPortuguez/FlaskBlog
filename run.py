from flaskblog import create_app

app = create_app()

#debug=True is used when we crated an app
if __name__ == '__main__':
    app.run(debug=True)



#if __name__ == '__main__':
    #app.run()

#python -m flask --app run.py --debug run

