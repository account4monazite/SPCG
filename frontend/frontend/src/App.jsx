import { useState } from 'react'
import './App.css'
import LiquidEther from './LiquidEther'
import Inputs from './components/Inputs'
import Navbar from './components/navbar/navbar'

function App() {
  return (
    <div className='w-full h-screen relative bg-black flex flex-col justify-between items-center overflow-hidden'>
      {/* BACKGROUND EFFECT */}
            {/* BACKGROUND EFFECT */}
      <LiquidEther
        style={{ position: 'fixed', zIndex: 0 }} // <-- Add this line here
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

      {/* NAVBAR (TOP LAYER) */}
      <div className='w-full relative z-20'>
        <Navbar />
      </div>

      {/* INPUTS (MIDDLE LAYER) */}
      <div className='flex-grow flex justify-center items-center relative z-10 w-full'>
        <Inputs />
      </div>
      <div className="mt-12 flex flex-col justify-between gap-6 border-t border-secondary pt-8 md:mt-16 md:flex-row md:items-center ">
                    
                    <p className="text-sm text-quaternary text-white-1000">Made by Shriya Rane :) </p></div>
    </div>
  )
}

export default App