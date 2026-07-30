import { Canvas } from "@react-three/fiber";
import { OrbitControls, useGLTF } from "@react-three/drei";

function LabModel() {
  const { scene } = useGLTF("/models/computer_lab.glb");

  return <primitive object={scene} scale={1} />;
}

export default function LabScene() {
  return (
    <Canvas camera={{ position: [10, 8, 10], fov: 50 }}>
      <ambientLight intensity={1} />
      <directionalLight position={[5, 10, 5]} />
      <LabModel />
      <OrbitControls />
    </Canvas>
  );
}