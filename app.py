from flask import Flask, redirect, request, send_from_directory
import os
import json
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/paul/mypro/my_flask/api_files'
ALLOWED_EXTENSIONS = set(['txt'])

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])           
def rest_api():
    return '''Hello guys, I am a Rest API'''

@app.route('/api/v1/<path:path>', methods=["GET"])
def get_file(path):
    '''Download a file
    Usage http://<IP>:5000/api/v1/<filename>
    '''
    if request.method == "GET":
        return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)


@app.route('/api/v1', methods=["POST"])
def post_file():
    lst_of_colors = ['blue', 'red', 'yellow']
    counter = {}

    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        filez = request.files['file']

        # if user does not select file, browser also
        # submit a empty part without filename
        if filez.filename == '':
            print('No selected file')
            return redirect(request.url)

        if filez and allowed_file(filez.filename):
            filename = secure_filename(filez.filename)
            filez.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))

        with open(UPLOAD_FOLDER + '/' + filename, encoding='utf-8', errors='ignore') as obj_file, \
                open(UPLOAD_FOLDER + '/' + "new_poem.txt", "w") as write_file, \
                open(UPLOAD_FOLDER + '/' + "occurrencies.txt", "w") as cntr:
        
            for line in obj_file:
                lst_of_line = line.split()
                for color in lst_of_colors:
                    for word in lst_of_line:
                        if color in word:
                            lst_of_line[lst_of_line.index(word)] = word.replace(color, color.capitalize())
                    
                            if color in counter.keys():
                                counter[color] += 1
                            else:
                                counter[color] = 1    

                write_file.write(" ".join(lst_of_line) + '\n')
            cntr.write(json.dumps(counter, indent=4))

        return '201, Done'

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')
