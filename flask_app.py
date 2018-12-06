
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

# Creates an instance of class Flask called app
app = Flask(__name__)
app.config["DEBUG"] = True

# Set up connection to database.
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="acklandobjects", password="acklandpassword", hostname="acklandobjects.mysql.pythonanywhere-services.com", databasename="acklandobjects$objects",)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# This is the main page.
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST': # This block should only be entered when a form is submitted
        user_number = request.form.get('user_number')

        if user_number == "12":
            return redirect(url_for('number12'))
        if user_number == "13":
            return redirect(url_for('number13'))
        if user_number == "14":
            return redirect(url_for('number14'))
        if user_number == "15":
            return redirect(url_for('number15'))
        if user_number == "16":
            return redirect(url_for('number16'))
        if user_number == "17":
            return redirect(url_for('number17'))
        else:
            return redirect(url_for('wrongnumber'))

    return render_template('main_page.html')

# Redirect to wrong number page.
@app.route('/wrongnumber', methods=['GET','POST'])
def wrongnumber():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('wrongnumber.html')

# Here starts object number 12.
# Creates a database table to save user_input_12_1
class Comment12_1(db.Model):

    __tablename__ = "input_12_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the first page for object 12 and gets user input.
@app.route('/number12', methods=['GET', 'POST'])
def number12():
    if request.method == 'POST':
        user_input_12_1 = request.form.get('user_input_12_1')
        comment = Comment12_1(content=request.form['user_input_12_1'])
        db.session.add(comment)
        db.session.commit()

        user_input_12_1 = user_input_12_1.lower().rstrip(".").split()
        keywords_12_1 = ["figures", "crouching", "people", "colors", "smudges", "mess", "messy", "confusing", "hard",
                         "tell", "color","shapes", "shadow", "charcoal", "brushstrokes", "bold", "brushy", "blue"]
        if any(x in user_input_12_1 for x in keywords_12_1):
            return redirect(url_for('number12_1'))
        else:
            return redirect(url_for('number12_no'))

    return render_template('number12.html')


# Creates a database table to save user_input_12_2
class Comment12_2(db.Model):

    __tablename__ = "input_12_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 12 and gets user input.
@app.route('/number12_1', methods=['GET','POST'])
def number12_1():
    if request.method == 'POST':
        user_input_12_2 = request.form.get('user_input_12_2')
        comment = Comment12_2(content=request.form['user_input_12_2'])
        db.session.add(comment)
        db.session.commit()

        user_input_12_2 = user_input_12_2.lower().rstrip(".").split()
        keywords_12_2 = ["rough", "unnatural", "lumpy", "sandpaper", "bumps", "bumpy", "white", "uneven", "course",
                         "ruts", "peeling", "abrasive", "blocky", "mushy", "plaster"]
        if any(x in user_input_12_2 for x in keywords_12_2):
            return redirect(url_for('number12_2'))
        else:
            return redirect(url_for('number12_no'))

    return render_template('number12_1.html')

# Creates a database table to save user_input_12_3
class Comment12_3(db.Model):

    __tablename__ = "input_12_3"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the third page for object 12 and gets user input.
@app.route('/number12_2', methods=['GET','POST'])
def number12_2():
    if request.method == 'POST':
        user_input_12_3 = request.form.get('user_input_12_3')
        comment = Comment12_3(content=request.form['user_input_12_3'])
        db.session.add(comment)
        db.session.commit()

        user_input_12_3 = user_input_12_3.lower().rstrip(".").split()
        keywords_12_3 = ["reserved", "sad", "tense", "nervous", "scared",
                        "hunched", "escape", "sulky", "defiant", "brooding",
                        "crouched", "angry", "pensive", "mad", "closed", "off",
                        "annoyed", "frustrated", "impatient", "stiff", "still",
                        "unmoving", "angry"]
        if any(x in user_input_12_3 for x in keywords_12_3):
            return redirect(url_for('number12_3'))
        else:
            return redirect(url_for('number12_no'))

    return render_template('number12_2.html')

# This is the final page for object 12 and redirects to main page.
@app.route('/number12_3', methods=['GET','POST'])
def number12_3():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number12_3.html')


# This is the wildcard page for object 12.
@app.route('/number12_no', methods=['GET', 'POST'])
def number12_no():
    if request.method == 'POST':

        user_input_12_no = request.form.get('user_input_12_no')
        user_input_12_no = user_input_12_no.lower().rstrip(".").split()

        keywords_12_1 = ["figures", "crouching", "people", "colors", "smudges", "mess", "messy", "confusing", "hard",
                         "tell", "color", "shapes", "shadow", "charcoal", "brushstrokes", "bold", "brushy", "blue"]
        keywords_12_2 = ["rough", "unnatural", "lumpy", "sandpaper", "bumps", "bumpy", "white", "uneven", "course",
                         "ruts", "peeling", "abrasive", "blocky", "mushy", "plaster"]
        keywords_12_3 = ["reserved", "sad", "tense", "nervous", "scared", "hunched", "escape", "sulky", "defiant", "brooding", "crouched",
                         "angry", "pensive", "mad", "closed", "off", "annoyed", "frustrated", "impatient", "stiff",
                         "still", "unmoving"]

        if any(x in user_input_12_no for x in keywords_12_1):
            return redirect(url_for('number12_1'))

        if any(x in user_input_12_no for x in keywords_12_2):
            return redirect(url_for('number12_2'))

        if any(x in user_input_12_no for x in keywords_12_3):
            return redirect(url_for('number12_3'))

        else:
            return redirect(url_for('number12_no'))

    return render_template('number12_no.html')

# Here starts object number 13.

# Creates a database table to save user_input_13_1
class Comment13_1(db.Model):

    __tablename__ = "input_13_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the first page for object 13 and gets user input.
@app.route('/number13', methods=['GET', 'POST'])
def number13():
    if request.method == 'POST':
        user_input_13_1 = request.form.get('user_input_13_1')
        comment = Comment13_1(content=request.form['user_input_13_1'])
        db.session.add(comment)
        db.session.commit()

        user_input_13_1 = user_input_13_1.lower().rstrip(".").split()
        keywords_13_1 = ["robes", "eyes", "clothing", "headdress", "jewelry", "face", "head", "earrings", "necklace", "objects",
                         "staring", "drapery", "arms", "hands", "gesture", "utensils", "instruments", "weaving"]
        if any(x in user_input_13_1 for x in keywords_13_1):
            return redirect(url_for('number13_1'))
        else:
            return redirect(url_for('number13_no'))

    return render_template('number13.html')

# Creates a database table to save user_input_13_2
class Comment13_2(db.Model):

    __tablename__ = "input_13_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 13 and gets user input.
@app.route('/number13_1', methods=['GET','POST'])
def number13_1():
    if request.method == 'POST':
        user_input_13_2 = request.form.get('user_input_13_2')
        comment = Comment13_2(content=request.form['user_input_13_2'])
        db.session.add(comment)
        db.session.commit()
        user_input_13_2 = user_input_13_2.lower().rstrip(".").split()
        keywords_13_2 = ["stone", "rock", "marble", "sandstone", "limestone", "broken", "damaged", "relief", "carving",
                         "three", "dimensional", "three-dimensional"]
        if any(x in user_input_13_2 for x in keywords_13_2):
            return redirect(url_for('number13_2'))
        else:
            return redirect(url_for('number13_no'))

    return render_template('number13_1.html')

# Creates a database table to save user_input_13_3
class Comment13_3(db.Model):

    __tablename__ = "input_13_3"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the third page for object 13 and gets user input.
@app.route('/number13_2', methods=['GET','POST'])
def number13_2():
    if request.method == 'POST':
        user_input_13_3 = request.form.get('user_input_13_3')
        comment = Comment13_3(content=request.form['user_input_13_3'])
        db.session.add(comment)
        db.session.commit()
        user_input_13_3 = user_input_13_3.lower().rstrip(".").split()
        keywords_13_3 = ["beautiful", "wealthy", "rich", "wife", "lineage", "important", "significant", "modest",
                         "humble", "maternal", "pretty", "kind"]
        if any(x in user_input_13_3 for x in keywords_13_3):
            return redirect(url_for('number13_3'))
        else:
            return redirect(url_for('number13_no'))

    return render_template('number13_2.html')

# This is the final page for object 13 and redirects to main page.
@app.route('/number13_3', methods=['GET','POST'])
def number13_3():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number13_3.html')

# This is the wild card page for object 13.
@app.route('/number13_no', methods=['GET', 'POST'])
def number13_no():
    if request.method == 'POST':

        user_input_13_no = request.form.get('user_input_13_no')
        user_input_13_no = user_input_13_no.lower().rstrip(".").split()

        keywords_13_1 = ["robes", "eyes", "clothing", "headdress", "jewelry", "face", "head", "earrings", "necklace", "objects",
                         "staring", "drapery", "arms", "hands", "gesture", "utensils", "instruments", "weaving"]
        keywords_13_2 = ["stone", "rock", "marble", "sandstone", "limestone", "broken", "damaged", "relief", "carving",
                         "three", "dimensional", "three-dimensional"]
        keywords_13_3 = ["beautiful", "wealthy", "rich", "wife", "lineage", "important", "significant", "modest",
                         "humble", "maternal", "pretty", "kind"]
        if any(x in user_input_13_no for x in keywords_13_1):
            return redirect(url_for('number13_1'))

        if any(x in user_input_13_no for x in keywords_13_2):
            return redirect(url_for('number13_2'))

        if any(x in user_input_13_no for x in keywords_13_3):
            return redirect(url_for('number13_3'))

        else:
            return redirect(url_for('number13_no'))

    return render_template('number13_no.html')


# Here starts object number 14.

# Creates a database table to save user_input_14_1
class Comment14_1(db.Model):

    __tablename__ = "input_14_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the first page for object 14 and gets user input.
@app.route('/number14', methods=['GET', 'POST'])
def number14():
    if request.method == 'POST':
        user_input_14_1 = request.form.get('user_input_14_1')
        comment = Comment14_1(content=request.form['user_input_14_1'])
        db.session.add(comment)
        db.session.commit()
        user_input_14_1 = user_input_14_1.lower().rstrip(".").split()
        keywords_14_1 = ["wild", "chaos", "violent", "scary", "torn", "stormy", "spooky", "destroyed", "desolate", "abandoned", "swirly",
                         "swirling", "chaotic", "dark", "bright", "bleak", "destruction", "rubble"]
        if any(x in user_input_14_1 for x in keywords_14_1):
            return redirect(url_for('number14_1'))
        else:
            return redirect(url_for('number14_no'))

    return render_template('number14.html')

# Creates a database table to save user_input_14_2
class Comment14_2(db.Model):

    __tablename__ = "input_14_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 14 and gets user input.
@app.route('/number14_1', methods=['GET','POST'])
def number14_1():
    if request.method == 'POST':
        user_input_14_2 = request.form.get('user_input_14_2')
        comment = Comment14_2(content=request.form['user_input_14_2'])
        db.session.add(comment)
        db.session.commit()
        user_input_14_2 = user_input_14_2.lower().rstrip(".").split()
        keywords_14_2 = ["rough", "raised", "loose", "blotches", "contrast", "impasto", "brushstroke", "movement",
                         "gestural", "thick", "sides", "vortex", "hole", "center", "swirl"]
        if any(x in user_input_14_2 for x in keywords_14_2):
            return redirect(url_for('number14_2'))
        else:
            return redirect(url_for('number14_no'))

    return render_template('number14_1.html')

# Creates a database table to save user_input_14_3
class Comment14_3(db.Model):

    __tablename__ = "input_14_3"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the third page for object 14 and gets user input.
@app.route('/number14_2', methods=['GET','POST'])
def number14_2():
    if request.method == 'POST':
        user_input_14_3 = request.form.get('user_input_14_3')
        comment = Comment14_3(content=request.form['user_input_14_3'])
        db.session.add(comment)
        db.session.commit()
        user_input_14_3 = user_input_14_3.lower().rstrip(".").split()
        keywords_14_3 = ["not", "bad", "dangerous", "destructive", "negative", "terrible", "inequality", "lack", "resources"]
        if any(x in user_input_14_3 for x in keywords_14_3):
            return redirect(url_for('number14_3'))
        else:
            return redirect(url_for('number14_no'))

    return render_template('number14_2.html')

# This is the final page for object 14 and redirects to main page.
@app.route('/number14_3', methods=['GET','POST'])
def number14_3():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number14_3.html')

# This is the wild card page for object 14.
@app.route('/number14_no', methods=['GET', 'POST'])
def number14_no():
    if request.method == 'POST':

        user_input_14_no = request.form.get('user_input_14_no')
        user_input_14_no = user_input_14_no.lower().rstrip(".").split()

        keywords_14_1 = ["wild", "chaos", "violent", "scary", "torn", "stormy", "spooky", "destroyed", "desolate", "abandoned", "swirly",
                         "swirling", "chaotic", "dark", "bright", "bleak", "destruction", "rubble"]
        keywords_14_2 = ["rough", "raised", "loose", "blotches", "contrast", "impasto", "brushstroke", "movement",
                         "gestural", "thick", "sides", "vortex", "hole", "center", "swirl"]
        keywords_14_3 = ["not", "bad", "dangerous", "destructive", "negative", "terrible", "inequality", "lack", "resources"]

        if any(x in user_input_14_no for x in keywords_14_1):
            return redirect(url_for('number14_1'))

        if any(x in user_input_14_no for x in keywords_14_2):
            return redirect(url_for('number14_2'))

        if any(x in user_input_14_no for x in keywords_14_3):
            return redirect(url_for('number14_3'))

        else:
            return redirect(url_for('number14_no'))

    return render_template('number14_no.html')


# Here starts object number 15.

# Creates a database table to save user_input_15_1
class Comment15_1(db.Model):

    __tablename__ = "input_15_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This the first page for object 15 and gets user input.
@app.route('/number15', methods=['GET', 'POST'])
def number15():
    if request.method == 'POST':
        user_input_15_1 = request.form.get('user_input_15_1')
        comment = Comment15_1(content=request.form['user_input_15_1'])
        db.session.add(comment)
        db.session.commit()
        user_input_15_1 = user_input_15_1.lower().rstrip(".").split()
        keywords_15_1 = ["prayer", "divine", "intervention", "vision", "holy", "praying", "begging", "receiving", "monk", "angel", "seraph", "stigmata",
                         "miracle", "looking", "up"]
        if any(x in user_input_15_1 for x in keywords_15_1):
            return redirect(url_for('number15_1'))
        else:
            return redirect(url_for('number15_no'))

    return render_template('number15.html')

# Creates a database table to save user_input_15_2
class Comment15_2(db.Model):

    __tablename__ = "input_15_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 15 and gets user input.
@app.route('/number15_1', methods=['GET','POST'])
def number15_1():
    if request.method == 'POST':
        user_input_15_2 = request.form.get('user_input_15_2')
        comment = Comment15_2(content=request.form['user_input_15_2'])
        db.session.add(comment)
        db.session.commit()
        user_input_15_2 = user_input_15_2.lower().rstrip(".").split()
        keywords_15_2 = ["awe", "wonder", "receptive", "supplication", "kneeling", "arms", "hands", "looking", "eyes", "pale", "gaze", "wounds", "red", "open", "up",
                         "scared", "surprised", "entranced", "emotional", "emaciated", "gaunt", "devout", "rapt",
                         "mesmerized"]
        if any(x in user_input_15_2 for x in keywords_15_2):
            return redirect(url_for('number15_2'))
        else:
            return redirect(url_for('number15_no'))

    return render_template('number15_1.html')

# Creates a database table to save user_input_15_3
class Comment15_3(db.Model):

    __tablename__ = "input_15_3"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the third page for object 15 and gets user input.
@app.route('/number15_2', methods=['GET','POST'])
def number15_2():
    if request.method == 'POST':
        user_input_15_3 = request.form.get('user_input_15_3')
        comment = Comment15_3(content=request.form['user_input_15_3'])
        db.session.add(comment)
        db.session.commit()
        user_input_15_3 = user_input_15_3.lower().rstrip(".").split()
        keywords_15_3 = ["church", "sanctuary", "chapel", "altar", "abbey", "basilica", "cathedral", "worship",
                         "castle", "house", "palace"]
        if any(x in user_input_15_3 for x in keywords_15_3):
            return redirect(url_for('number15_3'))
        else:
            return redirect(url_for('number15_no'))

    return render_template('number15_2.html')

# This is the final page for object 15 and redirects to main page.
@app.route('/number15_3', methods=['GET','POST'])
def number15_3():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number15_3.html')

# This is the wild card page for object 15.
@app.route('/number15_no', methods=['GET', 'POST'])
def number15_no():
    if request.method == 'POST':

        user_input_15_no = request.form.get('user_input_15_no')
        user_input_15_no = user_input_15_no.lower().rstrip(".").split()

        keywords_15_1 = ["prayer", "divine", "intervention", "vision", "holy", "praying", "begging", "receiving", "monk", "angel", "seraph", "stigmata",
                         "miracle", "looking", "up"]
        keywords_15_2 = ["awe", "wonder", "receptive", "supplication", "kneeling", "arms", "hands", "looking", "eyes", "pale", "gaze", "wounds", "red", "open", "up",
                         "scared", "surprised", "entranced", "emotional", "emaciated", "gaunt", "devout", "rapt",
                         "mesmerized"]
        keywords_15_3 = ["church", "sanctuary", "chapel", "altar", "abbey", "basilica", "cathedral", "worship",
                         "castle", "house", "palace"]

        if any(x in user_input_15_no for x in keywords_15_1):
            return redirect(url_for('number15_1'))

        if any(x in user_input_15_no for x in keywords_15_2):
            return redirect(url_for('number15_2'))

        if any(x in user_input_15_no for x in keywords_15_3):
            return redirect(url_for('number15_3'))

        else:
            return redirect(url_for('number15_no'))

    return render_template('number15_no.html')


# Here starts object number 16.

# Creates a database table to save user_input_16_1
class Comment16_1(db.Model):

    __tablename__ = "input_16_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the first page for object 16 and gets user input.
@app.route('/number16', methods=['GET', 'POST'])
def number16():
    if request.method == 'POST':
        user_input_16_1 = request.form.get('user_input_16_1')
        comment = Comment16_1(content=request.form['user_input_16_1'])
        db.session.add(comment)
        db.session.commit()
        user_input_16_1 = user_input_16_1.lower().rstrip(".").split()
        keywords_16_1 = ["stick", "sticks", "mother", "tools", "man", "woman", "weapons", "knife", "sword", "spear", "bracelets", "clothing", "beard", "eyes",
                         "headdress", "nude", "naked", "bag", "baby", "child", "shorts", "belt"]
        if any(x in user_input_16_1 for x in keywords_16_1):
            return redirect(url_for('number16_1'))
        else:
            return redirect(url_for('number16_no'))

    return render_template('number16.html')

# Creates a database table to save user_input_16_2
class Comment16_2(db.Model):

    __tablename__ = "input_16_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 16 and gets user input.
@app.route('/number16_1', methods=['GET','POST'])
def number16_1():
    if request.method == 'POST':
        user_input_16_2 = request.form.get('user_input_16_2')
        comment = Comment16_2(content=request.form['user_input_16_2'])
        db.session.add(comment)
        db.session.commit()
        user_input_16_2 = user_input_16_2.lower().rstrip(".").split()
        keywords_16_2 = ["two", "symmetry", "even", "sideways", "rhythm", "almond", "eyes", "both"]
        if any(x in user_input_16_2 for x in keywords_16_2):
            return redirect(url_for('number16_2'))
        else:
            return redirect(url_for('number16_no'))

    return render_template('number16_1.html')

# Creates a database table to save user_input_16_3
class Comment16_3(db.Model):

    __tablename__ = "input_16_3"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the third page for object 16 and gets user input.
@app.route('/number16_2', methods= ['GET','POST'])
def number16_2():
    if request.method == 'POST':
        user_input_16_3 = request.form.get('user_input_16_3')
        comment = Comment16_3(content=request.form['user_input_16_3'])
        db.session.add(comment)
        db.session.commit()
        user_input_16_3 = user_input_16_3.lower().rstrip(".").split()
        keywords_16_3 = ["post", "column", "support", "pillar", "wood", "house", "decoration", "architecture", "palace",
                         "carving"]
        if any(x in user_input_16_3 for x in keywords_16_3):
            return redirect(url_for('number16_3'))
        else:
            return redirect(url_for('number16_no'))

    return render_template('number16_2.html')

# This is the final page for object 16 and redirects to main page.
@app.route('/number16_3', methods= ['GET','POST'])
def number16_3():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number16_3.html')

# This is the wild card page for object 16.
@app.route('/number16_no', methods= ['GET', 'POST'])
def number16_no():
    if request.method == 'POST':

        user_input_16_no = request.form.get('user_input_16_no')
        user_input_16_no = user_input_16_no.lower().rstrip(".").split()

        keywords_16_1 = ["stick", "sticks", "mother", "tools", "man", "woman", "weapons", "knife", "sword", "spear", "bracelets", "clothing", "beard", "eyes",
                         "headdress", "nude", "naked", "bag", "baby", "child", "shorts", "belt"]
        keywords_16_2 = ["two", "symmetry", "even", "sideways", "rhythm", "almond", "eyes", "both"]
        keywords_16_3 = ["post", "column", "support", "pillar", "wood", "house", "decoration", "architecture", "palace",
                         "carving"]
        if any(x in user_input_16_no for x in keywords_16_1):
            return redirect(url_for('number16_1'))

        if any(x in user_input_16_no for x in keywords_16_2):
            return redirect(url_for('number16_2'))

        if any(x in user_input_16_no for x in keywords_16_3):
            return redirect(url_for('number16_3'))

        else:
            return redirect(url_for('number16_no'))

    return render_template('number16_no.html')


# Here starts object number 17.
# Creates a database table to save user_input_17_1
class Comment17_1(db.Model):

    __tablename__ = "input_17_1"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the first page for object 17 and gets user input.
@app.route('/number17', methods=['GET', 'POST'])
def number17():
    if request.method == 'POST':
        user_input_17_1 = request.form.get('user_input_17_1')
        comment = Comment17_1(content=request.form['user_input_17_1'])
        db.session.add(comment)
        db.session.commit()
        user_input_17_1 = user_input_17_1.lower().rstrip(".").split()
        keywords_17_1 = ["harvest", "harvesting", "workers", "laborers", "bent", "sitting", "working", "sketchy", "detailed", "clothing",
                         "standing", "interacting", "many", "outdoors", "groups", "hunched", "brushstrokes",
                         "brushstroke", "sloppy"]
        if any(x in user_input_17_1 for x in keywords_17_1):
            return redirect(url_for('number17_1'))
        else:
            return redirect(url_for('number17_no'))

    return render_template('number17.html')

# Creates a database table to save user_input_17_2
class Comment17_2(db.Model):

    __tablename__ = "input_17_2"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))

# This is the second page for object 17 and gets user input.
@app.route('/number17_1', methods=['GET', 'POST'])
def number17_1():
    if request.method == 'POST':
        user_input_17_2 = request.form.get('user_input_17_2')
        comment = Comment17_2(content=request.form['user_input_17_2'])
        db.session.add(comment)
        db.session.commit()
        user_input_17_2 = user_input_17_2.lower().rstrip(".").split()
        keywords_17_2 = ["dark", "small", "sketchy", "sketch", "blobs", "heavy", "dark", "background", "high", "horizon",
                        "light", "sky", "rough", "painterly", "impasto", "brown", "yellow", "white", "green", "muddy"]
        if any(x in user_input_17_2 for x in keywords_17_2):
            return redirect(url_for('number17_2'))
        else:
            return redirect(url_for('number17_no'))

    return render_template('number17_1.html')

# This is the final page for object 17 and redirects to main page.
@app.route('/number17_2', methods=['GET', 'POST'])
def number17_2():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('number17_2.html')

# This is the wild card page for object 17.
@app.route('/number17_no', methods=['GET', 'POST'])
def number17_no():
    if request.method == 'POST':

        user_input_17_no = request.form.get('user_input_17_no')
        user_input_17_no = user_input_17_no.lower().rstrip(".").split()

        keywords_17_1 = ["harvest", "harvesting", "workers", "laborers", "bent", "sitting", "working", "sketchy", "detailed", "clothing",
                         "standing", "interacting", "many", "outdoors", "groups", "hunched", "brushstrokes",
                         "brushstroke", "sloppy"]
        keywords_17_2 = ["dark", "small", "sketch", "blobs", "heavy", "dark", "background", "high", "horizon",
                        "light", "sky", "rough", "painterly", "impasto", "brown", "yellow", "white", "green", "muddy"]

        if any(x in user_input_17_no for x in keywords_17_1):
            return redirect(url_for('number17_1'))

        if any(x in user_input_17_no for x in keywords_17_2):
            return redirect(url_for('number17_2'))

        else:
            return redirect(url_for('number17_no'))

    return render_template('number17_no.html')