from .address import Address

class Customer(Person):
    def __init__(self,first_name: str, last_name: str, dob: str, social_security: str, address: Address):
        """[summary]
        Args:
            first_name (str): [description]
            last_name (str): [description]
            dob (str): [description]
            social_security (str): [description]
            address (str): [description]
        Returns:
            [type]: [description]
        """
