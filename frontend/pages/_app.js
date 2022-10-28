import '../styles/globals.css'

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import Navigation from '../Components/Navigation';
import { Container } from '@mui/material';

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Container>
        <Navigation/>
        <Component {...pageProps} />
      </Container>
    </>
  )
}

export default MyApp