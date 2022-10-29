import "../styles/globals.css";

import "@fontsource/roboto/300.css";
import "@fontsource/roboto/400.css";
import "@fontsource/roboto/500.css";
import "@fontsource/roboto/700.css";

import Navigation from "../Components/Navigation";
import { Container } from "@mui/material";
import { SessionProvider } from "next-auth/react";

function MyApp({ Component, pageProps: { session, ...pageProps } }) {
  return (
    <>
      <SessionProvider session={session}>
        <Container>
          <Navigation />
          <Component {...pageProps} />
        </Container>
      </SessionProvider>
    </>
  );
}

export default MyApp;