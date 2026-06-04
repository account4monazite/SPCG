
const MOODS = {
    "dark": "deep shadows, melancholic atmosphere",
    "nostalgic": "retro atmosphere, faded memories",
    "dreamy": "soft focus, surreal lighting",
    "happy": "sunny, smile, beach, flowers",
    "lonely": "isolated environment, empty spaces",
    "romantic": "warm glow, intimate atmosphere",
    "sad": "rainy mood, emotional stillness",
    "hopeful": "soft sunrise light, uplifting mood",
    "calm": "peaceful scenery, muted tones",
    "energetic": "dynamic motion, vibrant lighting",
    "aggressive": "harsh contrast, intense atmosphere",
    "mysterious": "fog, obscured details",
    "ethereal": "floating haze, heavenly lighting",
    "cozy": "warm lamps, indoor comfort",
    "cold": "blue tones, winter atmosphere",
    "chaotic": "glitchy composition, visual tension",
    "euphoric": "dreamlike glow, emotional intensity",
    "empty": "vast open spaces, minimal scenery",
    "anxious": "uneasy lighting, cinematic tension",
    "rebellious": "gritty streets, underground vibe",
    "spiritual": "celestial atmosphere, transcendence",
}


const GENRES = {
    "jazz": "noir piano bar, smoke haze",
    "lofi": "bedroom at night, study desk",
    "phonk": "neon streets, underground city",
    "pop": "cinematic modern aesthetic",
    "rock": "grungy textures, stage lighting",
    "indie": "film photography, candid atmosphere",
    "classical": "elegant halls, orchestral mood",
    "hyperpop": "maximalist, DIY,  neon green",
    "ambient": "vast landscapes, atmospheric minimalism",
    "electronic": "futuristic lighting, digital mood",
    "synthwave": "retro neon glow, 1980s aesthetic",
    "drill": "urban night streets, gritty realism",
    "hip hop": "city nightlife, cinematic realism",
    "rnb": "soft neon, intimate mood",
    "metal": "dark dramatic scenery, stormy atmosphere",
    "punk": "raw underground vibe, rebellion",
    "folk": "nature landscapes, rustic warmth",
    "country": "open highways, sunset fields",
    "house": "club lighting, energetic nightlife",
    "techno": "industrial atmosphere, dark rave mood",
    "blues": "smoky bars, vintage melancholy",
    "kpop": "stylized lighting, glossy visuals",
    "jpop": "bright cinematic youth aesthetic",
    "shoegaze": "dream haze, blurry lights",
    "emo": "rain, emotional solitude",
    "trap": "luxury night aesthetic, urban mood",
}

const PURPOSES = {
    "study": "focused atmosphere, minimal distractions",
    "sleep": "dim ambient lighting, soft calmness",
    "relax": "peaceful cinematic mood",
    "drive": "open roads, motion and distance",
    "workout": "high energy composition, intensity",
    "coding": "late night screen glow, hacker aesthetic",
    "reading": "quiet indoor atmosphere, warm lamps",
    "party": "crowded nightlife, energetic lights",
    "meditation": "tranquil scenery, spiritual calmness",
    "gaming": "neon glow, immersive atmosphere",
    "walking": "city streets at dusk, solitude",
    "rain": "storm clouds, wet reflections",
    "focus": "clean minimalist composition",
    "travel": "cinematic landscapes, wanderlust",
    "breakup": "emotional isolation, melancholic visuals",
    "healing": "gentle light, emotional warmth",
    "night": "moonlight, deep shadows",
    "morning": "soft sunrise tones",
    "summer": "warm golden lighting",
    "winter": "cold atmosphere, snow haze",
}
const moodkeys=Object.keys(MOODS)
export function ShuffleMood(){
    return moodkeys[Math.floor(Math.random()*moodkeys.length)];
}
const genrekeys=Object.keys(GENRES)
export function ShuffleGenre(){
    return genrekeys[Math.floor(Math.random()*genrekeys.length)];
}
const purposekeys=Object.keys(PURPOSES)
export function ShufflePurpose(){
    return purposekeys[Math.floor(Math.random()*purposekeys.length)];
}