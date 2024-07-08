// src/components/StockComparison.js

import React, { useState } from 'react';
import { compareStockWithNifty } from './api.js';  // Adjust path as necessary

function StockComparison() {
  const [stockName, setStockName] = useState('');
  const [comparisonResult, setComparisonResult] = useState('');

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      const result = await compareStockWithNifty(stockName);
      setComparisonResult(result);  // Assuming your backend returns the comparison result directly
    } catch (error) {
      console.error('Error fetching data:', error);
      setComparisonResult('Error fetching data. Please try again.');
    }
  };

  return (
    <div>
      <form onSubmit={handleFormSubmit}>
        <input type="text" value={stockName} onChange={(e) => setStockName(e.target.value)} />
        <button type="submit">Compare with Nifty</button>
      </form>
      <div>
        <h2>Comparison Result:</h2>
        <pre>{comparisonResult}</pre>
      </div>
    </div>
  );
}

export default StockComparison;
