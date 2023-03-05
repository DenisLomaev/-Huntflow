from typing import Any


class DataClient:
    @staticmethod
    def get_payload_for_registration_user(email: str, password: str, confirm_password: str) -> Any:
        return {
            "email": email,
            "password": password,
            "password_confirmation": confirm_password,
            "recaptcha": "random_str"
        }

    @staticmethod
    def get_payload_for_authorization_user(eamil: str, password: str):
        pass
