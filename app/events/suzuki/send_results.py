from flask import current_app
from app.models import SuzukiLead
from app.email_sender import send_email

def create_table(data, model):
    html_table = "<table border='1'>"
    
    # Table headers
    html_table += "<tr>"
    for column in model.__table__.columns:
        html_table += f"<th>{column.name}</th>"
    html_table += "</tr>"
    
    # Table data
    for row in data:
        html_table += "<tr>"
        for column in model.__table__.columns:
            value = getattr(row, column.name)
            html_table += f"<td>{value}</td>"
        html_table += "</tr>"
    
    html_table += "</table>"
    
    return html_table

def send_results_suzuki():
    suzuki_events = SuzukiLead.query.all()

    suzuki_events_str = create_table(suzuki_events, SuzukiLead)

    html_content = f"<h3>Suzuki Events</h3>{suzuki_events_str}"

    # Update the following line to include sender parameter
    subject="VROOM events: Suzuki"
    sender=current_app.config['DEFAULT_MAIL_SENDER']
    recipients=current_app.config['MAIL_RESULT_RECIPIENTS']
    recipients_list = recipients.split(';')
    text_body = ""
    html_body=html_content

    send_email(subject, sender, recipients_list, text_body, html_body)