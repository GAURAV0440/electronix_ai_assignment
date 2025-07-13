import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async () => {
    if (!text.trim()) return;
    try {
      const response = await axios.post("http://localhost:8000/predict", {
        text: text,
      });
      setResult(response.data);
    } catch (error) {
      console.error("Prediction error:", error);
    }
  };

  return (
    <div className="App" style={{ padding: "2rem", textAlign: "center" }}>
      <h1>Sentiment Analyzer</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Enter text..."
        rows={4}
        cols={50}
      />
      <br />
      <button onClick={handleSubmit} style={{ marginTop: "1rem" }}>
        Predict
      </button>
      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h3>Prediction:</h3>
          <p><strong>Label:</strong> {result.label}</p>
          <p><strong>Score:</strong> {result.score}</p>
        </div>
      )}
    </div>
  );
}

export default App;
