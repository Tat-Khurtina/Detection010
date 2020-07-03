

import re
from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import ValidationError, DataRequired


class FillingForm(FlaskForm):

    submit0 = SubmitField('Сохранить')

