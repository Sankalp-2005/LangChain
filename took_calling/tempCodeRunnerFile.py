
def get_conversion_factor(base_currency:str, target_currency:str)->float:
    """This function fetches the conversion factor between the two provided currencies, one being base currency other being the target currency using the exchange rate api

    Args:
        base_currency (str): The base currency from which the conversion is to be done
        target_currency (str): The target currency to which the conversion is to be done

    Returns:
        float: The conversion factor between the base and the target currency.
    """
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"
    result = requests.get(url)
    return result.json()