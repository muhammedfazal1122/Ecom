import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './Componets/Home';
import Login from './Componets/Login';
import Register from './Componets/Register';


function App() {

  return (
    <>
    <div>
    
    <BrowserRouter>

        <Routes>
          <Route path="/"  element={<Home />} />
          <Route path="/login"  element={<Login />} />
          <Route path="/register"  element={<Register />} />
        </Routes>

  </BrowserRouter>
      
    </div>
      
    </>
  )
}

export default App
