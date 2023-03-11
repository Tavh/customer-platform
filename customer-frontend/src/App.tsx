import React, { useState } from "react";
import axios from "axios";
import "./App.css";

interface Purchase {
  id: number;
  purchase_time: string;
  price_at_purchase_time: number;
  customer: Customer;
  item: Item;
}

interface Customer {
  id: number;
  name: string;
}

interface Item {
  id: number;
  name: string;
  price: number;
}

function App() {
  const [purchases, setPurchases] = useState<Purchase[]>([]);
  const [customerId, setCustomerId] = useState("");
  const [itemId, setItemId] = useState("");
  const [error, setError] = useState("");

  const handleBuyClick = async () => {
    if (!customerId || !itemId) {
      setError("Please provide both customer and item IDs.");
      return;
    }
    try {
      const response = await axios.post(
        `http://localhost:5000/customers/${customerId}/purchase/${itemId}`
      );
      console.log(response);
      setError("");
      alert("Purchase was successful!");
    } catch (error) {
      console.error(error);
    }
  };
  

  const handleGetAllUserBuysClick = async () => {
    if (!customerId) {
      setError("Please provide a customer ID.");
      return;
    }
    try {
      const response = await axios.get<Purchase[]>(
        `http://localhost:5000/customers/${customerId}/purchases`
      );
      console.log(response);
      setPurchases(response.data);
      setError("");
    } catch (error) {
      console.error(error);
    }
  };
  

  return (
    <div className="container">
      <h1 className="title">Purchase App</h1>
      <div className="input">
        <label htmlFor="customer-id">Customer ID:</label>
        <input
          type="text"
          id="customer-id"
          value={customerId}
          onChange={(e) => setCustomerId(e.target.value)}
          required
        />

        <input
          type="text"
          id="item-id"
          value={itemId}
          onChange={(e) => setItemId(e.target.value)}
          required
        />
      </div>
      <div className="error">{error}</div>
      <div className="buttons">
        <button className="buy-button" onClick={handleBuyClick}>
          Buy
        </button>
        <button
          className="get-all-buys-button"
          onClick={handleGetAllUserBuysClick}
        >
          Get All User Purchases
        </button>
      </div>
      <div className="purchases">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Purchase Time</th>
              <th>Price at Purchase Time</th>
              <th>Customer ID</th>
              <th>Customer Name</th>
              <th>Item ID</th>
              <th>Item Name</th>
              <th>Item Price</th>
            </tr>
          </thead>
          <tbody>
            {purchases.map((p) => (
              <tr key={p.id}>
                <td>{p.id}</td>
                <td>{p.purchase_time}</td>
                <td>{p.price_at_purchase_time}</td>
                <td>{p.customer.id}</td>
                <td>{p.customer.name}</td>
                <td>{p.item.id}</td>
                <td>{p.item.name}</td>
                <td>{p.item.price}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
