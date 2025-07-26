import React, { useState } from "react";
import axios from "axios";

export default function ChatBot() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleQuery = async () => {
    try {
      if (query.toLowerCase().includes("top 5")) {
        const res = await axios.get("/api/top-products");
        setResponse(JSON.stringify(res.data, null, 2));
      } else if (query.toLowerCase().includes("status")) {
        const id = prompt("Enter Order ID:");
        const res = await axios.get(`/api/order-status?id=${id}`);
        setResponse(JSON.stringify(res.data, null, 2));
      } else if (query.toLowerCase().includes("how many")) {
        const name = prompt("Enter product name:");
        const res = await axios.get(`/api/stock-check?name=${name}`);
        setResponse(JSON.stringify(res.data, null, 2));
      } else {
        setResponse("Sorry, I don't understand.");
      }
    } catch (err) {
      setResponse("Error: " + err.message);
    }
  };

  return (
    <div className="chatbox">
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Ask me something..."
      />
      <button onClick={handleQuery}>Send</button>
      <pre>{response}</pre>
    </div>
  );
}