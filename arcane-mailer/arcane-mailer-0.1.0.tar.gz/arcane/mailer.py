from typing import List, Union, Dict

from mailjet_rest import Client as MailerClient


class Client(MailerClient):
    def __init__(self, api_key=None, api_secret=None, version=None):
        super().__init__(auth=(api_key, api_secret), version=version)

    def send_to_recipients(
        self,
        recipients: List[Union[str, Dict]],
        subject: str,
        mail_content: str,
        sender: str,
        app_name: str,
        bcc_recipients: List[Union[str, Dict]] = []):
        """ Send mails to a list of recipients """
        self.send.create(data={
            'Messages': [
                {"From": {"Email": sender, "Name": f"{app_name} Notifications"},
                "To": [{'Email': single_recipient}],
                "Bcc": bcc_recipients,
                "Subject": subject,
                "HTMLPart": mail_content}
                for single_recipient in recipients]
        })
