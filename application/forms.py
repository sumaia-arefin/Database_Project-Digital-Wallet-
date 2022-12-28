from algosdk.constants import address_len, note_max_length, max_asset_decimals
from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField, IntegerField, BooleanField, PasswordField, EmailField,TelField
from wtforms.validators import InputRequired, Optional, Length, NumberRange, Email




class LoginForm(FlaskForm):
    """Form for logging into an account"""
    phone = TelField('Phone Number', validators=[InputRequired(), Length(11,11)])
    pin_number = PasswordField('Pin Number', validators=[InputRequired(),Length(6,6)])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    full_name = StringField("Full Name", validators=[InputRequired()])
    phone = TelField('Phone Number', validators=[InputRequired(), Length(11,11)])
    email= EmailField('Email', validators=[InputRequired(), Email()])
    pin_number = PasswordField('Pin Number', validators=[InputRequired(),Length(6,6)])
    pin_number_confirmation = PasswordField('Confirm Pin Number', validators=[InputRequired(),Length(6,6)])
    submit = SubmitField('Sign Up')

class SendForm(FlaskForm):
    """Form for creating a transaction"""
    quantity = DecimalField(
        'Quantity',
        validators=[InputRequired(), NumberRange(min=0)],
        render_kw={"placeholder": "Amount to Send"}
    )
    receiver = StringField(
        'Receiver',
        validators=[InputRequired(), Length(min=address_len, max=address_len)],
        render_kw={"placeholder": "Receiver Phone No"}
    )
    note = StringField(
        'Note',
        validators=[Optional(), Length(max=note_max_length)],
        render_kw={"placeholder": "Note"})
    submit = SubmitField('Send')


class AssetForm(FlaskForm):
    """Form for creating an asset"""
    asset_name = StringField(
        'Asset name',
        validators=[InputRequired()]
    )
    unit_name = StringField(
        'Unit name',
        validators=[InputRequired()]
    )
    total = IntegerField(
        'Total number',
        validators=[InputRequired(), NumberRange(min=1)]
    )
    decimals = IntegerField(
        'Number of decimals',
        validators=[InputRequired(), NumberRange(min=0, max=max_asset_decimals)]
    )
    default_frozen = BooleanField(
        'Frozen',
        validators=[Optional()]
    )
    url = StringField(
        'URL',
        validators=[Optional()]
    )
    submit = SubmitField('Create')


class FilterForm(FlaskForm):
    """Form for filtering transactions and assets"""
    substring = StringField(
        'Filter',
        validators=[Optional()],
        render_kw={"placeholder": "Filter list"}
    )
    submit = SubmitField('Search')
