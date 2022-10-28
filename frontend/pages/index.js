import { Button, Checkbox, IconButton, Dialog, DialogActions, DialogContent, DialogTitle, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Toolbar, Tooltip } from "@mui/material"
import { useState } from "react"
import DeleteIcon from '@mui/icons-material/Delete'

export default function Home({ results }) {

  const [selected, setSelected] = useState([])
  const [open, setOpen] = useState(false)

  const handleClick = (event, id) => {
    // https://mui.com/material-ui/react-table/
    const selectedIndex = selected.indexOf(id);
    let newSelected = [];

    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, id);
    } else if (selectedIndex === 0) {
      newSelected = newSelected.concat(selected.slice(1));
    } else if (selectedIndex === selected.length - 1) {
      newSelected = newSelected.concat(selected.slice(0, -1));
    } else if (selectedIndex > 0) {
      newSelected = newSelected.concat(
        selected.slice(0, selectedIndex),
        selected.slice(selectedIndex + 1),
      );
    }
    setSelected(newSelected);
  }

  const handleDelete = () => {
    setOpen(true)
  }

  const handleClose = () => {
    setSelected([])
    setOpen(false)
  }

  return (
    <>
      <Dialog open={open} maxWidth={"md"} fullWidth="true">
        <DialogTitle>Confirm delete</DialogTitle>
        <DialogContent>
          <div>
            Confirm you want to delete these:
            <ul>
              {selected.map((select, id) =>
                (<li key={id}>{select.S}</li>)
              )}
            </ul>
          </div>
          {selected.S}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleClose}>Confirm</Button>
        </DialogActions>
      </Dialog>

      <TableContainer component={Paper}>
        <Toolbar sx={{ flex: '1 1 100%', fontSize: '2rem', fontWeight: 'bold' }} color="inherit">Recently Played</Toolbar>
        {selected == 0 ? <></>
          :
          <div style={{ marginLeft: '3rem' }}>
            {selected.length} selected
            <Tooltip title="Delete">
              <IconButton onClick={() => handleDelete()}>
                <DeleteIcon />
              </IconButton>
            </Tooltip>
          </div>
        }
        <Table sx={{ minWidth: 900 }} stickyHeader aria-label="simple table">
          <TableHead>
            <TableRow>
              <TableCell padding="checkbox"></TableCell>
              <TableCell>id</TableCell>
              <TableCell>year_month</TableCell>
              <TableCell>song</TableCell>
              <TableCell>artist</TableCell>
              <TableCell>album</TableCell>
              <TableCell>device</TableCell>
              <TableCell>duplicate</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {results.map((result, id) => (
              <TableRow hover key={id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }} role="checkbox" onClick={(event) => handleClick(event, result.id)}>
                <TableCell padding="checkbox"><Checkbox></Checkbox></TableCell>
                <TableCell component="th" scope="row">
                  {result.id.S}
                </TableCell>
                <TableCell> {result.year_month.S} </TableCell>
                <TableCell> {result.song.S} </TableCell>
                <TableCell> {result.artist.S} </TableCell>
                <TableCell> {result.album.S} </TableCell>
                <TableCell> {result.deviceType.S} </TableCell>
                <TableCell> {result.possibleDuplicate.BOOL ? 'true' : 'false'} </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  )
}

export async function getServerSideProps() {

  // Fetch data from external API

  const res = await fetch('http://localhost:3000/api/read')
  const results = await res.json()

  return {
    props: { results }
  }
}