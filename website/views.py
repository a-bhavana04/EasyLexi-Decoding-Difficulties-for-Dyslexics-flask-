import os
from flask import Blueprint, render_template,request,flash,redirect,url_for
from flask_login import login_required, current_user
from .models import Post, User
from .import db
from . import ALLOWED_EXTENSIONS, UPLOAD_FOLDER
from werkzeug.utils import secure_filename
import PyPDF2
from textblob import Word

def punctuation_check(word):
    flag=0
    if (len(word)>1) and (word[-1].isalnum()):
        flag=0
    elif (len(word)>1):
        flag=1

    if flag==0:
        return ""
    else:
        return word[-1]

def correct_word_spelling(word):
    word = Word(word)
    result = word.spellcheck()
    if result[0][0] != word:
        return result[0][0]
        '''print("Did you mean",result[0][0],"?")'''
    else:
        return word



views = Blueprint("views", __name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@views.route("/files", methods=['GET', 'POST'])
def files():
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect("/files")
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            x = os.path.join(UPLOAD_FOLDER, filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            fileObj = open(x, 'rb')
            pdfReader = PyPDF2.PdfFileReader(fileObj,strict=False)
            n = pdfReader.numPages
            dataStr = ''
            WordsL = []
            tb = None

            for eachPage in range(0, n):
                pageObj = pdfReader.getPage(eachPage)
                dataStr = pageObj.extractText()
                WordsL = dataStr.split(sep=' ')
                correctedWordsL = []
                for eachWord in WordsL:
                    correctedWord = correct_word_spelling(eachWord)
                    print(correctedWord)
                    if ((len(correctedWord)>0) and (correctedWord[-1].isalnum()==True)):
                        p = punctuation_check(eachWord)
                        correctedWord=correctedWord+p

                    correctedWordsL.append(correctedWord)
                correctedStr = ' '.join(correctedWordsL)
                print(correctedStr)
            return render_template("crt.html", text = correctedStr)
            
    return render_template("files.html")

@views.route("/")
def all():
    return render_template("index.html")

@views.route("/spToText")
def spToText():
    return render_template("spToText.html")

@views.route("/textToSpeech")
def textToSpeech():
    return render_template("textToSpeech.html")


@views.route("/home")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)

@views.route("/createpost", methods=['GET', 'POST'])
@login_required
def createpost():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('createpost.html', user=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    print(post)
    if not post:
        flash("Post does not exist.", category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('views.home'))

@views.route("/post/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    posts = Post.query.filter_by(author=user.id).all()
    return render_template("post.html", user=current_user, posts=posts, username=username)