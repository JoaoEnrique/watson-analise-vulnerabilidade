import axios from "axios";
import React, { useState } from "react";
import {
  BarChart, Bar, XAxis, YAxis, Tooltip,
  PieChart, Pie, Cell, Legend,
  RadialBarChart,
  RadialBar,
  LabelList
} from "recharts";
import { API_URL } from "./utils/vars";
import "./main.css";

function App() {
  const [data, setData] = useState<WatsonResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    setErrorMessage(null);
    if (!e.target.files || e.target.files.length === 0) return;

    try {
      setLoading(true);
      const formData = new FormData();
      formData.append("file_input", e.target.files[0]);

      const response = await axios.post(`${API_URL}/process`, formData, {
        headers: { 
          "Content-Type": "multipart/form-data",
          "Accept": "application/json"
        },
      });

      setData(response.data);
      console.log(response.data);
      
    } catch (error: any) {
      console.error(error);
      if(error?.response?.data?.error){
        setErrorMessage(error.response.data.error);
      } else {
        setErrorMessage("Erro ao gerar relatório");
      }
    } finally {
      setLoading(false);
    }
  };

  const COLORS = ["#27ae60", "#f39c12", "#e74c3c", "#8e44ad"]; // baixo, médio, alto, crítico

  const categorizeSeverity = (score: any) => {
    const s = parseFloat(score);
    if (s < 4) return "Baixa";
    if (s < 7) return "Média";
    if (s < 9) return "Alta";
    return "Crítica";
  };

  // Transformando dados de pie chart, só se data existir
  const pieData = data?.severities
    ? Object.entries(data.severities).reduce((acc: any, [score, count]) => {
        const category = categorizeSeverity(score);
        const existing = acc.find((d: any) => d.name === category);
        if (existing) existing.value += count;
        else acc.push({ name: category, value: count });
        return acc;
      }, [])
    : [];

     // Dados para RadialBarChart (proporção por tipo)
  const radialData = data?.types
    ? Object.entries(data.types).map(([tipo, count]) => ({ name: tipo, value: count }))
    : [];

  return (
    <div className="container" style={{ padding: "20px" }}>
      <div className="card">
        <h1 className="text-center">Dashboard CVE</h1>
        <input className="form-control" type="file" onChange={handleUpload} />
        { data?.watsonx_summary &&  (
          <p className="mt-2" style={{ whiteSpace: "pre-wrap" }}>
            Waton: {data.watsonx_summary}
          </p>
        )}
      </div>

      {loading && (
        <div className="d-flex justify-content-center mt-5">
          <div className="spinner-border text-primary" style={{height: 100, width: 100, borderWidth: 5}} role="status">
            <span className="sr-only"></span>
          </div>
        </div>
      )}

      {errorMessage && <p className="color-red">{errorMessage}</p>}

      {data && (
        <div className="mt-5">
          <h2>CVEs por Ano</h2>
          <div className="row">
            <div className="col-12 col-mg-6 col-lg-6 col-xl-6">
              <BarChart width={600} height={300} data={Object.entries(data.years).map(([ano, count]) => ({ ano, count }))}>
                <XAxis dataKey="ano" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" fill="#1f70c1" />
              </BarChart>
            </div>

            <div className="col-12 col-mg-6 col-lg-6 col-xl-6">
              <h2>Top Tipos de Vulnerabilidade</h2>
              <BarChart width={600} height={300} data={Object.entries(data.years).map(([tipo, count]) => ({ tipo, count }))}>
                <XAxis dataKey="tipo" angle={-30} textAnchor="end" interval={0} height={100} />
                <YAxis />
                <Tooltip />
                <Bar dataKey="count" fill="#f39c12" />
              </BarChart>
            </div>

            <div className="col-12 col-mg-6 col-lg-6 col-xl-6">
              <h2>Distribuição CVSS</h2>
              <PieChart width={400} height={400}>
                <Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={120} label={({ name, percent }) => `${name}: ${(percent! * 100).toFixed(1)}%`}>
                  {pieData.map((entry: any, index: number) => (
                    <Cell key={index} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Legend />
                <Tooltip formatter={(value) => [`${value}`, "Quantidade"]} />
              </PieChart>
            </div>
            <div className="col-12 col-mg-6 col-lg-6 col-xl-6">
               <h2>Proporção por Tipo (Radial)</h2>
                <BarChart layout="vertical" width={600} height={400} data={Object.entries(data.types).map(([tipo, count]) => ({ tipo, count }))}>
                  <XAxis type="number" />
                  <YAxis dataKey="tipo" type="category" width={120} />
                  <Tooltip />
                  <Bar dataKey="count" fill="#8884d8" />
                </BarChart>
              </div>
            </div>
        </div>
      )}
    </div>
  );
}

export default App;
