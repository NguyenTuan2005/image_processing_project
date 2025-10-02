import { useEffect, useState } from "react";
import {hello} from "./utils/hello";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
      hello().then(data => setMessage(data))
  }, []);

  return (
    <div>
      <h1>React + Django</h1>
      <p>{message}</p>
    </div>
  );
}

export default App;

