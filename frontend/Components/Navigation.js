import { Button, Container, Grid, Menu, MenuItem } from "@mui/material";
import LoginButton from "./LoginButton";

export default function Navigation() {
  return (
    <>
      <Grid
        container
        spacing={2}
        style={{ marginTop: "1rem", marginLeft: "2rem" }}
      >
        <Grid item xs={8}>
          <Button>Dashboard</Button>
        </Grid>
        <Grid item>
          <LoginButton />
        </Grid>
      </Grid>
    </>
  );
}