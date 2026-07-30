import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatusCard from "../components/StatusCard";

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

          <h2>3D Computer Lab Coming Soon</h2>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;