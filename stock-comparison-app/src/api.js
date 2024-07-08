import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:5000/compare?stock=XYZ',  // Replace with your Flask backend URL
  timeout: 10000,  // Timeout duration in milliseconds
  headers: {
    'Content-Type': 'application/json',
  },
});

export const compareStockWithNifty = async (stockName) => {
  try {
    const response = await api.get(`/compare?stock=${stockName}`);
    return response.data;
  } catch (error) {
    throw new Error(`API Error: ${error}`);
  }
};
