import { useState } from 'react'
import './App.css'
import LiquidEther from './LiquidEther'
import Inputs from './components/Inputs'
import Navbar from './components/navbar/navbar'

function App() {
  return (
<div className='w-full h-screen relative bg-black flex justify-center items-center'>
<div style={{ width: '100%', height: 600, position: 'relative' }}>
  <LiquidEther
    colors={[ '#5227FF', '#FF9FFC', '#B497CF' ]}
    mouseForce={20}
    cursorSize={100}
    isViscous
    viscous={30}
    iterationsViscous={32}
    iterationsPoisson={32}
    resolution={0.5}
    isBounce={false}
    autoDemo
    autoSpeed={0.5}
    autoIntensity={2.2}
    takeoverDuration={0.25}
    autoResumeDelay={3000}
    autoRampDuration={0.6}
    color0="#5227FF"
    color1="#FF9FFC"
    color2="#B497CF"
/>
    </div>
      {/* FOREGROUND */}
      <div className='absoulute flex flex-col justify-center items-center'>
      
        <Navbar />
        <Inputs />
      
      </div>

</div>
  )
}

export default App