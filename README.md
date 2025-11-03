## 🪙 Python Currency Converter

A simple, command-line currency converter built in **Python** that fetches live exchange rates using the **ExchangeRate-API**.

-----

## ✨ Features

  * **Live Rates:** Fetches the most recent exchange rates from a reliable external API.
  * **Interactive CLI:** Prompts the user for the amount, source currency, and target currency.
  * **Input Validation:** Ensures amounts are positive numbers and currency codes are valid 3-letter codes.

-----

## 🚀 Getting Started

Follow these steps to get the converter running locally.

### Prerequisites

You need **Python 3** installed on your system.

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    This project requires the `requests` library to make HTTP calls to the API.

    ```bash
    pip install requests
    ```

3.  **Obtain and Configure API Key:**

      * Sign up for a free API key from **[ExchangeRate-API Website Link Here]**.
      * Open the `converter.py` file.
      * Replace `'YOUR_API_KEY'` in the configuration section with your actual key:

    <!-- end list -->

    ```python
    # --- Configuration ---
    API_KEY = 'YOUR_ACTUAL_API_KEY_HERE' # <-- REPLACE THIS LINE
    BASE_URL = 'https://v6.exchangerate-api.com/v6/'
    ```

### Usage

Run the main Python script from your terminal:

```bash
python converter.py
```

The program will prompt you sequentially for:

1.  The **amount** to convert.
2.  The **source currency code** (e.g., `USD`).
3.  The **target currency code** (e.g., `EUR`).

-----

## 🗂️ API Reference

The application relies on the **ExchangeRate-API**.

  * **Endpoint Used:** `/latest/{base_currency}` for fetching rates.
  * **Note:** Always verify the API key is correctly set in `converter.py` for the program to function.

-----

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn and create. If you have a suggestion that would make this project better, please **fork the repo** and **submit a pull request**. You can also just **open an issue** with the tag "enhancement."

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

-----

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

-----
