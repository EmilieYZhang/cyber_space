from flask import Blueprint, render_template, request, flash
# blueprint means it has a bunch of roots and url inside of it

views = Blueprint('views', __name__)

@views.route('/') # decorator to define the route
def home():
    return render_template("home.html")

@views.route('/story1', methods=['GET', 'POST'])
def story1():
    if request.method == 'POST':
        adj1 = request.form.get('s1_adj1')
        if len (adj1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        num1 = request.form.get('s1_num1')
        if len (num1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        sol1 = request.form.get('s1_soc1')
        if len (sol1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        cel1 = request.form.get('s1_cel1')
        if len (cel1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        pro1 = request.form.get('s1_pro1')
        if len (pro1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        adj2 = request.form.get('s1_adj2')
        if len (adj2) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        num2 = request.form.get('s1_num2')
        if len (num2) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        plunoun1 = request.form.get('s1_plunoun1')
        if len (plunoun1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        body1 = request.form.get('s1_body1')
        if len (body1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        store1 = request.form.get('s1_store1')
        if len (store1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        silly1 = request.form.get('s1_silly1')
        if len (silly1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        emo1 = request.form.get('s1_emo1')
        if len (emo1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        adj3 = request.form.get('s1_adj3')
        if len (adj3) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        num3 = request.form.get('s1_num3')
        if len (num3) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        verb1 = request.form.get('s1_verb1')
        if len (verb1) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        num4 = request.form.get('s1_num4')
        if len (num4) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        plunoun2 = request.form.get('s1_plunoun2')
        if len (plunoun2) < 1:
            flash('One of your entries is too short.', category ='error')
            return render_template("story1.html", complete_bool = False)
        else:
            flash('Success! Your story has been completed.', category = 'success')
            array = [adj1, num1, sol1, cel1, pro1, adj2, num2, plunoun1, body1, store1, silly1, emo1, adj3, num3, verb1, num4, plunoun2]
            return render_template("story1.html", complete_bool = True, array = array)
    else:
        return render_template("story1.html", complete_bool = False)

@views.route('/story2', methods=['GET', 'POST'])
def story2():
    if request.method == 'POST':
        soc1 = request.form.get('s2_soc1')
        if len(soc1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        plunoun1 = request.form.get('s2_plunoun1')
        if len(plunoun1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        verb1 = request.form.get('s2_verb1')
        if len(verb1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        adj1 = request.form.get('s2_adj1')
        if len(adj1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        plunoun2 = request.form.get('s2_plunoun2')
        if len(plunoun2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        num1 = request.form.get('s2_num1')
        if len(num1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        emo1 = request.form.get('s2_emo1')
        if len(emo1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        num2 = request.form.get('s2_num2')
        if len(num2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        adj2 = request.form.get('s2_adj2')
        if len(adj2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        verb2 = request.form.get('s2_verb2')
        if len(verb2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        num3 = request.form.get('s2_num3')
        if len(num3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        adj3 = request.form.get('s2_adj3')
        if len(adj3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        rel1 = request.form.get('s2_rel1')
        if len(rel1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        plunoun3 = request.form.get('s2_plunoun3')
        if len(plunoun3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        profession1 = request.form.get('s2_profession1')
        if len(profession1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        emo2 = request.form.get('s2_emo2')
        if len(emo2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        else:
            flash('Success! Your story has been completed.', category = 'success')
            array = [soc1, plunoun1, verb1, soc1, adj1, plunoun2, num1, emo1, num2, adj2, verb2, num3, adj3, rel1, plunoun3, profession1, emo2]
            return render_template("story2.html", complete_bool = True, array = array)

    else:
        return render_template("story2.html", complete_bool = False)

@views.route('/story3', methods=['GET', 'POST'])
def story3():
    if request.method == 'POST':
        wea1 = request.form.get('s3_wea1')
        if len(wea1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        noun1 = request.form.get('s3_noun1')
        if len(noun1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        verb1 = request.form.get('s3_verb1')
        if len(verb1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        plunoun1 = request.form.get('s3_plunoun1')
        if len(plunoun1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        plunoun2 = request.form.get('s3_plunoun2')
        if len(plunoun2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        adj1 = request.form.get('s3_adj1')
        if len(adj1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        num1 = request.form.get('s3_num1')
        if len(num1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        adj2 = request.form.get('s3_adj2')
        if len(adj2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        col1 = request.form.get('s3_col1')
        if len(col1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        verb2 = request.form.get('s3_verb2')
        if len(verb2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        adj3 = request.form.get('s3_adj3')
        if len(adj3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        noun2 = request.form.get('s3_noun2')
        if len(noun2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        liquid1 = request.form.get('s3_liquid1')
        if len(liquid1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story2.html", complete_bool = False)
        verb3 = request.form.get('s3_verb3')
        if len(verb3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        plunoun3 = request.form.get('s3_plunoun3')
        if len(plunoun3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        num2 = request.form.get('s3_num2')
        if len(num2) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        num3 = request.form.get('s3_num3')
        if len(num3) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        plunoun4 = request.form.get('s3_plunoun4')
        if len(plunoun4) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        excla1 = request.form.get('s3_excla1')
        if len(excla1) < 1:
            flash('One of your entries is too short.', category = 'error')
            return render_template("story3.html", complete_bool = False)
        else:
            flash('Success! Your story has been completed.', category = 'success')
            array = [wea1, noun1, verb1, plunoun1, plunoun2, adj1, num1, adj2, col1, verb2, adj3, noun2, liquid1, verb3, plunoun3, noun2, liquid1, num2, num3, plunoun4, excla1]
            return render_template("story3.html", complete_bool = True, array = array)

    else:
        return render_template("story3.html", complete_bool = False)