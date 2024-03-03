import os

from flask import Flask, render_template, flash, request, redirect, url_for, session
from werkzeug.utils import secure_filename
from . import gen_report

ALLOWED_EXTENSIONS = {'fasta'}



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config['UPLOAD_FOLDER'] = './flaskr/person_data'

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def index():
        return render_template('index.html.jinja')
    

    @app.route('/space')
    def start_space():
        return render_template('space_start.html.jinja')
    
    @app.route('/fasta-upload')
    def fastaUpload():
        return render_template('fasta_upload.html.jinja')
    
    
    
    @app.route('/earth-upload')
    def earthUpload():
        return render_template('fasta_upload.html.jinja', earth="true")

    @app.route('/post-earth', methods=['POST'])
    def postEarth():
        if request.method == 'POST':
            request_data = request.get_json()
        
            if request_data:
                if 'diet_type' in request_data:
                    session['diet'] = request_data['diet_type']
        
        return redirect(url_for('earthUpload'))
    
    @app.route('/earth', methods=['GET'])
    def start_earth():
        return render_template('earth_start.html.jinja')
    
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    @app.route('/post-fasta', methods=['POST'])
    def postFasta():
        if request.method == 'POST':
        # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # If the user does not select a file, the browser submits an
            # empty file without a filename.
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(os.path.normpath(app.config['UPLOAD_FOLDER']), filename))
                return render_template('mission_length.html.jinja')

    @app.route('/randomized')
    def randomPage():
        return render_template('randomized.html.jinja')
    

    

    @app.route('/earth-report')
    def earth_report():
        warnings_dict = gen_report.gen_earth()
        return render_template('earth_report.html.jinja', warnings=warnings_dict)
    
    @app.route('/space-report')
    def space_report():
        total = gen_report.gen_space(session['astro_ct'])
        return render_template('space_report.html.jinja', total=total)

    @app.route('/space-charts')
    def space_charts():
        astros = gen_report.gen_charts()
        return render_template('space_report.html.jinja', astros=astros)

    return app