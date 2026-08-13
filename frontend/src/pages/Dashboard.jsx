import { useState } from "react";

import Sidebar from "../components/Sidebar";
import Navbar from "../components/Navbar";
import StatusCard from "../components/StatusCard";
import ComputerAnalytics from "../components/ComputerAnalytics";
import LabScene from "../scenes/LabScene";

import computerData from "../services/computerData";

import "../styles/dashboard.css";
import "../styles/statuscard.css";

function Dashboard() {

  const [selectedComputer, setSelectedComputer] = useState(null);

  const handleComputerClick = (computerName) => {

    console.log("Clicked 3D object:", computerName);

    /*
      Temporary mapping.

      Example:
      Row1_PC_A_01 → PC01
      Row1_PC_A_02 → PC02
      Row1_PC_A_03 → PC03
    */

    const match = computerName.match(/_PC_[AB]_(\d+)/);

    if (!match) {
      console.log("Computer ID could not be detected.");
      return;
    }

    const number = parseInt(match[1], 10);

    const computerId = `PC${String(number).padStart(2, "0")}`;

    console.log("Mapped computer:", computerId);

    const computer = computerData[computerId];

    if (computer) {
      setSelectedComputer(computer);
    } else {
      console.log("No mock data available for:", computerId);
    }
  };

  return (
    <div className="dashboard">

      <Sidebar />

      <div className="content">

        <Navbar />

        <div className="cards">

          <StatusCard
            title="Healthy PCs"
            value="35"
          />

          <StatusCard
            title="Warning PCs"
            value="2"
          />

          <StatusCard
            title="Critical PCs"
            value="1"
          />

          <StatusCard
            title="Total PCs"
            value="38"
          />

        </div>

        <div className="scene-placeholder">

          <LabScene
            onComputerClick={handleComputerClick}
          />

        </div>

        <ComputerAnalytics
          computer={selectedComputer}
        />

      </div>

    </div>
  );
}

export default Dashboard;