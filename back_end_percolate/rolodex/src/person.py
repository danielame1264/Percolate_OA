"""
Data model for a line in the input file
"""
# import phonenumbers  See commented method below


class Person(object):
    """
    @param first_name
    @param last_name
    @param phone_number    10 digit number
    @param color
    @param zipcode  5 digit number
    """

    def __init__(self, first_name, last_name, phone_number, color, zipcode):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = self.convert_phone_number(phone_number)
        self.color = color
        self.zipcode = zipcode

    
    def convert_phone_number(self, number):
        """
        format phone numbers into xxx-xxx-xxxx
        """
        number_only_digit = filter(lambda x: x.isdigit(), number)
        return "%s-%s-%s" % (
                number_only_digit[0:3],
                number_only_digit[3:6],
                number_only_digit[6:10]
            )

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)

    def _asdict(self):
        return self.__dict__

    """
    I believe for phonenumbers, we should use some real validation. This lib is gonna invalidate 
    numbers that start with 1, which is the correct thing to do for US numbers, but the sample input
    contains quite a few of numbers starting with 1. So I didn't bother using it.

    def convert_phone_number2(self, number, country="US"):
        try:
            parsed_number = phonenumbers.parse(number, country)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            logger.debug("%s is possibly not a valid phone number" % number)
            return number
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumber())
        else:
            logger.debug("%s is possibly not a valid US phone number" % number)
            return number
    """