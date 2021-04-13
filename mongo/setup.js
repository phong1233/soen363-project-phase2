const { MongoClient } = require("mongodb");
const csvtojson = require("csvtojson");

const uri = "mongodb://127.0.0.1:27017";
const client = new MongoClient(uri, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function loadListings() {
  const csvData = await csvtojson().fromFile("../dataset/listings.csv");
  try {
    await client.connect();
    const db = client.db("soen363");
    await db.collection("listings").insertMany(csvData);
  } finally {
    client.close();
  }
}

loadListings();
