import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import Calendar from "react-calendar";
import "./CalendarPage.css";
import "react-calendar/dist/Calendar.css";

function CalendarPage() {
  const [tasks, setTasks] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = async () => {
    const response = await fetch("http://127.0.0.1:5000/tasks");
    const data = await response.json();
    setTasks(data.tasks);
  };

  const getTileContent = ({ date, view }) => {
    if (view === "month") {
      const formattedDate = date.toLocaleDateString('tr-TR'); 
      const dayTasks = tasks.filter((task) => task.date === formattedDate);
      if (dayTasks.length > 0) {
        return <div className="task-indicator"></div>;
      }
    }
    return null;
  };
  
  const handleDateClick = (value) => {
    const selectedDate = value.toLocaleDateString('tr-TR'); 
    navigate(`/tasks/${selectedDate}`);
  };
  
  return (
    <div className="calendar-container">
      <h1>Task Manager</h1>
      <Calendar onClickDay={handleDateClick} tileContent={getTileContent} />
    </div>
  );
}

export default CalendarPage;
