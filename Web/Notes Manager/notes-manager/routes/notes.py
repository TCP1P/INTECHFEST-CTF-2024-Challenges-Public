from flask import *
from app import app, db

from models.User import User
from models.Note import Note

from uuid import uuid4

@app.route('/notes', methods=['GET', 'POST'])
def notes():
    notes = Note.query.filter_by(user_id=session['uid']).all()
    if g.user.role == 'admin':
        notes = Note.query.all()

    return render_template('notes/index.html', title='Notes', notes=notes)

@app.route('/notes/create', methods=['GET', 'POST'])
def notes_create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        note_password = request.form['note_password']

        if not title:
            return redirect('/notes')
        
        if not content:
            return redirect('/notes')
        
        if len(title) > 100 or len(content) > 1000:
            return redirect('/notes')
        
        note = Note(
            id=str(uuid4()),
            title=title,
            content=content,
            password=note_password,
            user_id=session['uid']
        )

        db.session.add(note)
        db.session.commit()
    
        return redirect('/notes/' + note.id)

    return render_template('notes/create.html', title='Create Note')

@app.route('/notes/<note_id>', methods=['GET'])
def notes_view(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if not note:
        return jsonify({'success': False, 'message': 'Note not found'}), 404

    return render_template('notes/view.html', title='Notes', note=note)

@app.route('/notes/<note_id>/check-password', methods=['POST'])
def notes_check_password(note_id):
    note = Note.query.filter_by(id=note_id).first()
    if not note:
        return jsonify({'success': False, 'message': 'Note not found'}), 404

    if not note.password:
        return jsonify({'success': True, 'message': 'Note not password protected'}), 200

    if not request.form['password'] == note.password:
        return jsonify({'success': False, 'message': 'Incorrect password'}), 400

    return jsonify({'success': True, 'message': 'Correct password'}), 200