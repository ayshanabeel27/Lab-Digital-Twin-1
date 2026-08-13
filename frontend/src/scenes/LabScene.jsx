import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";

function LabModel({ onComputerClick }) {
  const { scene } = useGLTF("/models/computer_lab.glb");

  return (
    <primitive
      object={scene}
      onClick={(event) => {
        event.stopPropagation();

        let clickedObject = event.object;

        while (clickedObject) {
          if (clickedObject.name.includes("_PC_")) {
            console.log("Clicked computer:", clickedObject.name);

            onComputerClick(clickedObject.name);

            return;
          }

          clickedObject = clickedObject.parent;
        }
      }}
    />
  );
}

function LabScene({ onComputerClick }) {
  return (
    <Canvas camera={{ position: [10, 10, 10], fov: 50 }}>

      <ambientLight intensity={1} />

      <directionalLight
        position={[5, 10, 5]}
        intensity={2}
      />

      <LabModel
        onComputerClick={onComputerClick}
      />

      <OrbitControls />

    </Canvas>
  );
}

export default LabScene;