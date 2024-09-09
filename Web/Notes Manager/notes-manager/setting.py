from flask import *
from app import app, db, sha256

from models.User import User

@app.route('/setting')
def setting():
    return render_template('setting.html', title='Setting')

@app.route('/setting/dark-mode', methods=['GET', 'POST'])
def dark_mode():
    if request.method == 'GET':
        return jsonify({'success': True, 'state': session['darkMode'] if 'darkMode' in session else 'false'}), 200
    
    session['darkMode'] = request.form['state']
    return jsonify({'success': True, 'message': 'Dark mode updated'}), 200

@app.route('/setting/update-profile', methods=['POST'])
def update_profile():
    data = request.form.to_dict()

    result = {}

    try:
        user = User.query.filter_by(id=session['uid']).first()
        if not user:
            return jsonify({'success': False, 'message': 'User not found'}), 404
        
        for key in user.__dict__.keys():
            result[key] = str(user.__dict__[key])
            if key in data:
                if key == 'password':
                    user.password = sha256(data[key])
                else:
                    if data[key] == '':
                        continue
                    setattr(user, key, data[key])
            
    except Exception as e:
        print(e)

    db.session.commit()
    return jsonify({'success': True, 'message': 'Profile updated', 'data': result}), 200

@app.route('/setting/change-password', methods=['POST'])
def update_password():
    data = request.form

    user = User.query.filter_by(id=session['uid']).first()
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
    if not data['newPassword'] == data['confirmPassword']:
        return jsonify({'success': False, 'message': 'New password and confirm password not match'}), 400
    
    if not sha256(data['oldPassword']) == user.password:
        return jsonify({'success': False, 'message': 'Old password is incorrect'}), 400
    
    user.password = sha256(data['newPassword'])
    db.session.commit()

    return jsonify({'success': True, 'message': 'Password updated'}), 200