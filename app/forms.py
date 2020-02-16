from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, widgets, SelectField, TextAreaField
import pycountry
from wtforms.validators import DataRequired, Email, Length

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class CountrySelectField(SelectField):
    def __init__(self, *args, **kwargs):
        super(CountrySelectField, self).__init__(*args, **kwargs)
        self.choices = [(country.alpha_3, country.name) for country in pycountry.countries]

class ContactMeForm(FlaskForm):
    example = MultiCheckboxField('Please Select a Reason(s) for your Inquiry', choices=[('Professional IT or Software Services','' ), ('Venture Funding', 'Venture Funding'), ('Personal Inquiry', 'Personal Inquiry')])
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name')
    email = StringField('Email Address', validators = [DataRequired(), Email(message='Please enter a valid Email before submitting'), Length(min=6, max=50, message='Your Email is too long')])
    address = StringField('Mailing Address')
    city = StringField('City')
    country = CountrySelectField('Country')
    reasons = SelectMultipleField('Please Select a Reason(s) for your Inquiry [Ctrl + Click for multi-select]', choices=[('itservice','Professional IT or Software Services' ), ('venture', 'Venture Funding'), ('personal', 'Personal Inquiry'), ('art', 'Artistic Collaboration'), ('partner', 'Partnerships or Sponsorships'), ('misc', 'All Other Matters')])
    messagebody = TextAreaField('Please Compose Your Message Below', validators=[DataRequired(), Length(min=5, max=1600,message='There is a 1600 Character Limit, please modify to Submit')])
    # checkoptions = SelectField('Please Select a Reason(s) for your Inquiry', choices=[('opt1', 'Professional IT or Software Services'), ('opt2', 'Venture Funding'), ('opt3', 'Personal Inquiry')])
    submit = SubmitField('Submit')
 