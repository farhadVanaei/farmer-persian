from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from app import appbuilder, db
from app.models import Field,Location,Farmer




class fieldView(ModelView):
    datamodel = SQLAInterface(Field)

class locationView(ModelView):
    datamodel = SQLAInterface(Location)

class UserView(ModelView):
    datamodel = SQLAInterface(Farmer)

"""
    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(MyModelView, "My View", icon="fa-folder-open-o", category="My Category", category_icon='fa-envelope')
"""

"""
    Application wide 404 error handler
"""
@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


appbuilder.add_view(fieldView, "Field Management",icon = "fa-envelope",category = "Field")
appbuilder.add_view(locationView, "Location",icon = "fa-envelope",category = "Location")
appbuilder.add_view(UserView, "User",icon = "fa-envelope",category = "User")
db.create_all()



