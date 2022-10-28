export default function Home({ results }) {
  console.log(results)
  return (
    <>
      <div>
        <table style={{textAlign: 'center'}}>
          <tr>
            <th>id</th>
            <th>year_month</th>
            <th>song</th>
            <th>album</th>
            <th>artist</th>
          </tr>
          {results.map((result, id) => (
            <tr key={id}>
              <td>
                <div>{result.id.S}</div>
              </td>
              <td>
                <div>{result.year_month.S}</div>
              </td>
              <td>
                <div>{result.song.S}</div>
              </td>
              <td>
                <div>{result.artist.S}</div>
              </td>
              <td>
                <div>{result.album.S}</div>
              </td>
            </tr>
          ))}
        </table>

      </div>
    </>
  )
}

export async function getServerSideProps() {
  const query = await fetch('http://localhost:3000/api/read')
  const results = await query.json()

  return {
    props: {
      results
    }
  }
}