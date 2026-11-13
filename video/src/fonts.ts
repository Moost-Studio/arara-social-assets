import { continueRender, delayRender, staticFile } from 'remotion';
// Fontes locais (Nunito e Mochiy Pop One), carregadas antes do primeiro quadro.
const espera = delayRender('fontes');
Promise.all([
  new FontFace('Nunito', `url(${staticFile('assets/fontes/Nunito.ttf')})`, { weight: '200 1000' }).load(),
  new FontFace('Mochiy', `url(${staticFile('assets/fontes/MochiyPopOne-Regular.ttf')})`).load(),
]).then((fs) => { fs.forEach((f) => document.fonts.add(f)); continueRender(espera); });
