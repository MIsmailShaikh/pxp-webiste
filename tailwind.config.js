/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./*.html", "./**/*.html", "./js/**/*.js"],
  theme: {
    extend: {
      colors: {
        pxp: {
          blue: '#1A365D',
          lightBlue: '#2B6CB0',
          accent: '#3182CE'
        }
      }
    },
  },
  plugins: [],
}
