import React ,{useState,useEffect}from "react";
import shuffle from '../assets/shuffle.png';
import './Inputs.css';
//import axios from "axios";
import { ShuffleGenre,ShufflePurpose,ShuffleMood } from "./shuffle";


const Inputs =() =>{
    const [mood,setMood]=useState('');
    const [genre,setGenre]=useState('');
    const [purpose,setPurpose]=useState('');
    const [generatedImg,setGeneratedImg]=useState(null);
    const [loading,setLoading]=useState(false);
    const VITE_API_URL = import.meta.env.VITE_API_URL;
    const apiBaseUrl = VITE_API_URL.replace(/\/+$/g, '');
    const [error,setError]=useState("");
const handleGenerateAI = async () => {
  setError("");
  setLoading(true);
  try{
    if (!mood || !genre || !purpose) {
    alert("Choose mood, genre, and purpose first");
    setLoading(false);
    return;
  }

  const url = `${apiBaseUrl}/ai_cover?mood=${encodeURIComponent(mood)}&genre=${encodeURIComponent(genre)}&purpose=${encodeURIComponent(purpose)}`;

  const response = await fetch(url);
  if (!response.ok) {
    if (response.status === 503) {
      setError("Server is busy! Please try again later");
    } else {
      setError("Failed to generate image. Please try again.");
    }
    setLoading(false);
    return;
  }

  const blob = await response.blob();
  const imageUrl = URL.createObjectURL(blob);
  setGeneratedImg(imageUrl);
  setLoading(false);}catch (err){setError("Unable to connect to server!");setLoading(false);}
};

const handleGenerateCollage = async () => {
  setError("");
  setLoading(true);
  if (!mood || !genre || !purpose) {
    alert("Choose mood, genre, and purpose first");
    setLoading(false);
    return;
  }

  const url = `${apiBaseUrl}/cover?mood=${encodeURIComponent(mood)}&genre=${encodeURIComponent(genre)}&purpose=${encodeURIComponent(purpose)}`;

  const response = await fetch(url);
  if (!response.ok) {
    setError("Failed to generate collage. Please try again.");
    setLoading(false);
    return;
  }

  const blob = await response.blob();
  const imageUrl = URL.createObjectURL(blob);
  setGeneratedImg(imageUrl);
  setLoading(false);
};

const handleDownload = () => {
  const link = document.createElement('a');
  link.href = generatedImg;
  link.download = `${mood}-${genre}-${purpose}-cover.png`;
  link.click();
};

    return (
   <div className="container">
    <div className="header">
        <div className="text">
           Spotify Playlist Cover Generator
        </div>
        <div className="underline"></div>
    </div>
    <div className="inputs">
        <div className="input">

            <select name="Moods" id="mood" value={mood} onChange={(e)=>setMood(e.target.value)}>
<option disabled value="">Choose Mood</option>
                <option value="dark">Dark</option>
<option value="nostalgic">Nostalgic</option>
<option value="dreamy">Dreamy</option>
<option value="happy">Happy</option>
<option value="lonely">Lonely</option>
<option value="romantic">Romantic</option>
<option value="sad">Sad</option>
<option value="hopeful">Hopeful</option>
<option value="calm">Calm</option>
<option value="energetic">Energetic</option>
<option value="aggressive">Aggressive</option>
<option value="mysterious">Mysterious</option>
<option value="ethereal">Ethereal</option>
<option value="cozy">Cozy</option>
<option value="cold">Cold</option>
<option value="chaotic">Chaotic</option>
<option value="euphoric">Euphoric</option>
<option value="empty">Empty</option>
<option value="anxious">Anxious</option>
<option value="rebellious">Rebellious</option>
<option value="spiritual">Spiritual</option></select>
            <button type='button'id='mix' onClick={()=>setMood(ShuffleMood())}><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-shuffle" viewBox="0 0 16 16">
  <path fillRule="evenodd" d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5"/>
  <path d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192"/>
</svg></button>
        </div>
        <div className="input">
            <select name="Genre"id="genre"  value={genre} onChange={(e)=>setGenre(e.target.value)}>
<option disabled value="">Choose genre</option>        
<option value="jazz">Jazz</option>
<option value="lofi">Lofi</option>
<option value="phonk">Phonk</option>
<option value="pop">Pop</option>
<option value="rock">Rock</option>
<option value="indie">Indie</option>
<option value="classical">Classical</option>
<option value="hyperpop">Hyperpop</option>
<option value="ambient">Ambient</option>
<option value="electronic">Electronic</option>
<option value="synthwave">Synthwave</option>
<option value="drill">Drill</option>
<option value="hip hop">Hip Hop</option>
<option value="rnb">Rnb</option>
<option value="metal">Metal</option>
<option value="punk">Punk</option>
<option value="folk">Folk</option>
<option value="country">Country</option>
<option value="house">House</option>
<option value="techno">Techno</option>
<option value="blues">Blues</option>
<option value="kpop">Kpop</option>
<option value="jpop">Jpop</option>
<option value="shoegaze">Shoegaze</option>
<option value="emo">Emo</option>
<option value="trap">Trap</option></select>
            <button type='button' id='mixup' onClick={()=>setGenre(ShuffleGenre())}><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-shuffle" viewBox="0 0 16 16">
  <path fillRule="evenodd" d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5"/>
  <path d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192"/>
</svg></button>
        </div>
        <div className="input">
            <select name="Purpose"id="purpose"  value={purpose} onChange={(e)=>setPurpose(e.target.value)}>
<option disabled value="">Choose purpose</option>
<option value="study">Study</option>
<option value="sleep">Sleep</option>
<option value="relax">Relax</option>
<option value="drive">Drive</option>
<option value="workout">Workout</option>
<option value="coding">Coding</option>
<option value="reading">Reading</option>
<option value="party">Party</option>
<option value="meditation">Meditation</option>
<option value="gaming">Gaming</option>
<option value="walking">Walking</option>
<option value="rain">Rain</option>
<option value="focus">Focus</option>
<option value="travel">Travel</option>
<option value="breakup">Breakup</option>
<option value="healing">Healing</option>
<option value="night">Night</option>
<option value="morning">Morning</option>
<option value="summer">Summer</option>
<option value="winter">Winter</option></select>
            <button type='button' id='remix' onClick={()=>setPurpose(ShufflePurpose())}><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" className="bi bi-shuffle" viewBox="0 0 16 16">
  <path fillRule="evenodd" d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5"/>
  <path d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192"/>
</svg></button>
        </div>
        <div className="submit-container">
        <div className="submit" id='AI' onClick={handleGenerateAI} style={{opacity: loading ? 0.6 : 1, cursor: loading ? 'not-allowed' : 'pointer'}} disabled={loading}>
          {loading ? "Generating..." : "Generate with AI"}
        </div>
        <div className="submit" id='collage' onClick={handleGenerateCollage} style={{opacity: loading ? 0.6 : 1, cursor: loading ? 'not-allowed' : 'pointer'}} disabled={loading}>
          {loading ? "Generating..." : "Generate a collage"}
        </div>

        </div>
        {error && (
          <div className="error-message">
            {error}
          </div>
        )}
        {loading && (
          <div className="loading-message">
            ⏳ Generating your image...
          </div>
        )}
        {generatedImg && (
  <div className="cover-preview">
    <p style={{color:'#fff'}}>Generated Image</p>
    <img id="imggen"
      src={generatedImg}
      alt="Generated Playlist Cover"
    />
    <button type="button" id="save"onClick={handleDownload}>
      Download Cover
    </button>
  </div>
)}
    </div>
   </div>
    )
}

export default Inputs;