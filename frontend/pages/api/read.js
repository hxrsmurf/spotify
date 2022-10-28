import { DynamoDB } from "aws-sdk"

const client = new DynamoDB({
  credentials: {
    accessKeyId: process.env.ACCESS_KEY,
    secretAccessKey: process.env.SECRET_KEY
  },
  region: process.env.REGION
})


export default async function handler(req, res) {
  if (req.method === 'GET') {
    client.query(
      {
        TableName: process.env.TABLE_NAME,
        IndexName: 'year_month-id-index',
        Limit: 300,
        ScanIndexForward: false,
        KeyConditionExpression: 'year_month = :value',
        ExpressionAttributeValues: {
          ':value': {
            S: '2022-10'
          }
        }
      },
      function (err, data) {
        if (err) console.log(err, err.stack)
        else {
          return res.status(200).json(data.Items)
        }
      }
    )
  }
}
