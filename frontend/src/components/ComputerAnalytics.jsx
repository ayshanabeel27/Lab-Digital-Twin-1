import "../styles/analytics.css";

function ComputerAnalytics({ computer }) {
  if (!computer) {
    return (
      <div className="analytics-panel">
        <h2>Computer Analytics</h2>
        <p>Click a computer in the 3D lab to view its analytics.</p>
      </div>
    );
  }

  const { telemetry, prediction } = computer;

  return (
    <div className="analytics-panel">

      <h2>{telemetry.computer_id} Analytics</h2>

      <h3>Telemetry</h3>

      <div className="analytics-row">
        <span>Room</span>
        <strong>{telemetry.room_id}</strong>
      </div>

      <div className="analytics-row">
        <span>CPU Usage</span>
        <strong>{telemetry.cpu_pct}%</strong>
      </div>

      <div className="analytics-row">
        <span>RAM Usage</span>
        <strong>{telemetry.ram_pct}%</strong>
      </div>

      <div className="analytics-row">
        <span>Disk Usage</span>
        <strong>{telemetry.disk_pct}%</strong>
      </div>

      <div className="analytics-row">
        <span>CPU Temperature</span>
        <strong>{telemetry.cpu_temp}°C</strong>
      </div>

      <div className="analytics-row">
        <span>Network In</span>
        <strong>{telemetry.net_in}</strong>
      </div>

      <div className="analytics-row">
        <span>Network Out</span>
        <strong>{telemetry.net_out}</strong>
      </div>

      <h3>AI Prediction</h3>

      <div className="analytics-row">
        <span>Prediction</span>
        <strong>{prediction.prediction_type}</strong>
      </div>

      <div className="analytics-row">
        <span>Probability</span>
        <strong>
          {(prediction.probability * 100).toFixed(0)}%
        </strong>
      </div>

      <div className="analytics-row">
        <span>Model Version</span>
        <strong>{prediction.model_version}</strong>
      </div>

    </div>
  );
}

export default ComputerAnalytics;