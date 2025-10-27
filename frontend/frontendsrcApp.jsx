import React, { useState } from "react";
import axios from "axios";

export default function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please select a PDF first!");
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/summarize", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    setSummary(res.data.summary || "Error: could not summarize.");
    setLoading(false);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-6">
      <h1 className="text-3xl font-bold mb-6">AI Notes Summarizer</h1>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="mb-4"
      />
      <button
        onClick={handleUpload}
        className="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
      >
        {loading ? "Summarizing..." : "Summarize Notes"}
      </button>

      {summary && (
        <div className="mt-6 bg-white p-4 rounded-lg shadow-lg w-2/3">
          <h2 className="text-xl font-semibold mb-2">Summary:</h2>
          <pre className="whitespace-pre-wrap">{summary}</pre>
        </div>
      )}
    </div>
  );
}
