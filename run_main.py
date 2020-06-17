# _*_ coding: utf-8 _*_

from BeautifulReport import BeautifulReport
import unittest
import os

# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from email.mime.application import MIMEApplication

# # Sender
# from_address = "xx.qq.com"
# from_password = ""
#
# # Receptor
# rec_address = "xxx.qq.com"
#
# # Delivery server
# smtp_server = 'smtp.qq.com'
#
# # Email content
# msg = MIMEText('Send by python', 'plain', 'utf-8')
#
# # Email header information
# msg['From'] = Header(from_address)
# msg['To'] = Header(rec_address)
# msg['Subject'] = Header('Python Test')
#
# # Turn on the send email service, there is use the encrypt transfer
# server = smtplib.SMTP_SSL()
# server.connect(smtp_server, 465)
#
# # Login in the send email
# server.login(from_address, from_password)
#
# # Send email
# server.sendmail(from_address, rec_address, msg.as_string())
#
# # Exit server
# server.quit()

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Reports")

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('TestCases', pattern='*.py')
    result = BeautifulReport(test_suite)
    result.report(filename='Test Report', description='测试报告', report_dir=path)
