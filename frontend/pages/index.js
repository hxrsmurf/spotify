import { Button, Checkbox, IconButton, Dialog, DialogActions, DialogContent, DialogTitle, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Toolbar, Tooltip, Container } from "@mui/material"
import React, { useEffect, useState } from "react"
import DeleteIcon from '@mui/icons-material/Delete'
import { useRouter } from 'next/router'
import FilterAltIcon from '@mui/icons-material/FilterAlt';
import FilterAltOffIcon from '@mui/icons-material/FilterAltOff';
import { useSession } from "next-auth/react";

export default function Home({ results }) {

  const [selected, setSelected] = useState([])
  const [open, setOpen] = useState(false)
  const [checkAllDuplicates, setcheckAllDuplicates] = useState(false)
  const {data: session} = useSession()

  if (!session) {
    return (
      "Please login"
    )
  }

  const router = useRouter()

  const handleClick = (event, result) => {
    // https://mui.com/material-ui/react-table/
    const selectedIndex = selected.indexOf(result.id);
    let newSelected = [];

    // Need to be able to support the original selected index, still otherwise checkbox won't show.
    let newSelected_index = [];

    if (selectedIndex === -1) {
      newSelected = newSelected.concat(selected, {"id": result.id.S, "song": result.song.S, "artist": result.artist.S});
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
    setOpen(false)
  }

  async function handleDBDelete(select) {
    const res = await fetch('http://localhost:3000/api/delete?id=' + select.id)
    const resp = await res.json()
    console.log(resp)
  }

  const handleConfirm = () => {
    {selected.map((select, id)=> (
      handleDBDelete(select)
    ))}

    // Reset everything
    setOpen(false)
    setcheckAllDuplicates(false)
    setSelected([])
  }

  const handleSelectAllDuplicates = (event) => {
    let newSelected = []
    setcheckAllDuplicates(true)
    results.map((result, id) =>
      {result.possibleDuplicate.BOOL ?
        newSelected.push({"id": result.id.S, "song": result.song.S, "artist": result.artist.S})
        :
        <></>}
    )
    setSelected(newSelected)
  }

  const handleDeSelectAllDuplicates = (event) => {
    setcheckAllDuplicates(false)
    setSelected([])
  }

  const isSelected = (id) => selected.indexOf(id) != -1

  return (
    <>
      <Dialog open={open} maxWidth={"md"} fullWidth={true}>
        <DialogTitle>Confirm delete</DialogTitle>
        <DialogContent>
          <div>
            Confirm you want to delete these:
            <ul>
              {selected.map((select, id) =>
                (<li key={id}>{select.id} - {select.song} by {select.artist} </li>)
              )}
            </ul>
          </div>
          {selected.S}
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose}>Cancel</Button>
          <Button onClick={handleConfirm}>Confirm</Button>
        </DialogActions>
      </Dialog>

      <TableContainer component={Paper}>
        <Toolbar sx={{ flex: '1 1 100%', fontSize: '2rem', fontWeight: 'bold' }} color="inherit">Recently Played</Toolbar>
        <Container><Button
          startIcon={checkAllDuplicates ? <FilterAltOffIcon/> : <FilterAltIcon/>}
          variant='contained'
          onClick={checkAllDuplicates ? (event) => handleDeSelectAllDuplicates(event) : (event) => handleSelectAllDuplicates(event)}
          >{checkAllDuplicates ? "Deselect" : "Select"} All Duplicates</Button></Container>
        {selected == 0 ? <></>
          :
          <Container>
            {selected.length} selected
            <Tooltip title="Delete">
              <IconButton onClick={() => handleDelete()}>
                <DeleteIcon />
              </IconButton>
            </Tooltip>
          </Container>
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
              <TableRow hover key={id} sx={{ '&:last-child td, &:last-child th': { border: 0 } }} role="checkbox" onClick={(event) => handleClick(event, result)}>
              {!result.possibleDuplicate ? <></> :
              <>
                <TableCell padding="checkbox"><Checkbox checked={ isSelected(result.id) }></Checkbox></TableCell>
                <TableCell component="th" scope="row">
                  {result.id.S}
                </TableCell>
                <TableCell> {result.year_month.S} </TableCell>
                <TableCell> {result.song.S} </TableCell>
                <TableCell> {result.artist.S} </TableCell>
                <TableCell> {result.album.S} </TableCell>
                <TableCell> {result.deviceType.S} </TableCell>
                <TableCell> {result.possibleDuplicate.BOOL ? 'true' : 'false'} </TableCell>
              </>
              }
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