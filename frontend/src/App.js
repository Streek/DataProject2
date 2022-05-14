import "./App.css";
import React, { useState } from "react";
import axios from "axios";
import Table from "./table";

function App() {
  const [results, setResults] = useState([]);
  const [text, setText] = useState([]);

  async function fetchData(text) {
    let url = process.env.REMOTE_URL
      ? process.env.REMOTE_URL
      : "http://127.0.0.1:5000";
    const result = await axios.get(url + "?text=" + text, {
      withCredentials: false,
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*",
      },
    });

    setResults(result.data);
  }

  const categories = [
    "related",
    "request",
    "offer",
    "aid_related",
    "medical_help",
    "medical_products",
    "search_and_rescue",
    "security",
    "military",
    "child_alone",
    "water",
    "food",
    "shelter",
    "clothing",
    "money",
    "missing_people",
    "refugees",
    "death",
    "other_aid",
    "infrastructure_related",
    "transport",
    "buildings",
    "electricity",
    "tools",
    "hospitals",
    "shops",
    "aid_centers",
    "other_infrastructure",
    "weather_related",
    "floods",
    "storm",
    "fire",
    "earthquake",
    "cold",
    "other_weather",
    "direct_report",
  ];

  return (
    <div className="flex-row items-center px-32 justify-center min-h-screen from-cyan-100 via-pink-200 to-yellow-200 bg-gradient-to-br">
      <div className="pt-8 text-center text-5xl text-black-600 font-bold font-serif">
        Welcome
      </div>
      <div className="flex items-center w-full mx-auto bg-white rounded-lg ">
        <div className="w-full">
          <input
            type="search"
            className="w-full px-4 py-1 text-gray-800 rounded-full focus:outline-none"
            placeholder="start typing to get started..."
            x-model="search"
            onChange={(e) => {
              setText(e.target.value);
              fetchData(text);
            }}
          />
        </div>
        <div>
          <button
            type="submit"
            className="flex items-center bg-blue-500 justify-center w-12 h-12 text-white rounded-r-lg"
          ></button>
        </div>
      </div>
      <div>
        <Table rows={results}></Table>
      </div>

      <div className="grid mt-8 grid-cols-4 gap-4">
        <p className="bg-green-200 border border-green p-8">
          You can view a generated heatmap of the F1 score, precision, and
          recall of each trained output here. You can also click on the image to
          get a larger view of the image if you need to.
        </p>
        {categories.map((image) => (
          <a
            class="pointer"
            target="_blank"
            href={`./plots/${image}_cv.png`}
            rel="noreferrer"
          >
            <img class="" src={`./plots/${image}_cv.png`} alt="plot of data" />
          </a>
        ))}
      </div>
    </div>
  );
}

export default App;
