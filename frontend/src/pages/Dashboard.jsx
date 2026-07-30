import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatusCard from "../components/StatusCard";
import LabScene from "../scenes/LabScene";
import "../styles/dashboard.css";
import "../styles/statuscard.css";

function Dashboard() {
  return (
    <div className="dashboard">
      <Sidebar />

      <div className="content">
        <Navbar />

        <div className="cards">
          <StatusCard title="Healthy PCs" value="35" />
          <StatusCard title="Warning PCs" value="2" />
          <StatusCard title="Critical PCs" value="1" />
          <StatusCard title="Total PCs" value="38" />
        </div>

        <div className="scene-placeholder">
            <LabScene />
        </div>
      </div>
    </div>
  );
}

export default Dashboard;