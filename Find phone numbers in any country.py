import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number = input("Enter Your Phone Number: ")

number_country = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(number_country, "en"))

number_operator = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(number_operator, "en"))

number_timezone = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(number_timezone))

