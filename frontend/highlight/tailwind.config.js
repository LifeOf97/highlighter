module.exports = {
  future: {
    removeDeprecatedGapUtilities: true,
    purgeLayersByDefault: true,
    defaultLineHeights: true,
    standardFontWeights: true
  },
  purge: [],
  theme: {
    extend: {
      spacing: {
        '66':	'18rem',
        '68':	'20rem',
        '70':	'22rem',
        '72': '24rem',
        '74':	'26rem',
        '76':	'28rem',
        '78':	'30rem',
        '80': '32rem',
      },
    },
  },
  variants: [
    'responsive', 'group-hover', 'group-focus', 'focus-within', 'first',
    'last', 'odd', 'even', 'hover', 'focus', 'active', 'visited', 'disabled'
  ],
  plugins: []
}
