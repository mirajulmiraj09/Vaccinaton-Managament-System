import { Routes, Route } from 'react-router-dom'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<div>Landing Page</div>} />
      <Route path="/login" element={<div>Login Page</div>} />
      <Route path="/register" element={<div>Register Page</div>} />
      <Route path="/patient/dashboard" element={<div>Patient Dashboard</div>} />
      <Route path="/doctor/dashboard" element={<div>Doctor Dashboard</div>} />
      <Route path="/admin/dashboard" element={<div>Admin Dashboard</div>} />
    </Routes>
  )
}