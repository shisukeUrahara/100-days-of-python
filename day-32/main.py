# import smtplib
#
# my_email="test@gmail.com"
# # connection= smtplib.SMTP('smtp.gmail.com')
# # #enable security
# # connection.starttls()
# # connection.login(user=my_email, password="testpassword")
# # connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"subject:test subject\n\nhello python")
# # connection.close()
#
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # enable security
#     connection.starttls()
#     connection.login(user=my_email, password="pvyh uvwy iczi onrs")
#     connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"subject:test subject\n\nhello python")


#  working with date time module
import datetime as dt

now=dt.datetime.now()

print(now)
print(type(now))
print(now.year)
print(now.month)
print(now.day)

