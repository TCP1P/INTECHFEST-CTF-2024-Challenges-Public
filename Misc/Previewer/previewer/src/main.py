import os
import uuid
import subprocess
from flask import *

import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            code = request.form['code'].replace("'", "")

            filename = str(uuid.uuid4())
            with open(f'/tmp/{filename}.ui', 'w') as f:
                f.write(code)
            
            error = subprocess.Popen(['pyuic5', f'/tmp/{filename}.ui', '-o', f'/tmp/{filename}.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stderr.read().decode('utf-8')
            if error:
                return render_template('index.html', error='Something went wrong while converting UI to Python code.')

            with open(f'/tmp/{filename}.py', 'r') as r:
                code = r.read()
                code += f"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    def screenshot():
        screen = QtWidgets.QApplication.primaryScreen()
        screenshot = screen.grabWindow(MainWindow.winId())
        screenshot.save('/tmp/{filename}.png', 'png')

        QtCore.QCoreApplication.quit()

    QtCore.QTimer.singleShot(1000, screenshot)

    sys.exit(app.exec_())
        """
                
                with open(f'/tmp/{filename}.py', 'w') as w:
                    w.write(code)

            error = subprocess.Popen(['python3', f'/tmp/{filename}.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stderr.read().decode('utf-8')
            if error:
                return render_template('index.html', error='Something went wrong while running the Python code.')
            
            os.system(f'cp /tmp/{filename}.png /app/src/static/results/{filename}.png')

            os.system(f'rm /tmp/{filename}.ui')
            os.system(f'rm /tmp/{filename}.py')
            os.system(f'rm /tmp/{filename}.png')

            return redirect(f'/view?id={filename}')
        except Exception as e:
            return render_template('index.html', error=e)
    
    return render_template('index.html')

@app.route('/view', methods=['GET'])
def view():
    id = request.args.get('id')
    return render_template('index.html', filename=id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)