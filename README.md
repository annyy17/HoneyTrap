# HoneyTrap
A honeypot project is a cybersecurity tool or system designed to attract, detect, and study malicious activity on a network by simulating vulnerabilities or tempting targets for attackers. a honeypot project is a powerful tool in cybersecurity to trap, study, and learn from malicious activities .
############################################################################################################################################################################################
The honeypot is built using Flask, a lightweight Python web framework. Below are key implementation details:
•	The main page (/) provides a login form where user inputs are logged.
•	The admin panel (/admin) acts as bait for attackers trying to gain privileged access.
•	Logs are stored in a file (honeypot.log) for further analysis.
#############################################################################################################################################################################################
Each attack attempt is logged with the following information:
•	IP Address: Identifies the attack source.
•	Username & Password: Captures credentials used by attackers.
•	User-Agent: Provides insights into the attacker's browser or automated tool.
•	Endpoint Accessed: Distinguishes whether the attacker targeted the main login or the admin panel.
