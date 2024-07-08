from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/compare', methods=['GET'])
def compare_with_nifty():
    stock_name = request.args.get('stock', '')
    if not stock_name:
        return jsonify({'error': 'Stock name is required.'}), 400

    # Call your existing Python function to fetch and compare stock data
    comparison_result = get_stock_comparison(stock_name)

    return jsonify({'result': comparison_result})

def get_stock_comparison(stock):
    url = f'https://www.screener.in/company/{stock}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Replace with actual scraping and comparison logic
    NameS = "name"
    NumberS = "number"
    nameArray = soup.find_all(class_=NameS)
    numberArray = soup.find_all(class_=NumberS)

    if not nameArray or not numberArray:
        return f"Failed to compare {stock} with Nifty."

    # Example logic: Calculate average or compare data
    # Replace with your actual comparison logic
    average_stock_value = sum(int(item.text.strip()) for item in numberArray) / len(numberArray)
    return f"Average stock value for {stock} is {average_stock_value}."

if __name__ == '__main__':
    app.run(debug=True)
