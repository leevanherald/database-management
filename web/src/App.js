import React from 'react';
import MainPage from './MainPage'; // Adjust the path according to your file structure
import {useState, useEffect} from 'react'

function App() {
  useEffect(() => {
    console.log(process.env.REACT_APP_API_URL);
  }, [])
  return (
    <div className="App">
      <MainPage />
    </div>
  );
}

export default App;
