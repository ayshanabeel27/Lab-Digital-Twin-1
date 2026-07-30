function StatusCard({ title, value }) {
  return (
    <div className="status-card">
      <h3>{title}</h3>
      <h2>{value}</h2>
    </div>
  );
}

export default StatusCard;