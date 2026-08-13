const computerData = {
  PC01: {
    telemetry: {
      computer_id: "PC01",
      room_id: "LAB01",
      timestamp: "2026-08-13T09:30:00",
      cpu_pct: 45,
      ram_pct: 62,
      disk_pct: 38,
      cpu_temp: 52,
      net_in: 1200,
      net_out: 850,
    },

    prediction: {
      computer_id: "PC01",
      prediction_type: "failure",
      probability: 0.82,
      model_version: "v1.2",
      explanation: [],
    },
  },

  PC02: {
    telemetry: {
      computer_id: "PC02",
      room_id: "LAB01",
      timestamp: "2026-08-13T09:30:00",
      cpu_pct: 30,
      ram_pct: 45,
      disk_pct: 35,
      cpu_temp: 43,
      net_in: 900,
      net_out: 700,
    },

    prediction: {
      computer_id: "PC02",
      prediction_type: "failure",
      probability: 0.15,
      model_version: "v1.2",
      explanation: [],
    },
  },

  PC03: {
    telemetry: {
      computer_id: "PC03",
      room_id: "LAB01",
      timestamp: "2026-08-13T09:30:00",
      cpu_pct: 91,
      ram_pct: 94,
      disk_pct: 80,
      cpu_temp: 82,
      net_in: 1800,
      net_out: 1500,
    },

    prediction: {
      computer_id: "PC03",
      prediction_type: "failure",
      probability: 0.91,
      model_version: "v1.2",
      explanation: [],
    },
  },

  PC04: {
    telemetry: {
      computer_id: "PC04",
      room_id: "LAB01",
      timestamp: "2026-08-13T09:30:00",
      cpu_pct: 40,
      ram_pct: 50,
      disk_pct: 42,
      cpu_temp: 46,
      net_in: 1000,
      net_out: 800,
    },

    prediction: {
      computer_id: "PC04",
      prediction_type: "failure",
      probability: 0.08,
      model_version: "v1.2",
      explanation: [],
    },
  },
};

export default computerData;