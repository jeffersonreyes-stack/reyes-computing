module.exports = {
  content: ['./*.html'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        orbitron: ['Orbitron', 'sans-serif'],
        mono: ['Space Mono', 'monospace'],
      },
      colors: {
        reyes: {
          black: '#050505',
          navy: '#020202',
          dark: '#020202',
          cyan: '#00F3FF',
          cyanDark: '#008b91',
          silver: '#E2E8F0',
          white: '#E0E0E0',
          gold: '#FFD700',
          slate: '#2A2A2A',
          text: '#E0E0E0'
        }
      },
      backgroundImage: {
        'hero-pattern': 'linear-gradient(to bottom, rgba(5,5,5,0.8), rgba(5,5,5,1))',
      },
      boxShadow: {
        'neon': '0 0 10px rgba(0, 243, 255, 0.5), 0 0 20px rgba(0, 243, 255, 0.3)',
      }
    }
  }
}
