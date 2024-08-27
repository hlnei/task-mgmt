import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CalendarPage from "./CalendarPage";
import TaskPage from "./TaskPage";
import "./App.css";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<CalendarPage />} />
        <Route path="/tasks/:date" element={<TaskPage />} />
      </Routes>
    </Router>
  );
}

export default App;
