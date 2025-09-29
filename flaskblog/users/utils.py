import os
import secrets
import smtplib
from PIL import Image
from flask import url_for, current_app
from email.message import EmailMessage
from markupsafe import escape

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    i.save(picture_path)

    return picture_fn

def send_request_email(user):
    token = user.get_reset_token()
    sender_email = os.getenv('EMAIL_USER')
    sender_password = os.getenv('EMAIL_PASSWORD')
    receiver_email = user.email

    msg = EmailMessage()
    msg['Subject'] = "Password Reset Request"  # UTF-8 funciona nativo
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Texto plano
    msg.set_content(f"""
Hi {escape(user.username)},

To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
""")

    # HTML
    msg.add_alternative(f"""
<html>
  <body>
    <p>Hi {escape(user.username)},</p>
    <p>To reset your password, visit the following link:</p>
    <p><a href="{url_for('users.reset_token', token=token, _external=True)}">Reset Password</a></p>
    <p>If you did not make this request then simply ignore this email and no changes will be made.</p>
  </body>
</html>
""", subtype='html')

    # Configura tu SMTP (Gmail de ejemplo)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)  # usa contraseña de app de Gmail
        server.send_message(msg)