from curses import flash
from unicodedata import category
from flask import Blueprint ,render_template, redirect,request,url_for, flash
from flask_login import  current_user

from .models import Task
from . import db


views      = Blueprint("views", __name__)



@views.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        added_task               =   request.form.get('task-name')
        added_description        =   request.form.get('description')
        added_priority           =   request.form.get('priority')
        added_status             =   request.form.get('status')
        user                     =   current_user

        try:
            print(type(user.id))

            if added_task == " ":
                flash('Please try to write a task!!', category="warning")
            elif len(added_task) < 5:
                flash('The task name too samll, at least 5 latters!!', category="warning")
            elif added_priority == " " or added_priority == "Priority":
                flash('Please set a priority!!', category="warning")
            elif added_status == " " or added_status == "Status":
                flash('Please set a current status of your!!', category="warning")
            else:
                new_task             =   Task(  task_name   = added_task, 
                                                description = added_description,
                                                priority    = added_priority,
                                                status      = added_status,
                                                user_id     = user.id,
                                                created_by  = (user.fname +" " +user.lname) )

                db.session.add(new_task)
                db.session.commit()
                flash('A new task added successfully!!', category="sccess")
                return redirect(url_for('views.home'))
        except AttributeError :
            flash('It seems you are not signing in, Try to sign in from here !!', category="singin-error")

    return render_template("home.html", user = current_user)

@views.route('/delete/<int:id>')
def delete(id):
    delete_task_by_id = Task.query.get_or_404(id)
    print(delete_task_by_id)

    try:
        db.session.delete(delete_task_by_id)
        db.session.commit()
        flash('The task has been deleted successfully!!', category='success')
        return redirect(url_for('views.home'))
    except:
        flash('Sorry! unable to delete this task!!', category='error')

        redirect(url_for('views.home'))


@views.route('/update/<int:id>', methods=['POST','GET'])
def update(id):

    update   = Task.query.get_or_404(id)
    print(update)
    if  request.method        == "POST":
        update.task_name      =  request.form.get('task-name')
        update.description    =  request.form.get('description')
        update.priority       =  request.form.get('priority')
        update.status         =  request.form.get('status')
        if update.task_name   == " ":
            flash('Please try to write a task!!', category="warning")
        elif len(update.task_name) < 5:
            flash('The task name too samll, at least 5 latters!!', category="warning")
        elif update.priority == " " or update.priority == "Priority":
            flash('Please set a priority!!', category="warning")
        elif update.status  == " " or update.status  == "Status":
            flash('Please set a current status of your!!', category="warning")
        else:
            db.session.commit()
            flash('The Task updated successfully!!', category="sccess")
            return redirect(url_for('views.home'))
    
    return  render_template('home.html', user= current_user )




# @views.route('/dashboard', methods=['POST','GET'])
# @login_required #means do not show this page unless the user logged in.
# def dashboard():
#     pass 

