import React, { useState } from 'react';
import axios from 'axios';

type Purchase = {
  customer_id: number;
  item_id: number;
};

const url = "http://customer-bff-service:5000";

const App: React.FC = () => {
  const [customerID, setCustomerID] = useState<number | undefined>(undefined);
  const [purchases, setPurchases] = useState<Purchase[]>([]);

  const handleBuyClick = async () => {
    const customerID = Math.floor(Math.random() * 1000) + 1;
    const itemID = Math.floor(Math.random() * 1000) + 1;
    await axios.post(`${url}/customers/${customerID}/purchase/${itemID}`);
    setCustomerID(customerID);
  };

  const handleGetAllUserBuysClick = async () => {
    if (!customerID) {
      alert('Please make a purchase first.');
      return;
    }
    const response = await axios.get(`${url}/customers/${customerID}/purchases`);
    setPurchases(response.data);
  };

  return (
    <div>
      <button onClick={handleBuyClick}>Buy</button>
      <button onClick={handleGetAllUserBuysClick}>Get All User Buys</button>
      {customerID && <p>Customer ID: {customerID}</p>}
      {purchases.length > 0 && (
        <table>
          <thead>
            <tr>
              <th>Customer ID</th>
              <th>Item ID</th>
            </tr>
          </thead>
          <tbody>
            {purchases.map((purchase) => (
              <tr key={`${purchase.customer_id}-${purchase.item_id}`}>
                <td>{purchase.customer_id}</td>
                <td>{purchase.item_id}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

export default App;
