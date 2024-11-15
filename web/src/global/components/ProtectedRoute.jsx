// global/components/ProtectedRoute.js
import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ element, ...rest }) => {
  const token = localStorage.getItem('token');

  // If there's no token, redirect to the Django login page
  if (!token) {
    // Redirect to the Django login page
    window.location.href = "http://localhost:8000/login"; // Use window.location.href for external redirects
    return null; // Return null as the component will not render anything
  }

  // If the token exists, return the specified element
  return element;
};

export default ProtectedRoute;
