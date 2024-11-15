import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const TokenValidation = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    // Check for token in the query parameter or localStorage
    const queryParams = new URLSearchParams(location.search);
    const token = queryParams.get('token') || localStorage.getItem('token');

    if (token) {
      // Store the token in localStorage if found in the URL
      localStorage.setItem('token', token);

      // Optionally, you can remove the token from the URL after storing it
      if (queryParams.get('token')) {
        navigate(location.pathname, { replace: true });
      }
    } else {
      // If no token, redirect to login page
      navigate('/login');
    }
  }, [location, navigate]);

  return null; // No UI is needed, just handle the token validation
};

export default TokenValidation;
