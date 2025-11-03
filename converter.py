import requests
API_KEY = 'd0813643a81dc0e9f50bf7ce'
BASE_URL = 'https://v6.exchangerate-api.com/v6/'

def get_conversion_rates(base_currency):
    base_currency = base_currency.upper()
    endpoint = f'{BASE_URL}{API_KEY}/latest/{base_currency}'

    try:
        response = requests.get(endpoint)
        response.raise_for_status()
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print(
                f"❌ API Error fetching rates for {base_currency}: {data.get('error-type', 'Unknown error')}. Please check your API key or currency code.")
            return None

    except requests.exceptions.RequestException as e:
        print(f"❌ Network or request error: Check your internet connection or API_KEY: {e}")
        return None


def run_converter():
    print("-------------------------------------------------------")
    print("🌎 Welcome to the Interactive Currency Converter! 💰")
    print("-------------------------------------------------------")
    while True:
        try:
            amount_str = input("Enter the amount to convert: ")
            amount = float(amount_str)
            if amount <= 0:
                raise ValueError
            break
        except ValueError:
            print("🛑 Invalid amount. Please enter a positive number.")
    while True:
        from_curr = input("Enter the source currency code (e.g., USD, EUR): ").strip().upper()
        if len(from_curr) == 3 and from_curr.isalpha():
            break
        print("🛑 Invalid source currency code. Must be a 3-letter code (e.g., JPY).")
    while True:
        to_curr = input("Enter the target currency code (e.g., GBP, JPY): ").strip().upper()
        if len(to_curr) == 3 and to_curr.isalpha() and to_curr != from_curr:
            break
        print("🛑 Invalid target currency code. Must be a unique 3-letter code.")

    print(f"\n⚙️ Calculating conversion for {amount:.2f} {from_curr} to {to_curr}...")
    rates = get_conversion_rates(from_curr)

    if not rates:
        print("\n🛑 Could not fetch rates. Conversion failed.")
        return
    if to_curr not in rates:
        print(f"\n🛑 Conversion target '{to_curr}' not supported or found in the rates for '{from_curr}'.")
        return

    exchange_rate = rates[to_curr]
    converted_amount = amount * exchange_rate
    print("\n--- ✅ Conversion Result ---")
    print(f"   Source Amount: {amount:.2f} **{from_curr}**")
    print(f"   Exchange Rate (1 {from_curr}): {exchange_rate:.4f} {to_curr}")
    print(f"   Converted Amount: **{converted_amount:.2f} {to_curr}**")
    print("-----------------------------\n")


if __name__ == '__main__':
    run_converter()