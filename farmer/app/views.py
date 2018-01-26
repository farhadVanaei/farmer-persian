
from flask import render_template
from flask.ext.appbuilder.models.sqla.interface import SQLAInterface
from flask.ext.appbuilder import ModelView
from flask_babel import lazy_gettext as _

from app import appbuilder, db
from app.models import Field,Location,Farmer


class fieldView(ModelView):
    label_columns = {
                    'kind':_('kind')
                     }
    datamodel = SQLAInterface(Field)

class locationView(ModelView):
    label_columns = {
                    'Country':_('Country'),
                     'State':_("State"),
                     'City':_('City'),
                     'Part':_('Part'),
                     'village':_('village')
                     }
    datamodel = SQLAInterface(Location)

class UserView(ModelView):
    label_columns = {
                    'username':_('Username'),
                     'name':_("Name"),
                     'family':_('Family'),
                     'mobile':_('Mobile'),
                     'fields':_('Fields'),
                     'fathername':_('fathername'),
                     'NationalNumber':_('Nationalnumber'),
                     'phone':_('Phone'),
                     'Location ':_('Location'),
                     'password':_('Password'),
                     'email':_('Email')
                     }
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


appbuilder.add_view(fieldView, "Field Management",icon = "fa-product-hunt",category = "Field",category_icon = "fa-product-hunt" )
appbuilder.add_view(locationView, "Location",icon = "fa fa-map-o",category = "Location",category_icon = "fa fa-map-o" )
appbuilder.add_view(UserView, "User",icon = "fa fa-truck",category = "User",category_icon = "fa fa-truck" )
db.create_all()



