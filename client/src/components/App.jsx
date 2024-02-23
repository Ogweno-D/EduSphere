import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from "react-router-dom";
import Header from "./Header.jsx";
import HeroSection from "./HeroSection.jsx";
import Footer from "./Footer.jsx";
import SignIn from "/src/components/sign in and sign up/SignIn.jsx";
import SignUp from "/src/components/sign in and sign up/SignUp.jsx";
import StudentDashboard from "./StudentDashboard.jsx";
import LecturerDashboard from "./LecturerDashboard.jsx";
import AdminDashboard from "./AdminDashboard.jsx";
import Course_WorkList from "/src/components/WorkManagement/Course_WorkList.jsx";
import UnitList from "./UnitManagement/UnitList.jsx";
import DepartList from "./Department/DeptList.jsx";
import LecturerList from "./Lecturer/LecturerList.jsx";

async function getUserData() {
  const response = await fetch("http://127.0.0.1:5000/users");
  const data = await response.json();
  return data;
}

function App() {
  const [userRole, setUserRole] = useState(null);

  useEffect(() => {
    getUserData().then((data) => setUserRole(data.role));
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/login-page" element={<SignIn />} />
        <Route
          path="/student"
          element={
            userRole === "student" ? (
              <StudentDashboard />
            ) : (
              <Navigate to="/login-page" />
            )
          }
        />
        <Route
          path="/lecturer"
          element={
            userRole === "lecturer" ? (
              <LecturerDashboard />
            ) : (
              <Navigate to="/login-page" />
            )
          }
        />
        <Route
          path="/admin"
          element={
            userRole === "admin" ? (
              <AdminDashboard />
            ) : (
              <Navigate to="/login-page" />
            )
          }
        />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/course_work" element={<Course_WorkList />} />
        <Route path="/units" element={<UnitList />} />
        <Route path="/departments" element={<DepartList />} />
        <Route path="/lecturers" element={<LecturerList />} />

        <Route
          path="/"
          element={
            <>
              <Header />
              <HeroSection />
              <Footer />
            </>
          }
        />
      </Routes>
    </Router>
  );
}

export default App;
