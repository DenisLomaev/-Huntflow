class MainURL:
    @staticmethod
    def get_url_from_dict(key: str) -> str:
        all_url = {"base_url": "https://dev-100-api.huntflow.dev"}
        return all_url[key]
