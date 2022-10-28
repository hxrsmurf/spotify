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
    client.deleteItem({
        TableName: process.env.TABLE_NAME,
        Key: {
            "id": {
                S: req.query.id
            }
        }
    },
    function (err, data){
        if (err) {
            console.log(err, err.stack)
            return res.status(400).json({'statusCode': 'ERROR'})
        }
        else {
            return res.status(200).json({'statusCode': 'success'})
        }
    }
    )
  }
}
