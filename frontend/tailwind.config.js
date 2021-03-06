module.exports = {
  purge: [
    './index.html',
    './src/**/*.{vue,js,ts,jsx,tsx}',
    './../backend/templates/**/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: {
          900: '#008d4e',
          800: '#00ac6f',
          700: '#00be7e',
          600: '#00d191',
          500: '#00e1a0',
          400: '#00eaae',
          300: '#00f4bd',
          200: '#29fbd1',
          100: '#9cfde4',
          50: '#d8fff5',
        },
        secondary: {
          900: '#0000c7',
          800: '#001ed7',
          700: '#002de1',
          600: '#0239ee',
          500: '#0942fa',
          400: '#4a62fe',
          300: '#7181ff',
          200: '#9ea5fe',
          100: '#c6c8fe',
          50: '#e9e9ff',
        },
        font: {
          light: '#dddddd',
          dark: '#444444',
        },
        backg: {
          light: '#fafafa',
          dark: '#05181a',
          trans: '#00000066'
        }
      },
      fontFamily: {
        body: ['Roboto'],
      },
      width: {
        'middle': '40rem',
        'desktop': '50rem',
        'phone': '25rem',
      },
      inset: {
        '1/6': '16.666667%'
      },
      stroke: theme => ({
        'primary': theme('colors.primary'),
        'secondary': theme('colors.secondary'),
        'font': theme('colors.font'),
        'white': 'white',
      }),
      fill: theme => ({
        'primary': theme('colors.primary'),
        'secondary': theme('colors.secondary'),
        'font': theme('colors.font'),
        'white': 'white',
      }),
    },
  },
  variants: {
    extend: {
      stroke: ['group-hover'],
      fill: ['group-hover'],
      borderRadius: ['hover'],
    },
  },
  plugins: [],
}
